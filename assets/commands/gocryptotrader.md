# TAGLINE

带 CLI 客户端的加密货币交易引擎

# TLDR

**启动交易引擎**

```gocryptotrader```

**使用指定配置文件启动**

```gocryptotrader -config [config.json]```

**用 CLI 客户端列出支持的交易所**

```gctcli getexchanges```

**获取货币对的行情**

```gctcli getticker --exchange [binance] --pair [BTC-USDT] --asset [spot]```

**获取账户投资组合摘要**

```gctcli getportfoliosummary```

**启用或禁用某个交易所**

```gctcli enableexchange --exchange [binance]```

**获取货币对的订单簿**

```gctcli getorderbook --exchange [binance] --pair [BTC-USDT] --asset [spot]```

# SYNOPSIS

**gocryptotrader** [_options_]

**gctcli** _command_ [_options_]

# PARAMETERS

**-config** _FILE_
> 配置文件的路径。

**-verbose**
> 启用详细输出。

**-version**
> 显示版本。

**-help**
> 显示帮助。

**-grpchost** _HOST_
> gRPC 主机地址（gctcli，默认：localhost）。

**-grpcport** _PORT_
> gRPC 端口（gctcli，默认：9052）。

# DESCRIPTION

**gocryptotrader** 是一个用 Go 编写的开源加密货币交易引擎。它支持同时连接多个交易所，进行交易、投资组合管理和市场数据获取。

配套的 CLI 工具 **gctcli** 通过 gRPC 提供对交易引擎的命令行访问，让用户可以查询行情、管理订单、查看投资组合以及配置交易所连接。该引擎支持回测、实盘交易和模拟交易三种模式。

# CAVEATS

交易功能需要受支持交易所的 API 密钥。gctcli 命令只有在交易引擎运行时才能工作。采用 Go 编写。

# SEE ALSO

[freqtrade](/man/freqtrade)(1), [cointop](/man/cointop)(1)
