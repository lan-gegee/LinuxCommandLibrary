# TAGLINE

系统活动数据收集后端

# TLDR

以一秒为间隔将 **10 条记录**写入二进制文件

```sadc 1 10 [/tmp/datafile]```

将数据写入**默认的每日数据文件**（/var/log/sa/saDD）

```sadc 1 10 -```

收集**所有可用统计数据**，包括磁盘和中断

```sadc -S ALL 1 10 [/tmp/datafile]```

收集带**磁盘和分区统计信息**的数据

```sadc -S XDISK 1 10 [/tmp/datafile]```

向数据文件添加一条**注释记录**

```sadc -C "[system reboot]" [/var/log/sa/sa01]```

# SYNOPSIS

**sadc** [_-C comment_] [_-D_] [_-F_] [_-L_] [_-V_] [_-S {keyword,...}_] [_interval_] [_count_] [_outfile_]

# PARAMETERS

**-C** _comment_
> 在未指定 interval 和 count 时，写入一条包含指定注释字符串的哑记录

**-D**
> 标准每日数据文件名使用 saYYYYMMDD 而非 saDD

**-F**
> 强制创建 outfile；若已存在且格式不兼容则截断

**-L**
> 在写入或截断前尝试对 outfile 获取独占锁

**-S** _keyword_
> 指定要收集的可选活动：INT（中断）、DISK（块设备）、XDISK（分区/文件系统）、SNMP、IPV6、POWER、ALL、XALL

**-V**
> 打印版本号并退出

# DESCRIPTION

**sadc**（System Activity Data Collector）是 **sar** 命令的后端数据采集器，属于 sysstat 软件包。它按指定间隔采样系统性能数据，并以二进制格式写入输出文件。

采集器收集的指标包括 CPU 利用率、内存使用、I/O 统计、网络活动和进程信息。默认情况下，它收集大多数内核数据，但中断和磁盘统计需要显式指定 **-S** 选项。

当 outfile 设为 **-** 时，sadc 写入标准每日数据文件 /var/log/sa/saDD。如果省略 count，sadc 将无限运行。二进制输出不可直接阅读，需要用 **sar** 来解析。

# CAVEATS

必须挂载 **/proc** 文件系统 sadc 才能工作。可用的统计项取决于内核版本。sadc 通常由 cron 通过 **sa1** 脚本调用，而非直接运行。旧版本 sadc 生成的输出文件可能与新版本不兼容。

# HISTORY

sadc 属于 **sysstat** 软件包，最初由 Sebastien Godard 编写。sysstat 工具族源自更早的 Unix 系统记账工具，而 sadc 提供的二进制数据采集层让 sar 能够进行历史性能分析。

# SEE ALSO

[sar](/man/sar)(1), [iostat](/man/iostat)(1), [mpstat](/man/mpstat)(1), [vmstat](/man/vmstat)(8)
