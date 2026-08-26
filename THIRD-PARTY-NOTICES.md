# 第三方开源组件声明

泠音乐（Ling Music）程序本体源码暂不开放。发行包中随附的下列独立动态库仍按其原许可证分发。

本声明随安装包提供。完整许可文本见 `licenses/` 目录。

---

## 1. NAudio 2.2.1

- 项目：https://github.com/naudio/NAudio
- 许可证：**MIT**
- 用途：音频解码、播放、频谱
- 发行文件：`NAudio.dll` 以及 `NAudio.Core.dll`、`NAudio.WinMM.dll`、`NAudio.Wasapi.dll`、`NAudio.Asio.dll`、`NAudio.Midi.dll`、`NAudio.WinForms.dll` 等
- 全文：[`licenses/MIT-NAudio.txt`](licenses/MIT-NAudio.txt)

Copyright 2020 Mark Heath

---

## 2. TagLibSharp 2.3.0（TagLib#）

- 项目：https://github.com/mono/taglib-sharp
- 许可证：**GNU Lesser General Public License v2.1（LGPL-2.1）**
- 用途：读取本地音频标签、内嵌封面与内嵌歌词
- 发行文件：`TagLibSharp.dll`（独立动态库，**未**静态链入 `Ling.exe`）
- 全文：[`licenses/LGPL-2.1.txt`](licenses/LGPL-2.1.txt)

Copyright © The TagLib# Contributors.

对应上游版本：https://github.com/mono/taglib-sharp/tree/TaglibSharp-2.3.0.0  
NuGet：https://www.nuget.org/packages/TagLibSharp/2.3.0

### 按 LGPL-2.1 第 6 条说明

1. **显著声明**：本程序使用 TagLib#，该库及其使用受 GNU LGPL-2.1 约束。
2. **提供许可证**：完整 LGPL-2.1 文本位于发行包 `licenses/LGPL-2.1.txt`。
3. **提供库源码**：本项目未修改 TagLibSharp。对应源码可从此处取得（等效提供，LGPL-2.1 §6(d)）：
   - https://github.com/mono/taglib-sharp/tree/TaglibSharp-2.3.0.0
   - https://www.nuget.org/packages/TagLibSharp/2.3.0
4. **替换权**：可将发行目录中的 `TagLibSharp.dll` 替换为接口兼容的修改版，程序通过运行时加载该 DLL，无需重新编译泠音乐。
5. **逆向工程**：仅为调试或替换上述 LGPL 库之目的，允许对与该库的链接进行必要的逆向。
6. **未修改**：若未来修改了 TagLibSharp 本身，修改部分将按 LGPL-2.1 公开。当前发行未修改该库。

“泠音乐”代码不是 TagLib# 的衍生作品，不因使用该库而改为 LGPL 或 GPL。

---

## 与本项目协议的关系

本文件只约束随包分发的第三方库。泠音乐程序本体的使用条件见 [README.md](README.md)「项目协议」。二者冲突时：第三方库按其原许可证执行；程序本体按项目协议执行。
