# TAGLINE

为选定的进程捕获内核堆栈跟踪（Oracle Linux 增强诊断工具）

# TLDR

一次性**显示所有进程的内核堆栈**

```kstack -a```

**显示等待 I/O 的进程的内核堆栈**

```kstack -D```

**显示指定 PID 的内核堆栈**

```kstack -p [pid1],[pid2]```

**组合选择器：D 状态加指定 PID**

```kstack -Dp [pid1],[pid2]```

**后台每 30 秒采样一次 D 状态进程，持续 30 分钟**

```kstack -D -b -t [30] -i [30]```

**后台采样，并将日志写入自定义目录**

```kstack -b -d [/var/log/kstack]```

# SYNOPSIS

**kstack** **-a** | **-DIRSZ** **-p** _PID_[**,**...] [_options_]

# PARAMETERS

**-a**
> 所有进程（不能与状态选择器组合）。

**-D**
> 处于 **D** 状态的进程（不可中断睡眠，例如等待 I/O 或锁）。

**-R**
> 正在运行或可运行的进程。

**-S**
> 睡眠中（可中断）的进程。

**-Z**
> 僵尸进程。

**-p** _PID_[**,**...]
> 为列出的 PID 转储内核堆栈（逗号分隔）。

**-b**
> 以后台模式运行，按间隔采样并将文件写入磁盘。

**-t** _MINUTES_
> 后台模式的运行分钟数（默认 **30**）。

**-i** _SECONDS_
> 后台模式的采样间隔秒数（默认 **60**）。

**-d** _DIRECTORY_
> 后台模式日志文件的输出目录（默认 **/var/oled/kstack**）。

**-m** _SIZE_MB_
> 日志文件轮转压缩前的最大大小（MB）（默认 **1**）。

**-n** _COUNT_
> 保留的轮转日志文件数量（默认 **5**）。

**-x** _PERCENT_
> 当目标文件系统使用率超过 _PERCENT_ 时拒绝运行（默认 **85**）。

**-h**, **--help**
> 显示帮助文本。

**-v**, **--verbose**
> 打印调试信息。

# DESCRIPTION

**kstack** 是 **Oracle Linux Enhanced Diagnostics (OLED)** 工具集中的一款诊断实用程序，用于捕获一个或多个进程的内核堆栈跟踪。它从 **/proc/[pid]/stack** 和 **/proc/[pid]/status** 读取数据，然后将共享相同堆栈的进程分组归并，避免重复。

在前台模式（默认）下，**kstack** 向标准输出发出一次采样。在后台模式（**-b**）下，它按配置的间隔循环运行指定的时长，并在 **/var/oled/kstack** 下写入门控轮转的日志文件（可用 **-d** 覆盖）。状态选择器 **-D**、**-R**、**-S**、**-Z** 与 **-p** 可以组合使用；**-a** 是互斥的。

该工具最常用于排查挂起的任务、I/O 延迟和锁竞争——查看处于 **D** 状态进程的内核调用栈可以揭示它阻塞在哪个内核函数上。

# CAVEATS

必须以 **root** 身份运行。默认拒绝写入使用率超过 **85%** 的文件系统（可用 **-x** 调整）。在进程非常多的系统上，**-a** 可能产生大量输出。由 Oracle Linux 7、8 和 9 上的 **oled-tools** 软件包提供；在其他发行版上一般不可用。

# HISTORY

**kstack** 随 **Oracle Linux Enhanced Diagnostics (OLED)** 一起发布。OLED 是 Oracle 于 **2021 年**开源的一组调试实用程序，用于支持 Oracle Linux 上复杂内核问题的诊断。该集合还包括 **lkce**、**memstate**、**syswatch**、**trace** 等工具。

# SEE ALSO

[ps](/man/ps)(1), [top](/man/top)(1), [strace](/man/strace)(1), [perf](/man/perf)(1), [proc](/man/proc)(5)
