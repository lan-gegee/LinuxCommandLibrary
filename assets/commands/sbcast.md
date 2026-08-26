# TAGLINE

向 Slurm 作业分配的节点广播文件

# TLDR

**将文件发送**到所有已分配的节点

```sbcast path/to/file path/to/destination```

发送时启用**共享库**自动检测

```sbcast --send-libs=yes path/to/executable path/to/destination```

# SYNOPSIS

**sbcast** [_options_] _source_ _destination_

# PARAMETERS

**--send-libs** _yes|no_
> 自动检测并传输共享库依赖

# DESCRIPTION

**sbcast** 将文件发送到分配给 Slurm 作业的所有节点。它利用 Slurm 基础设施在计算节点间高效分发文件。

该命令只能在 Slurm 批处理作业内部使用，不能直接在登录节点上运行。

# CAVEATS

必须在 Slurm 作业上下文中运行。文件分发时间取决于文件大小和节点数量。

# HISTORY

属于 **Slurm** 工作负载管理器，为 HPC 工作流提供高效的文件分发。

# INSTALL

```apt: sudo apt install slurm-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sbatch](/man/sbatch)(1), [srun](/man/srun)(1), [salloc](/man/salloc)(1)
