# TAGLINE

施加 CPU、内存和 I/O 负载

# TLDR

启动 4 个工作进程对 **CPU** 进行压力测试

```stress -c 4```

启动 2 个工作进程带超时地对 **IO** 施压

```stress -i 2 -t 5```

启动 2 个工作进程对**内存**施压

```stress -m 2 --vm-bytes 256M```

启动 2 个工作进程对**磁盘**施压

```stress -d 2 --hdd-bytes 1GB```

以**详细输出**运行

```stress -v -c 2```

# SYNOPSIS

**stress** [_-c N_] [_-i N_] [_-m N_] [_-d N_] [_-t seconds_] [_OPTIONS_]

# DESCRIPTION

**stress** 在符合 POSIX 标准的操作系统上施加可配置强度的 CPU、内存、I/O 或磁盘压力，并报告检测到的错误。它适用于评估系统的可伸缩性和性能特征，并暴露在高负载条件下才会出现的问题。

# PARAMETERS

**-c, --cpu N**
> 启动 N 个计算平方根的工作进程

**-i, --io N**
> 启动 N 个调用 sync() 的工作进程

**-m, --vm N**
> 启动 N 个分配并释放内存的工作进程

**--vm-bytes B**
> 每个 vm 工作进程分配 B 字节（默认为 256MB）

**--vm-stride B**
> 以 B 字节间隔访问内存（默认为 4096）

**--vm-hang N**
> 释放内存前休眠 N 秒

**--vm-keep**
> 反复弄脏内存而不是重新分配

**-d, --hdd N**
> 启动 N 个写入并删除文件的工作进程

**--hdd-bytes B**
> 每个 hdd 工作进程写入 B 字节（默认为 1GB）

**-t, --timeout N**
> N 秒后终止

**--backoff N**
> 开始工作前等待 N 微秒

**-v, --verbose**
> 启用详细输出

**-q, --quiet**
> 不显示非错误消息

**-n, --dry-run**
> 仅显示将要执行的操作，不实际执行

# CAVEATS

该工具明确不是基准测试工具。数字可带 s、m、h、d、y（时间）或 B、K、M、G（大小）后缀。运行过度的压力测试可能导致系统不稳定。

# HISTORY

**stress** 由 **Amos Waterland** 编写，是面向 POSIX 系统的简单负载生成器。由 Colin Ian King 开发的相关工具 **stress-ng** 提供了多得多的压力源类型和指标。

# INSTALL

```apt: sudo apt install stress```

```dnf: sudo dnf install stress```

```pacman: sudo pacman -S stress```

```brew: brew install stress```

```nix: nix profile install nixpkgs#stress```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[stress-ng](/man/stress-ng)(1), [sysbench](/man/sysbench)(1), [memtester](/man/memtester)(1), [fio](/man/fio)(1), [top](/man/top)(1), [free](/man/free)(1), [vmstat](/man/vmstat)(1), [uptime](/man/uptime)(1)
