# TAGLINE

实时追踪文件访问事件

# TLDR

在**所有**文件系统上打印文件访问事件

```sudo fatrace```

限定特定的**命令**名称

```sudo fatrace -C [program_name]```

只在**当前挂载点**上打印事件

```sudo fatrace -c```

在输出中添加**时间戳**

```sudo fatrace -t```

只显示**读取和写入**事件

```sudo fatrace -f RW```

**10 秒后**停止并写入文件

```sudo fatrace -s [10] -o [output.log]```

# SYNOPSIS

**fatrace** [_options_]

# DESCRIPTION

**fatrace** 报告来自内核 fanotify 接口的文件访问事件。它实时显示哪些进程正在访问哪些文件，帮助找出造成不必要磁盘活动或唤醒的进程。

可用于调试、安全监控，以及理解应用程序的文件访问模式。

# PARAMETERS

**-c**, **--current-mount**
> 只记录当前目录所在分区/挂载点上的事件。

**-C**, **--command** _COMMAND_
> 只显示此命令名称的事件。

**-f**, **--filter** _TYPES_
> 只显示给定的事件类型：C（关闭）、R（读取）、O（打开）、W（写入）、D（删除）、+（创建）、<（移动）。

**-o**, **--output** _FILE_
> 将事件写入指定文件而不是标准输出。

**-p**, **--ignore-pid** _PID_
> 忽略此进程 ID 的事件。可多次指定。

**-s**, **--seconds** _SECONDS_
> 在给定的秒数后停止。

**-t**, **--timestamp**
> 为事件添加时间戳。指定两次则以 epoch 格式显示。

**-h**, **--help**
> 打印帮助并退出。

# CAVEATS

需要 root 权限。使用 fanotify，要求 Linux 2.6.37 及以上版本。在繁忙的系统上可能影响性能。

# INSTALL

```apt: sudo apt install fatrace```

```dnf: sudo dnf install fatrace```

```zypper: sudo zypper install fatrace```

```nix: nix profile install nixpkgs#fatrace```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[inotifywait](/man/inotifywait)(1), [lsof](/man/lsof)(8), [strace](/man/strace)(1)
