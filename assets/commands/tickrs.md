# TAGLINE

在终端中查看实时股票行情

# TLDR

**以指定的股票代码启动**

```tickrs -s [AAPL],[MSFT]```

**1 个月周期的蜡烛图**

```tickrs -s [AAPL] -c candle -t 1M```

**显示盘前/盘后交易时段**

```tickrs -s [TSLA] -p```

**以汇总模式启动并显示成交量图**

```tickrs -s [AAPL],[GOOGL] --summary --show-volumes```

**显示 x 轴标签并自定义更新间隔**

```tickrs -s [MSFT] -x -i [5]```

# SYNOPSIS

**tickrs** [_flags_] [_options_]

# PARAMETERS

**-s, --symbols** _SYMBOLS_
> 启动时要显示的股票代码列表，以逗号分隔。

**-c, --chart-type** _TYPE_
> 图表类型：line（默认）、candle 或 kagi。

**-t, --time-frame** _FRAME_
> 时间周期：1D（默认）、1W、1M、3M、6M、1Y、5Y。

**-i, --update-interval** _SECONDS_
> 从 API 更新数据的间隔（默认：1）。

**-p, --enable-pre-post**
> 为图表启用盘前/盘后交易时段。

**--show-volumes**
> 显示成交量图。

**-x, --show-x-labels**
> 显示 x 轴标签。

**--summary**
> 以汇总模式启动。

**--hide-prev-close**
> 在 1D 图表上隐藏昨收线。

**--trunc-pre**
> 将盘前图表截断至开盘前 30 分钟。

# DESCRIPTION

**tickrs** 直接在你的终端中显示来自 Yahoo! Finance 的实时行情数据。它支持多种图表类型、多种时间周期、盘前/盘后交易时段、成交量图，以及带盈亏显示的投资组合跟踪。

# HISTORY

**tickrs** 由 **tarkah** 创建，使用 **Rust** 编写。

# INSTALL

```pacman: sudo pacman -S tickrs```

```nix: nix profile install nixpkgs#tickrs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ticker](/man/ticker)(1), [cointop](/man/cointop)(1)
