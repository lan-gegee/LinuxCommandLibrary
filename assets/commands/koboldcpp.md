# TAGLINE

本地 AI 文本生成服务器与推理引擎

# TLDR

用 GGUF 模型文件**启动**

```koboldcpp --model [path/to/model.gguf]```

使用 CUDA **以 GPU 加速启动**

```koboldcpp --model [path/to/model.gguf] --usecuda --gpulayers [35]```

在自定义端口上**以 Vulkan GPU 支持**

```koboldcpp --model [path/to/model.gguf] --usevulkan --gpulayers [35] --port [8080]```

不启动服务器而**运行单条提示词**

```koboldcpp --model [path/to/model.gguf] --prompt "[What is the meaning of life?]"```

不带 Web UI 而**以 CLI 交互模式启动**

```koboldcpp --model [path/to/model.gguf] --cli```

**加载已保存的配置**文件

```koboldcpp --config [path/to/config.kcpps]```

# SYNOPSIS

**koboldcpp** [_options_] [**--model** _model_path_]

# PARAMETERS

**--model** _path_
> 指定要加载的 GGUF/GGML 模型文件

**--config** _file_
> 加载 .kcpps 配置文件

**--usecuda**
> 启用 NVIDIA CUDA GPU 加速

**--usevulkan**
> 启用 Vulkan GPU 加速（AMD/NVIDIA）

**--gpulayers** _n_
> 卸载到 GPU 的模型层数

**--threads** _n_
> 设置推理使用的 CPU 线程数

**--contextsize** _n_
> 设置以 token 计的最大上下文长度

**--port** _n_
> 更改服务器端口（默认：5001）

**--host** _addr_
> 绑定到指定的 IP 地址

**--multiuser** _n_
> 以 _n_ 个并发槽位启用多用户模式

**--password** _key_
> 要求使用给定密钥进行 API 身份验证

**--cli**
> 不启动服务器，直接启动交互式命令行界面

**--prompt** _text_
> 运行单条提示词，输出结果后退出

**--benchmark**
> 运行性能基准测试模式

**--flashattention**
> 启用 flash attention 以提升性能

**--smartcontext**
> 启用智能上下文处理以减少重复计算

**--usemmap**
> 为模型加载启用内存映射文件 I/O

**--usemlock**
> 强制模型驻留内存（防止换出）

**--ssl**
> 为 HTTPS 连接启用 SSL

**--remotetunnel**
> 启用远程隧道访问以便分享服务器

**--sdmodel** _path_
> 加载 Stable Diffusion 模型用于图像生成

**--noavx2**
> 面向不支持 AVX2 的旧 CPU 的兼容模式

**--showgui**
> 即使使用了命令行选项也显示 GUI 启动器

**--skiplauncher**
> 跳过 GUI 启动器，直接启动服务器

**--quiet**
> 抑制控制台输出

**--whispermodel** _path_
> 加载 Whisper 模型用于语音识别

**--ttsmodel** _path_
> 加载文本转语音模型

**--mmproj** _path_
> 加载多模态投影文件以获得视觉能力

**--lora** _path_
> 将 LoRA 适配器应用到基础模型

**--help**
> 显示所有可用命令

# DESCRIPTION

**koboldcpp** 是一个自成一体的 AI 文本生成服务器，可在本地运行大语言模型。它构建于 **llama.cpp** 之上，内置 Web UI（KoboldAI Lite），支持所有 GGML 和 GGUF 模型格式。它没有任何外部依赖，以单个可执行文件运行。

该服务器提供兼容 KoboldAI 和 OpenAI 格式的 API，因此可以配合大量前端和应用使用。它支持 CPU 推理，也支持通过 **CUDA**（NVIDIA）、**Vulkan**（AMD/NVIDIA）和 **Metal**（Apple Silicon）进行 GPU 加速。

除文本生成外，koboldcpp 还在同一个可执行文件中支持**图像生成**（Stable Diffusion）、**语音识别**（Whisper）和**文本转语音**。内置的 Web UI 提供多种交互模式，包括聊天、指令、冒险和故事创作。

# CONFIGURATION

不带参数启动时，koboldcpp 会打开一个用于交互式配置的 **GUI 启动器**。设置可以保存到 **.kcpps** 配置文件中，也可以从其中加载。同时使用两者时，命令行选项会覆盖 GUI 设置。

关键配置要点包括 **GPU 层卸载**（放到 GPU 的层越多推理越快，但需要更多显存）、**上下文大小**（上下文越大占用内存越多），以及**线程数**（通常设置为物理 CPU 核心数）。

# CAVEATS

模型文件可能非常大（几 GB 到超过 100 GB），需要大量内存或显存。GPU 加速需要相应的驱动和硬件支持。性能因模型大小、量化级别和可用硬件而有显著差异。Vulkan 后端兼容性更广，但在 NVIDIA 硬件上通常比 CUDA 慢。Flash attention 需要兼容的模型架构。

# HISTORY

KoboldCpp 由一位化名 **LostRuins**（又名 **Concedo**）的开发者创建，于 **2023 年 3 月 16 日**首次发布，是 **llama.cpp** 与 KoboldAI 界面结合的分支。它的设计目标是提供一种简单、自成一体的方式来在本地运行大语言模型，无需复杂配置。该项目随开源 LLM 浪潮迅速成长，持续加入多模态支持、GPU 后端和图像生成等特性。它采用 **AGPL-3.0** 许可证。

# INSTALL

```nix: nix profile install nixpkgs#koboldcpp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ollama](/man/ollama)(1)
