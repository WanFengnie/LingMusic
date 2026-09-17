# 第三方开源组件声明 (v0.5.0 new)

泠音乐（Ling Music）发行包中随附的下列独立开源组件按其原许可证分发。

本声明随安装包提供。完整许可文本见 licenses/ 目录。

---

## 1. Avalonia UI 11.2

- 项目：https://github.com/AvaloniaUI/Avalonia
- 许可证：**MIT**
- 用途：跨平台 XAML UI 框架与 Skia 硬件加速渲染
- Copyright © .NET Foundation and Contributors

---

## 2. CSCore 1.2.1

- 项目：https://github.com/filoe/cscore
- 许可证：**Microsoft Public License (MS-PL)**
- 用途：Windows 桌面端高质量音频解码、流媒体与实时频域分析
- 全文：[licenses/MS-PL.txt](licenses/MS-PL.txt)
- Copyright © 2013-2017 Florian R.

---

## 3. TagLibSharp 2.3.0（TagLib#）

- 项目：https://github.com/mono/taglib-sharp
- 许可证：**GNU Lesser General Public License v2.1（LGPL-2.1）**
- 用途：读取本地音频标签、内嵌封面与内嵌歌词
- 发行文件：TagLibSharp.dll（独立动态库）
- 全文：[licenses/LGPL-2.1.txt](licenses/LGPL-2.1.txt)

Copyright © The TagLib# Contributors.

对应上游版本：https://github.com/mono/taglib-sharp/tree/TaglibSharp-2.3.0.0  
NuGet：https://www.nuget.org/packages/TagLibSharp/2.3.0

### 按 LGPL-2.1 第 6 条说明

1. **显著声明**：本程序使用 TagLib#，该库及其使用受 GNU LGPL-2.1 约束。
2. **提供许可证**：完整 LGPL-2.1 文本位于发行包 licenses/LGPL-2.1.txt。
3. **提供库源码**：本项目未修改 TagLibSharp。对应源码可从此处取得（等效提供，LGPL-2.1 §6(d)）：
   - https://github.com/mono/taglib-sharp/tree/TaglibSharp-2.3.0.0
   - https://www.nuget.org/packages/TagLibSharp/2.3.0
4. **替换权**：可将发行目录中的 TagLibSharp.dll 替换为接口兼容的修改版，程序通过运行时加载该 DLL，无需重新编译泠音乐。
5. **逆向工程**：仅为调试或替换上述 LGPL 库之目的，允许对与该库的链接进行必要的逆向。
6. **未修改**：若未来修改了 TagLibSharp 本身，修改部分将按 LGPL-2.1 公开。当前发行未修改该库。

“泠音乐”代码不是 TagLib# 的衍生作品，不因使用该库而改为 LGPL 或 GPL。

---

## 与本项目协议的关系

本文件只约束随包分发的第三方库。泠音乐程序本体的使用条件见 [README.md](README.md)「项目协议」。二者冲突时：第三方库按其原许可证执行；程序本体按项目协议执行。
