<p align="center">
  <img src="https://github.com/user-attachments/assets/0051f112-645f-47c7-9947-252959083bc1" width="128" alt="泠音乐 Ling Music"/>
</p>

<h1 align="center">泠音乐</h1>
<h4 align="center">Ling Music</h4>
<p align="center">原生美观的 Windows 音乐播放器</p>

<p align="center">
  <img alt=".NET 10" src="https://img.shields.io/badge/.NET-10-512BD4?logo=dotnet&logoColor=white">
  <img alt="WPF" src="https://img.shields.io/badge/UI-WPF-0078D4?logo=windows&logoColor=white">
  <img alt="NAudio" src="https://img.shields.io/badge/Audio-NAudio%202.2-orange">
  <img alt="Windows" src="https://img.shields.io/badge/Platform-Windows%2010%2B-0e7a0d">
  <img alt="Version" src="https://img.shields.io/badge/Version-0.3.1-FC3C44">
</p>

<p align="center">
  本软件主体为 <b>本地音乐播放器</b><br>
  网易云音乐与 QQ 音乐接口仅供学习研究且不能保证时刻可用<br>
  如构成侵权，将立即删除相关内容与能力<br>
  请尊重版权，支持正版
</p>



## 界面预览

<p align="center">
  <img src="https://raw.githubusercontent.com/WanFengnie/LingMusic/assets/screenshot-home.png" width="49%" alt="资料库首页">
  <img src="https://raw.githubusercontent.com/WanFengnie/LingMusic/assets/screenshot-local.png" width="49%" alt="本地曲库">
</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/WanFengnie/LingMusic/assets/screenshot-player-blue.png" width="49%" alt="播放页 · 扁平主题">
  <img src="https://raw.githubusercontent.com/WanFengnie/LingMusic/assets/screenshot-player-red.png" width="49%" alt="播放页 · 黑胶封面">
</p>

## 下载

本仓库 **不包含源码，也不包含安装包**。<br>请到 [Releases](https://github.com/WanFengnie/LingMusic/releases) 下载压缩包，解压后运行 `Ling.exe`。

要求：Windows 10 及以上（x64）。无需自行编译。

目前本项目的原始发布地址只有 [**GitHub**](https://github.com/WanFengnie/LingMusic)，其他渠道均为第三方转载，与本项目无关。


## 安全提示

**病毒查杀与误报说明**：因个人项目未购买昂贵的商业数字签名证书，Windows SmartScreen 或部分杀毒软件可能将未签名的可执行程序标记为“未知发布者”或产生误报拦截。程序无任何恶意代码或后台后门，可点击“仍要运行”或添加到安全信任名单，亦可上传至第三方查毒平台自行检测。


## 功能

### 1. 本地曲库
- 自选文件夹扫描与文件拖入收录，无系统全局扫描
- 支持主流音频格式：`MP3`、`FLAC`、`WAV`、`M4A`、`AAC`、`OGG`、`APE`、`WMA`
- 可解析音频标题、艺人、专辑、时长、内嵌封面与内嵌歌词
- 支持本地音频标签元数据手动编辑并同时写回物理文件
- 支持内嵌歌词与同目录 `.lrc` 文件解析
- 支持本地独立歌单创建、单曲收藏及歌单封面自定义

### 2. 多源集成
- 侧边栏支持 **本地曲库**、**网易云音乐**、**QQ 音乐** 三种平台模式切换，各平台资料库、登录态与歌单独立管理
- 支持在线歌曲/歌单检索、每日推荐、官方排行榜及云端歌单同步
- 支持将常用歌单固定至主界面侧边导航栏

### 3. 播放与音频控制
- 支持断点平滑续播
- 支持顺序播放、单曲循环、随机播放
- 支持外设按键控制

### 4. 视觉呈现与视听交互
- 支持扁平与浮岛两种主题
- 具备自适应色彩提取与动态流光背景渲染
- 支持对齐方式、基准字号、字体粗细调节
- 支持双语歌词
- 支持非当前句缩放/透明度/模糊控制
- 支持多种歌词动态动效
- 黑胶/圆角封面样式切换

## 隐私处理

- **数据本地化存储**：程序所有配置参数、歌单数据、曲库索引及播放记忆均保存在当前设备的本地系统目录（`%APPDATA%\Ling`），不部署任何外部数据收集或中转服务。
- **登录凭据保护**：程序不收集或保存账号明文密码。第三方平台登录凭据（Cookie / Token）采用 Windows DPAPI（数据保护应用程序编程接口）进行硬件绑定加密，仅限当前 Windows 用户会话具备解密权限。
- **磁盘读取权限边界**：文件扫描操作仅限于明确选定或拖入的目标目录与文件，不访问未授权的系统路径，不执行全盘遍历扫描。
- **网络通信边界**：网络交互仅与对应官方音乐服务接口直接建立安全连接（HTTPS）以获取音频流与元数据，程序内不包含任何遥测（Telemetry）、用户行为追踪或第三方广告代码。


## 数据存储

| 内容 | 位置 |
|------|------|
| 设置、登录态、歌单、播放记忆 | `%APPDATA%\Ling\settings.json` |
| 本地曲库索引 | `%APPDATA%\Ling\local_library.json` |
| 内嵌封面缓存 | `%LOCALAPPDATA%\Ling\covers` |


## 常见问题

**为什么有的歌提示没有可播放的音源？**  
未登录、无相应会员、或平台侧无版权时，接口不会返回播放地址。请登录对应账号，或改听本地文件。本项目不会绕过这一限制。若接口只返回试听片段，状态栏会提示「试听中」，完整播放需对应平台会员。

**高音质没生效？**  
确认已登录、账号权益足够，并且音质设置匹配<br>
无会员时接口会按档位向下回退，不会解锁会员曲库

**扫码遇到问题？**  
二维码会过期，点击刷新<br>
网络环境可能导致登录接口失败<br>
如果始终存在问题可能是接口失效请提交反馈


**会扫描整个磁盘吗？**  
不会，只扫描明确添加或拖入的文件夹/文件




## 使用的开源组件

程序本体源码暂不开放。发行包中的独立动态库仍按其原许可证分发，详见 [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md)。

| 组件 | 许可 | 用途 | 发行文件 |
|------|------|------|----------|
| [NAudio](https://github.com/naudio/NAudio) 2.2.1 | MIT | 播放、解码、频谱 | `NAudio*.dll` |
| [TagLibSharp](https://github.com/mono/taglib-sharp) 2.3.0 | LGPL-2.1 | 本地标签、封面、内嵌歌词 | `TagLibSharp.dll` |

- MIT 全文：[`licenses/MIT-NAudio.txt`](licenses/MIT-NAudio.txt)
- LGPL-2.1 全文：[`licenses/LGPL-2.1.txt`](licenses/LGPL-2.1.txt)
- TagLibSharp **未静态链入** `Ling.exe`。可将安装目录中的 `TagLibSharp.dll` 替换为接口兼容的修改版。
- 本项目未修改 TagLibSharp。对应源码：https://github.com/mono/taglib-sharp/tree/TaglibSharp-2.3.0.0
  
## 版权

**播放器著作权归属**：泠音乐（Ling Music）播放器程序本体的架构实现、原创交互界面设计及相关美术资产等软件著作权与知识产权均归属于原作者（[WanFengnie](https://github.com/WanFengnie)）所有。未经原作者书面授权许可，严禁用于任何形式的商业分发、二次打包转售或商业牟利。

## 第三方音乐声明

本软件为非盈利性软件、请勿将此软件用于商业用途

- **不提供** VIP 音源破解、解灰、付费内容解锁等服务。高音质与会员曲库取决于你在对应平台已取得的身份。
- 所有在线内容（音源、封面、歌词、歌单、用户资料等）版权归 **网易云音乐**、**QQ 音乐** 及唱片版权方所有。
- 软件主体是本地多媒体播放器；网易云音乐与 QQ 音乐仅为学习研究用途，不对数据的合法性、准确性负责。
- 如构成侵权，请通过 Issue 或联系作者，相关内容与在线能力将立即删除。


## 项目协议

本项目的第三方音乐接入功能以学习、研究技术可行性为目的发布。以下条款约束泠音乐程序本体的使用。随包分发的第三方库（NAudio、TagLibSharp 等）仍按各自原许可证执行，本协议不覆盖这些许可证。

---

词语约定：本协议中的「本项目」指泠音乐（Ling Music）；「使用者」指使用本项目的个人；「官方音乐平台」指网易云音乐、QQ 音乐等；「版权数据」指包括但不限于音频、歌词、图像、歌单名、艺人名等他人拥有版权的数据。

### 一、数据来源

1.1 本项目的在线数据来自各平台接口（与在网页或未越权状态下可取得的数据同类），经筛选后展示。本项目不对数据的合法性、准确性负责。

1.2 本项目本身不生产音频文件。播放在线歌曲时，仅向接口请求播放地址；若接口返回链接，则按该链接播放。链接是否对应期望曲目、能否播放，以平台为准。


### 二、版权数据

2.1 使用过程中可能缓存封面、歌词、登录凭据等版权或隐私数据。如权利方认为构成侵权，作者将删除相关内容与在线能力。

### 三、平台名称

3.1 文中「网易云音乐」「QQ 音乐」等为对官方平台的中性称呼。若平台方认为不妥，可联系更改或移除相关对接。

### 四、资源使用

4.1 项目内部分字体、图标、参考实现来自互联网或开源社区。如出现侵权，可联系移除。

### 五、免责声明

5.1 因使用或无法使用本项目造成的任何直接、间接、特殊、偶然或结果性损害（包括但不限于数据丢失、账号异常、设备故障、商誉或商业损失）由使用者自行承担。

### 六、使用限制

6.1 本项目免费使用，面向学习交流。不对其中技术是否符合使用者所在地法律法规作保证。

6.2 禁止在违反当地法律法规的情况下使用本项目。 由此产生的一切后果由使用者承担。

6.3 禁止使用本项目从事破解、盗链牟利、批量爬取、商业分发或任何侵犯版权的行为。

### 七、版权保护

7.1 音乐平台与创作者不易，请尊重版权，支持正版。需要高音质或会员曲库时，请在官方应用内开通相应服务。

### 八、非商业性质

8.1 本项目仅用于技术学习与研究，禁止用作商业用途

### 九、接受协议

9.1 若你下载、运行或分发了本项目，即代表你接受本协议。

---

请支持正版：

- [网易云音乐](https://music.163.com/)
- [QQ 音乐](https://y.qq.com/)
