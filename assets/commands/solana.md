# TAGLINE

Solana 区块链命令行界面

# TLDR

**检查钱包余额**

```solana balance```

**检查特定地址的余额**

```solana balance [address]```

**获取当前集群配置**

```solana config get```

将集群**设置**为 devnet、testnet 或 mainnet

```solana config set --url [devnet|testnet|mainnet-beta]```

**创建新密钥对**

```solana-keygen new```

在 devnet/testnet 上**空投 SOL**

```solana airdrop [amount]```

将 SOL **转账**到另一个地址

```solana transfer [recipient_address] [amount]```

**部署程序**

```solana program deploy [path/to/program.so]```

# SYNOPSIS

**solana** [_flags_] [_options_] _subcommand_

# PARAMETERS

**-u**, **--url** _URL_
> Solana 的 JSON RPC 端点 URL 或集群别名（devnet、testnet、mainnet-beta）。

**-k**, **--keypair** _KEYPAIR_
> 用于签署交易的密钥对文件路径或 URL。

**-C**, **--config** _FILEPATH_
> 要使用的配置文件。

**--no-address-labels**
> 输出中不使用地址标签。

**--skip-preflight**
> 跳过 preflight 交易模拟。

**--skip-seed-phrase-validation**
> 跳过助记词验证。

**--commitment** _LEVEL_
> 以选定的确认级别返回信息（processed、confirmed、finalized）。

**--use-quic**
> 发送交易时使用 QUIC 协议。

**--ws** _URL_
> Solana 集群的 WebSocket URL。

**--output** _FORMAT_
> 输出格式：json、json-compact。

**-h**, **--help**
> 打印帮助信息。

**-V**, **--version**
> 打印版本信息。

# SUBCOMMANDS

**balance**
> 获取你的余额或指定地址的余额。

**transfer**
> 在账户之间转移 SOL。

**airdrop**
> 请求空投 SOL（仅限 devnet/testnet）。

**config**
> 获取和设置 CLI 配置。

**account**
> 显示账户内容。

**address**
> 获取你的公钥。

**program deploy**
> 部署一个 Solana 程序。

**stake-account**
> 管理质押账户。

**validator-info**
> 发布或获取验证者信息。

**epoch-info**
> 获取当前 epoch 的信息。

**slot**
> 获取当前 slot。

**block-height**
> 获取当前区块高度。

**logs**
> 流式查看交易日志。

**confirm**
> 按签名确认交易。

# DESCRIPTION

**solana** 是与 Solana 区块链交互的命令行界面。它提供管理钱包、转移代币、部署程序（智能合约）、质押以及查询区块链状态的工具。

CLI 通过 JSON-RPC 连接到 Solana 集群。有三个主要集群可用：**mainnet-beta**（生产环境）、**testnet**（测试）和 **devnet**（开发）。配置存储在 **~/.config/solana/cli/config.yml** 中。

用于签署交易的密钥对可以用 **solana-keygen** 生成，通常保存为 JSON 文件。该 CLI 是 Solana 验证者和程序开发者的主要工具。

# CONFIGURATION

**~/.config/solana/cli/config.yml**
> CLI 配置文件，存储默认 RPC URL、密钥对路径和确认级别。

**~/.config/solana/id.json**
> 用于签署交易的默认密钥对文件。

# CAVEATS

空投仅在 devnet 和 testnet 上可用，mainnet 不支持。交易需要 SOL 支付手续费。私钥应妥善保护；切勿共享密钥对文件。CLI 需要连接到所配置集群的网络。公共 RPC 端点可能有速率限制。

# HISTORY

**Solana** 由 Anatoly Yakovenko 于 **2017 年**创立，并于 **2020 年**启动主网 beta。自诞生以来，CLI 一直是与 Solana 交互的主要工具。**2024 年**，开发工作从 Solana Labs 移交给 **Anza**（Agave 客户端），而 CLI 继续作为新功能最先落地的位置。Solana 以高吞吐量和低交易成本著称。


# INSTALL

```brew: brew install solana```

<!-- packages: 2026-07-22 -->
