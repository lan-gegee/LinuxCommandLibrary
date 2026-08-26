# TAGLINE

用于账户和智能合约的 Aptos 区块链 CLI

# TLDR

**初始化新的 Aptos 账户**

```aptos init```

**在链上创建新账户**

```aptos account create --account [address]```

**查询账户余额**

```aptos account balance --account [address]```

**编译 Move 模块**

```aptos move compile --package-dir [path/to/package]```

**发布 Move 模块**

```aptos move publish --package-dir [path/to/package]```

**运行 Move 函数**

```aptos move run --function-id [address::module::function]```

**转账 APT 代币**

```aptos account transfer --account [recipient] --amount [amount]```

**获取交易详情**

```aptos transaction show --hash [transaction_hash]```

# SYNOPSIS

**aptos** _command_ [_subcommand_] [_options_]

# PARAMETERS

**init**
> 初始化配置并创建新账户。

**account**
> 账户相关操作（create、balance、transfer）。

**move**
> Move 语言操作（compile、publish、run、test）。

**node**
> 节点操作（run、show-status）。

**key**
> 密钥管理（generate、extract）。

**config**
> 配置管理。

**--profile** _name_
> 使用配置中的指定 profile。

**--network** _network_
> 目标网络：mainnet、testnet、devnet 或自定义 URL。

**--private-key** _key_
> 用于签署交易的私钥。

**--assume-yes**
> 对所有提示自动回答 yes。

**--output** _format_
> 输出格式：json 或 text。

# DESCRIPTION

**aptos** 是与 Aptos 区块链交互的官方命令行接口。它提供账户管理、使用 Move 语言进行智能合约开发以及区块链交互的工具。

该 CLI 支持完整的开发生命周期：初始化项目、编译 Move 模块、运行测试、部署到各种网络（devnet、testnet、mainnet）以及执行链上函数。它为不同环境管理账户、密钥和 profile。

Move 是 Aptos 的智能合约语言，源自 Facebook 的 Diem 项目。CLI 的 Move 命令负责 Move 软件包的编译、测试和发布到区块链。

# CONFIGURATION

**~/.aptos/config.yaml**
> 主 CLI 配置文件，存储 profile、私钥和网络设置。

**Move.toml**
> 项目目录中的 Move 软件包清单文件，定义依赖和地址。

# CAVEATS

私钥应妥善保护；避免将其存入 shell 历史或纯文本文件。Testnet 和 devnet 代币没有价值，仅供开发使用。主网交易需支付 gas 费用。测试代币水龙头可能存在速率限制。

# HISTORY

Aptos 源自 **Meta (Facebook)** 开发的 Diem（前身为 Libra）区块链项目。当 Diem 于 **2022** 年终止时，原团队成员创立了 **Aptos Labs**，并于 **2022 年 10 月**上线 Aptos 主网。该 CLI 和 Move 语言延续了 Diem 研究的创新成果，包括用于形式化验证的 Move Prover。

# INSTALL

```aur: yay -S aptos```

```brew: brew install aptos```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[solana](/man/solana)(1), [sui](/man/sui)(1)
