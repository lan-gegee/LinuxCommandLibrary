# TAGLINE

显示 LSF 批处理作业的历史信息

# TLDR

**显示**自己作业的**历史**

```bhist```

**显示**指定作业的**历史**

```bhist [job_id]```

**显示**所有用户的**历史**

```bhist -a```

**显示详细历史**

```bhist -l [job_id]```

**显示**特定队列中作业的**历史**

```bhist -q [queue_name]```

**显示**指定时间范围内的**历史**

```bhist -t -b [12/01/08:00] -e [12/01/18:00]```

**显示具有特定状态的作业**

```bhist -d```

# SYNOPSIS

**bhist** [_options_] [_job_id_...]

# DESCRIPTION

**bhist** 显示 LSF（Load Sharing Facility）作业的历史信息。它根据作业事件日志展示作业历史，包括提交时间、开始时间、完成时间、退出状态和资源使用情况。

该命令查询 LSF 作业事件日志文件（lsb.events）来重建作业历史。默认只显示你自己的作业，管理员则可查看所有作业。

bhist 是 IBM Spectrum LSF 的一部分。LSF 是一个工作负载管理平台，在 HPC（高性能计算）环境中用于调度和管理计算集群上的批处理作业。

# PARAMETERS

**-a**
> 显示所有用户的作业历史。

**-d**
> 显示已完成的作业（DONE/EXIT）。

**-l**
> 长格式，包含详细信息。

**-p**
> 显示挂起作业的历史。

**-r**
> 显示运行中作业的历史。

**-q** _queue_
> 显示来自指定队列的作业。

**-u** _user_
> 显示指定用户的作业。

**-m** _host_
> 显示指定主机上的作业。

**-t**
> 显示基于时间的作业历史。

**-b** _time_
> 历史搜索的开始时间。

**-e** _time_
> 历史搜索的结束时间。

**-n** _num_
> 限制为最近的 num 个作业。

**-J** _name_
> 显示名称匹配的作业。

# CAVEATS

需要能访问 LSF 作业事件日志。历史数据的可用性取决于日志保留策略。如果日志已归档或清除，很早以前的作业可能无法查询。在历史数据庞大的大型集群上，基于时间的搜索可能较慢。

# HISTORY

**bhist** 属于 **IBM Spectrum LSF**（前身为 Platform LSF），最初由 **Platform Computing** 于 **1990 年代初**开发。LSF 成为 HPC 集群领先的工作负载管理系统之一。Platform Computing 于 **2012 年**被 IBM 收购，产品更名为 IBM Spectrum LSF。它至今仍广泛应用于学术研究、金融服务和生命科学领域。

# SEE ALSO

[bjobs](/man/bjobs)(1), [bsub](/man/bsub)(1), [bkill](/man/bkill)(1)
