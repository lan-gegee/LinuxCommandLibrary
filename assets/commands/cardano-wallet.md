# TAGLINE

用于管理 Cardano 钱包的钱包服务器与命令行工具

# TLDR

**启动钱包服务器**

```cardano-wallet serve --port [8090] --node-socket [/path/to/node.socket] --database [/path/to/wallet-db] --mainnet```

**从助记词创建钱包**

```cardano-wallet wallet create from-recovery-phrase [wallet_name]```

**列出所有钱包**

```cardano-wallet wallet list```

**获取钱包余额**

```cardano-wallet wallet get --id [wallet_id]```

**生成收款地址**

```cardano-wallet address list --id [wallet_id]```

**创建交易**

```cardano-wallet transaction create --id [wallet_id] --payment [addr1...@amount]```

**提交交易**

```cardano-wallet transaction submit --id [wallet_id] --transaction [tx_binary]```

# SYNOPSIS

**cardano-wallet** _command_ [_options_]

# DESCRIPTION

**cardano-wallet** 是一个用于管理 Cardano 钱包的 HTTP 服务器和命令行工具。它提供带 RESTful API 的分层确定性（HD）钱包功能，使应用程序能够创建钱包、管理地址和提交交易。

钱包服务器连接到 cardano-node，以查询区块链状态并提交交易。它在本地数据库中维护钱包状态，跟踪 UTxO 和交易历史。该服务器支持多个钱包，并为交易构建提供硬币选择功能。

钱包通过遵循 BIP39/CIP11 标准的 15 或 24 个单词的助记词恢复。CLI 同时提供交互式命令和适合脚本的输出格式。

# PARAMETERS

**serve**
> 启动钱包 HTTP 服务器。

**wallet create**
> 创建新钱包。

**wallet list**
> 列出所有钱包。

**wallet get**
> 获取钱包详情。

**wallet delete**
> 删除钱包。

**address list**
> 列出钱包地址。

**transaction create**
> 构建交易。

**transaction submit**
> 提交已签署的交易。

**transaction list**
> 列出钱包交易。

**stake-pool list**
> 列出可用的权益池。

**--port** _port_
> HTTP 服务器端口。

**--node-socket** _path_
> 节点套接字路径。

**--database** _path_
> 钱包数据库目录。

**--mainnet**
> 连接主网。

**--testnet** _magic_
> 连接测试网。

**--id** _wallet_id_
> 钱包标识符。

# CAVEATS

需要已同步的 cardano-node。数据库必须持久化保存以便恢复钱包。助记词必须安全离线保管。服务器会暴露敏感操作，因此应妥善加固。恢复钱包时同步钱包状态可能需要较长时间。

# HISTORY

**cardano-wallet** 由 **Input Output Global (IOG)** 开发，是 Cardano 的官方钱包后端。它于 **2020 年的 Shelley era** 期间推出，用于提供标准的钱包实现。该工具支持不断演进的 Cardano 协议，包括质押、原生代币和智能合约交互。

# INSTALL

```aur: yay -S cardano-wallet```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cardano-cli](/man/cardano-cli)(1), [cardano-node](/man/cardano-node)(1)
