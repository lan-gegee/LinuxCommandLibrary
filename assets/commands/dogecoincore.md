# TAGLINE

Dogecoin Core 守护进程与 CLI 客户端

# TLDR

**启动 Dogecoin 守护进程**

```dogecoind -daemon```

**获取区块链信息**

```dogecoin-cli getblockchaininfo```

**获取钱包余额**

```dogecoin-cli getbalance```

**向指定地址发送 Dogecoin**

```dogecoin-cli sendtoaddress "[address]" [amount]```

**停止守护进程**

```dogecoin-cli stop```

# SYNOPSIS

**dogecoind** [_options_]

**dogecoin-cli** [_options_] _command_ [_params_]

# PARAMETERS

**-daemon**
> 在后台以守护进程方式运行 dogecoind。

**-testnet**
> 使用测试网络。

**-datadir** _DIR_
> 指定数据目录。

**-conf** _FILE_
> 指定配置文件。

**-rpcuser** _USER_
> JSON-RPC 连接的用户名。

**-rpcpassword** _PASS_
> JSON-RPC 连接的密码。

**-rpcport** _PORT_
> 在该端口监听 JSON-RPC 连接。

**-help**
> 显示帮助信息。

**-version**
> 显示版本信息。

# DESCRIPTION

**Dogecoin Core** 由两部分组成：**dogecoind** 是完整节点守护进程，负责在 Dogecoin 网络上验证并转发交易；**dogecoin-cli** 是命令行客户端，通过 JSON-RPC 与守护进程交互。

该 CLI 支持钱包操作（发送、接收、余额查询）、区块链查询、网络管理以及挖矿控制。配置保存在 **dogecoin.conf** 中。

# CAVEATS

运行完整节点需要下载整条 Dogecoin 区块链。dogecoin-cli 必须在守护进程处于运行状态时才能工作。本项目基于 Bitcoin Core 开发。

# SEE ALSO

[bitcoind](/man/bitcoind)(1), [bitcoin-cli](/man/bitcoin-cli)(1), [electrum](/man/electrum)(1), [geth](/man/geth)(1)
