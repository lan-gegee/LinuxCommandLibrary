# TAGLINE

注重隐私、支持 CoinJoin 的 Bitcoin 钱包

# TLDR

**启动钱包 GUI**

```wassabee```

**启动无界面守护进程**

```wassabeed```

**在测试网上启动守护进程**

```wassabeed --network testnet```

**指定自定义数据目录**

```wassabeed --datadir [/path/to/data]```

# SYNOPSIS

**wassabee** [_options_]

**wassabeed** [_options_]

# PARAMETERS

**--network** _NETWORK_
> 要使用的 Bitcoin 网络（main、testnet、regtest）。

**--datadir** _DIR_
> 自定义数据目录路径。

**--usetor** _BOOL_
> 启用或禁用 Tor 路由（默认：true）。

**--blockonly** _BOOL_
> 忽略 P2P 交易；只处理区块数据。

**--jsonrpcserverenabled** _BOOL_
> 启用 JSON-RPC 服务器以供远程控制。

**--jsonrpcserverprefix** _URL_
> JSON-RPC 服务器的 URL 前缀。

**--help**
> 显示帮助。

**--version**
> 显示版本。

# DESCRIPTION

**Wasabi Wallet** 是一款开源、注重隐私的 Bitcoin 钱包，通过实现 **CoinJoin** 对交易进行匿名化。它使用 **WabiSabi** 协议实现无需信任的、基于协调者的混币。

该钱包既可以作为图形应用运行（**wassabee**），也可以作为无界面守护进程（**wassabeed**）用于服务器部署。守护进程提供 JSON-RPC 接口以便程序化控制钱包。所有连接默认经由 **Tor** 路由，以保证网络层面的隐私。

# CAVEATS

CoinJoin 交易有最低金额要求，并会产生协调者费用。默认捆绑并使用 Tor。使用 C#（.NET）编写。

# INSTALL

```aur: yay -S wasabi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[electrum](/man/electrum)(1), [lnd](/man/lnd)(1)
