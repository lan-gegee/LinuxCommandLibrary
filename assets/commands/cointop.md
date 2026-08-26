# TAGLINE

基于终端的加密货币行情跟踪工具

# TLDR

**打开**交互式 TUI

```cointop```

**以投资组合视图启动**

```cointop --portfolio```

**只显示市值前 N 名**的加密货币

```cointop --top [50]```

**清除**缓存

```cointop clean```

**以人类可读格式显示当前持仓**

```cointop holdings --human```

**查询特定币种的价格**

```cointop price --coins [bitcoin,ethereum]```

**将配置重置**为默认值

```cointop reset --config```

# SYNOPSIS

**cointop** [_command_] [_options_]

# PARAMETERS

**clean**
> 清除缓存。

**holdings**
> 显示投资组合持仓。

**price**
> 查询特定币种的价格。

**reset**
> 重置配置或缓存。

**version**
> 显示版本信息。

**--portfolio**
> 以投资组合视图启动。

**--top** _N_
> 只显示市值前 N 名的加密货币。

**--no-color**
> 禁用彩色输出。

**--refresh-rate** _seconds_
> 数据刷新间隔（秒）。

**--human**
> 以人类可读格式显示数值（配合 holdings 使用）。

**--coins** _coins_
> 币种名称列表，以逗号分隔（配合 price 使用）。

# DESCRIPTION

**cointop** 是一款快速、轻量的基于终端的加密货币行情跟踪与投资组合管理工具。它通过交互式文本用户界面显示数千种加密货币的实时价格、市值、交易量和价格变动。

界面采用键盘驱动的 vim 风格按键（灵感来自 htop），可以快速浏览币种列表、详细图表和投资组合视图。用户可以标记收藏、按各种指标排序，并以成本价和盈亏计算来跟踪个人持仓。

数据来自加密货币 API（默认 CoinGecko），并在本地缓存以提升性能。该工具支持以多种货币显示价格，并提供以 ASCII 渲染的历史价格图表。配置存储在 **~/.config/cointop/config.toml**。

# CAVEATS

获取价格数据需要联网。API 可能存在速率限制。市场数据取决于所配置的数据源（CoinGecko 或 CoinMarketCap）。

# INSTALL

```nix: nix profile install nixpkgs#cointop```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ticker](/man/ticker)(1)
