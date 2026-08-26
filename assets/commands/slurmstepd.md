# TAGLINE

Slurm 作业步骤管理守护进程

# TLDR

启动守护进程（通常**自动被调用**）

```slurmstepd```

# SYNOPSIS

**slurmstepd**

# DESCRIPTION

**slurmstepd** 是 Slurm 的作业步骤管理守护进程。当作业步骤启动时，它由 **slurmd** 自动派生；作业步骤完成时随之终止。用户和管理员不应手动调用该守护进程。

该守护进程管理作业步骤的 I/O 流（stdin、stdout、stderr），跟踪包括 CPU 时间、内存使用和 I/O 统计在内的记账信息，并处理发往作业步骤的信号。多步骤作业中的每个作业步骤都有各自的 slurmstepd 进程。

# SIGNALS

**SIGINT, SIGTERM, SIGQUIT**
> 触发优雅关闭

**SIGPROF**
> 记录连接管理器状态（需要 debug 级别或更高的日志级别）

**SIGTSTP, SIGPIPE, SIGUSR1, SIGUSR2, SIGALRM, SIGHUP**
> 显式忽略

# CAVEATS

绝不应手动启动；它由 slurmd 自动派生。多步骤作业可能同时运行多个 slurmstepd 进程。直接杀死 slurmstepd 可能使作业步骤处于不一致的状态；请改用 **scancel**。

# HISTORY

**slurmstepd** 是 **Slurm**（Simple Linux Utility for Resource Management）的一部分，由 **Lawrence Livermore 国家实验室**自 **2002 年**起开发。这种步骤守护进程架构可以高效管理包含多个步骤、且各步骤资源需求各不相同的复杂作业。Slurm 由 **SchedMD** 维护。

# SEE ALSO

[slurmd](/man/slurmd)(8), [srun](/man/srun)(1), [scancel](/man/scancel)(1), [sstat](/man/sstat)(1)
