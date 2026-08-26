# TAGLINE

显示批处理作业队列状态

# TLDR

**显示所有作业**

```qstat```

**显示用户的作业**

```qstat -u [username]```

**显示完整的作业详情**

```qstat -f [job_id]```

**显示队列状态**

```qstat -Q```

**显示正在运行的作业**

```qstat -r```

# SYNOPSIS

**qstat** [_options_] [_job_ids_...]

# PARAMETERS

**-f**
> 完整的作业信息。

**-u** _user_
> 特定用户的作业。

**-Q**
> 队列状态。

**-q**
> 队列摘要。

**-r**
> 仅显示正在运行的作业。

**-n**
> 显示节点。

**-a**
> 所有作业。

# DESCRIPTION

**qstat** 显示 PBS/Torque、SGE 或类似作业调度系统中批处理作业的状态，包括作业状态、队列、资源和时间信息。

# EXAMPLES

```bash
# All jobs
qstat

# My jobs
qstat -u $USER

# Job details
qstat -f 12345

# Queue status
qstat -Q

# Jobs with nodes
qstat -n

# All jobs, all users
qstat -a
```

# OUTPUT FORMAT

```
Job ID    Name       User     Time  S  Queue
--------- ---------- -------- ----- -  -----
12345.srv myjob      user01   02:30 R  batch
12346.srv analysis   user01   --    Q  batch
```

# JOB STATES

```
Q - Queued
R - Running
H - Held
E - Exiting
C - Completed
```

# CAVEATS

PBS、SGE、SLURM 之间的语法各不相同。SLURM 系统请使用 squeue。

# HISTORY

qstat 是 **PBS**（Portable Batch System）的一部分，由 NASA 为 HPC 作业调度而开发。

# INSTALL

```apt: sudo apt install gridengine-client```

```dnf: sudo dnf install qstat```

```brew: brew install qstat```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qsub](/man/qsub)(1), [qdel](/man/qdel)(1), [squeue](/man/squeue)(1), [bjobs](/man/bjobs)(1)
