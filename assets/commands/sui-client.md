# TAGLINE

Sui 区块链钱包与交易客户端

# TLDR

**查看当前活跃地址**

```sui client active-address```

**列出所拥有的对象**

```sui client objects```

**切换环境**

```sui client switch --env [testnet]```

**从水龙头获取 SUI**

```sui client faucet```

**转账 SUI**

```sui client transfer-sui --to [address] --sui-coin-object-id [object_id] --gas-budget [1000]```

# SYNOPSIS

**sui client** _command_ [_options_]

# PARAMETERS

**active-address**
> 显示当前地址。

**objects**
> 列出所拥有的对象。

**switch**
> 切换环境或地址。

**faucet**
> 从水龙头请求代币。

**transfer-sui**
> 转账 SUI 代币。

**call**
> 调用已发布软件包上的 Move 函数。

**publish**
> 将 Move 软件包发布到链上。

**addresses**
> 列出本地密钥库中的所有地址。

**new-address**
> 生成新的密钥对（ed25519、secp256k1 或 secp256r1）。

**gas**
> 列出某地址拥有的 gas 对象。

**pay-sui**
> 在一笔交易中向多个接收方支付 SUI。

**merge-coin**
> 将两个 coin 对象合并为一个。

**split-coin**
> 将一个 coin 对象拆分为多个 coin。

**--env** _name_
> 目标环境（如 mainnet、testnet、devnet、localnet）。

**--gas-budget** _N_
> 一笔交易最多可消耗的 gas 单位数量。

**--json**
> 以 JSON 格式输出。

# DESCRIPTION

**sui client** 是 Sui 区块链的 CLI 客户端，用于管理钱包、转账代币以及与 Move 智能合约交互，是 Sui 区块链开发工具集的一部分。

# INSTALL

```brew: brew install sui```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sui-move](/man/sui-move)(1)
