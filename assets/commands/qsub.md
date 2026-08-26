# TAGLINE

向批处理队列系统提交作业

# TLDR

按默认设置**提交**脚本

```qsub [script.sh]```

设置 **walltime** 限制

```qsub -l walltime=[1]:[30]:[00] [script.sh]```

申请**节点和核心数**

```qsub -l nodes=[2]:ppn=[4] [script.sh]```

提交到指定**队列**

```qsub -q [queue_name] [script.sh]```

# SYNOPSIS

**qsub** [**-l** _resources_] [**-q** _queue_] [**-N** _name_] [**-o** _output_] _script_

# PARAMETERS

**-l _resource_=_value_**
> 申请资源（walltime、nodes、mem 等）

**-q _queue_**
> 提交到指定队列

**-N _name_**
> 作业名称

**-o _path_**
> 标准输出文件路径

**-e _path_**
> 标准错误文件路径

**-j oe**
> 合并标准输出和标准错误

**-M _email_**
> 用于通知的电子邮件地址

**-m _events_**
> 在特定事件时发送邮件（b=开始，e=结束，a=中止）

**-V**
> 将所有环境变量导出给作业

**-I**
> 以交互式作业方式提交

**-S _path_**
> 作业脚本使用的 Shell

**-a _date_time_**
> 延迟到指定的日期/时间执行

**-v _variable_list_**
> 将特定的环境变量导出给作业

# DESCRIPTION

**qsub** 向 TORQUE 或 PBS（Portable Batch System）队列管理器提交批处理作业。它用于高性能计算集群中，在资源可用时调度作业执行。

作业是指定了资源需求和要执行命令的脚本。队列管理器会根据申请分配节点、CPU 和内存。

# CAVEATS

资源限制因队列和集群配置而异。作业可能在队列中等待可用资源。超出 walltime 会终止作业。环境变量可能不会被继承。

# HISTORY

**qsub** 源自 NASA 开发的 PBS（Portable Batch System）。TORQUE 是其开源衍生版本。Slurm（sbatch）和其他作业调度器中也有类似的命令。

# INSTALL

```apt: sudo apt install gridengine-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qstat](/man/qstat)(1), [qdel](/man/qdel)(1), [pbsnodes](/man/pbsnodes)(1), [sbatch](/man/sbatch)(1)
