# TAGLINE

从批处理队列系统中删除作业

# TLDR

**删除作业**

```qdel [job_id]```

**删除多个作业**

```qdel [job_id1] [job_id2] [job_id3]```

**删除某用户的全部作业**

```qdel -u [username]```

**强制删除**

```qdel -f [job_id]```

**删除作业数组**

```qdel [job_id][]```

# SYNOPSIS

**qdel** [_options_] _job_ids_...

# PARAMETERS

**-f**, **--force**
> 强制删除。

**-u** _user_
> 删除指定用户的所有作业。

**-W** _time_
> 延迟删除。

**-p**
> 彻底清除作业（移除所有痕迹）。

# DESCRIPTION

**qdel** 从批处理作业队列中删除作业。它属于 PBS/Torque、SGE 或类似的作业调度系统，常见于 HPC 集群上。

# EXAMPLES

```bash
# Delete single job
qdel 12345

# Delete multiple jobs
qdel 12345 12346 12347

# Delete range
qdel 12345-12350

# Force kill
qdel -f 12345

# Delete all my jobs
qdel -u $(whoami)

# Delete array job
qdel 12345[]

# Delete specific array task
qdel 12345[5]
```

# JOB STATES

处于以下状态的作业可以被删除：
- 排队中（Q）
- 运行中（R）
- 保持中（H）

# CAVEATS

PBS、SGE、SLURM 之间的语法各有差异。正在运行的作业可能需要一段时间才能终止。管理员可能限制删除操作。

# HISTORY

qdel 属于 **PBS**（Portable Batch System），最初由 NASA Ames 研究中心开发。

# INSTALL

```apt: sudo apt install gridengine-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qsub](/man/qsub)(1), [qstat](/man/qstat)(1), [scancel](/man/scancel)(1)
