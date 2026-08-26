# TAGLINE

macOS 本地双声道会议转录工具

# TLDR

通过 Homebrew **安装**并授予权限

```brew tap rokib16x/listnr https://github.com/rokib16x/listnr```

```brew trust --tap rokib16x/listnr```

```brew install listnr```

```listnr setup```

启动**交互式** shell，然后进行实时转录

```listnr```

```/live```

为**N 秒**的一次性会话录音，预期两位远程发言人

```listnr start --seconds 60 --speakers 2```

转录**孟加拉语**（或其他支持的语言）

```listnr start --language bn --seconds 120```

用任意语言发言；转录稿为**英文**

```listnr start --language bn --translate --seconds 120```

**列出 / 下载** Whisper 模型

```listnr models list```

```listnr models download whisper-large-v2```

检查**权限**和环境

```listnr doctor```

# SYNOPSIS

**listnr** [_command_] [_options_]

# PARAMETERS

**(no command)**
> 启动交互式 REPL（**listnr>** 提示符）。常用的会话内命令：**/live** [_seconds_]、**/stop** 或 **q**、**/lang** _code_、**/translate**、**/speakers** _n_、**/model** _id_、**/diarize**、**/sensitivity** high|low、**/dump**、**/status**、**/help**。

**start** [**--seconds** _n_] [**--speakers** _n_] [**--language** _code_] [**--translate**] ...
> 不进入交互 shell 的一次性录制。转录稿写入 **stdout**；进度和音量指示写入 **stderr**。省略 **--seconds** 时将持续运行直到按下 Ctrl+C。

**setup**
> 引导你向宿主终端应用授予**麦克风**以及**屏幕与系统音频录制**权限。

**doctor**
> 报告缺失的权限和依赖项。

**models list**
> 列出可用的 WhisperKit 模型 ID 和大小。

**models download** _id_
> 从 Hugging Face 预取模型权重到本地缓存。

# DESCRIPTION

**listnr** 是一款 macOS 命令行会议监听工具。它捕获**两条独立的音频通道**：你的**麦克风**（始终标记为 **You**）和**系统 / 扬声器音频**（远程参会者）。两条通道都使用 **WhisperKit**（Core ML）在**设备本地**转录。会话结束后，远程发言人通过 **SpeakerKit** 的说话人分离被拆分为 **Speaker 1…N**。除了一次性的模型下载外，音频和转录稿不会离开本机。

强烈建议佩戴**耳机**，以免远程音频串入麦克风通道。每次会话会在 **~/Documents/Listnr/** 下生成 Markdown 转录稿。可选的 **/dump** 会以仅所有者可读的权限写出原始 WAV 调试音频。

支持的语言包括英语、孟加拉语、印地语、西班牙语、法语、德语、日语和中文。**/translate** 使用 Whisper 的翻译成英语任务（单向）。默认模型兼顾实时延迟；更大的模型能提高准确率，但会牺牲实时性余量。

# CAVEATS

**仅支持 Apple Silicon 上的 macOS 14+**（不支持 Intel Mac）。权限与**终端应用**绑定而非二进制文件——在 Terminal 与 iTerm 之间切换需要重新授权。测试版软件（**0.x**）：CLI 标志和行为可能变化。远程说话人的分离在你停止之后才运行（实时标签一律为 **Others**）。内存占用随会话时长增长（双声道音频在内存中约每小时 460 MB）。根据当地法律，录制他人可能需要**所有参与方同意**——使用前请先取得同意。语言和模型等会话选项目前不会跨重启保留。

# HISTORY

**Listnr** 是 Rokibul Hasan 开发的 MIT 许可开源项目。它基于 **WhisperKit** / **SpeakerKit** 实现设备端语音识别和说话人分离，以预构建的 Homebrew formula、经公证的 **.pkg** 以及通过 Swift Package Manager 的源码构建方式分发。

# SEE ALSO

[whisper](/man/whisper)(1), [ffmpeg](/man/ffmpeg)(1)

# RESOURCES

```[Source code](https://github.com/rokib16x/listnr)```

```[Homepage](https://github.com/rokib16x/listnr)```

<!-- verified: 2026-08-04 -->
