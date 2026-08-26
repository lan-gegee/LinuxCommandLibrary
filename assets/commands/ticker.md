# TAGLINE

终端股票与加密货币价格跟踪器

# TLDR

实时**监视股票价格**

```ticker -w [AAPL,MSFT,GOOG]```

通过配置文件**跟踪股票**及持仓

```ticker```

以 JSON 格式**显示股票价格**

```ticker -w [AAPL,MSFT] --format json```

以 CSV 格式**显示股票价格**

```ticker -w [AAPL,MSFT] --format csv```

**监视加密货币价格**

```ticker -w [BTC-USD,ETH-USD]```

**使用自定义配置文件**

```ticker -c [path/to/config.yaml]```

# SYNOPSIS

**ticker** [**-c** _config_] [**-w** _symbols_] [**--format** _format_] [**--show-fundamentals**] [**--show-tags**] [**--show-separator**]

# PARAMETERS

**-w**, **--watchlist** _symbols_
> 要监视的股票或加密货币代码列表，以逗号分隔。

**-c**, **--config** _file_
> 配置文件的路径。默认为 ~/.ticker.yaml。

**--format** _format_
> 输出格式：default、json 或 csv。

**--show-fundamentals**
> 显示市盈率、市值等基本面数据。

**--show-tags**
> 显示代码关联的标签。

**--show-separator**
> 在输出中的各代码之间显示分隔线。

**--show-holdings**
> 显示持仓和仓位价值。

**--sort** _field_
> 按字段排序输出（如 change、changePercent）。

**--proxy** _url_
> API 请求使用的代理 URL。

**-i**, **--interval** _seconds_
> 刷新间隔（秒）。

# DESCRIPTION

**ticker** 是一款基于终端的股票和加密货币跟踪工具，可显示实时价格更新和持仓跟踪。它使用 Go 编写，从 Yahoo Finance 和 CoinMarketCap 获取实时报价，支持股票、ETF、共同基金和加密货币。

该工具可以同时跟踪当前价格和你的投资组合持仓，支持多个成本批次。有数据时会显示盘前和盘后价格，适合在常规交易时间之外监控投资。

配置通常通过 YAML 文件（~/.ticker.yaml）完成，你可以在其中定义关注列表、带成本基础的持仓以及显示偏好。配置文件支持用标签对代码分组，并可设置多个投资组合。

# CAVEATS

受中间系统影响，来自 Yahoo Finance 的行情数据可能有轻微延迟（最多 30 秒）。NYSE 和 NASDAQ 提供实时数据，但其他交易所可能存在额外延迟。加密货币价格由 CoinMarketCap 通过 Yahoo Finance 提供。

# HISTORY

**ticker** 由 **Ani Channarasappa** 创建，首次发布于 **2020 年**。它的开发初衷是提供一个轻量级、基于终端的网络股票跟踪工具替代品，吸引了偏爱命令行工作流的开发者和终端爱好者。

# INSTALL

```apt: sudo apt install ticker```

```nix: nix profile install nixpkgs#ticker```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[curl](/man/curl)(1), [jq](/man/jq)(1)
