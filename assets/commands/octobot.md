# TAGLINE

开源加密货币交易机器人

# TLDR

**启动机器人**

```octobot```

**以模拟交易模式启动**

```octobot --simulate```

**不带网页界面启动**

```octobot --no_web```

**以回测模式启动**

```octobot --backtesting```

**使用指定策略运行策略优化器**

```octobot --strategy_optimizer [StrategyClass]```

**管理 tentacles（插件）**

```octobot tentacles --install --all```

# SYNOPSIS

**octobot** [_options_]

**octobot** **tentacles** [_options_]

**octobot** **node** [_options_]

# PARAMETERS

**-s**, **--simulate**
> 仅以交易模拟器模式启动（不做实盘交易）。

**-nw**, **--no_web**
> 不带网页界面启动。

**-nt**, **--no-telegram**
> 不带 Telegram 界面启动。

**-nl**, **--no_logs**
> 禁用回测日志。

**-b**, **--backtesting**
> 使用 config.json 中的设置以回测模式启动。

**-bf**, **--backtesting-files** _FILES_
> 指定回测数据文件（需要 `-b`）。

**-wdr**, **--whole-data-range**
> 回测时使用整个数据集而不是公共重叠部分。

**-ebt**, **--enable-backtesting-timeout**
> 将回测运行限制在 30 分钟以内。

**-r**, **--risk** _VALUE_
> 设置介于 0 到 1 之间的风险配置。

**-rts**, **--reset-trading-history**
> 重置交易历史并以全新的投资组合开始。

**-o**, **--strategy_optimizer** _STRATEGY_
> 使用指定的策略类运行策略优化器。

**-u**, **--update**
> 将 OctoBot 更新到最新的可用版本。

**--encrypter**
> 启动交易所 API 密钥加密工具。

**--identifier** _ID_
> 设置 OctoBot 社区标识符。

**-v**, **--version**
> 显示版本信息。

# DESCRIPTION

**octobot** 是一个开源的加密货币交易机器人，支持在 15+ 家交易所上进行自动化交易，包括 AI 驱动策略、网格交易、DCA（定投）以及自定义策略。

机器人可以通过命令行无界面运行，也可以通过网页界面进行配置和监控。它支持用于评估策略的回测，以及用于无风险测试的模拟交易。策略和交易所通过名为 tentacles 的插件配置，由 `tentacles` 子命令管理。

`node` 子命令以网络节点模式启动 OctoBot，支持 `--host`、`--port`、`--master` 和 `--consumer_only` 等选项，适用于分布式部署。

# CAVEATS

需要 Python 3.10 及以上版本。实盘交易需要交易所 API 密钥。交易存在财务风险。可通过 pip 或 Docker 获取。

# SEE ALSO

[freqtrade](/man/freqtrade)(1), [hummingbot](/man/hummingbot)(1), [cointop](/man/cointop)(1)
