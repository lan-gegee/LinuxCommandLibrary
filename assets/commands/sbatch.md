# TAGLINE

向 Slurm 调度器提交批处理作业

# TLDR

**提交**批处理作业

```sbatch [job.sh]```

以**自定义名称**提交

```sbatch --job-name=[myjob] [job.sh]```

设置**时限**

```sbatch --time=[00:30:00] [job.sh]```

申请**多个节点**

```sbatch --nodes=[3] [job.sh]```

# SYNOPSIS

**sbatch** [**--job-name** _name_] [**--time** _limit_] [**--nodes** _n_] [**--cpus-per-task** _n_] [_script_]

# PARAMETERS

**--job-name _name_**
> 作业名称

**--time _time_**
> 时限（HH:MM:SS）

**--nodes _n_**
> 节点数

**--ntasks _n_**
> 任务数

**--cpus-per-task _n_**
> 每个任务的 CPU 数

**--mem _size_**
> 每个节点的内存

**--partition _name_**
> 要使用的分区/队列

**--output _file_**
> 输出文件（%j 表示作业 ID）

**--error _file_**
> 错误文件

**--mail-type _type_**
> 邮件通知（BEGIN、END、FAIL）

# DESCRIPTION

**sbatch** 向 SLURM 工作负载管理器提交批处理作业脚本。作业会进入队列，当集群上所请求的资源可用时被执行。

作业脚本包含 SLURM 指令（以 #SBATCH 开头的行），用于指定资源需求，其后是要执行的命令。SLURM 负责作业调度和资源分配。

# CAVEATS

资源请求会影响排队等待时间。超过时限会终止作业。执行环境可能与提交时的 shell 不同。请用 sinfo 查看分区限制。

# HISTORY

**sbatch** 属于 **SLURM**（Simple Linux Utility for Resource Management），由劳伦斯利弗莫尔国家实验室开发。SLURM 是目前使用最广泛的 HPC 作业调度器。

# INSTALL

```apt: sudo apt install slurm-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[squeue](/man/squeue)(1), [scancel](/man/scancel)(1), [sinfo](/man/sinfo)(1), [srun](/man/srun)(1)
