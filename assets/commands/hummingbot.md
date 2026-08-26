# TAGLINE

开源加密货币交易机器人框架

# TLDR

**启动交互式 TUI**

```hummingbot```

**以指定策略启动**

```hummingbot -s [strategy_name]```

**以指定配置文件启动**

```hummingbot --config-file-name [config.yml]```

**带密码启动**

```hummingbot --config-password [password]```

# SYNOPSIS

**hummingbot** [_options_]

# PARAMETERS

**-s** _STRATEGY_, **--strategy** _STRATEGY_
> 启动时使用的策略。

**--config-file-name** _FILE_
> 要使用的配置文件。

**--config-password** _PASSWORD_
> 加密配置文件的密码。

**-h**, **--help**
> 显示帮助。

# DESCRIPTION

**hummingbot** 是一个开源加密货币交易机器人框架，提供用于自动化交易的交互式终端界面。它支持做市、套利、流动性挖矿等策略，覆盖中心化与去中心化交易所。

TUI 提供实时状态更新、订单跟踪和盈亏报告。用户可以通过交互式提示或 YAML 配置文件配置策略。该机器人支持模拟盘（paper trading）模式，可在不承担资金风险的情况下测试策略。

# CAVEATS

需要受支持交易所的 API 密钥。交易涉及财务风险。需要 Python 3.8+ 及各类依赖项。可通过 Docker 或源码安装。

# SEE ALSO

[freqtrade](/man/freqtrade)(1), [gocryptotrader](/man/gocryptotrader)(1), [cointop](/man/cointop)(1)
