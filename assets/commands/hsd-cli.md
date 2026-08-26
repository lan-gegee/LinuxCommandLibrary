# TAGLINE

Handshake 守护进程的命令行接口

# TLDR

**显示钱包信息**

```hsd-cli wallet get```

**生成地址**

```hsd-cli wallet createaddress```

**发送币**

```hsd-cli wallet send [address] [amount]```

**显示余额**

```hsd-cli wallet balance```

**查询名称**

```hsd-cli rpc getnameinfo [name]```

# SYNOPSIS

**hsd-cli** _command_ [_options_]

# PARAMETERS

_COMMAND_
> 要执行的命令。

**wallet**
> 钱包操作。

**rpc**
> RPC 方法调用。

**--url** _URL_
> 节点 URL。

**--api-key** _KEY_
> API 密钥。

**--network** _NETWORK_
> 要使用的网络（main、testnet、regtest、simnet）。

**--wallet** _ID_
> 钱包 ID。

**--help**
> 显示帮助信息。

# DESCRIPTION

**hsd-cli** 是 Handshake 守护进程（hsd）的命令行接口。Handshake 是一个与 DNS 兼容的去中心化命名协议，其顶级域名注册在区块链上。

该工具与 hsd 节点服务器交互，进行区块链查询和名称操作。钱包相关的操作则由配套工具 **hsw-cli** 与钱包服务器通信完成。RPC 命令通过 `hsd-cli rpc <command>` 调用。

# CAVEATS

需要运行中的 hsd 节点。需要 Node.js。名称拍卖遵循特定的出价规则和时间表。

# HISTORY

hsd-cli 是 **Handshake**（HNS）的一部分，这是一个去中心化的命名和证书颁发机构项目。

# SEE ALSO

[hsw-cli](/man/hsw-cli)(1)
