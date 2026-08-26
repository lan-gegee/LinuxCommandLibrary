# TAGLINE

Slurm 集群使用情况报告生成器

# TLDR

显示**集群利用率**（可解析格式）

```sreport -p cluster utilization```

显示已运行的**作业数量**

```sreport job sizes printjobcount```

显示 **CPU 使用率最高**的用户

```sreport user topusage```

按用户显示**账户利用率**

```sreport cluster AccountUtilizationByUser```

指定**时间段**

```sreport cluster utilization Start=[YYYY-MM-DD] End=[YYYY-MM-DD]```

针对**特定集群**显示

```sreport -M [cluster_name] cluster utilization```

# SYNOPSIS

**sreport** [_OPTIONS_...] [_COMMAND_...]

# PARAMETERS

**-a, --all_clusters**
> 报告所有集群，而不仅是本地集群

**-M, --cluster** _names_
> 指定报告涉及的集群

**-n, --noheader**
> 输出中省略标题行

**-p, --parsable**
> 以竖线分隔且末尾带竖线的输出

**-P, --parsable2**
> 以竖线分隔但末尾不带竖线的输出

**-t** _time_format_
> 设置输出的时间格式（例如 Seconds、Minutes、Hours、Percent）

**-T, --tres** _tres_names_
> 指定要报告的可跟踪资源

**--federation**
> 报告整个联邦的数据

**--local**
> 只报告本地集群

**-Q, --quiet**
> 只显示错误

**-v, --verbose**
> 详细输出

**-V, --version**
> 打印版本

# REPORT TYPES

**cluster**
> AccountUtilizationByUser, UserUtilizationByAccount, Utilization, WCKeyUtilizationByUser

**job**
> SizesByAccount, SizesByAccountAndWckey, SizesByWckey

**reservation**
> Utilization

**user**
> TopUsage

# REPORT OPTIONS

**Start** _date_
> 报告周期开始时间（默认：前一天 00:00）

**End** _date_
> 报告周期结束时间（默认：前一天 23:59）

**Accounts** _list_
> 按账户过滤

**Users** _list_
> 按用户过滤

# DESCRIPTION

**sreport** 基于 slurmdbd 中存储的 Slurm 计费数据生成使用情况和利用率报告。它依据小时、日、月的汇总表，生成作业统计、用户使用量、集群利用率和预留使用量等报告。

这些报告帮助管理员了解集群的使用模式、找出用量最大的用户，并跟踪各账户和项目的资源消耗。

# CAVEATS

需要配置并运行 slurmdbd。报告的准确性取决于正确的计费配置。历史数据的可用性取决于数据库保留策略设置。时间段使用集群本地时间。

# HISTORY

**sreport** 是 **Slurm** 的一部分，自 **2002 年**起由**劳伦斯利弗莫尔国家实验室**开发。计费与报告功能帮助 HPC 中心跟踪使用量，用于计费、容量规划和公平共享调度。Slurm 目前由 **SchedMD** 维护。

# INSTALL

```apt: sudo apt install slurm-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sacct](/man/sacct)(1), [sshare](/man/sshare)(1), [sacctmgr](/man/sacctmgr)(1), [slurmdbd](/man/slurmdbd)(8)
