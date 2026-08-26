# TAGLINE

本地多模态 AI 推理运行时与 CLI

# TLDR

**检查**机器并列出推荐模型

```mere.run setup```

```mere.run model capabilities --recommended```

**拉取**小型图像模型并**生成**图像

```mere.run model pull image-zimage-nano```

```mere.run image generate --model image-zimage-nano --prompt "[a ceramic mug in soft morning light]" --output [./mug.png]```

与本地文本模型**对话**

```mere.run text chat --model [text-chat-gemma4-12b-4bit] --prompt "[Explain unified memory.]"```

将语音**合成**为 WAV 文件

```mere.run speech synthesize "[Hello from mere.run]" --output [./hello.wav]```

在本地回环地址上**提供** OpenAI 兼容的 API

```mere.run api serve --engine [text-chat-gemma4]```

**列出**已安装的模型和运行时状态

```mere.run model list```

```mere.run status```

# SYNOPSIS

**mere.run** [_global-options_] _command_ [_subcommand_] [_options_] [_args_...]

# PARAMETERS

**setup**
> 面向本地运行时和模型库的引导式首次运行设置。

**guide** [_command-path_]
> 按命令路径阅读随附的离线操作手册；用 **guide --list** 可列出全部手册。

**model** {_list_, _pull_, _remove_, _info_, _capabilities_, _runtime_, _benchmark_, ...}
> 管理本地模型库：按托管 ID 拉取、检查安装状态，并报告本机可运行的模型。

**image** {_generate_, _train-lora_, _run-plan_, _validate_, ...}
> 本地图像生成、LoRA 训练及相关图像工作流。

**text** {_chat_, _code_, _embed_, _anonymize_, _train-lora_}
> 本地对话、代码生成（llama.cpp）、嵌入向量和个人身份信息脱敏。

**speech** {_synthesize_, _transcribe_, _diarize_, _listen_, _profile_}
> 语音合成、自动语音识别、说话人分离和声纹配置。

**vision** {_caption_, _inspect_, _face_, _ground_, _segment_, _track_, _pose_, _ocr_, ...}
> 图像描述生成、视觉问答、人脸分析、目标定位、分割、跟踪、姿态估计和 OCR。

**music** {_analyze_, _generate_, _realtime_, _transcribe_}
> 音乐生成、分析、实时演奏和 MIDI 转写。

**sfx** {_generate_, _video_, _ae_, _clap_, ...}
> 音效生成，包括基于视频条件驱动的拟音。

**video** {_generate_, _animate_, _prepare-masks_, _session_, ...}
> 本地视频生成与主体动画流水线。

**api serve**
> 在本地主机/端口上提供 OpenAI 兼容的聊天、嵌入、图像、TTS 和 STT 服务。

**status**
> 显示本地服务器、正在服务的模型、模型库路径及已安装模型。

**plugin** {_list_, _info_, _install_, _doctor_}
> 发现并管理配套的可执行插件。

**--models-root** _path_
> 为本次调用覆盖本地模型库目录。

**--help**
> 显示公开命令树或某个组/子命令的帮助。

# DESCRIPTION

**mere.run** 是一个以本地优先的推理运行时和面向公众的多模态生成与理解 CLI。一条命令即可涵盖图像、文本、语音、视觉、音乐、声音、视频、3D 相关重建辅助功能、模型管理，以及可选的 OpenAI 兼容 API 服务器。可选的 macOS Studio 应用复用同一套 CLI、模型库和运行历史，而不依赖独立的后端。

该 CLI 以模态为先：创作与分析类工作位于 **image**、**text**、**speech**、**vision**、**music**、**sfx**、**video** 等组之下，而 **model**、**adapter**、**api**、**status**、**plugin** 负责运维操作。托管模型 ID 会被拉取到本地模型库（macOS 上默认位于 Application Support 下）；在大体积下载之前请先使用 **model capabilities**。随附的离线操作手册可通过 **mere.run guide** 查看。

主要开发目标是 Apple Silicon macOS；同时提供面向无界面环境的 Linux CLI 包，但不包含 macOS SwiftUI studio。媒体工作流通常要求 **ffmpeg** 和 **ffprobe** 在 **PATH** 中（可通过 **MERERUN_FFMPEG** / **MERERUN_FFPROBE** 覆盖）。

# CONFIGURATION

**~/Library/Application Support/MereRun/models**
> macOS 上的默认本地模型库。可用 **MERERUN_MODELS_DIR** 或 **--models-root** 覆盖。

**MERERUN_HUB_CACHE** / **MERERUN_MODEL_CACHE_HOME**
> 控制 **model pull** 及自动下载路径所使用的 Hugging Face 快照缓存。

**MERERUN_API_KEY**
> 用于非回环 **api serve** 绑定的 API 密钥；默认情况下回环绑定无需认证即可运行。

**MERERUN_FFMPEG** / **MERERUN_FFPROBE**
> 当 ffmpeg/ffprobe 未在 **PATH** 中找到时的绝对路径。

使用 **mere.run config** {_get_, _set_, _unset_, _list_, _path_} 管理当前模型库旁边的运行时配置。

# CAVEATS

大模型需要大量 RAM/统一内存；拉取前请先用 **model capabilities** 检查。许可证、下载体积和硬件适配因模型 ID 而异——重新分发权重前请查阅项目的 model-sources 文档。Linux 支持面向无界面 CLI；SwiftUI studio 和 DMG 安装包仅限 macOS。将 **api serve** 绑定到回环之外需要显式设置 API 密钥。聊天中的工具循环和 shell 功能需要通过显式开关启用，这些开关会削弱默认安全策略。

# HISTORY

**mere.run** 是由 **sawfwair** 开发的开源 Swift/MLX 本地推理运行时与 CLI，将多模态创作工作流（图像、文本、语音、视觉、音频、视频）封装在单一 **mere.run** 可执行文件之后，并提供可选的 macOS Studio 与 Linux 无界面软件包。

# SEE ALSO

[ollama](/man/ollama)(1), [llama.cpp](/man/llama.cpp)(1), [ffmpeg](/man/ffmpeg)(1)

# RESOURCES

```[Source code](https://github.com/sawfwair/mere-run)```

```[Homepage](https://mere.run)```

```[Documentation](https://docs.mere.run/)```

<!-- verified: 2026-07-31 -->
