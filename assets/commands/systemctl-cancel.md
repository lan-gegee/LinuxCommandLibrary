# TAGLINE

取消挂起的 systemd 作业

# TLDR

按 ID **取消**作业

```systemctl cancel [job_id]```

取消**多个**作业

```systemctl cancel [job_id1 job_id2 ...]```

取消**所有**挂起的作业

```systemctl cancel```

取消**用户**作业

```systemctl cancel [job_id] --user```

# SYNOPSIS

**systemctl cancel** [_JOB_...]

# PARAMETERS

**--user**
> 取消用户服务管理器中的作业

**--system**
> 取消系统管理器中的作业（默认）

**-M**, **--machine** _container_
> 在本地容器上执行操作

**-H**, **--host** _user@host_
> 通过 SSH 在远程主机上执行操作

**--no-pager**
> 不将输出通过管道传给分页器

# DESCRIPTION

**systemctl cancel** 取消 systemd 服务管理器中的一个或多个挂起作业。作业表示启动、停止或重启 unit 等待处理的操作。不带参数调用时，会取消所有挂起的作业。

作业 ID 可通过 `systemctl list-jobs` 查询。取消作业会中止挂起的操作，但不影响 unit 的当前状态。

# CAVEATS

无法取消已完成的作业。某些作业可能有依赖会在之后重新触发。取消关键引导作业可能使系统处于不一致状态。

# HISTORY

**cancel** 子命令是 **systemd** 项目中 **systemctl** 的一部分。它用于控制管理 unit 状态转换的作业队列。

# SEE ALSO

[systemctl](/man/systemctl)(1), [systemctl-list-jobs](/man/systemctl-list-jobs)(1)
