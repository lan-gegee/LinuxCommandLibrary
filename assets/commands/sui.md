# TAGLINE

Sui 区块链命令行界面

# TLDR

**启动本地网络**

```sui start```

**创建新地址**

```sui client new-address ed25519```

**查看 gas**

```sui client gas```

**发布软件包**

```sui client publish --gas-budget [1000000]```

**调用函数**

```sui client call --package [pkg] --module [mod] --function [fn]```

**切换环境**

```sui client switch --env [devnet]```

# SYNOPSIS

**sui** _command_ [_subcommand_] [_options_]

# PARAMETERS

**start**
> 启动本地网络。

**client**
> 客户端操作。

**move**
> Move 语言工具。

**keytool**
> 密钥管理。

**--gas-budget** _N_
> gas 上限。

**--env** _NAME_
> 环境。

# DESCRIPTION

**sui** 是与 Sui 区块链交互的命令行界面。Sui 是一条使用 Move 编程语言编写智能合约的 Layer 1 区块链。该 CLI 提供管理钱包、部署和交互 Move 软件包、执行交易以及运行本地开发网络的工具。

此 CLI 包含多个子命令：用于钱包管理和交易的 client 操作、用于构建和测试智能合约的 move 命令，以及用于加密密钥管理的 keytool。它支持连接 devnet、testnet 和 mainnet 环境。

可以启动本地网络用于开发和测试，提供自包含的 Sui 环境而无需连接公共网络。gas 预算管理是 Sui 区块链上所有交易的必要环节。

# CAVEATS

Sui 区块链专用。需要 Move 语言。需要账户。

# HISTORY

**sui** 是 **Sui** 区块链的 CLI，后者是一条使用 Move 语言编写智能合约的 Layer 1 区块链。

# INSTALL

```brew: brew install sui```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[solana](/man/solana)(1), [aptos](/man/aptos)(1)
