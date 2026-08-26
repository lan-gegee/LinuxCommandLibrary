# TAGLINE

Slurm 作业调度优先级查看器

# TLDR

查看**所有待处理作业**的优先级因子

```sprio```

查看**特定作业**的优先级

```sprio -j [job_id1,job_id2]```

显示**扩展**信息

```sprio -l```

查看**特定用户**的作业

```sprio -u [user1,user2]```

打印**优先级权重**

```sprio -w```

显示**归一化**的优先级因子

```sprio -n```

# SYNOPSIS

**sprio** [_OPTIONS_...]

# PARAMETERS

**-j, --jobs** _job_ids_
> 显示特定作业 ID（逗号分隔）的优先级

**-u, --user** _users_
> 按用户名或用户 ID 过滤（逗号分隔）

**-p, --partition** _partitions_
> 限定于特定分区

**-l, --long**
> 显示扩展输出信息

**-n, --norm**
> 显示归一化的优先级因子（0.0-1.0）

**-w, --weights**
> 显示已配置的优先级权重值

**-o, --format** _format_
> 自定义输出格式

**-S, --sort** _fields_
> 按指定字段对结果排序

**-h, --noheader**
> 不显示列标题

**-M, --clusters** _names_
> 面向特定集群

**--federation**
> 显示所有联邦集群的作业

**--local**
> 只显示本地集群的作业

**-v, --verbose**
> 详细输出

**-V, --version**
> 显示版本

# DESCRIPTION

当 Slurm 的多因子优先级插件启用时，**sprio** 会显示决定作业调度优先级的各个组成部分。它会展示 age、fairshare、job size、partition、QOS 等因子如何共同构成每个作业的总优先级得分。

默认情况下，它显示所有待处理作业的信息。该工具可帮助管理员和用户理解为什么某些作业先于其他作业被调度，并排查调度问题。

# FORMAT SPECIFIERS

**%i**: 作业 ID
**%Y**: 优先级
**%A**: Age 因子
**%F**: Fairshare 因子
**%J**: 作业规模因子
**%P**: 分区因子
**%Q**: QOS 因子
**%u**: 用户名

# CAVEATS

只有在 Slurm 中配置了多因子优先级插件时才能使用。这是一个只读工具，无法修改优先级。优先级值是相对的，取决于集群配置。若某些因子未配置，其值可能为零。

# HISTORY

**sprio** 是 **Slurm**（Simple Linux Utility for Resource Management）的一部分，自 **2002 年**起由 **劳伦斯利弗莫尔国家实验室** 开发。多因子优先级插件的加入是为了在高性能计算环境中提供公平且可配置的作业调度。Slurm 目前由 **SchedMD** 维护。

# INSTALL

```apt: sudo apt install slurm-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[squeue](/man/squeue)(1), [scontrol](/man/scontrol)(1), [sacct](/man/sacct)(1), [sprio](/man/sprio)(1)
