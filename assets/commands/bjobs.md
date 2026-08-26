# TAGLINE

显示 LSF 批处理作业的信息

# TLDR

**显示你所有等待中与运行中的作业**

```bjobs```

**显示所有作业**（包括已完成的）

```bjobs -a```

**显示某个作业的详细信息**

```bjobs -l [job_id]```

**显示特定队列中的作业**

```bjobs -q [queue_name]```

**只显示运行中的作业**

```bjobs -r```

**只显示等待中的作业**

```bjobs -p```

**以宽格式显示作业**

```bjobs -w```

**显示所有用户的作业**

```bjobs -u all```

# SYNOPSIS

**bjobs** [_options_] [_job_id_...]

# DESCRIPTION

**bjobs** 显示 LSF（Load Sharing Facility）批处理作业的信息。默认情况下，它显示你的等待中和运行中的作业及其状态、队列、提交主机和执行主机。

作业状态包括 PEND（等待）、RUN（执行中）、DONE（成功完成）、EXIT（失败）、PSUSP（排队时挂起）、USUSP（用户挂起）和 SSUSP（系统挂起）。

bjobs 是 IBM Spectrum LSF 的一部分，后者是一个工作负载管理平台，用于在 HPC 环境和大型计算集群中调度和管理批处理作业。

# PARAMETERS

**-a**
> 显示所有作业，包括最近完成的。

**-d**
> 显示最近完成的作业。

**-l**
> 长格式，包含详细信息。

**-p**
> 只显示等待中的作业。

**-r**
> 只显示运行中的作业。

**-s**
> 只显示挂起的作业。

**-w**
> 宽格式，不截断字段。

**-W**
> 显示等待中作业的预计开始时间。

**-q** _queue_
> 显示特定队列中的作业。

**-u** _user_
> 显示特定用户的作业（或 "all"）。

**-m** _host_
> 显示特定执行主机上的作业。

**-J** _name_
> 显示作业名匹配的作业。

**-g** _group_
> 显示特定作业组中的作业。

**-o** _format_
> 自定义输出格式。

**-noheader**
> 不显示表头行。

# CAVEATS

最近完成的作业会在一段可配置的时间后（通常为 1 小时）从 bjobs 中消失。历史作业信息请使用 bhist。作业 ID 一段时间后可能被复用。宽格式在字段特别长时仍可能截断。

# HISTORY

**bjobs** 是 **IBM Spectrum LSF** 的一部分，最初由 **Platform Computing** 于 **20 世纪 90 年代初**开发。LSF（Load Sharing Facility）开创了分布式计算的工作负载管理。Platform Computing 于 **2012 年**被 IBM 收购。数十年来 bjobs 接口基本保持稳定，在添加新功能的同时维持了向后兼容性。

# SEE ALSO

[bsub](/man/bsub)(1), [bkill](/man/bkill)(1), [bhist](/man/bhist)(1)
