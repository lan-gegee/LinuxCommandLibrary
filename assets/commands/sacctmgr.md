# TAGLINE

管理 Slurm 的账户、用户和集群

# TLDR

**查看**当前配置

```sacctmgr show configuration```

向 Slurm 数据库**添加**集群

```sacctmgr add cluster [cluster_name]```

向 Slurm 数据库**添加**账户

```sacctmgr add account [account_name] cluster=[cluster_name]```

向账户**添加**用户

```sacctmgr add user [username] account=[account_name] cluster=[cluster_name]```

以自定义格式列**显示**详情

```sacctmgr show account format=Account%20,Description%30```

**查看** QOS 定义

```sacctmgr show qos```

将集群关联数据**导出**到文件

```sacctmgr dump [cluster_name] file=[output.cfg]```

**修改**用户的 QOS

```sacctmgr modify user where name=[username] set qos=[qos_name]```

# SYNOPSIS

**sacctmgr** [_options_] [_command_]

# PARAMETERS

**show** / **list**
> 显示账户、集群、用户、关联、QOS 等信息。

**add** / **create**
> 向数据库添加新的账户、集群、用户或 QOS。

**modify**
> 修改现有条目。

**delete** / **remove**
> 从数据库中删除条目。

**dump**
> 将集群关联数据导出到文件。

**load**
> 从文件导入集群关联数据。

**archive dump** / **archive load**
> 将数据库记录归档到纯文件，或从中恢复。

**ping**
> 测试与 slurmdbd 守护进程的连接。

**reconfigure**
> 重新配置 SlurmDBD 守护进程。

**-i**, **--immediate**
> 直接提交更改，无需确认。

**-n**, **--noheader**
> 输出中省略表头。

**-p**, **--parsable**
> 以竖线分隔输出，末尾带竖线。

**-P**, **--parsable2**
> 以竖线分隔输出，末尾不带竖线。

**-Q**, **--quiet**
> 抑制非错误消息。

**-r**, **--readonly**
> 禁止任何修改（交互模式）。

**-s**, **--associations**
> 显示用户时同时显示其关联信息。

**-v**, **--verbose**
> 启用详细输出。

**--json**
> 以 JSON 格式输出。

**--yaml**
> 以 YAML 格式输出。

# DESCRIPTION

**sacctmgr** 是 Slurm 账户管理工具，用于查看和管理 Slurm 记账数据库中的账户、集群和用户。它是配置多用户 HPC 集群环境的必备工具。

该工具管理账户的层级结构，控制 Slurm 管理的集群中的资源分配、作业优先级和使用限额。账户信息基于关联（association）记录，关联由用户、集群、分区和账户参数组合而成。

可管理的实体类型包括：账户、用户、集群、关联、QOS（服务质量）、资源、预留、协调员、联邦以及 TRES（可追踪资源）。

# CAVEATS

需要配置并运行 Slurm 数据库（slurmdbd）。修改操作通常需要管理员权限。更改可能影响正在运行的作业调度。协调员只能修改其被授权账户范围内的实体。

# INSTALL

```apt: sudo apt install slurm-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sacct](/man/sacct)(1), [scontrol](/man/scontrol)(1), [squeue](/man/squeue)(1), [sbatch](/man/sbatch)(1), [sinfo](/man/sinfo)(1), [srun](/man/srun)(1)
