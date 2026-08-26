# TAGLINE

管理 Slurm 集群事件触发器

# TLDR

为系统事件**注册**触发器

```strigger --set --primary_slurmctld_failure -p [path/to/script]```

为**作业完成**注册触发器

```strigger --set -j [job_id] -f -p "[path/to/script] [args]"```

**查看**活动触发器

```strigger --get```

查看**特定作业**的触发器

```strigger --get -j [job_id]```

**清除**一个触发器

```strigger --clear [trigger_id]```

注册**永久**触发器

```strigger --set --down --flags=PERM -p [path/to/script]```

# SYNOPSIS

**strigger** **--set** [_OPTIONS_...]
**strigger** **--get** [_OPTIONS_...]
**strigger** **--clear** [_OPTIONS_...]

# PARAMETERS

**--set**
> 注册新触发器

**--get**
> 显示已注册的触发器

**--clear**
> 移除触发器

**-j, --jobid** _id_
> 针对特定作业

**--node** _name_
> 针对特定节点

**-p, --program** _path_
> 触发器触发时要执行的脚本

**--offset** _seconds_
> 时间调整（负值 = 事件发生前）

**--flags** _flags_
> 触发器标志（PERM = 永久）

**-u, --user** _name_
> 按触发器创建者过滤

**-v, --verbose**
> 详细输出

**-q, --quiet**
> 不显示非关键错误

# EVENT TYPES

**节点事件**：--down、--up、--drained、--draining、--idle、--fail
**作业事件**：--fini、--time
**系统事件**：--primary_slurmctld_failure、--primary_slurmdbd_failure、--reconfig

# DESCRIPTION

**strigger** 管理 Slurm 中的事件触发器，当特定事件发生时自动执行脚本。触发器可以响应节点状态变化、作业完成、系统故障和其他集群事件。守护进程大约每 15 秒检查一次触发器。

被触发的程序在 slurmctld 节点上执行，超时时间为 5 分钟。默认情况下，触发器在执行后即被移除，除非通过 **--flags=PERM** 标记为永久。

# CAVEATS

只有 SlurmUser（通常是 root）能设置触发器。程序在 slurmctld 节点上运行，而不是计算节点。除非是永久触发器，否则执行后必须重新注册。脚本必须可执行且 slurmctld 主机可访问。

# HISTORY

**strigger** 是 **Slurm** 的一部分，Slurm 由 **劳伦斯利弗莫尔国家实验室**（Lawrence Livermore National Laboratory）从 **2002 年**开始开发。事件触发器可实现对集群事件的自动化响应，用于监控、告警和工作流自动化。Slurm 现由 **SchedMD** 维护。

# INSTALL

```apt: sudo apt install slurm-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[scontrol](/man/scontrol)(1), [slurmctld](/man/slurmctld)(8)
