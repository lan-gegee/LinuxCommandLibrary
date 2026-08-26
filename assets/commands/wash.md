# TAGLINE

wasmCloud 开发与管理 CLI

# TLDR

**创建新的 WebAssembly 组件项目**

```wash new component [project-name]```

**构建组件**

```wash build```

**启动支持热重载的开发服务器**

```wash dev```

**启动本地 wasmCloud 环境**

```wash up```

**停止本地 wasmCloud 环境**

```wash down```

**将组件推送到 OCI 仓库**

```wash push [registry.example.com/component:tag] [component.wasm]```

**查看组件接口**

```wash inspect [component.wasm]```

# SYNOPSIS

**wash** [_options_] _command_ [_arguments_]

# COMMANDS

**new**: 从模板创建项目（component、provider）。

**build**: 构建并签名组件或提供者。

**dev**: 启动热重载开发循环。

**up**: 引导启动本地 wasmCloud 环境。

**down**: 拆除本地环境。

**app**: 管理声明式应用（wadm）。

**start**: 启动组件或提供者。

**stop**: 停止正在运行的组件或提供者。

**scale**: 扩缩容组件实例。

**push**: 将制品推送到 OCI 仓库。

**pull**: 从 OCI 仓库拉取制品。

**inspect**: 显示组件的 WIT 接口和元数据。

**lint**: 检查组件中的常见问题。

**completions**: 生成 shell 补全脚本。

# PARAMETERS

**-o** _format_
> 输出格式：text、json。

**--nats-host** _host_
> NATS 服务器主机。

**--nats-port** _port_
> NATS 服务器端口。

**--lattice** _id_
> 要连接的 lattice ID。

**--ctl-host** _host_
> 控制接口主机。

# DESCRIPTION

**wash**（wasmCloud Shell）是用于开发 WebAssembly 组件和管理 wasmCloud 分布式应用的综合性 CLI。它提供从项目脚手架到部署的完整开发生命周期工具链。

该 CLI 支持多语言组件开发，包括 Rust、Go 和 TypeScript。项目按照 Component Model 规范构建为 WebAssembly 组件。dev 命令提供热重载开发服务器，便于快速迭代。

wasmCloud 支持分布式应用，组件通过网络、存储等能力提供者进行通信以访问系统服务。wash 负责管理本地开发环境，并与远程 wasmCloud lattice 交互。

# CAVEATS

构建组件需要相应语言的工具链（Rust、Go、TinyGo）。本地开发需要 Docker 或 Podman 来运行 NATS 消息服务。某些功能要求 wasmCloud host 正在运行。

# HISTORY

**wash** 由 wasmCloud 项目创建，作为 WebAssembly 组件开发的主要接口。wasmCloud 平台源自 Wasm 社区使用 Component Model 构建分布式系统的努力。wash 将多个工具整合为单一 CLI，成为 wasmCloud 生态的标准接口。

# INSTALL

```apt: sudo apt install reaver```

```dnf: sudo dnf install reaver```

```pacman: sudo pacman -S reaver```

```brew: brew install reaver```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wasmtime](/man/wasmtime)(1), [docker](/man/docker)(1), [podman](/man/podman)(1)
