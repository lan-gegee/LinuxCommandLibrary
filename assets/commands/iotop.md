# TAGLINE

类 top 的实用工具，实时监视各进程的磁盘 I/O 使用情况

# TLDR

**启动 iotop**（显示所有进程）

```sudo iotop```

**只显示正在做 I/O 的进程**

```sudo iotop -o```

**显示累计 I/O** 而非带宽

```sudo iotop -a```

**不显示线程**（仅进程）

```sudo iotop -P```

带指定迭代次数的**非交互模式**

```sudo iotop -b -n [10]```

按 PID **监视特定进程**

```sudo iotop -p [PID]```

**监视特定用户**

```sudo iotop -u [username]```

**每 N 秒刷新一次**

```sudo iotop -d [2]```

# SYNOPSIS

**iotop** [_-oaPbkqtd_] [_-n iterations_] [_-p pid_] [_-u user_]

# PARAMETERS

**-o**, **--only**
> 只显示实际在做 I/O 的进程。

**-a**, **--accumulated**
> 显示累计 I/O 而非带宽。

**-P**, **--processes**
> 仅显示进程，不显示线程。

**-b**, **--batch**
> 非交互批处理模式（用于日志记录）。

**-n** _NUM_
> 退出前的迭代次数。

**-d** _SEC_
> 刷新间隔（秒）。

**-p** _PID_
> 监视指定进程。

**-u** _USER_
> 监视指定用户的进程。

**-k**, **--kilobytes**
> 以千字节而非人类可读格式显示。

**-t**, **--time**
> 为每行添加时间戳（批处理模式）。

**-q**, **--quiet**
> 抑制表头行（批处理模式）。使用两次可同时抑制列名。

**--no-help**
> 抑制交互帮助行。

# INTERACTIVE KEYS

**Left/Right arrows**
> 更改排序列。

**r**
> 反转排序方向。

**o**
> 切换是否只显示活跃进程。

**p**
> 切换显示进程/线程。

**a**
> 切换累计/带宽模式。

**q**
> 退出。

**i**
> 更改所选进程的 ionice 优先级。

# DESCRIPTION

**iotop** 是一款类 top 的实用工具，实时监视各进程的磁盘 I/O 使用情况。它实时显示每个进程的读写操作，帮助找出哪些应用在造成磁盘活动。

显示内容包括线程/进程 ID、优先级、用户、磁盘读取速率、磁盘写入速率、swap-in 百分比、I/O 百分比和命令等列。I/O 百分比表示等待 I/O 操作所花费的时间比例。

累计模式（-a）适合找出那些偶发但 I/O 量大的进程。它不显示瞬时带宽，而是显示自 iotop 启动以来读/写的总字节数，从而暴露那些即使只做了短暂重度 I/O 的进程。

该工具需要 root 权限才能访问内核 taskstats 接口的 I/O 统计数据。内核必须启用 CONFIG_TASK_IO_ACCOUNTING（大多数发行版都已启用）。

批处理模式可持续记录 I/O 活动。配合 -t 添加时间戳，可以在问题时段捕获活动，诊断间歇性 I/O 问题。

# CAVEATS

需要 root 权限。内核必须启用 IO 统计（CONFIG_TASK_IO_ACCOUNTING）。只显示磁盘 I/O，不包括网络或其他 I/O。可能带来轻微开销。某些 I/O 可能被归因于内核线程而非用户进程。

# HISTORY

**iotop** 由 Guillaume Chazarain 编写，约 **2007 年**首次发布。它的诞生填补了 Linux 监控工具的空白 —— CPU 和内存监控有 top，而磁盘 I/O 监控一直没有对应的工具。该工具依赖 Linux 2.6.20 中加入的内核特性（taskstats）。另有一个基于 Rust 的替代实现 **iotop-c**，界面类似。

# INSTALL

```pacman: sudo pacman -S iotop```

```apk: sudo apk add iotop```

```zypper: sudo zypper install iotop```

```nix: nix profile install nixpkgs#iotop```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[htop](/man/htop)(1), [top](/man/top)(1), [iostat](/man/iostat)(1), [vmstat](/man/vmstat)(8), [dstat](/man/dstat)(1)
