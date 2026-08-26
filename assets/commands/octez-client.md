# TAGLINE

Tezos 区块链客户端

# TLDR

**查询账户余额**

```octez-client get balance for [address]```

**转账代币**

```octez-client transfer [amount] from [source] to [destination]```

**生成新账户**

```octez-client gen keys [alias]```

**显示账户地址**

```octez-client show address [alias]```

**列出已知地址**

```octez-client list known addresses```

# SYNOPSIS

**octez-client** [_command_] [_options_]

# PARAMETERS

**get balance for** _ADDRESS_
> 显示账户余额。

**transfer** _AMOUNT_ **from** _SRC_ **to** _DST_
> 发送代币。

**gen keys** _ALIAS_
> 创建新账户。

**show address** _ALIAS_
> 显示地址。

**-A** _NODE_
> 节点地址。

**--help**
> 显示帮助信息。

# DESCRIPTION

**octez-client** 是 Tezos 区块链客户端，用于管理账户和交易。

该工具与 Tezos 网络交互，支持智能合约。

# CAVEATS

需要连接 Tezos 节点。交易会产生手续费。依赖网络状况。

# HISTORY

octez-client 是与 Tezos 区块链交互的**官方客户端**。

# SEE ALSO

[octez-node](/man/octez-node)(1), [octez-baker](/man/octez-baker)(1)
