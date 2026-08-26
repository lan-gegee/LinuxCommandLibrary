# TAGLINE

显示 Slurm 集群分区和节点状态

# TLDR

**查看**集群的快速摘要概览

```sinfo -s```

**查看**所有分区的详细状态

```sinfo```

**查看**特定分区的详细状态

```sinfo -p [partition_name]```

**查看**空闲节点的信息

```sinfo -t idle```

汇总无响应的节点

```sinfo -d```

**列出**故障节点及其原因

```sinfo -R```

# SYNOPSIS

**sinfo** [_options_]

# PARAMETERS

**-s, --summarize**
> 显示分区摘要

**-p, --partition _name_**
> 显示特定分区

**-t, --states _states_**
> 按节点状态过滤（idle、allocated、down 等）

**-d, --dead**
> 只显示无响应的节点

**-R, --list-reasons**
> 列出节点 down 或 drain 的原因

**-l, --long**
> 输出更详细的详细信息

**-N, --Node**
> 以节点为中心输出

**-o, --format _format_**
> 自定义输出格式

# DESCRIPTION

**sinfo** 报告 Slurm 管理的分区和节点状态。它显示可用计算资源的信息，包括节点数量、分区限制和当前状态。

常见的节点状态包括：**idle**（可用）、**allocated**（占用中）、**down**（不可用）、**drain**（正在排空）和 **mix**（部分 CPU 已分配）。

# CAVEATS

信息反映的是当前 Slurm 调度器状态，与实际节点状态相比可能有短暂延迟。复杂的集群可能需要过滤才能看到相关信息。

# INSTALL

```apt: sudo apt install slurm-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[squeue](/man/squeue)(1), [sbatch](/man/sbatch)(1), [scontrol](/man/scontrol)(1), [srun](/man/srun)(1)
