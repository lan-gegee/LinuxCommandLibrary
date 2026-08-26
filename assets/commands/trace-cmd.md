# TAGLINE

Linux 内核 Ftrace 跟踪前端

# TLDR

显示跟踪**状态**

```sudo trace-cmd stat```

列出可用的**跟踪器**

```sudo trace-cmd list -t```

使用插件**开始**跟踪

```sudo trace-cmd start -p [function|function_graph|irqsoff|wakeup]```

**查看**跟踪输出

```sudo trace-cmd show```

**停止**跟踪

```sudo trace-cmd stop```

**清空**跟踪缓冲区

```sudo trace-cmd clear```

**记录**特定事件的跟踪

```sudo trace-cmd record -e [sched_switch]```

为特定函数**记录**函数调用图跟踪

```sudo trace-cmd record -p function_graph -g [function_name]```

显示文件中**已记录的**跟踪

```trace-cmd report```

列出可用的**事件**

```sudo trace-cmd list -e```

# SYNOPSIS

**trace-cmd** _COMMAND_ [_OPTIONS_]

# COMMANDS

**stat**
> 显示跟踪系统状态

**start**
> 启动内核跟踪器

**stop**
> 停止内核跟踪器

**show**
> 查看当前跟踪输出

**clear**
> 清空跟踪缓冲区

**record**
> 将跟踪记录到文件

**report**
> 显示已记录的跟踪

**list**
> 列出可用的跟踪器、事件和函数

# PARAMETERS

**-p** _PLUGIN_
> 指定跟踪器插件（function、function_graph、irqsoff、wakeup 等）

**-e** _EVENT_
> 启用一个跟踪事件（可多次指定）

**-g** _FUNCTION_
> 从特定函数开始跟踪调用（与 function_graph 配合使用）

**-o** _FILE_
> 将跟踪输出写入指定文件（默认：trace.dat）

**-t**
> 列出可用的跟踪器（与 list 子命令配合使用）

**-F**
> 只跟踪 fork 之后的子进程

# DESCRIPTION

**trace-cmd** 是一个用于与 Linux 内核 Ftrace 跟踪框架交互的工具。它提供友好的接口来配置和捕获内核跟踪，分析函数调用、耗时和系统事件。

该工具支持多种跟踪器插件，包括函数跟踪、函数调用图以及用于调试和性能分析的延迟跟踪器。

# CAVEATS

需要 root 权限。跟踪可能影响系统性能。大型跟踪会占用大量内存和存储空间。某些功能取决于内核配置。

# HISTORY

**trace-cmd** 由 **Steven Rostedt** 创建，是 Linux 内核 Ftrace 框架的前端，简化了内核跟踪与分析的过程。

# INSTALL

```apt: sudo apt install trace-cmd```

```dnf: sudo dnf install trace-cmd```

```pacman: sudo pacman -S trace-cmd```

```zypper: sudo zypper install trace-cmd```

```nix: nix profile install nixpkgs#trace-cmd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[trace-cmd-list](/man/trace-cmd-list)(1), [trace-cmd-record](/man/trace-cmd-record)(1), [trace-cmd-report](/man/trace-cmd-report)(1), [perf](/man/perf)(1), [strace](/man/strace)(1)
