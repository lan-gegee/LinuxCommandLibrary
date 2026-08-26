# TAGLINE

Bitcoin Core 的命令行界面

# TLDR

**获取**区块链信息

```bitcoin-cli getblockchaininfo```

**获取**钱包余额

```bitcoin-cli getbalance```

**发送**比特币

```bitcoin-cli sendtoaddress [address] [amount]```

**获取**新地址

```bitcoin-cli getnewaddress```

**列出**交易

```bitcoin-cli listtransactions```

# SYNOPSIS

**bitcoin-cli** [_options_] _command_ [_params_]

# DESCRIPTION

**bitcoin-cli** 是 Bitcoin Core 的命令行接口。它通过 RPC 连接到正在运行的 bitcoind 守护进程，可用于查询区块链数据、管理钱包和执行交易。

该工具对于以编程方式或从脚本与 Bitcoin Core 节点交互至关重要。

# PARAMETERS

**-conf=**_file_
> 配置文件

**-datadir=**_dir_
> 数据目录

**-rpcuser=**_user_
> RPC 用户名

**-rpcpassword=**_pass_
> RPC 密码

**-rpcconnect=**_host_
> RPC 主机（默认：localhost）

**-rpcport=**_port_
> RPC 端口（默认：8332）

**-testnet**
> 使用测试网络

**-regtest**
> 使用回归测试网络

**-named**
> 使用命名参数而非位置参数

**-getinfo**
> 通过单次调用从远程服务器获取常规信息

**-stdin**
> 从标准输入读取额外参数，每行一个（适合输入密码短语）

# COMMON COMMANDS

**Blockchain:**
- **getblockchaininfo** - 链信息
- **getblock** - 获取区块数据
- **getblockhash** - 按高度获取区块哈希

**Wallet:**
- **getbalance** - 钱包余额
- **getnewaddress** - 生成新地址
- **sendtoaddress** - 发送比特币
- **listtransactions** - 列出交易

**Network:**
- **getpeerinfo** - 已连接的对等节点
- **getnetworkinfo** - 网络信息
- **getmempoolinfo** - 内存池状态
- **help** - 列出所有命令或获取某个命令的帮助

# WORKFLOW

```bash
# 检查区块链同步状态
bitcoin-cli getblockchaininfo

# 获取余额
bitcoin-cli getbalance

# 生成新的接收地址
bitcoin-cli getnewaddress

# 发送比特币
bitcoin-cli sendtoaddress "1ABC..." 0.1

# 列出最近的交易
bitcoin-cli listtransactions "*" 10
```

# CONFIGURATION

**~/.bitcoin/bitcoin.conf**
> Bitcoin Core 配置文件，用于 RPC 凭证、网络设置和守护进程选项。

# CAVEATS

需要 bitcoind 正在运行。需要 RPC 凭证。交易不可撤销。测试网仅用于测试。钱包操作若配置不当可能造成资金损失。请妥善保管 RPC 凭证。

# HISTORY

**bitcoin-cli** 自中本聪于 **2009 年**创建该项目以来一直是 Bitcoin Core 的组成部分，提供对节点的命令行访问。

# INSTALL

```apk: sudo apk add bitcoin-cli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bitcoind](/man/bitcoind)(1), [bitcoin-qt](/man/bitcoin-qt)(1)

# RESOURCES

```[Source code](https://github.com/bitcoin/bitcoin)```

```[Homepage](https://bitcoincore.org)```

<!-- verified: 2026-06-19 -->
