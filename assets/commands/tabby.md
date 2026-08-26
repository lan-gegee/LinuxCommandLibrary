# TAGLINE

自托管的 AI 编程助手

# TLDR

以 GPU 加速**启动 Tabby 服务器**

```tabby serve --model [StarCoder-1B] --device cuda```

带聊天模型**启动服务器**

```tabby serve --model [StarCoder-1B] --chat-model [Qwen2-1.5B-Instruct] --device cuda```

仅用 **CPU 运行**

```tabby serve --model [StarCoder-1B] --device cpu```

通过 **Docker 运行**并启用 GPU 支持

```docker run -it --gpus all -p 8080:8080 -v $HOME/.tabby:/data tabbyml/tabby serve --model [StarCoder-1B] --device cuda```

为服务器**指定端口**

```tabby serve --model [StarCoder-1B] --port [8080]```

# SYNOPSIS

**tabby** serve [**--model** _name_] [**--chat-model** _name_] [**--device** _type_] [**--port** _port_]

# PARAMETERS

**--model** _name_
> 要使用的代码补全模型（例如 StarCoder-1B、CodeLlama-7B）。

**--chat-model** _name_
> 用于聊天功能的对话式 AI 模型（例如 Qwen2-1.5B-Instruct）。

**--device** _type_
> 硬件加速方式：cuda（NVIDIA GPU）、metal（Apple M1/M2）、cpu。

**--port** _port_
> API 服务器暴露的端口。默认：8080。

**--help**
> 显示帮助信息。

# DESCRIPTION

**tabby** 是一个自托管的 AI 编程助手，提供代码补全、内联编辑和聊天功能。与云端托管方案不同，Tabby 完全运行在你自己的基础设施上，让你完全掌控模型、数据和成本。

**serve** 命令启动 Tabby API 服务器，它暴露一个兼容 OpenAPI 的接口供 IDE 扩展和其他客户端使用。服务器支持多种代码补全模型，包括 StarCoder、CodeLlama 和 CodeGen 系列。

Tabby 针对消费级 GPU 进行了优化，在 Linux/Windows 上支持 NVIDIA CUDA，在 macOS 上支持 Apple Metal。没有 GPU 加速的环境可以使用纯 CPU 模式，但性能会降低。

数据默认存储在 **~/.tabby** 中，包括模型权重、配置和已索引的代码仓库。服务器会在配置的端口提供 Web UI，用于管理、模型管理和仓库索引。

# CAVEATS

GPU 加速需要相应的驱动程序（NVIDIA 需要 CUDA 工具包，Apple Silicon 使用 Metal）。根据所选模型不同，模型下载可能有数 GB 之大。自托管需要足够的硬件资源；GPU 模式建议至少 8GB 显存，CPU 模式建议至少 16GB 内存。

# HISTORY

Tabby 由 TabbyML 创建并于 **2023 年**作为开源项目发布，定位为 GitHub Copilot 的自托管替代品。该项目受到追求隐私保护和成本控制的企业和开发者的青睐。**2025 年 2 月**发布的 0.24 版本加入了 LDAP 认证，**2025 年 7 月**的 0.30 版本引入了 GitLab 合并请求上下文索引。

# INSTALL

```nix: nix profile install nixpkgs#tabby```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ollama](/man/ollama)(1), [copilot](/man/copilot)(1), [docker](/man/docker)(1)
