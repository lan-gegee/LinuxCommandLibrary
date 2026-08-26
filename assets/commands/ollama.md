# TAGLINE

在本地运行大型语言模型

# TLDR

**以交互方式运行模型**

```ollama run [llama3]```

**带提示词运行模型**

```ollama run [llama3] "[What is the capital of France?]"```

**列出已安装的模型**

```ollama list```

**拉取模型**

```ollama pull [mistral]```

**显示模型信息**

```ollama show [llama3]```

**列出正在运行的模型**

```ollama ps```

**删除模型**

```ollama rm [model_name]```

**启动 API 服务器**

```ollama serve```

# SYNOPSIS

**ollama** [_command_] [_options_]

# PARAMETERS

**run** _MODEL_ [_PROMPT_]
> 交互式运行模型，或用一次性提示词运行。

**pull** _MODEL_
> 从仓库下载模型。

**push** _MODEL_
> 将模型推送到仓库。

**list**（或 **ls**）
> 列出本地可用的模型。

**show** _MODEL_
> 显示模型信息（架构、参数、许可证）。

**ps**
> 列出当前正在运行的模型。

**stop** _MODEL_
> 停止正在运行的模型。

**rm** _MODEL_
> 删除本地模型。

**cp** _SOURCE_ _DESTINATION_
> 在本地以新名称复制模型。

**serve**
> 启动 Ollama API 服务器（默认端口 11434）。

**create** _NAME_ **-f** _MODELFILE_
> 基于 Modelfile 创建自定义模型。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ollama** 用于在本地运行大型语言模型。它负责模型下载，通过 REST API 提供服务，并支持交互式对话会话。

支持多种开源模型，包括 Llama、Mistral、Gemma、Phi、Qwen、DeepSeek 等。模型从 Ollama 仓库拉取并缓存在本地。

API 服务器提供与 OpenAI 兼容的端点，涵盖聊天补全、嵌入和模型管理。可以使用 Modelfile 创建自定义模型，在其中指定基础模型、系统提示词、参数和适配器层。

# CAVEATS

需要足够的 RAM/VRAM，具体取决于模型大小。支持 GPU 加速（NVIDIA、AMD、Apple Silicon）。API 服务器默认监听 localhost:11434；可通过 OLLAMA_HOST 环境变量配置。

# HISTORY

**Ollama** 由 **Jeffrey Morgan** 创建，于 **2023** 年首次发布。它基于 **llama.cpp** 构建，简化了在本地下载、运行和管理开源语言模型的流程。随着人们在无需云端 API 的情况下运行 LLM 的需求增长，该项目迅速流行起来。

# INSTALL

```dnf: sudo dnf install ollama```

```pacman: sudo pacman -S ollama```

```apk: sudo apk add ollama```

```zypper: sudo zypper install ollama```

```brew: brew install ollama```

```nix: nix profile install nixpkgs#ollama```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[llama.cpp](/man/llama.cpp)(1), [llamafile](/man/llamafile)(1)
