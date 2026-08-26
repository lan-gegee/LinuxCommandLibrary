# TAGLINE

加密货币交易机器人框架

# TLDR

使用配置和策略**开始交易**

```freqtrade trade --config [config.json] --strategy [StrategyName]```

对历史数据**运行回测**

```freqtrade backtesting --config [config.json] --strategy [StrategyName]```

为回测**下载历史数据**

```freqtrade download-data --config [config.json] --pairs [BTC/USDT] --timeframes [1h]```

以交互方式**创建新的配置文件**

```freqtrade new-config```

用 hyperopt **优化策略参数**

```freqtrade hyperopt --config [config.json] --strategy [StrategyName] --hyperopt-loss [SharpeHyperOptLoss]```

**列出可用的交易所**

```freqtrade list-exchanges```

列出某个交易所的**交易对**

```freqtrade list-pairs --config [config.json] --exchange [binance]```

**启动 Web UI**

```freqtrade webserver --config [config.json]```

# SYNOPSIS

**freqtrade** _command_ [_options_]

**freqtrade** trade [_-c config_] [_-s strategy_]

**freqtrade** backtesting [_-c config_] [_-s strategy_]

# PARAMETERS

**-c**, **--config** _PATH_
> 指定配置文件（默认：config.json）。

**-s**, **--strategy** _NAME_
> 指定策略类名。

**--strategy-path** _PATH_
> 额外的策略查找路径。

**-d**, **--datadir** _PATH_
> 历史数据目录路径。

**--userdir** _PATH_
> 用户数据目录路径。

**-v**, **--verbose**
> 详细模式（-vv 输出更多，-vvv 输出全部）。

**--logfile** _FILE_
> 将日志写入指定文件。

**--no-color**
> 禁用彩色输出。

**--db-url** _URL_
> 用于存储交易的数据库 URL。

**--dry-run**
> 以模拟模式运行，不进行真实交易。

**-V**, **--version**
> 显示版本号。

**-h**, **--help**
> 显示帮助信息。

# CONFIGURATION

**config.json**
> 主配置文件，指定交易所、API 密钥、交易参数、投入金额（stake amount）和策略设置。

**user_data/strategies/**
> 存放自定义交易策略 Python 类的目录。

# COMMANDS

**trade**
> 开始实盘或模拟交易。

**backtesting**
> 在历史数据上测试策略。

**hyperopt**
> 优化策略参数。

**download-data**
> 下载历史 OHLCV 数据。

**new-config**
> 以交互方式创建新配置。

**create-userdir**
> 创建用户数据目录结构。

**list-exchanges**
> 列出可用的交易所。

**list-pairs**
> 列出可用的交易对。

**list-strategies**
> 列出可用的策略。

**list-timeframes**
> 列出可用的时间周期。

**show-trades**
> 显示数据库中的交易记录。

**plot-dataframe**
> 将策略信号绘制到图表上。

**plot-profit**
> 绘制随时间变化的收益曲线。

**webserver**
> 启动 FreqUI Web 界面。

**install-ui**
> 安装 FreqUI Web 界面。

# DESCRIPTION

**freqtrade** 是一个用 Python 编写的开源加密货币交易机器人。它通过 CCXT 库支持在 Binance、Kraken、Coinbase 等主要交易所进行自动化交易。

该机器人执行用户自定义的交易策略，这些策略基于技术指标指定入场和出场条件。策略是 Python 类，可以在实盘部署前先对历史数据进行回测。hyperopt 功能利用机器学习优化策略参数。

Freqtrade 默认在 dry-run 模式下运行，即模拟交易而不动真钱。它可以通过 Telegram 机器人或 FreqUI Web 界面控制。交易数据存储在 SQLite 数据库中以便分析，plot 命令可将策略表现可视化。

# CAVEATS

加密货币交易具有重大财务风险。回测结果不能保证未来的表现。交易所 API 可能有限速，影响机器人运行。策略在实盘交易前必须在 dry-run 模式下充分测试。配置文件包含 API 密钥，应妥善保管。机器人需要持续运行和稳定的网络连接。

# HISTORY

Freqtrade 于 **2017** 年作为社区驱动的开源项目启动。它以 **Python 3** 编写，从一个简单的交易机器人发展为集回测、优化和可视化工具于一体的完整交易框架。该项目在 2020-2021 年加密货币牛市期间获得大量关注，并于 **2022** 年推出用于机器学习自适应策略的 FreqAI。开发仍在 GitHub 上活跃进行，并定期发布新版本。

# SEE ALSO

[ccxt](/man/ccxt)(1), [python](/man/python)(1)
