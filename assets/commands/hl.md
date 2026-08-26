# TAGLINE

面向 JSON 和 logfmt 的高速日志查看与处理工具

# TLDR

**查看 JSON 日志**文件

```hl [path/to/logfile.json]```

**按级别过滤日志**

```hl -l [error] [path/to/logfile]```

**按字段值过滤**

```hl -f [key]=[value] [path/to/logfile]```

**不用分页器流式输出日志**

```hl -P [path/to/logfile]```

**按时间范围过滤**

```hl --since "[2024-01-01]" --until "[2024-01-02]" [path/to/logfile]```

**以本地时区显示日志**

```hl -L [path/to/logfile]```

**从 stdin 读取**

```cat [path/to/logfile] | hl```

# SYNOPSIS

**hl** [**-l** _level_] [**-f** _filter_] [**--since** _time_] [**--until** _time_] [**-P**] [**-L**] [_file_...]

# PARAMETERS

**-l** _LEVEL_
> 按日志级别过滤（debug、info、warn、error）

**-f** _KEY=VALUE_
> 按字段值过滤

**--since** _TIME_
> 只显示此时间戳之后的日志

**--until** _TIME_
> 只显示此时间戳之前的日志

**-P**
> 禁用分页器（流式模式）

**-L**
> 以本地时区显示时间戳

**-Z** _ZONE_
> 以指定时区显示时间戳

**--allow-prefix**
> 处理带非 JSON 前缀的日志

# DESCRIPTION

**hl** 是一个高性能的日志查看与处理工具，可将 **JSON** 日志和 **logfmt** 日志转换为清晰的人类可读格式。它会自动检测日志格式，并以彩色编码的输出呈现，便于快速分析。

该工具支持按字段过滤、按日志级别过滤以及按时间戳范围过滤。它自动集成分页器（默认为 **less**），并支持通过配置文件自定义主题。

# CAVEATS

专为结构化日志格式（JSON、logfmt）设计；纯文本日志会原样透传。处理非常大的日志文件时，可利用其流式模式避免将整个文件缓冲到内存中。

# HISTORY

**hl** 由 **pamburus** 创建，使用 **Rust** 编写。其设计目标是成为 **jq** 等工具在日志分析场景下极快的替代品，内置对常见日志格式和级别的理解。

# INSTALL

```pacman: sudo pacman -S hl```

```brew: brew install hl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jq](/man/jq)(1), [less](/man/less)(1), [tailspin](/man/tailspin)(1)
