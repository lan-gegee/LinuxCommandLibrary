# TAGLINE

core dump 的获取与分析

# TLDR

**列出**所有捕获到的 core dump

```coredumpctl```

列出**特定程序**的 core dump

```coredumpctl list program```

显示指定 PID 的 core dump **信息**

```coredumpctl info 1234```

使用最后一个 core dump 进行**调试**

```coredumpctl debug```

调试**特定程序**最近一次的 core dump

```coredumpctl debug program```

将 core dump **提取**到文件

```coredumpctl -o /path/to/file dump program```

使用自定义的 **gdb 参数**进行调试

```coredumpctl debug -A "-ex bt"```

# SYNOPSIS

**coredumpctl** [_OPTIONS_] [_COMMAND_] [_MATCHES_...]

# DESCRIPTION

**coredumpctl** 是一个 systemd 工具，用于管理 core dump——程序崩溃时产生的内存快照。systemd-coredump 不再把传统的 core dump 文件散落在文件系统各处，而是捕获崩溃并将其连同丰富元数据（包括时间戳、进程信息和系统状态）一起存储在 journal 中。

该工具为操作这些捕获到的 core dump 提供了统一接口。你可以列出所有崩溃、按程序或时间范围过滤、查看特定崩溃的详细信息，还可以启动调试器来分析故障。core dump 也可以提取到文件中，便于离线分析或分享给开发者。

这种集中式的 core dump 管理方式让排查偶发崩溃、调试生产问题以及维护系统可靠性变得容易得多。与 journalctl 的集成意味着崩溃数据与系统日志一同保存，为调试提供完整上下文。该工具要求将 systemd-coredump 配置为系统的 core dump 处理器——在大多数现代基于 systemd 的发行版上这是默认设置。

# COMMANDS

**list [MATCHES]**
> 列出 journal 中的 core dump（默认命令）

**info [MATCHES]**
> 显示 core dump 的详细信息

**dump [MATCHES]**
> 将 core dump 数据导出到 stdout 或文件

**debug [MATCHES]**
> 对某个 core dump 调用调试器

# PARAMETERS

**-o, --output FILE**
> 将 dump 输出写入文件

**-1**
> 只显示最近的 core dump

**-S, --since TIME**
> 按起始时间过滤

**-U, --until TIME**
> 按结束时间过滤

**-r, --reverse**
> 最新的条目优先显示

**-F, --field FIELD**
> 打印指定字段的所有值

**-D, --directory DIR**
> 使用指定目录中的 journal 文件

**--debugger DEBUGGER**
> 使用指定的调试器（默认：gdb）

**-A, --debugger-arguments ARGS**
> 向调试器传递参数

**-n, --lines NUM**
> 要显示的 journal 行数

**-q, --quiet**
> 抑制提示性消息

**--json MODE**
> 以 JSON 输出（short、pretty、off）

# MATCHES

匹配条件可按以下内容过滤：PID、可执行文件名、路径或 core dump 时间戳。

# CONFIGURATION

**/etc/systemd/coredump.conf**
> 控制 core dump 存储、压缩和保留策略的配置文件。

# CAVEATS

core dump 可能包含敏感数据。请确保提取出的文件具有合适的权限。需要将 systemd-coredump 配置为系统的 core dump 处理器。

# HISTORY

**coredumpctl** 是 **systemd** 的一部分，通过 systemd-coredump 和 journal 提供集中式的 core dump 管理。

# INSTALL

```apt: sudo apt install systemd-coredump```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gdb](/man/gdb)(1), [journalctl](/man/journalctl)(1)
