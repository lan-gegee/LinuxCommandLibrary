# TAGLINE

实时重新执行已录制的终端会话

# TLDR

**实时执行** typescript 文件

```scriptlive path/to/timing_file path/to/typescript```

以**两倍速度**执行

```scriptlive path/to/timing_file path/to/typescript --divisor 2```

从 **stdin 日志**执行 typescript

```scriptlive --log-in path/to/stdin_log path/to/typescript```

以命令间**最大延迟**执行

```scriptlive path/to/timing_file path/to/typescript --maxdelay 2```

# SYNOPSIS

**scriptlive** [_options_] _timing_file_ _typescript_

# PARAMETERS

**--divisor** _n_
> 速度倍率（2 表示两倍速）

**--log-in** _file_
> 使用 stdin 日志文件作为输入

**--maxdelay** _seconds_
> 命令之间的最大等待时间

# DESCRIPTION

**scriptlive** 重新执行先前由 **script** 命令录制的终端会话。与只是被动显示录制输出的 **scriptreplay** 不同，scriptlive 实际上在活动的 shell 中运行这些命令，重现会话的操作及其真实效果。

该工具使用计时数据来控制命令执行的节奏，匹配原始会话的节奏。可以使用 **--divisor** 选项加快或减慢执行速度，**--maxdelay** 则限制命令之间的等待时间上限，从而跳过长时间的停顿。这对于自动化演示、复现测试场景以及重建特定的终端工作流程非常有用。

# CAVEATS

命令会被实际执行，可能产生副作用。对来自不可信来源的录制内容请谨慎使用。

# HISTORY

属于 **util-linux** 软件包，通过实时执行扩展了 script 的录制功能。

# INSTALL

```apt: sudo apt install bsdutils```

```apk: sudo apk add util-linux-misc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[script](/man/script)(1), [scriptreplay](/man/scriptreplay)(1)
