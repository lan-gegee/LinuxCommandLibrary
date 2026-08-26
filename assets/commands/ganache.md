# TAGLINE

用于开发的个人以太坊区块链

# TLDR

**启动 Ganache CLI**

```ganache```

**在指定端口启动**

```ganache -p [8545]```

**以指定数量的账户启动**

```ganache -a [20]```

**以助记词启动**

```ganache -m "[word1 word2 ... word12]"```

**分叉主网**

```ganache -f [https://mainnet.infura.io/v3/KEY]```

**以确定性账户启动**

```ganache -d```

# SYNOPSIS

**ganache** [_options_]

# PARAMETERS

**-p**, **--port** _port_
> 监听端口（默认 8545）。

**-h**, **--host** _host_
> 主机名（默认 127.0.0.1）。

**-a**, **--accounts** _num_
> 生成的账户数量（默认 10）。

**-e**, **--defaultBalanceEther** _amount_
> 默认账户余额，单位 ether（默认 100）。

**-m**, **--mnemonic** _phrase_
> HD 钱包的 BIP39 助记词。

**-s**, **--seed** _seed_
> HD 钱包账户生成所用的种子。

**-d**, **--deterministic**
> 生成确定性的地址和助记词。

**-n**, **--secure**
> 默认锁定所有可用账户。

**-u**, **--unlock** _accounts_
> 指定要解锁的账户。

**-f**, **--fork** _url_
> 从 URL 指定的网络分叉。

**-b**, **--blockTime** _seconds_
> 自动出块的区块时间（默认 0，即时打包）。

**-g**, **--gasPrice** _price_
> gas 价格，单位 wei（默认 20000000000）。

**-l**, **--gasLimit** _limit_
> 区块 gas 上限（默认 6721975）。

**-i**, **--networkId** _id_
> 网络 ID。

**--chain.chainId** _id_
> 链 ID。

**--db** _path_
> 保存链数据库的目录，用于持久化。

**--verbose**
> 将所有传入请求记录到 stdout。

**--allowUnlimitedContractSize**
> 允许不限大小的合约，便于调试。

# DESCRIPTION

**Ganache** 是一个面向开发的个人以太坊区块链。它模拟完整的客户端行为，提供即时交易打包、可配置账户和区块链分叉能力。

开发者用 Ganache 在部署到测试网或主网之前本地测试智能合约。它与 Truffle、Hardhat 及其他开发框架集成。

# CAVEATS

不可用于生产环境。行为可能与主网不同。重启后状态会丢失（持久化请使用 --db）。分叉需要归档节点访问权限。**Ganache 已于 2023 年 12 月弃用**，当时 Consensys 同时停止维护 Truffle 和 Ganache。建议开发者迁移至 Hardhat 或 Foundry。

# HISTORY

Ganache 由 **Truffle Suite**（Consensys 旗下）开发。它从 TestRPC 演进而来，约在 **2017 年**更名为 Ganache。当前版本（Ganache 7+）是一次彻底的重写，支持分叉并改进了兼容性。**2023 年 9 月**，Consensys 宣布停止维护 Truffle 和 Ganache，两个代码库于 2023 年 12 月归档。

# SEE ALSO

[hardhat](/man/hardhat)(1), [truffle](/man/truffle)(1), [geth](/man/geth)(1)
