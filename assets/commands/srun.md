# TAGLINE

在 Slurm 下运行并行作业

# TLDR

**提交**一个基本的交互式作业

```srun --pty /bin/bash```

**提交**自定义资源的交互式作业

```srun --ntasks-per-node [num_cores] --mem-per-cpu [memory_MB] --pty /bin/bash```

在特定分区上**限时运行**作业

```srun -p [partition_name] -t [HH:MM:SS] [command]```

**运行**申请 GPU 的作业

```srun --gpus=[num_gpus] --pty /bin/bash```

**运行**带多个任务且每个任务占用多 CPU 的并行作业

```srun -n [num_tasks] -c [cpus_per_task] [command]```

**连接**到有作业正在运行的 worker 节点

```srun --jobid [job_id] --pty /bin/bash```

# SYNOPSIS

**srun** [_options_] _executable_ [_arguments_]

# PARAMETERS

**--pty**
> 以伪终端模式执行（用于交互式使用）

**--jobid _id_**
> 在已分配的作业下启动一个作业步骤（job step）

**-n, --ntasks _number_**
> 要运行的任务数量

**--ntasks-per-node _ntasks_**
> 每个节点上调用的任务数量

**-c, --cpus-per-task _ncpus_**
> 每个任务分配的 CPU 数量

**--mem _size[units]_**
> 每个节点所需的内存（默认单位：MB；支持 K、M、G、T）

**--mem-per-cpu _size[units]_**
> 每个可用分配 CPU 所需的最小内存

**-p, --partition _name_**
> 请求在特定分区进行资源分配

**-N, --nodes _min[-max]_**
> 所需的节点数（可选指定范围）

**-t, --time _time_**
> 作业时限（格式：HH:MM:SS 或 天-HH:MM:SS）

**-J, --job-name _name_**
> 为作业指定名称

**-G, --gpus _[type:]number_**
> 作业所需的 GPU 总数

**--gres _list_**
> 以逗号分隔的通用消耗性资源列表（例如 gpu:2）

**-w, --nodelist _node_list_**
> 请求指定的主机列表

**-x, --exclude _host_list_**
> 将特定主机排除在分配之外

**-o, --output _filename_**
> 将标准输出重定向到指定文件

**-e, --error _filename_**
> 将标准错误重定向到指定文件

**-D, --chdir _path_**
> 执行前切换到指定目录

**--exclusive**
> 作业不得与其他正在运行的作业共享节点

**--export _{ALL|NONE|variables}_**
> 控制哪些环境变量会传递给作业

**--mpi _type_**
> 指定要使用的 MPI 类型

# DESCRIPTION

**srun** 提交作业以供执行，或实时启动作业步骤。对于交互式工作，它会在计算节点上创建交互式会话。它也可以在批处理脚本中用来启动并行任务。

该命令自动处理资源分配，向调度器请求节点，并在分配到的资源上启动指定程序。

# CAVEATS

交互式作业（**--pty**）可能要在队列中等待资源。资源请求必须符合分区的限额。连接到已有作业需要相应权限。

# INSTALL

```apt: sudo apt install slurm-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sbatch](/man/sbatch)(1), [squeue](/man/squeue)(1), [salloc](/man/salloc)(1), [scontrol](/man/scontrol)(1), [scancel](/man/scancel)(1), [sinfo](/man/sinfo)(1)
