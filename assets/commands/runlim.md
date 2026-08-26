# TAGLINE

测量并限制命令的资源使用

# TLDR

打印命令的**时间和内存**使用情况

```runlim command arguments```

将统计信息记录到**文件**

```runlim -o path/to/file command arguments```

限制 **CPU 时间**（秒）

```runlim -t 60 command arguments```

限制**实际时间**（秒）

```runlim -r 120 command arguments```

限制**内存空间**（MB）

```runlim -s 1024 command arguments```

组合**时间与空间限制**并输出日志

```runlim -t 300 -s 2048 -o path/to/log command arguments```

# SYNOPSIS

**runlim** [_options_] _command_ [_arguments_...]

# PARAMETERS

**-o** _FILE_, **--output-file**=_FILE_
> 覆盖或创建 FILE 用于输出日志记录

**-t** _NUM_, **--time-limit**=_NUM_
> 将 CPU 时间限制设为 NUM 秒

**-r** _NUM_, **--real-time-limit**=_NUM_
> 将实际时间（墙上时钟）限制设为 NUM 秒

**-s** _NUM_, **--space-limit**=_NUM_
> 将内存限制设为 NUM 兆字节

**-k**, **--kill**
> 向子进程传播信号

**-h**, **--help**
> 显示选项摘要

**--version**
> 显示程序版本

# DESCRIPTION

**runlim** 执行命令的同时对其时间与内存使用情况进行采样和限制，包括所有子进程。它通过 /proc 文件系统每 100 毫秒采样一次资源消耗，并每秒向 stderr 记录一次状态信息。

该工具适用于基准测试、自动化测试，以及防止失控进程消耗过多资源。

# CAVEATS

仅限 Linux；依赖 /proc 文件系统。资源测量是采样值，并非精确值。

# HISTORY

由 **Armin Biere** 和 **Toni Jussila** 编写。常用于 SAT 求解器竞赛和自动化测试环境。

# INSTALL

```apt: sudo apt install runlim```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[time](/man/time)(1), [timeout](/man/timeout)(1), [ulimit](/man/ulimit)(1)
