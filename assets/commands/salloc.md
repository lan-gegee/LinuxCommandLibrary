# TAGLINE

以交互方式分配 Slurm 集群资源

# TLDR

在集群节点上启动**交互式 Shell**

```salloc```

在集群节点上**执行命令**

```salloc ls --all```

带**约束条件**分配节点

```salloc -C "(amd|intel)&gpu"```

# SYNOPSIS

**salloc** [_options_] [_command_]

# PARAMETERS

**-C**, **--constraint** _expr_
> 节点特性约束

# DESCRIPTION

**salloc** 从 Slurm 集群分配资源，并启动交互式 shell 或执行指定命令。它会等待资源可用后再启动。

约束条件可以指定所需的节点特性，例如 CPU 类型、GPU 可用性或内存配置。

# CAVEATS

资源会一直被占用，直到 shell 退出或命令执行完毕。分配等待时间取决于集群负载和所请求的资源。

# HISTORY

属于 **Slurm** 工作负载管理器，为 HPC 集群提供交互式资源分配。

# INSTALL

```apt: sudo apt install slurm-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[srun](/man/srun)(1), [sbatch](/man/sbatch)(1), [squeue](/man/squeue)(1)
