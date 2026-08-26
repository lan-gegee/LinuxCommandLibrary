# TAGLINE

命令行以太坊测试区块链

# TLDR

**启动以太坊测试区块链**

```ganache-cli```

**在指定端口启动**

```ganache-cli -p [8545]```

**以指定数量的账户启动**

```ganache-cli -a [10]```

**以助记词启动**

```ganache-cli -m "[mnemonic phrase]"```

**以确定性地址启动**

```ganache-cli -d```

**从主网分叉**

```ganache-cli -f [https://mainnet.infura.io/v3/key]```

**设置 gas 上限**

```ganache-cli -l [8000000]```

# SYNOPSIS

**ganache-cli** [_options_]

# PARAMETERS

**-p**, **--port** _port_
> 端口号。

**-a**, **--accounts** _num_
> 账户数量。

**-m**, **--mnemonic** _phrase_
> HD 钱包助记词。

**-d**, **--deterministic**
> 使用确定性地址。

**-f**, **--fork** _url_
> 从网络分叉。

**-l**, **--gasLimit** _limit_
> 区块 gas 上限。

**-e**, **--defaultBalanceEther** _amount_
> 默认账户余额。

**-i**, **--networkId** _id_
> 网络 ID。

# DESCRIPTION

**ganache-cli**（现已并入 Ganache）创建用于开发和测试的本地以太坊区块链。它提供即时交易打包和可配置的测试账户，服务于智能合约开发。

这个命令行版本现在已被 **ganache** 命令取代，后者提供相同的功能并有更多特性。ganache-cli 原名 TestRPC，后来更名并整合进 Ganache 套件。

该工具模拟完整的以太坊客户端，非常适合在部署到测试网或主网之前本地测试智能合约。它与 Truffle 和 Hardhat 等开发框架集成。

# CAVEATS

ganache-cli 已弃用，请改用 **ganache** 命令。不可用于生产环境。除非配置了持久化，否则区块链状态会在重启时重置。行为可能与真实的以太坊主网不同。

# HISTORY

最初发布时名为 **TestRPC**，大约在 **2017 年**并入 Truffle Suite 时更名为 **ganache-cli**。从 Ganache 7 开始，该工具已被统一的 **ganache** 命令取代。

# INSTALL

```aur: yay -S ganache-cli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[geth](/man/geth)(1), [truffle](/man/truffle)(1)

# RESOURCES

```[Source code](https://github.com/trufflesuite/ganache)```

<!-- verified: 2026-07-15 -->
