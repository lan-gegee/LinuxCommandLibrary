# TAGLINE

终止 LSF 批处理作业

# TLDR

**终止特定作业**

```bkill [job_id]```

**终止你的所有作业**

```bkill 0```

**按名称终止作业**

```bkill -J [job_name]```

**终止特定队列中的作业**

```bkill -q [queue_name] 0```

**强制终止作业**（不执行清理）

```bkill -r [job_id]```

**向作业发送指定信号**

```bkill -s [SIGTERM] [job_id]```

**终止匹配某模式的作业**

```bkill -J "[pattern*]" 0```

**终止作业数组的元素**

```bkill "[job_id][1-10]"```

# SYNOPSIS

**bkill** [_options_] [_job_id_ | **0**]...

# DESCRIPTION

**bkill** 终止 LSF（Load Sharing Facility）批处理作业。它向运行中的作业发送信号，或将等待中的作业从队列中移除。使用作业 ID 0 会作用于你自己的所有作业。

对于运行中的作业，bkill 先发送 SIGINT，等待一个宽限期，然后发送 SIGTERM，若作业仍未终止则最后发送 SIGKILL。-r 选项会跳过这一序列并强制立即移除。

bkill 是 IBM Spectrum LSF 工作负载管理系统的一部分，用于 HPC 环境。

# PARAMETERS

**-r**
> 强制移除：立即从 LSF 中删除作业、将其标记为 EXIT 并释放受监控的资源。不能与 **-s** 组合使用。

**-s** _signal_
> 按名称或编号发送指定信号，而非默认的 SIGINT/SIGTERM/SIGKILL 序列。

**-J** _name_
> 终止名称或名称模式匹配的作业。

**-q** _queue_
> 终止特定队列中的作业。

**-m** _host_
> 终止特定主机或主机组上的作业。

**-g** _group_
> 终止特定作业组中的作业。

**-u** _user_
> 终止特定用户或用户组的作业（仅管理员）。

**-app** _profile_
> 终止使用特定应用配置文件的作业。

**-sla** _class_
> 终止属于特定服务类的作业。

**-b**
> 快速终止；等待中的作业被立即移除，无需等待。

**-l**
> 显示此平台上 bkill 支持的信号名称。

**-V**
> 显示 LSF 版本信息。

**0**
> 作用于你所有的作业（可结合过滤器按队列、主机等缩小范围）。

# CAVEATS

只有管理员才能终止其他用户的作业。强制终止（-r）可能在执行主机上留下孤儿进程。终止作业数组的主作业会终止其所有元素。等待中的作业会被立即移除而不经过信号序列。某些作业可能不响应信号而需要强制终止。

# HISTORY

**bkill** 是 **IBM Spectrum LSF** 的一部分，最初由 **Platform Computing** 于 **20 世纪 90 年代初**开发。该命令遵循 Unix 的信号处理惯例，同时与 LSF 调度器集成。Platform Computing 于 **2012 年**被 IBM 收购，继续为企业的 HPC 工作负载管理开发 LSF 套件。

# SEE ALSO

[bjobs](/man/bjobs)(1), [bsub](/man/bsub)(1)
