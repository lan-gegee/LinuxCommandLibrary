# TAGLINE

比特币闪电网络守护进程

# TLDR

**启动守护进程**

```lnd```

**使用指定的比特币后端启动**

```lnd --bitcoin.active --bitcoin.mainnet --bitcoind.rpcuser=[user] --bitcoind.rpcpass=[pass]```

**在测试网上启动**

```lnd --bitcoin.active --bitcoin.testnet```

**指定自定义数据目录**

```lnd --lnddir=[~/.lnd]```

# SYNOPSIS

**lnd** [_options_]

# PARAMETERS

**--bitcoin.active**
> 启用 Bitcoin 作为活动链。

**--bitcoin.mainnet**
> 使用 Bitcoin 主网。

**--bitcoin.testnet**
> 使用 Bitcoin 测试网。

**--bitcoind.rpcuser** _USER_
> bitcoind RPC 身份验证的用户名。

**--bitcoind.rpcpass** _PASS_
> bitcoind RPC 身份验证的密码。

**--lnddir** _DIR_
> lnd 数据目录的自定义路径。

**--listen** _ADDR_
> 添加用于监听对等节点连接的接口/端口。

**--rpclisten** _ADDR_
> 添加 RPC 服务器监听的接口/端口。

**--restlisten** _ADDR_
> 添加 REST 服务器监听的接口/端口。

**--debuglevel** _LEVEL_
> 日志级别（trace、debug、info、warn、error、critical）。

**--help**, **-h**
> 显示帮助。

**--version**, **-v**
> 显示版本信息。

# DESCRIPTION

**lnd**（Lightning Network Daemon）是 **Lightning Network** 协议的完整实现。它通过支付通道实现快速、低成本的比特币交易，无需等待区块链确认即可完成近乎即时的支付。

该守护进程管理支付通道、在网络中路由支付并维护本地通道图。它提供 gRPC 和 REST API 用于交互，通常通过配套的 **lncli** 命令行客户端使用。

# CAVEATS

需要 Bitcoin 全节点后端（bitcoind、btcd 或 neutrino）。主网上的通道管理涉及真实资金。采用 Go 编写。

# INSTALL

```nix: nix profile install nixpkgs#lnd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[electrum](/man/electrum)(1), [geth](/man/geth)(1)
