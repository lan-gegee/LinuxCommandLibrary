# TAGLINE

查看 Slurm 作业队列状态

# TLDR

**查看**作业队列

```squeue```

**查看**特定用户排队的作业

```squeue -u [username]```

**查看**队列并每 5 秒刷新一次

```squeue -i 5```

**查看**队列及预计开始时间

```squeue --start```

# SYNOPSIS

**squeue** [_options_]

# PARAMETERS

**-u, --user _username_**
> 只显示指定用户拥有的作业

**-i, --iterate _seconds_**
> 按指定间隔刷新显示

**--start**
> 显示待处理作业的预计开始时间

**-j, --jobs _job_list_**
> 显示特定的作业 ID

**-p, --partition _name_**
> 显示特定分区中的作业

**-t, --states _states_**
> 按作业状态过滤（pending、running 等）

**-l, --long**
> 长格式输出

**-o, --format _format_**
> 自定义输出格式

**-S, --sort _field_**
> 按字段对输出排序

# DESCRIPTION

**squeue** 显示 Slurm 调度队列中作业的信息。它会列出集群上等待或正在运行的作业的作业 ID、分区、名称、用户、状态、时间、节点及节点列表。

常见的作业状态包括：**PD**（待处理）、**R**（运行中）、**CG**（正在完成）、**CD**（已完成）、**F**（失败）和 **CA**（已取消）。

# CAVEATS

根据 Slurm 的访问控制，只显示查询用户可见的作业。非常大的作业队列可能需要借助过滤选项。**--start** 给出的预计时间只是近似值。

# INSTALL

```apt: sudo apt install slurm-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sbatch](/man/sbatch)(1), [sinfo](/man/sinfo)(1), [scancel](/man/scancel)(1), [scontrol](/man/scontrol)(1)
