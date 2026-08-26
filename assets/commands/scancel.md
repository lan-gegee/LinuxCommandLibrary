# TAGLINE

按 ID 或条件取消 Slurm 作业

# TLDR

**取消**指定 ID 的作业

```scancel [job_id]```

**取消**某**用户**的所有作业

```scancel -u [username]```

取消所有**待处理**的作业

```scancel -t PENDING```

按**名称**取消作业

```scancel --name [job_name]```

取消指定的**数组任务**

```scancel [job_id]_[task_id]```

**发送信号**而不是直接取消

```scancel -s [SIGTERM] [job_id]```

# SYNOPSIS

**scancel** [_options_] [_job_id_...]

# PARAMETERS

**-u**, **--user** _username_
> 取消该用户拥有的所有作业

**-t**, **--state** _state_
> 取消处于指定状态的作业（PENDING、RUNNING、SUSPENDED）

**-n**, **--name** _name_
> 取消具有指定名称的作业

**-p**, **--partition** _name_
> 取消指定分区中的作业

**-s**, **--signal** _signal_
> 发送信号代替 SIGKILL

**-A**, **--account** _account_
> 取消指定账户下的作业

**-q**, **--qos** _qos_
> 取消具有指定 QOS 的作业

**-i**, **--interactive**
> 每次取消前确认

**-v**, **--verbose**
> 详细输出

# DESCRIPTION

**scancel** 用于取消 Slurm 集群中待处理或正在运行的作业。可以按数字 ID 取消作业，也可以按用户、分区、状态或作业名进行过滤。命令行上可一次指定多个作业 ID。

对于作业数组，可以使用 `job_id_task_id` 记法取消单个任务。被取消的作业会被终止，资源会释放回集群。

# CAVEATS

除非拥有管理员权限，否则用户只能取消自己的作业。取消正在运行的作业可能导致工作不完整。默认信号是 SIGKILL；建议先用 **-s** 发送更温和的信号。

# HISTORY

**Slurm** 工作负载管理器的组成部分，为 HPC 集群提供作业控制功能。

# INSTALL

```apt: sudo apt install slurm-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[squeue](/man/squeue)(1), [sbatch](/man/sbatch)(1), [scontrol](/man/scontrol)(1)
