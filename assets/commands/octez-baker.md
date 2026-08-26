# TAGLINE

Tezos 烘焙（baking）守护进程

# TLDR

**启动烘焙进程**

```octez-baker-[protocol] run with local node [~/.tezos-node] [baker_alias]```

**通过 RPC 端点运行**

```octez-baker-[protocol] --endpoint [http://localhost:8732] run with local node [data_dir] [baker]```

**附带投票运行**

```octez-baker-[protocol] run with local node [data_dir] [baker] --liquidity-baking-toggle-vote [pass]```

**列出已知烘焙者**

```octez-baker-[protocol] list known addresses```

# SYNOPSIS

**octez-baker-_protocol_** [_options_] _command_

# PARAMETERS

**run**
> 运行烘焙守护进程。

**--endpoint** _uri_
> 节点 RPC 端点。

**--liquidity-baking-toggle-vote** _vote_
> on、off 或 pass。

**with local node** _dir_
> 节点数据目录。

# DESCRIPTION

**octez-baker** 是 Tezos 的烘焙（baking）守护进程。烘焙者负责创建新区块并参与共识。烘焙进程监视区块链，并在被选中时生产区块。

命令名中包含协议版本（例如 octez-baker-PtParisA）。

# REQUIREMENTS

```
- Running octez-node
- Registered baker key
- Sufficient stake
- Key imported to client
```

# CAVEATS

需要已注册的委托账户。二进制文件与特定协议绑定。需要节点已完成同步。须满足质押要求。

# HISTORY

Tezos 烘焙器是 **Arthur 和 Kathleen Breitman** 开发的 **Tezos** 区块链的组成部分，该链采用流动性质押证明（liquid proof-of-stake）共识机制。

# SEE ALSO

[octez-node](/man/octez-node)(1), [octez-client](/man/octez-client)(1)
