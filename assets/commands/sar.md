# TAGLINE

收集并报告系统活动统计信息

# TLDR

每秒报告 **I/O 统计**

```sar -b 1```

每 2 秒报告一次**网络**统计，共 10 次

```sar -n DEV 2 10```

每 2 秒报告 **CPU 利用率**

```sar -u ALL 2```

报告**内存**使用情况

```sar -r ALL 1 20```

报告**运行队列**和平均负载

```sar -q 1```

报告**分页**统计

```sar -B 5```

报告**磁盘**统计

```sar -d 1```

# SYNOPSIS

**sar** [_options_] [_interval_ [_count_]]

# DESCRIPTION

**sar**（System Activity Reporter）收集、报告和保存系统活动信息。它可以报告 CPU、内存、I/O、网络等子系统的性能。

# PARAMETERS

**-b**
> 报告 I/O 和传输速率统计

**-B**
> 报告分页统计

**-d**
> 报告磁盘 I/O 统计

**-n KEYWORD**
> 报告网络统计（DEV、EDEV、NFS、SOCK、IP 等）

**-q**
> 报告队列长度和平均负载

**-r [ALL]**
> 报告内存利用率统计

**-u [ALL]**
> 报告 CPU 利用率

**-v**
> 报告 inode、文件及其他内核表的状态

**-w**
> 报告任务创建和系统切换活动

**-W**
> 报告交换（swapping）统计

**-y**
> 报告 TTY 设备活动

**-f FILE**
> 从指定文件读取数据

**-o FILE**
> 将数据写入指定文件

**-s TIME**
> 设置报告的起始时间

**-e TIME**
> 设置报告的结束时间

**-P {cpu|ALL}**
> 报告每个处理器的统计

**-j {ID|LABEL|PATH|UUID}**
> 显示持久化设备名

# CONFIGURATION

**/var/log/sa/**
> 存放由 sadc 收集的二进制系统活动数据文件的目录，按日期命名为 sa01-sa31。

**/etc/sysstat/sysstat**
> Sysstat 配置文件，控制数据收集间隔、保留时长和压缩设置。

# CAVEATS

不带 interval 时，sar 会从系统活动数据文件中读取。数据由 sadc 守护进程收集并存储在 /var/log/sa/ 中。历史数据需要启用 sysstat 的 cron 任务。

# HISTORY

**sar** 属于 **sysstat** 软件包，最早源自 System V Unix。它提供全面的系统活动报告和历史数据分析能力。

# INSTALL

```dnf: sudo dnf install sysstat```

```pacman: sudo pacman -S sysstat```

```apk: sudo apk add sysstat```

```zypper: sudo zypper install sysstat```

```brew: brew install sysstat```

```nix: nix profile install nixpkgs#sysstat```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[iostat](/man/iostat)(1), [mpstat](/man/mpstat)(1), [pidstat](/man/pidstat)(1), [sadc](/man/sadc)(8)
