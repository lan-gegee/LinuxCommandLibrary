# TAGLINE

Tezos 区块链节点

# TLDR

**启动节点**

```octez-node run```

**为特定网络初始化配置**

```octez-node config init --network=[mainnet]```

**生成节点身份**

```octez-node identity generate```

**启用 RPC 启动**

```octez-node run --rpc-addr=[127.0.0.1:8732]```

**重建存储**

```octez-node reconstruct```

**导出快照**

```octez-node snapshot export [snapshot.full]```

**从快照导入**

```octez-node snapshot import [snapshot.full]```

# SYNOPSIS

**octez-node** _command_ [_options_]

# PARAMETERS

**run**
> 运行节点。

**config init**
> 初始化配置。

**snapshot export**
> 导出快照。

**snapshot import**
> 导入快照。

**identity generate**
> 生成新的节点身份（首次启动时必需）。

**reconstruct**
> 从 full 模式存储重建归档存储。

**--rpc-addr** _addr_
> RPC 监听地址（默认：localhost:8732）。

**--network** _name_
> 要连接的网络（mainnet、ghostnet 等）。

**--data-dir** _dir_
> 数据目录（默认：~/.tezos-node）。

**--history-mode** _mode_
> 存储模式：archive、full（默认）或 rolling。

**--connections** _num_
> 对等连接的最大数量。

**--net-addr** _addr_
> P2P 监听地址（默认：[::]:9732）。

# DESCRIPTION

**octez-node** 是 Tezos 区块链节点。它连接到 Tezos 网络，验证区块，并为客户端、烘焙者和应用程序提供 RPC 访问。

节点存储区块链数据并参与点对点网络通信。

# STORAGE MODES

```
archive - All block history + full context (largest)
full    - All block headers, operations, but pruned contexts (default)
rolling - Only recent blocks and contexts (smallest)
```

# CONFIGURATION

```
~/.tezos-node/
├── config.json
├── context/
└── store/
```

# CAVEATS

需要大量磁盘空间。初次同步耗时较长。使用快照可以更快完成引导。

# HISTORY

Tezos 由 **Arthur Breitman** 和 **Kathleen Breitman** 创建，主网于 **2018** 年上线。节点软件后来更名为 Octez。

# INSTALL

```aur: yay -S octez-node```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[octez-client](/man/octez-client)(1), [octez-baker](/man/octez-baker)(1)
