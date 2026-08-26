# TAGLINE

端侧语音识别、意图匹配与文本转语音

# TLDR

**安装** Python 软件包（同时安装 CLI）

```pip install moonshine-voice```

把**实时麦克风**输入转录到终端

```moonshine-voice mic --language [en]```

**转录 WAV 文件**（可选说话人 ID 和词级时间戳）

```moonshine-voice transcribe --wav-path [audio.wav] --speaker-ids --word-timestamps```

**合成语音**并播放（或写入 WAV）

```moonshine-voice tts --language [en_us] --text ["Hello world"]```

从一小段参考音频**克隆音色**，然后朗读文本

```moonshine-voice tts --clone [reference.wav] --text ["This is my cloned voice"]```

从麦克风**识别口述意图**

```moonshine-voice intent --intents ["turn on the lights,turn off the lights,what is the weather"]```

**下载模型资源**（STT、TTS、G2P 或 intent）

```moonshine-voice download --stt --language [en]```

用内置 G2P 引擎**把文本转换为 IPA 音素**

```moonshine-voice g2p --language [en_us] --text ["Hello world"]```

# SYNOPSIS

**moonshine-voice** _command_ [_options_]

**moonshine-voice** {**mic** | **transcribe** | **tts** | **intent** | **download** | **g2p**} [_options_]

# DESCRIPTION

**moonshine-voice** 是 **Moonshine Voice** 的命令行前端。Moonshine Voice 是一套面向实时语音交互的开源端侧工具包。同一个软件包同时提供 Python 库和可移植的 C++ 核心；通过 **pip** 安装后，**moonshine-voice**（以及更短的 **moonshine** 别名）会作为内置演示模块之上的一个轻量分发器注册进来。

模型缓存之后，所有处理都可以完全离线运行。流式 STT 模型采用灵活的输入窗口和增量缓存，因此即使用户还在讲话，部分转录结果也会持续更新，相比固定 30 秒窗口的 Whisper 式方案，实时麦克场景下的延迟更低。该技术栈还涵盖语义**意图**匹配、多引擎 **TTS**（Kokoro、Piper 以及可选音色克隆的 ZipVoice），以及供合成使用的 MIT 许可的字素转音素（**G2P**）路径。

STT 支持的语言包括英语、西班牙语、中文普通话、日语、韩语、越南语、乌克兰语和阿拉伯语（各语言专用模型）。TTS 通过 Kokoro/Piper/ZipVoice 语音包覆盖更多地区语言。该项目还另行发布了面向微控制器的 **Moonshine Micro** 版本（在约 500 KiB 内存内实现 VAD/STT/TTS），与本 CLI 分开。

# COMMANDS

**mic**

> 从默认麦克风采集音频流，并把实时的转录更新打印到终端。

**transcribe**

> 离线转录 WAV 文件。支持说话人分离（**--speaker-ids**）和词级时间戳（**--word-timestamps**）。

**tts**

> 从文本合成语音，输出到 WAV 文件或默认音频设备。可通过 **--clone** 使用 ZipVoice 克隆音色。

**intent**

> 监听用户定义的动作短语（逗号分隔），并报告带置信度的语义匹配结果。

**download**

> 把 STT、TTS、G2P 或 intent/嵌入模型资源预取到本地缓存（或自定义的 **--root**）。

**g2p**

> 使用 Moonshine 的 G2P 引擎将输入文本转换为国际音标（IPA）。

# PARAMETERS

通用顶层选项：

**-h**, **--help**

> 显示用法及子命令列表。

**-V**, **--version**

> 打印已安装的 **moonshine-voice** 软件包版本。

子命令标志（最常用）：

**mic** / **intent**: **--language** _code_（默认 **en**）、**--model-arch** _n_

**transcribe**: **--wav-path** _file_、**--language** _code_、**--model-path** _dir_、**--speaker-ids**、**--word-timestamps**、**--quiet**、**--options** _key=value,..._

**tts**: **--language** _tag_（默认 **en_us**）、**--text** _string_、**--voice** _id_、**--clone** _wav_、**--clone-transcript** _text_、**--out** _path_、**--device** _index_or_name_、**--asset-root** _path_、**--options** _KEY=VALUE_

**download**: **--stt**、**--tts**、**--g2p**、**--intent**、**--language** _tag_、**--voice** _id_、**--root** _dir_（**--stt** / **--tts** / **--g2p** / **--intent** 至少需要其一）

**g2p**: **-l** / **--language** _tag_、**--text** _string_、**--asset-root** _path_、**--no-download**

**intent**: **--intents** _comma-list_、**--threshold** _float_（默认 **0.8**）、**--wav-file** _path_、**--embedding-model** _name_、**--quantization** {_fp32_ | _fp16_ | _q8_ | _q4_ | _q4f16_}

每个子命令也接受 **--help** 以查看其完整标志列表。用相同的标志调用 **python -m moonshine_voice.**_module_ 是等价的。

# CAVEATS

首次运行下载模型需要访问 **download.moonshine.ai**（或该软件包使用的 Hugging Face 镜像）；此后只要资源已缓存即可离线推理。实时麦克风模式需要可用的采集设备和相应的操作系统音频权限。在 Raspberry Pi OS 上，系统级安装通常需要 **pip install --break-system-packages**（或使用 virtualenv）。基于 **--clone** 的 TTS 使用 ZipVoice，比 Kokoro/Piper 慢。**moonshine** 这个短名只是同一入口的别名，并非独立工具。

# HISTORY

Moonshine 第一代模型随论文 *Moonshine: Speech Recognition for Live Transcription and Voice Commands*（arXiv:2410.15608）发布。后续工作加入了针对特定语言的 "Flavors of Moonshine" 模型，以及面向流式延迟和边缘精度的第二代模型，最终形成了 **Moonshine Voice** 多平台库和 **moonshine-voice** pip 包（Python 控制台脚本加 C++/Swift/Android 绑定）。该项目由 **Moonshine AI** 基于 MIT 许可证开发。

# INSTALL

```aur: yay -S moonshine```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[whisper](/man/whisper)(1), [faster-whisper](/man/faster-whisper)(1), [piper](/man/piper)(1), [tts](/man/tts)(1), [deepspeech](/man/deepspeech)(1)

# RESOURCES

```[Source code](https://github.com/moonshine-ai/moonshine)```

```[Homepage](https://moonshine.ai)```

```[Documentation](https://github.com/moonshine-ai/moonshine#readme)```

<!-- verified: 2026-07-18 -->
