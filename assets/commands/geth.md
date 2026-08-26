# TAGLINE

以太坊协议的官方 Go 实现

# TLDR

**启动以太坊节点**

```geth```

**同步主网**

```geth --syncmode [snap]```

**附带控制台启动**

```geth console```

**连接到运行中的**节点

```geth attach```

**创建新账户**

```geth account new```

# SYNOPSIS

**geth** [_options_] [_command_]

# PARAMETERS

_COMMAND_
> 子命令：console、attach、account 等。

**--syncmode** _MODE_
> 同步模式：full、snap（light 模式在 The Merge 之后已弃用）。

**--datadir** _PATH_
> 数据目录。

**--http**
> 启用 HTTP RPC。

**--ws**
> 启用 WebSocket RPC。

**console**
> 交互式 JavaScript 控制台。

**attach**
> 连接到运行中的节点。

**account** _CMD_
> 账户管理。

**--port** _PORT_
> 网络监听端口（默认：30303）。

**--maxpeers** _N_
> 最大网络对等节点数量。

**--networkid** _ID_
> 网络标识符（1=主网，5=goerli）。

**--goerli**
> 连接 Goerli 测试网络。

**--sepolia**
> 连接 Sepolia 测试网络。

**--help**
> 显示帮助信息。

# DESCRIPTION

**geth**（go-ethereum）是以太坊协议的官方 Go 实现。它运行完整的以太坊节点，支持区块链同步、交易验证、挖矿操作和智能合约部署。

该客户端提供多种同步模式："snap" 借助状态快照快速同步，"full" 进行完整的区块链验证。light 同步模式自转向权益证明（The Merge）以来已被弃用且无法使用。它通过 HTTP、WebSocket 和 IPC 暴露 JSON-RPC API，便于应用程序集成。

geth 包含用于直接与区块链交互的交互式 JavaScript 控制台、用于创建和管理以太坊钱包的账户管理功能，并支持主网和测试网络。它是运行生产节点和开发环境时使用最广泛的以太坊客户端。

# CAVEATS

完整同步需要大量磁盘空间。资源占用高。主网同步耗时较长。

# HISTORY

geth 由 **Ethereum Foundation** 开发，是其官方 Go 实现。它是最早的以太坊客户端之一，至今仍是运行节点时最受欢迎的选择。

# INSTALL

```apk: sudo apk add geth```

```brew: brew install geth```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[solc](/man/solc)(1)
