# TLDR

显示**运行中作业**的状态

```sstat -j [job_id]```

以可解析格式显示**指定字段**

```sstat -p -j [job_id] -o JobID,AveCPU,AveVMSize```

列出**可用字段**

```sstat -e```

显示**所有作业步骤**

```sstat -a -j [job_id]```

显示每个步骤的 **PID**

```sstat -i -j [job_id]```

# SYNOPSIS

**sstat** [_OPTIONS_...]

# PARAMETERS

**-j, --jobs** _job[.step]_
> 要查询的作业 ID 或 job.step（必需）

**-o, --format, --fields** _fields_
> 要显示的字段的逗号分隔列表

**-e, --helpformat**
> 列出可用的格式字段

**-a, --allsteps**
> 显示指定作业的所有步骤

**-i, --pidformat**
> 显示每个作业步骤的 PID

**-n, --noheader**
> 输出中省略表头

**-p, --parsable**
> 以竖线分隔，末尾带竖线

**-P, --parsable2**
> 以竖线分隔，末尾不带竖线

**--noconvert**
> 保留原始单位（不转换）

**-v, --verbose**
> 详细输出

**-V, --version**
> 打印版本

# COMMON FIELDS

**JobID**: 作业标识符
**AveCPU**: 平均 CPU 时间
**AveRSS**: 平均常驻内存集大小
**AveVMSize**: 平均虚拟内存
**MaxRSS**: 最大 RSS
**MaxVMSize**: 最大虚拟内存大小
**NTasks**: 任务数量
**MinCPU**: 最小 CPU 时间

# DESCRIPTION

**sstat** 显示运行中 Slurm 作业的实时状态信息，包括 CPU 使用率、内存消耗和 I/O 统计。它通过 jobacct_gather 插件查询当前正在执行的作业及其步骤的指标。

root 用户可以查看所有正在运行的作业；普通用户只能看到自己的作业。该命令可用于在作业执行期间监控资源使用情况并诊断性能问题。

# CAVEATS

仅对运行中的作业有效；已完成的作业请使用 **sacct**。需要 jobacct_gather 插件。可用指标取决于具体插件（linux、cgroup）。非 root 用户的可见范围有限。

# HISTORY

**sstat** 属于 **Slurm**，由 **劳伦斯利弗莫尔国家实验室** 自 **2002 年**起开发。作业记账功能帮助用户和管理员实时监控资源消耗。Slurm 目前由 **SchedMD** 维护。

# INSTALL

```apt: sudo apt install slurm-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sacct](/man/sacct)(1), [squeue](/man/squeue)(1), [scontrol](/man/scontrol)(1), [srun](/man/srun)(1)

# RESOURCES

```[Source code](https://github.com/SchedMD/slurm)```

```[Homepage](https://slurm.schedmd.com/)```

```[Documentation](https://slurm.schedmd.com/sstat.html)```

<!-- verified: 2026-06-10 -->
