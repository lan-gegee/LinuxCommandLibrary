# TAGLINE

跟踪块层 I/O 事件

# TLDR

**跟踪某设备上的块 I/O**

```blktrace -d [/dev/sda]```

**跟踪并将输出写入指定目录**

```blktrace -d [/dev/sda] -D [/tmp/traces]```

**跟踪多个设备**

```blktrace -d [/dev/sda] -d [/dev/sdb]```

**跟踪指定时长**

```blktrace -d [/dev/sda] -w [10]```

**跟踪并通过管道传给 blkparse**

```blktrace -d [/dev/sda] -o - | blkparse -i -```

**以指定的缓冲区大小跟踪**

```blktrace -d [/dev/sda] -b [1024]```

**停止跟踪**（在另一个终端中）

```killall blktrace```

# SYNOPSIS

**blktrace** [_options_]

# DESCRIPTION

**blktrace** 是一个 Linux 块层 I/O 跟踪工具，可捕获块设备操作的详细信息。它跟踪请求从提交、经过 I/O 调度器到完成的整个过程，让你了解存储子系统的行为。

跟踪内容涵盖队列插入、合并、向驱动的下发以及完成事件等。每个事件包含时间戳、进程 ID、动作代码和 I/O 参数（扇区、大小、标志）。

blktrace 产生二进制跟踪文件，可用 blkparse、btt 或其他工具分析。它对于诊断 I/O 性能问题、理解负载模式和调优存储配置非常有价值。

# PARAMETERS

**-d** _device_
> 要跟踪的设备（可指定多个）。

**-o** _file_
> 输出文件基本名。

**-D** _dir_
> 输出文件所在目录。

**-w** _seconds_
> 跟踪时长，单位为秒。

**-b** _size_
> 每个 CPU 的缓冲区大小，单位 KiB（默认 512）。

**-n** _num_
> 每个 CPU 的子缓冲区数量（默认 4）。

**-a** _action_
> 向跟踪过滤器掩码添加一个动作（如 queue、complete）。

**-A** _mask_
> 将跟踪过滤器设为给定的十六进制动作掩码。

**-r** _path_
> 要使用的 debugfs 挂载点（默认 /sys/kernel/debug）。

**-I** _file_
> 将 _file_ 中列出的设备加入跟踪目标。

**-l**, **--listen**
> 以服务器模式运行，通过网络接收跟踪数据。

**-h** _host_, **--host** _host_
> 跟踪时连接到给定的网络服务器。

**-V**, **-v**
> 显示版本。

# CAVEATS

需要 root 权限。必须已挂载 debugfs（通常位于 /sys/kernel/debug）。会为每个 CPU 创建需要 blkparse 才能读取的二进制跟踪文件。高 I/O 速率会迅速产生大量跟踪文件。在非常繁忙的系统上可能因跟踪开销影响性能。

# HISTORY

**blktrace** 由 **Jens Axboe** 开发，于 **2.6.17** 版本（**2006 年**发布）合并进 Linux 内核。其创建目的是深入洞察 Linux 块 I/O 层，取代较旧且不够详细的跟踪方法。该工具已成为 Linux 存储性能分析的标准工具，与 blkparse 和 btt 同属 blktrace 软件包。

# INSTALL

```apt: sudo apt install blktrace```

```dnf: sudo dnf install blktrace```

```zypper: sudo zypper install blktrace```

```nix: nix profile install nixpkgs#blktrace```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[blkparse](/man/blkparse)(1), [btrace](/man/btrace)(8), [btt](/man/btt)(1), [iostat](/man/iostat)(1), [iotop](/man/iotop)(1)

# RESOURCES

```[Source code](https://git.kernel.org/pub/scm/linux/kernel/git/axboe/blktrace.git)```

<!-- verified: 2026-06-19 -->
