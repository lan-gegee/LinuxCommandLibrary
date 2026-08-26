# TAGLINE

调度 Slurm 集群中的周期性作业

# TLDR

从文件**安装** crontab

```scrontab path/to/file```

**编辑**当前用户的 crontab

```scrontab -e```

编辑**指定用户**的 crontab（需要 root 或 SlurmUser 权限）

```scrontab -u username -e```

**移除**当前 crontab

```scrontab -r```

**打印**当前 crontab

```scrontab -l```

# SYNOPSIS

**scrontab** [**-u** _user_] _file_
**scrontab** [**-u** _user_] [**-e** | **-l** | **-r**]

# PARAMETERS

**-e**
> 编辑 crontab；若不存在则创建默认模板

**-l**
> 将当前 crontab 打印到 stdout

**-r**
> 移除 crontab；正在运行的作业会继续执行，但不会再重复

**-u** _user_
> 操作指定用户的 crontab（列出需要 Operator/Admin 权限；编辑/移除需要 root 或 SlurmUser 权限）

# DESCRIPTION

**scrontab** 管理 Slurm 的 crontab 文件，用于在 HPC 集群上调度周期性的批处理作业。它使用标准的 cron 时间规范（分钟、小时、日、月、星期），并通过 **#SCRON** 注释行结合 Slurm 的 **sbatch** 指令。

以 **#SCRON** 开头的行为其后紧随的单个 crontab 条目定义 sbatch 选项；选项在各条目之间会重置。与传统的 **crontab** 不同，用户环境变量不会被继承。作业会在指定的间隔自动提交到 Slurm 调度器。

# CAVEATS

需要集群管理员启用 Slurm 的 cron 功能。与传统的 crontab 不同，用户环境变量会被忽略。

# HISTORY

属于 **Slurm** 工作负载管理器，为 HPC 环境提供周期性作业调度功能。

# INSTALL

```apt: sudo apt install slurm-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sbatch](/man/sbatch)(1), [crontab](/man/crontab)(1), [scontrol](/man/scontrol)(1), [squeue](/man/squeue)(1)
