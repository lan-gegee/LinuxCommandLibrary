# TAGLINE

Handshake 钱包客户端

# TLDR

**显示钱包信息**

```hsw-cli get```

**列出钱包**

```hsw-cli wallets```

**创建钱包**

```hsw-cli create [wallet-name]```

**显示余额**

```hsw-cli balance```

**生成地址**

```hsw-cli address```

# SYNOPSIS

**hsw-cli** _command_ [_options_]

# PARAMETERS

_COMMAND_
> 要执行的命令。

**get**
> 获取钱包信息。

**wallets**
> 列出钱包。

**create**
> 创建钱包。

**balance**
> 显示余额。

**address**
> 生成地址。

**--url** _URL_
> 钱包服务 URL。

**--api-key** _KEY_
> API 密钥。

**--help**
> 显示帮助信息。

# DESCRIPTION

**hsw-cli** 是 Handshake 的钱包客户端。它连接钱包服务，管理 HNS 钱包和交易。

该工具处理钱包创建、余额查询和地址生成。它将钱包功能与主节点分离。

# CAVEATS

需要钱包服务正在运行。独立于节点客户端。加密货币工具。

# HISTORY

hsw-cli 是 **Handshake** 的钱包专用 CLI，作为 hsd-cli 节点客户端的补充。

# SEE ALSO

[hsd-cli](/man/hsd-cli)(1)
