# TAGLINE

Slurm 数据库记账守护进程

# TLDR

以**前台**模式运行，并将日志输出到 stdout

```slurmdbd -D```

设置守护进程的 **nice 值**

```slurmdbd -n [value]```

将工作目录切换到 **LogFile 路径**

```slurmdbd -s```

以**详细输出**运行

```slurmdbd -v```

显示**版本**

```slurmdbd -V```

显示**帮助**

```slurmdbd -h```

# SYNOPSIS

**slurmdbd** [_OPTIONS_...]

# PARAMETERS

**-D**
> 在前台运行守护进程并将日志输出到 stdout

**-h**
> 显示帮助和选项简要说明

**-n** _value_
> 设置守护进程的 nice 值（通常为负值）

**-s**
> 将工作目录切换到 LogFile 路径或 /var/tmp

**-u**
> 显示数据库版本和转换状态后退出

**-v**
> 详细运行（多个 v 最多可达 6 级）

**-V**
> 打印版本信息并退出

# DESCRIPTION

**slurmdbd**（Slurm Database Daemon）为 Slurm 工作负载管理器提供安全的企业级数据库接口。它对于归档记账记录、跟踪作业历史、使用统计以及跨集群的用户/账户关联至关重要。

该守护进程负责处理数据库连接、管理记账数据存储，并向 slurmctld 提供公平共享调度信息。它通常运行在一台能够访问记账数据库（MySQL/MariaDB）的专用主机上。

# SIGNALS

**SIGTERM, SIGINT, SIGQUIT**
> 优雅关闭并完成数据汇总

**SIGHUP**
> 重新加载配置文件

**SIGUSR2**
> 重新读取日志级别并重新打开日志文件（配合 logrotate 使用）

# CONFIGURATION

**/etc/slurm/slurmdbd.conf**
> 数据库守护进程配置，指定数据库连接参数、身份验证设置和日志选项。

**/etc/slurm/slurm.conf**
> 主 Slurm 配置，用于集群级设置和 AccountingStorageHost。

# CAVEATS

启动前需要在 **slurmdbd.conf** 中完成正确配置。数据库必须可访问且配置妥当。为保证可靠性，应运行在独立于计算节点的主机上。作业历史庞大的大型集群会占用大量内存。

# HISTORY

**slurmdbd** 是 **Slurm**（Simple Linux Utility for Resource Management）的一部分，由 **Lawrence Livermore 国家实验室**自 **2002 年**起开发。加入数据库守护进程是为了支持企业级记账和公平共享调度。Slurm 现由 **SchedMD** 维护，被世界上许多最大的超级计算机采用。

# INSTALL

```apt: sudo apt install slurmdbd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[slurmctld](/man/slurmctld)(8), [slurmd](/man/slurmd)(8), [sacct](/man/sacct)(1), [sacctmgr](/man/sacctmgr)(1)
