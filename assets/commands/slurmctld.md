# TAGLINE

Slurm 中央管理守护进程

# TLDR

**清除**上次检查点的全部旧状态

```slurmctld -c```

**设置**守护进程的 nice 值

```slurmctld -n [value]```

将日志消息**写入**指定文件

```slurmctld -L [path/to/output_file]```

# SYNOPSIS

**slurmctld** [_options_]

# PARAMETERS

**-c**
> 清除所有旧状态，全新启动

**-n _value_**
> 设置 nice 值（通常取负值以获得更高优先级）

**-L _logfile_**
> 将日志写入指定文件

**-f _config_**
> 从指定文件读取配置

**-D**
> 在前台运行（不守护进程化）

**-v**
> 详细日志（可重复使用）

**-h**
> 显示帮助信息

**-V**
> 显示版本信息

# DESCRIPTION

**slurmctld** 是 Slurm 的中央管理守护进程。它监视所有其他 Slurm 守护进程和资源，接收用户提交的工作（作业），并为这些作业分配计算资源。

该控制节点维护整个集群的状态，包括节点可用性、作业队列和资源分配。它通常运行在专用的管理节点上。

# CONFIGURATION

**/etc/slurm/slurm.conf**
> Slurm 主配置文件，定义集群节点、分区、调度策略和控制器设置。

**/etc/slurm/cgroup.conf**
> 用于资源隔离和统计的控制组配置。

# CAVEATS

必须以 root 或配置的 SlurmUser 身份运行。需要 slurm.conf 配置。为实现高可用，可配置备用控制器。清除状态（**-c**）会丢失全部作业历史。

# SEE ALSO

[slurmd](/man/slurmd)(8), [scontrol](/man/scontrol)(1), [sbatch](/man/sbatch)(1), [squeue](/man/squeue)(1)
