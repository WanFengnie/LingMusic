#!/usr/bin/env python3
"""发行后自动更新 gh-pages 上的 latest.json（更新清单）。

做什么：读 LingVersion.props（或 --version）得到版本号，向 GitHub 查该版本发行（v<版本>）里**实际上传了哪些安装包**，
只给「安装包已在发行页」的平台渠道登记新版本；还没上传包的渠道保持原样（不会被误提醒更新）。

用法（在仓库根执行）：
    python tools/update_manifest.py                 # 预览：只打印将要做的改动，不写文件
    python tools/update_manifest.py --apply         # 写入 latest.json 并在 gh-pages 本地提交
    python tools/update_manifest.py --apply --push  # 同上并推送（闭源项目：推送前请自己确认）

常用选项：
    --version 2.0.3          不读 LingVersion.props，指定版本（发行必须已是正式发布，草稿 / 预发布加 --apply 会被拒绝）
    --ghpages ../Ling-ghpages   gh-pages 工作副本（默认就是它）
    --force-channels a,b     不查发行页，强制登记这几个渠道（发行页暂时查不了时用）

安全约束：版本只升不降；下载页只写本仓库的发行页；写完会再按客户端同样的规则校验一遍。
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

REPO = "WanFengnie/LingMusic"

# 渠道 → 该版本发行里必须出现的安装包文件名（{v} = 版本号）。与 pack_*.ps1 / pack_*.sh 的产物命名一致。
ASSETS = {
    "windows-x64": "LingMusic-v{v}.zip",
    "windows-arm64": "LingMusic-v{v}-win-arm64.zip",
    "android": "LingMusic-v{v}.apk",
    "macos-arm64": "LingMusic-v{v}-mac-arm64.dmg",
    "ios": "LingMusic-v{v}.ipa",
}


def read_version(root: Path) -> str:
    text = (root / "LingVersion.props").read_text(encoding="utf-8-sig")
    m = re.search(r"<LingVersion[^>]*>\s*([0-9]+\.[0-9]+\.[0-9]+)\s*</LingVersion>", text)
    if not m:
        sys.exit("无法从 LingVersion.props 解析版本号（要求 M.m.p 三段数字）")
    return m.group(1)


def ver_tuple(v: str):
    return tuple(int(x) for x in v.split("."))


def release_assets(tag: str, require_public: bool) -> set:
    out = subprocess.run(
        ["gh", "release", "view", tag, "--repo", REPO, "--json", "assets,isDraft,isPrerelease"],
        capture_output=True, text=True, encoding="utf-8",
    )
    if out.returncode != 0:
        sys.exit(f"查不到发行 {tag}（{out.stderr.strip() or '请确认已发行且 gh 已登录'}）。"
                 "发行页暂时查不了时可用 --force-channels 强制登记。")
    data = json.loads(out.stdout)
    state = "草稿" if data.get("isDraft") else "预发布" if data.get("isPrerelease") else ""
    if state:
        # 草稿对用户不可见，登记后客户端点「下载」会 404；预发布不该推给正式渠道。
        if require_public:
            sys.exit(f"发行 {tag} 还是{state}，不登记（发布为正式发行后再来）。")
        print(f"  注意：发行 {tag} 目前是{state}，下面只是预览；加 --apply 时会拒绝。")
    return {a["name"] for a in data.get("assets", [])}


def main() -> int:
    ap = argparse.ArgumentParser(description="更新 gh-pages 的 latest.json")
    ap.add_argument("--version")
    ap.add_argument("--ghpages", default=None)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--push", action="store_true")
    ap.add_argument("--force-channels", default="")
    args = ap.parse_args()

    root = Path(__file__).resolve().parent.parent
    version = args.version or read_version(root)
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        sys.exit(f"版本号格式不对：{version}")
    tag = f"v{version}"
    ghp = Path(args.ghpages) if args.ghpages else root.parent / "Ling-ghpages"
    manifest_path = ghp / "latest.json"
    if not manifest_path.exists():
        sys.exit(f"找不到 {manifest_path}（gh-pages 工作副本不在这里？用 --ghpages 指定）")

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("schema") != 1 or "channels" not in manifest:
        sys.exit("latest.json 格式不对（schema 必须为 1）")

    if args.force_channels:
        present = {ASSETS[c.strip()].format(v=version) for c in args.force_channels.split(",") if c.strip() in ASSETS}
    else:
        present = release_assets(tag, require_public=args.apply)
    url = f"https://github.com/{REPO}/releases/tag/{tag}"

    changed = []
    for channel, pattern in ASSETS.items():
        asset = pattern.format(v=version)
        old = manifest["channels"].get(channel, {}).get("version")
        if asset not in present:
            print(f"  跳过 {channel:<14} 发行里没有 {asset}（保持 {old or '未登记'}）")
            continue
        if old and ver_tuple(old) > ver_tuple(version):
            print(f"  跳过 {channel:<14} 清单里的 {old} 比 {version} 新，版本只升不降")
            continue
        if old == version:
            print(f"  不变 {channel:<14} 已是 {version}")
            continue
        manifest["channels"][channel] = {"version": version, "url": url}
        changed.append(channel)
        print(f"  登记 {channel:<14} {old or '（新增）'} → {version}")

    if not changed:
        print("没有需要更新的渠道。")
        return 0
    if not args.apply:
        print("\n这是预览。确认无误后加 --apply 写入并在 gh-pages 本地提交。")
        return 0

    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    # 与客户端同一条规则再校验一遍
    for name, entry in manifest["channels"].items():
        assert re.fullmatch(r"\d+\.\d+\.\d+", entry["version"]), f"{name} 版本格式错误"
        assert re.match(rf"^https://github\.com/{REPO}(/|$)", entry["url"]), f"{name} 下载页不是本仓库"

    def git(*a):
        return subprocess.run(["git", "-C", str(ghp), *a], capture_output=True, text=True, encoding="utf-8")

    git("add", "latest.json")
    msg = f"chore: 更新清单 {version}（{', '.join(changed)}）"
    r = git("commit", "-m", msg)
    if r.returncode != 0:
        sys.exit("提交失败：" + (r.stdout + r.stderr).strip())
    print(f"\n已在 gh-pages 本地提交：{msg}")
    if args.push:
        r = git("push", "origin", "gh-pages")
        if r.returncode != 0:
            sys.exit("推送失败：" + (r.stdout + r.stderr).strip())
        print("已推送 gh-pages，几十秒后线上生效。")
    else:
        print("还没推送。要上线请在 Ling-ghpages 里执行：git push origin gh-pages")
    return 0


if __name__ == "__main__":
    sys.exit(main())
