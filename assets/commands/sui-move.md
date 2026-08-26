# TAGLINE

Sui Move 智能合约开发工具

# TLDR

**构建 Move 软件包**

```sui move build```

**运行测试**

```sui move test```

**发布软件包**

```sui move publish --gas-budget [10000]```

**创建新软件包**

```sui move new [package_name]```

# SYNOPSIS

**sui move** _command_ [_options_]

# PARAMETERS

**build**
> 构建 Move 软件包。

**test**
> 运行 Move 测试。

**publish**
> 发布到网络。

**new** _name_
> 创建新软件包。

**prove**
> 运行 Move Prover。

**--gas-budget** _amount_
> 交易的 gas 预算。

**--path** _path_
> 软件包路径。

# DESCRIPTION

**sui move** 用于管理 Sui 区块链上的 Move 智能合约，可以构建、测试和部署 Move 软件包，是 Sui 区块链开发工具集的一部分。

# INSTALL

```brew: brew install sui```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sui-client](/man/sui-client)(1)
