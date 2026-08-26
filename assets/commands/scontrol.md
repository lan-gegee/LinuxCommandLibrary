# TAGLINE

查看和修改 Slurm 配置与状态

# TLDR

**显示**作业信息

```scontrol show job [job_id]```

**挂起**以逗号分隔的正在运行的作业列表

```scontrol suspend [job_id1,job_id2,...]```

**恢复**以逗号分隔的已挂起作业列表

```scontrol resume [job_id1,job_id2,...]```

**暂扣（hold）**以逗号分隔的排队作业列表

```scontrol hold [job_id1,job_id2,...]```

**释放**以逗号分隔的被暂扣作业列表

```scontrol release [job_id1,job_id2,...]```

# SYNOPSIS

**scontrol** [_options_] [_command_] [_arguments_]

# PARAMETERS

**show job _job_id_**
> 显示作业的详细信息

**suspend _job_id_**
> 挂起正在运行的作业

**resume _job_id_**
> 恢复已挂起的作业

**hold _job_id_**
> 阻止待处理作业启动

**release _job_id_**
> 释放被暂扣的作业以便调度

**requeue _job_id_**
> 将正在运行的作业重新放回队列

**update**
> 修改作业、节点或分区的属性

**-d, --details**
> 显示详细信息

# DESCRIPTION

**scontrol** 是 Slurm 的控制工具，用于查看和修改作业、分区、节点和配置。它是管理 Slurm 集群工作负载的主要管理接口。

常见用途包括检查作业状态、挂起/恢复作业、在队列中暂扣作业以及修改作业参数。

# CAVEATS

某些操作需要管理员权限。挂起作业可能给时间敏感的应用带来问题。对运行中作业的更改可能影响其他已调度的作业。

# INSTALL

```apt: sudo apt install slurm-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sbatch](/man/sbatch)(1), [squeue](/man/squeue)(1), [scancel](/man/scancel)(1), [sacctmgr](/man/sacctmgr)(1)
