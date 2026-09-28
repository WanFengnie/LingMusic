# 第三方开源组件声明

> 版本号唯一来源：仓库根 `LingVersion.props`（此处不再写死，避免与产物漂移）。

泠音乐（Ling Music）发行包中随附的下列独立开源组件按其原许可证分发。

本声明随安装包提供。完整许可文本见 licenses/ 目录（含 SkiaSharp / HarfBuzzSharp native 包自带的第三方声明原文）。各组件版权行以随包 `.nuspec` 的 `<copyright>` 为准。

---

## 1. Avalonia UI 12.1.2

- 项目：https://github.com/AvaloniaUI/Avalonia
- 许可证：**MIT**
- 用途：跨平台 XAML UI 框架与 Skia 硬件加速渲染
- Copyright 2013-2026 © The AvaloniaUI Project

---

## 2. NAudio 2.2.1

- 项目：https://github.com/naudio/NAudio
- 许可证：**MIT**
- 用途：Windows 桌面端高质量音频解码、流媒体与实时频域分析
- Copyright © Mark Heath

---

## 3. TagLibSharp 2.3.0（TagLib#）

- 项目：https://github.com/mono/taglib-sharp
- 许可证：**GNU Lesser General Public License v2.1（LGPL-2.1）**
- 用途：读取本地音频标签、内嵌封面与内嵌歌词
- 发行文件：TagLibSharp.dll（独立动态库）
- 全文：[licenses/LGPL-2.1.txt](licenses/LGPL-2.1.txt)

Copyright © 2006-2007 Brian Nickel；2009-2020 Other contributors.

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

## 4. 其他随包分发的组件

以下组件由 Avalonia 与 .NET 运行时间接引入，随发行包一同分发（除注明者外均为 **MIT**）：

- **SkiaSharp 3.119.4 / HarfBuzzSharp 8.3.1.3** —— 2D 图形光栅化与文字排版引擎（`libSkiaSharp.dll` / `libHarfBuzzSharp.dll`，Android 侧为同名 `.so`），https://github.com/mono/SkiaSharp
  - 许可证：**MIT** —— Copyright © 2015-2016 Xamarin, Inc.；2017-2018 Microsoft Corporation
  - 这两个库内另外静态链接了 23 项第三方代码（ANGLE、HarfBuzz、skia、etc1、gif、libpng、DNG SDK、expat、freetype、ICU、imgui、jsoncpp、libjpeg-turbo、libwebp、libmicrohttpd、piex、sdl、sfntly、SPIR-V Headers、SPIR-V Tools、zlib），其版权声明与许可原文见
    [licenses/SkiaSharp-HarfBuzzSharp-THIRD-PARTY-NOTICES.txt](licenses/SkiaSharp-HarfBuzzSharp-THIRD-PARTY-NOTICES.txt)
    —— 2,716 行 / 139,775 B，由 `SkiaSharp.NativeAssets.*` 与 `HarfBuzzSharp.NativeAssets.*` 包原样附带，四个 native 包内该文件字节完全相同
- **ANGLE**（`av_libglesv2.dll`，随 `Avalonia.Angle.Windows.Natives 2.1.27548.20260419` 分发）—— 把 OpenGL ES 调用转译为 Direct3D 的图形后端，**BSD-3-Clause** —— Copyright 2018 The ANGLE Project Authors，全文 [licenses/ANGLE-BSD-3.txt](licenses/ANGLE-BSD-3.txt)
- **Tmds.DBus.Protocol** —— D-Bus 协议实现（Tom Deseyn），https://github.com/tmds/Tmds.DBus
- **MicroCom.Runtime** —— COM 互操作运行时（Copyright © 2021 Nikita Tsukanov），https://github.com/AvaloniaUI/Avalonia
- **.NET 运行时与 CsWinRT 投影**（Microsoft）—— 自包含发行包内含 `System.*`、`coreclr`、`hostfxr` 等 .NET 运行时文件，以及 `WinRT.Runtime`、`Microsoft.Windows.SDK.NET`

## 5. Android 发行包另含

Android 版除上述组件外，还在 APK 内捆绑下列库（各个构件以其包内附带的许可文本为准）：

- **AndroidX**（Android Open Source Project）—— **Apache License 2.0**，全文见 https://www.apache.org/licenses/LICENSE-2.0
  - 直接引用：`androidx.core`、`androidx.core.core.ktx`、`androidx.appcompat`、`androidx.media`、`androidx.window`、`androidx.window.windowjava`
  - 传递依赖：`androidx.lifecycle.*`、`androidx.fragment`、`androidx.activity` 等
- **.NET for Android 运行时**（Microsoft）—— **MIT**
- **SkiaSharp / HarfBuzzSharp native 库**（`libSkiaSharp.so`、`libHarfBuzzSharp.so`）—— 与 Windows 侧同一份第三方声明：[licenses/SkiaSharp-HarfBuzzSharp-THIRD-PARTY-NOTICES.txt](licenses/SkiaSharp-HarfBuzzSharp-THIRD-PARTY-NOTICES.txt)

---

## 与本项目协议的关系

本文件只约束随包分发的第三方库。泠音乐程序本体的使用条件见 [README.md](README.md)「项目协议」。二者冲突时：第三方库按其原许可证执行；程序本体按项目协议执行。
