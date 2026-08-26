# TAGLINE

Cardano 区块链的命令行界面

# TLDR

**查询 tip**（最新区块信息）

```cardano-cli query tip --mainnet```

**生成支付密钥**

```cardano-cli address key-gen --verification-key-file [payment.vkey] --signing-key-file [payment.skey]```

**构建支付地址**

```cardano-cli address build --payment-verification-key-file [payment.vkey] --out-file [payment.addr] --mainnet```

**查询某地址的 UTxO**

```cardano-cli query utxo --address [addr1...] --mainnet```

**构建交易**

```cardano-cli transaction build --tx-in [txhash#index] --tx-out [addr]+[lovelace] --change-address [addr] --mainnet --out-file [tx.raw]```

**签署交易**

```cardano-cli transaction sign --tx-body-file [tx.raw] --signing-key-file [payment.skey] --mainnet --out-file [tx.signed]```

**提交交易**

```cardano-cli transaction submit --tx-file [tx.signed] --mainnet```

# SYNOPSIS

**cardano-cli** _command_ [_subcommand_] [_options_]

# DESCRIPTION

**cardano-cli** 是用于与 Cardano 区块链交互的命令行界面。它提供密钥生成、地址创建、交易构建以及查询区块链状态等功能。

该工具与运行中的 cardano-node 交互，以查询区块链数据并提交交易。它同时支持主网和多种测试网（preprod、preview）。操作范围包括管理权益密钥、向权益池委托、铸造原生代币，以及参与链上治理（Conway era）。

Cardano 采用扩展 UTxO（EUTxO）模型，交易会消耗并产生未花费的交易输出。CLI 负责处理构建有效交易时涉及的手续费计算和余额平衡等复杂问题。自版本 10.11 起，默认 era 为 Conway。

# PARAMETERS

**query**
> 查询区块链状态（tip、utxo、protocol-parameters）。

**address**
> 地址相关命令（key-gen、build）。

**transaction**
> 交易相关命令（build、sign、submit）。

**stake-address**
> 权益地址与委托相关命令。

**stake-pool**
> 权益池操作。

**governance**
> 治理命令：行动、DRep 注册、委员会和投票（Conway era）。

**key**
> 密钥工具命令。

**node**
> 节点操作证书及密钥演进签名相关命令。

**hash**
> 针对文件和脚本的哈希工具。

**genesis**
> 创世区块相关命令。

**--mainnet**
> 使用主网网络魔数。

**--testnet-magic** _num_
> 使用具有指定魔数的测试网。

**--socket-path** _path_
> 节点套接字路径（或使用 CARDANO_NODE_SOCKET_PATH 环境变量）。

**--out-file** _file_
> 结果的输出文件。

**--signing-key-file** _file_
> 用于签署的私钥。

**--verification-key-file** _file_
> 公钥文件。

# CAVEATS

需要运行中且已同步的 cardano-node。套接字路径必须可访问。交易需要正确的手续费计算和找零输出。密钥应妥善安全保存；一旦丢失即意味着资金丢失。测试网代币没有实际价值。

# HISTORY

**cardano-cli** 由 **Input Output Global (IOG)** 开发，属于 **Charles Hoskinson** 创立的 Cardano 区块链项目的一部分。Cardano 主网于 **2017 年 9 月**上线（Byron era）。**2020 年**的 Shelley era 引入了质押功能。**2021 年 9 月**的 Alonzo 升级增加了智能合约支持。该工具随每次协议升级持续演进。

# SEE ALSO

[cardano-node](/man/cardano-node)(1), [cardano-wallet](/man/cardano-wallet)(1)
