# TAGLINE

终端中的 Nginx 日志分析工具

# TLDR

**分析默认的 nginx 日志文件**

```rhit```

**筛选从指定日期开始的日志**

```rhit -d '[2024-01-15]..'```

**按传输字节数统计**

```rhit -m bytes [/var/log/nginx/access.log]```

# SYNOPSIS

**rhit** [_options_] [_logfile_...]

# PARAMETERS

**-d** _DATE_RANGE_
> 按日期范围筛选日志（例如 '2024-01-15..'、'..2024-02-01'）。

**-m** _METRIC_
> 按给定指标统计：hits（请求数）或 bytes（字节数）。

# DESCRIPTION

**rhit** 从标准位置读取 nginx 日志文件（包括 gzip 压缩的日志），进行分析，并在终端中以格式化表格展示结果。它支持按日期筛选、按请求数或字节数统计，以及查看热门或冷门的 IP 地址。

# HISTORY

**rhit** 由 **Canop**（Denys Seguret）创建，使用 **Rust** 编写。

# INSTALL

```pacman: sudo pacman -S rhit```

```brew: brew install rhit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[goaccess](/man/goaccess)(1), [broot](/man/broot)(1)
