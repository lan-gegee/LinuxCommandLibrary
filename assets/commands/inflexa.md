# TAGLINE

面向可复现生物分析的本地优先 CLI

# TLDR

**通过 Homebrew 安装**

```brew install inflexa-ai/tap/inflexa```

**一次性初始化设置**（模型提供商、沙箱镜像、本地服务）

```inflexa setup```

**在数据目录中启动** TUI

```inflexa```

**在初始化后修改**配置

```inflexa config```

**通过官方安装脚本安装**

```curl -fsSL https://inflexa.ai/install.sh | bash```

**免全局安装运行**（Node 18+）

```npx @inflexa-ai/inflexa```

# SYNOPSIS

**inflexa** [_command_] [_options_]

# DESCRIPTION

**inflexa** 是一个本地优先的智能体 CLI，用于可复现的生物与生物信息学数据分析。它把自然语言请求转换为可运行的代码，在隔离沙箱中执行，并记录完整的来源信息（provenance），使结果可审计、可重放。

默认情况下，数据、代码和结果都保留在本机。分析在资源受限的 Docker 沙箱中运行，且默认无网络访问。模型提供商自带（bring-your-own）：可以使用云端 API（Claude、OpenAI、Gemini 等，经本地代理），也可以使用完全本地的模型实现离线使用。来源与血缘信息存储在本地 SQLite 数据库中。

**inflexa setup** 会引导完成模型连接、基于 Docker Compose 的 Postgres/pgvector、资源配额、嵌入模型以及沙箱镜像拉取。设置完成后，不带参数运行 **inflexa** 即可从当前工作目录（通常是你的数据集路径）启动 TUI/聊天界面。之后可用 **inflexa config** 重新调整设置。

开源版 CLI 是完整的 Apache-2.0 产品；另有单独的商业托管平台提供团队功能。沙箱化分析必须运行 Docker。提供 macOS 和 Linux x86_64 二进制（Homebrew、安装脚本、npm 或 GitHub releases）。

# PARAMETERS

**setup**
> 交互式首次配置：模型提供商、数据库容器、资源限制、嵌入模型、沙箱镜像。

**config**
> 设置完成后重新配置提供商和运行时选项。

_(no command)_
> 启动本地 TUI/CLI 聊天界面以处理分析请求。

# CAVEATS

执行分析需要一个正常工作的 **Docker** 守护进程。首次设置会拉取容器镜像，可能需要较大的磁盘空间和 CPU/内存余量。模型质量与成本取决于所配置的提供商；完全离线使用需要本地模型端点。Windows 可通过单独的安装脚本使用；Homebrew 主要面向 Linux/macOS。

# HISTORY

Inflexa 由 Inflexa, Inc. 开发，是一个开源自托管编排工具，旨在构建可信、可复现的计算生物学工作流，并从设计上内置来源追踪。

# SEE ALSO

[docker](/man/docker)(1), [curl](/man/curl)(1), [npm](/man/npm)(1)

# RESOURCES

```[Source code](https://github.com/inflexa-ai/inflexa)```

```[Homepage](https://inflexa.ai)```

<!-- verified: 2026-07-22 -->
