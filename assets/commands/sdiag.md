# TAGLINE

显示 Slurm 控制器诊断信息

# TLDR

**显示调度诊断信息**（默认模式）

```sdiag```

**显示按 RPC 总运行时间排序的诊断信息**

```sdiag -t```

**显示按 RPC 平均运行时间排序的诊断信息**

```sdiag -T```

**重置性能计数器**（需要 operator/admin 权限）

```sdiag -r```

**以 JSON 格式输出诊断信息**

```sdiag --json```

# SYNOPSIS

**sdiag** [_options_]

# PARAMETERS

**-a**, **--all**
> 获取并报告信息。这是默认的操作模式。

**-h**, **--help**
> 打印选项说明并退出。

**-i**, **--sort-by-id**
> 按消息类型 ID 和用户 ID 对 RPC 数据排序。

**-r**, **--reset**
> 将调度器和 RPC 计数器重置为 0。仅 Slurm 操作员和管理员可用。

**-t**, **--sort-by-time**
> 按 RPC 总运行时间对数据排序。

**-T**, **--sort-by-time2**
> 按 RPC 平均运行时间对数据排序。

**--json**
> 以 JSON 格式输出信息。

**--yaml**
> 以 YAML 格式输出信息。

**-V**, **--version**
> 打印版本号并退出。

**--usage**
> 打印选项列表并退出。

# DESCRIPTION

**sdiag** 显示 slurmctld（Slurm 控制器守护进程）的诊断信息，包括性能指标、调度统计、RPC 计数器和资源使用数据。

这可用于监控集群健康状况、排查调度性能问题以及识别 Slurm 控制器中的瓶颈。

# CAVEATS

需要适当的权限才能访问 Slurm 控制器数据。重置选项需要 operator 或 administrator 权限，并且会影响所有用户看到的计数器视图。

# HISTORY

属于 **Slurm** 工作负载管理器，为集群管理员提供诊断工具。

# INSTALL

```apt: sudo apt install slurm-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[scontrol](/man/scontrol)(1), [sinfo](/man/sinfo)(1), [squeue](/man/squeue)(1), [sacct](/man/sacct)(1)
