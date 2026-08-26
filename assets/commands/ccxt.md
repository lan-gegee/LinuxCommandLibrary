# TAGLINE

加密货币交易所交易 CLI

# TLDR

**获取**交易对的**订单簿**

```ccxt [binance] fetchOrderBook [BTC/USDT]```

**获取市场最近的成交记录**

```ccxt [okx] fetchTrades [ETH/USDT]```

**以表格格式获取所有行情**

```ccxt [bitget] fetchTickers --table```

**获取账户余额**（需要 API 密钥）

```ccxt [bybit] fetchBalance```

**显示交易所的可用市场**

```ccxt [gate] markets```

**创建限价单**（需要 API 密钥）

```ccxt [binance] createOrder [BTC/USDT] limit buy [0.001] [50000]```

**使用沙箱模式**进行测试

```ccxt [okx] fetchTicker [BTC/USDT] --sandbox```

**查看某方法的帮助**

```ccxt explain createOrder```

# SYNOPSIS

**ccxt** _exchange_id_ [_method_] [_arguments_...] [_OPTIONS_]

# PARAMETERS

**--table**
> 将输出格式化为易读的表格而不是 JSON。

**--raw**
> 输出未经格式化的原始 JSON。

**--sandbox**
> 使用交易所的沙箱/测试网环境。

# COMMANDS

_exchange_id_
> 要连接的交易所（例如 binance、okx、bybit、kraken、coinbase）。

_exchange_id_ **markets**
> 列出交易所上所有可用的市场。

_exchange_id_ **currencies**
> 显示可用的币种及其属性。

_exchange_id_ **fetchTicker** _symbol_
> 获取某个交易对的当前行情数据。

_exchange_id_ **fetchOrderBook** _symbol_
> 获取某个交易对的订单簿。

_exchange_id_ **fetchTrades** _symbol_
> 获取某个市场的最近成交记录。

_exchange_id_ **fetchOHLCV** _symbol_ _timeframe_
> 获取 K 线/OHLCV 数据。

_exchange_id_ **fetchBalance**
> 获取账户余额（需要身份验证）。

_exchange_id_ **createOrder** _symbol_ _type_ _side_ _amount_ [_price_]
> 创建新订单（需要身份验证）。

**explain** _method_
> 显示某个方法所需的参数。

# DESCRIPTION

**CCXT**（CryptoCurrency eXchange Trading）CLI 是一个命令行界面，基于 CCXT 库与 100 多家加密货币交易所交互。它让你无需编写代码即可获取行情数据、查询余额、下单等。

该 CLI 同时支持公共 API（无需身份验证）和私有 API（需要 API 密钥）。凭据可通过环境变量（例如 BINANCE_APIKEY、BINANCE_SECRET）或 keys.local.json 配置文件提供。

输出默认为 JSON，可以通过管道传给 **jq** 等工具处理。**--table** 选项提供人类可读的格式化输出。

# CONFIGURATION

**keys.local.json**
> 存储用于交易所身份验证的 API 密钥和私钥。位于工作目录中。

# CAVEATS

CLI 会立即执行命令而不做确认。将数量误当作价格可能导致资金损失。CCXT 是非托管软件——它不持有资金，只提供对交易所的直接 API 访问。务必先用沙箱模式或小额资金测试。速率限制和 API 限制因交易所而异。

# HISTORY

CCXT 的创建目的是为各加密货币交易所提供统一的 API，屏蔽不同交易所 API 之间的差异。该项目始于约 **2017** 年，如今已支持 100 多家交易所。它提供了 JavaScript、TypeScript、Python、C#、PHP 和 Go 的库版本，而 CLI 则通过命令行提供同样的功能。

# SEE ALSO

[curl](/man/curl)(1), [jq](/man/jq)(1), [node](/man/node)(1)

# RESOURCES

```[Source code](https://github.com/ccxt/ccxt)```

```[Documentation](https://docs.ccxt.com)```

<!-- verified: 2026-06-22 -->
