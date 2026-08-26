# TAGLINE

Polkadot 区块链节点

# TLDR

**启动全节点**

```polkadot```

**启动验证人节点**

```polkadot --validator --name [myValidator]```

**与特定链同步**

```polkadot --chain [kusama]```

**使用 warp 同步加快初始同步速度**

```polkadot --sync [warp]```

**指定自定义数据目录**

```polkadot --base-path [/path/to/data]```

**清除本地链数据**

```polkadot purge-chain --chain [polkadot]```

# SYNOPSIS

**polkadot** [_options_] [_subcommand_]

# PARAMETERS

**--validator**
> 以验证人节点身份运行。

**--name** _NAME_
> 用于遥测的易读节点名称。

**--chain** _CHAIN_
> 指定链：polkadot、kusama、westend、paseo，或链规格 JSON 文件的路径。

**--base-path** _DIR_
> 自定义数据目录。

**--sync** _MODE_
> 同步模式：Full（默认）、Fast 或 Warp。

**--state-pruning** _N_
> 保留的区块状态数量。使用 `archive` 或 `archive-canonical` 保留全部。默认：256。

**--blocks-pruning** _N_
> 保留的区块数量。使用 `archive` 或 `archive-canonical` 保留全部。默认：archive-canonical。

**--rpc-port** _PORT_
> 统一的 JSON-RPC 与 WebSocket 服务端口（默认：9944）。

**--rpc-external**
> 在所有网络接口上监听 RPC 连接。

**--rpc-methods** _METHOD_
> 暴露的 RPC 方法：Auto（默认）、Safe 或 Unsafe。

**--bootnodes** _ADDRS_
> 指定引导节点。

**purge-chain**
> 移除整个本地链数据库。

**key**
> 密钥管理工具（generate、insert、inspect）。

**export-chain-spec**
> 导出链规格。

**--help**, **-h**
> 显示帮助。

**--version**, **-V**
> 显示版本。

# DESCRIPTION

**polkadot** 是 **Polkadot** 区块链网络的参考节点实现，Polkadot 是一种支持跨链互操作的多链协议。该节点通过验证交易、生产区块以及在平行链之间中继消息来参与网络。

节点可以作为全节点（同步并验证链）、验证人（参与共识）或收集人（为平行链生产区块）运行。它基于 Substrate 框架构建，属于 **polkadot-sdk** monorepo 的一部分，使用 Rust 编写。

# CAVEATS

验证人节点需要质押 DOT 代币。运行全节点需要可观的磁盘空间和带宽。`--pruning` 标志仍可作为 `--state-pruning` 的别名使用。HTTP 和 WebSocket 通过同一个统一端口提供服务（默认 9944）。

# INSTALL

```nix: nix profile install nixpkgs#polkadot```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cardano-node](/man/cardano-node)(1), [geth](/man/geth)(1)
