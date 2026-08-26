# TAGLINE

交互式命令行基准测试工具

# TLDR

以默认 10 次运行对单条命令进行**基准测试**

```cmdperf "sleep 0.1"```

并排**比较**两条命令

```cmdperf "grep 'ERROR' log.txt" "rg 'ERROR' log.txt"```

**运行**一条命令 100 次迭代

```cmdperf -n 100 "ls -la"```

**模拟** 10 个并发请求

```cmdperf -c 10 "curl -s https://example.com > /dev/null"```

**运行**固定时长 30 秒

```cmdperf -d 30s "redis-cli PING"```

将结果**导出**到 markdown 文件

```cmdperf --markdown [results.md] "sleep 0.1" "sleep 0.2"```

# SYNOPSIS

**cmdperf** [_options_] _command_ [_command_...]

# PARAMETERS

**-n**, **--runs=**_N_
> 要运行的迭代次数（默认：10）。

**-c**, **--concurrency=**_N_
> 并行执行的数量（默认：1）。

**-d**, **--duration=**_DURATION_
> 按固定时长运行，而非固定次数。

**-r**, **--rate=**_RATE_
> 目标请求速率，以每秒请求数计。

**-t**, **--timeout=**_DURATION_
> 单条命令的超时时间（默认：1m）。

**-s**, **--shell=**_SHELL_
> 用于执行命令的 Shell（默认：/bin/sh）。

**--shell-opt=**_OPT_
> Shell 选项，可重复指定（默认：-c）。

**-N**, **--no-shell**
> 直接执行命令，不经 Shell 包装。

**--csv=**_FILE_
> 将结果导出到 CSV 文件。

**--markdown=**_FILE_
> 将结果导出到 Markdown 文件。

**--fail-on-error**
> 任一命令返回非零退出码时以非零状态退出。

**--color-scheme=**_SCHEME_
> 设置配色方案（auto、catppuccin、tokyonight、nord、monokai、solarized、solarized-light、gruvbox、monochrome）。

**--list-color-schemes**
> 显示可用的配色方案。

**--version**
> 显示版本信息。

# DESCRIPTION

**cmdperf** 反复运行一条或多条 shell 命令并收集计时统计数据，通过实时终端界面展示进度条、预计剩余时间和关键指标，包括平均执行时间、标准差和最小/最大范围。它支持单命令基准测试、多命令比较、模拟负载的并发执行、基于时长的运行，以及面向 HTTP 端点测试的速率限制。

# CAVEATS

设计用于快速交互式基准测试，不能替代严谨的统计分析工具。默认的 Shell 包装会带来额外开销；当不需要 Shell 特性时，可使用 **-N/--no-shell** 获得更精确的测量结果。

# HISTORY

**cmdperf** 由 **miklosn** 创建，采用 Go 编写并以 MIT 许可证发布。最新版本为 v0.1.4（2026 年 1 月）。它是 **hyperfine** 等工具的轻量交互式替代品，专注于实时 TUI 体验和并发执行模拟。

# SEE ALSO

[hyperfine](/man/hyperfine)(1), [time](/man/time)(1), [perf](/man/perf)(1)
