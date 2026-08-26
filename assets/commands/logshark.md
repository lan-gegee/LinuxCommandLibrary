# TAGLINE

JSON 日志的 CLI 和 TUI 调试工具

# TLDR

**流式调试 JSON 日志**

```logshark```

从命令管道传入日志

```cat [logfile.json] | logshark```

# SYNOPSIS

**logshark** [_options_]

# DESCRIPTION

**logshark** 是一款用于调试 JSON 日志的命令行工具。它与 Beats 和 Logstash 集成，提供实时日志分析，支持 JSON 格式化、带语法高亮的美化打印以及事件指标统计。

TUI 模式允许在日志条目列表中导航并使用彩色格式化显示，更便于调试和分析来自 Elastic Stack 及类似日志管道的结构化日志数据。

# CAVEATS

专为 JSON 格式的日志设计。不支持非 JSON 日志格式。

# HISTORY

**logshark** 由 **ugosan** 创建，采用 **Go** 编写。

# SEE ALSO

[jq](/man/jq)(1), [lnav](/man/lnav)(1), [loggo](/man/loggo)(1)
