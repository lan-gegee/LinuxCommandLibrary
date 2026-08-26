# TAGLINE

Slurm 计算节点守护进程

# TLDR

守护进程重启时**报告**节点已重启（用于测试）

```slurmd -b```

在前台以详细日志**运行**守护进程

```slurmd -D -v```

使用给定的节点名**运行**守护进程

```slurmd -N [nodename]```

将日志消息**写入**指定文件

```slurmd -L [path/to/output_file]```

从指定文件**读取**配置

```slurmd -f [path/to/file]```

**清除**旧的节点状态并全新启动

```slurmd -c```

# SYNOPSIS

**slurmd** [_options_]

# PARAMETERS

**-b**
> 守护进程重启时报告节点已重启

**-N _nodename_**
> 以指定的节点名运行

**-L _logfile_**
> 将日志写入指定文件

**-f _config_**
> 从指定文件读取配置

**-c**
> 清除旧的节点状态

**-D**
> 在前台运行（不守护进程化）

**-v**
> 详细日志

**-M**
> 以多个节点名运行守护进程（必须具有唯一的端口和 NodeAddr）

**-h**
> 显示帮助信息

**-V**
> 显示版本信息

# DESCRIPTION

**slurmd** 是 Slurm 的计算节点守护进程。它监视计算节点上运行的所有任务，接受来自中央控制器的新任务，启动任务，并按请求终止正在运行的任务。

Slurm 集群中的每个计算节点都运行 slurmd 以参与工作负载的调度和执行。该守护进程与 **slurmctld**（中央控制器）通信以进行作业管理。

# CAVEATS

必须以 root 身份运行。需要正确的 Slurm 配置（slurm.conf）。节点必须在 Slurm 控制器中注册。防火墙必须允许与 slurmctld 通信。

# SEE ALSO

[slurmctld](/man/slurmctld)(8), [scontrol](/man/scontrol)(1), [sbatch](/man/sbatch)(1), [srun](/man/srun)(1), [squeue](/man/squeue)(1), [sinfo](/man/sinfo)(1)
