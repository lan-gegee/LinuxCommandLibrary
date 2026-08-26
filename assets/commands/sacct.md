# TAGLINE

显示 Slurm 作业记账信息

# TLDR

以默认字段显示**最近的作业**

```sacct```

显示**简要**作业信息

```sacct -b```

显示指定作业的**分配情况**

```sacct -j job_id -X```

显示作业的**自定义字段**

```sacct -j job_id -o Elapsed,JobName,ReqCPUS,ReqMem```

显示**一周前以来**的作业

```sacct -S $(date -d "1 week ago" +'%F')```

为较长的值**加宽字段宽度**

```sacct -o JobID,JobName%100```

# SYNOPSIS

**sacct** [_options_]

# PARAMETERS

**-b**, **--brief**
> 显示简要作业信息

**-j**, **--jobs** _id_
> 显示指定作业

**-X**, **--allocations**
> 只显示分配记录

**-o**, **--format** _fields_
> 自定义输出格式

**-S**, **--starttime** _date_
> 按开始时间过滤

# DESCRIPTION

**sacct** 显示来自 Slurm 工作负载管理器的记账数据。它展示作业历史，包括已完成和运行中作业的资源使用、状态和退出码。

输出格式高度可定制，提供大量可用字段用于详细的作业分析。

# CAVEATS

需要配置 Slurm 记账功能。历史数据的保留时长取决于 Slurm 配置。

# HISTORY

属于 **Slurm** 工作负载管理器，即主流的 HPC 集群资源管理系统。

# INSTALL

```apt: sudo apt install slurm-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[squeue](/man/squeue)(1), [sinfo](/man/sinfo)(1), [scontrol](/man/scontrol)(1)
