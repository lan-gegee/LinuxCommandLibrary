# TAGLINE

the0 算法交易平台 CLI

# TLDR

**安装** the0 CLI

```curl -sSL https://install.the0.app | sh```

以 root 管理员凭据**初始化本地堆栈**

```the0 local init --email [you@example.com] --password [password]```

**启动**本地 Docker Compose 平台

```the0 local start```

**查看** CLI 帮助

```the0 --help```

**登录**并获取用于远程或 MCP 场景的 API 凭据

```the0 auth login```

**将 CLI 指向**本地 Docker Compose API

```export THE0_API_URL=http://localhost:3000```

# SYNOPSIS

**the0** \<command\> [_options_]

# DESCRIPTION

**the0** 是 **the0**（一个开源算法交易执行引擎）的命令行界面。该 CLI 可安装和管理自托管堆栈（通过 Docker Compose 或 Kubernetes 部署的 API、Web 仪表盘、bot 运行器及配套服务），针对 API 进行身份验证，是开发、部署和管理交易 bot 的主要工作流入口。

Bot 可以使用官方 SDK 以 Python、TypeScript、Rust、C++、C#、Scala 或 Haskell 编写。平台支持定时（cron）和实时 bot、自定义 React 仪表盘以及与交易所无关的策略。本地部署通常在前端端口 **3001**、API 端口 **3000**、MinIO 端口 **9001** 上提供服务。安装脚本会把二进制文件放到 **~/.the0/bin/the0**（请确保该目录在 **PATH** 中）。从 **the0/cli** 源码构建则安装到 **~/bin/the0**。

API 还暴露了一个 MCP（Model Context Protocol）HTTP 端点，AI 助手在持有 API 密钥的情况下可以列出 bot、部署配置并读取日志。

# PARAMETERS

**local init**
> 生成本地 Docker Compose 配置骨架，并设置 root 管理员（**--email**、**--password**）。需要 Docker 20.10+ 及 Compose。

**local start**
> 启动所有本地平台服务。

**auth login**
> 进行身份验证并获取 API 凭据（也用于 MCP 集成）。

**--help**
> 显示 CLI 帮助和可用子命令。

**THE0_API_URL**
> 指定 API 基础 URL 的环境变量（Docker Compose 用 **http://localhost:3000**，Kubernetes 则为服务 URL）。

# CAVEATS

该项目处于 **beta** 阶段，尚未达到生产可用状态。本地部署需要带 Compose 的 Docker，容器大约需要 4 GB 空闲内存。Kubernetes（Helm）部署需要运维人员自备 PostgreSQL、MongoDB、S3 兼容存储、JWT 密钥和管理员配置——并非一条命令即可完成安装。交易 bot 使用你自己的凭据连接真实或模拟券商；CLI 本身不提供行情访问能力。

# HISTORY

**the0** 由 **AlphaNeuron**（Alexander Wanyoike）开发，是基于 Apache License 2.0 的开源多语言 bot 执行平台，采用 Go 编写的 CLI（Cobra）、NestJS API 以及 Go 运行时服务。

# SEE ALSO

[docker](/man/docker)(1), [docker-compose](/man/docker-compose)(1), [helm](/man/helm)(1), [curl](/man/curl)(1)

# RESOURCES

```[Source code](https://github.com/alexanderwanyoike/the0)```

```[Homepage](https://the0.app)```

```[Documentation](https://docs.the0.app/the0-cli/)```

<!-- verified: 2026-07-21 -->
