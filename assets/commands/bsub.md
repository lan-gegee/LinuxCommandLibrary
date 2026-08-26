# TAGLINE

向 IBM Spectrum LSF 提交批处理作业

# TLDR

将脚本文件作为作业**提交**

```bsub [path/to/script.sh]```

向**指定队列**提交作业

```bsub -q [queue_name] make all```

以**指定名称和输出重定向**提交作业

```bsub -J [job_name] --output [path/to/output.log] --error [path/to/error.log] [path/to/script.sh]```

申请 **CPU 核心数和内存**

```bsub -n 8 -M 16G cargo build --release```

运行**交互式 shell**

```bsub -I bash```

以**运行时长限制**提交

```bsub -W 45 [path/to/script.sh]```

# SYNOPSIS

**bsub** [_options_] _command_ [_arguments_]

# DESCRIPTION

**bsub** 向 IBM Spectrum LSF（Load Sharing Facility）提交批处理作业，后者是面向分布式 HPC 环境的工作负载管理平台。它会根据资源需求和可用性，将作业调度到集群节点上运行。

作业可以是命令、脚本或交互式会话。调度器会将作业需求与可用资源进行匹配。

# PARAMETERS

**-q** _queue_
> 提交到指定队列

**-J** _name_
> 为作业指定名称

**-n** _cores_
> 所需的 CPU 核心数量

**-M** _memory_
> 内存限制（例如 16G、4096M）

**-W** _minutes_
> 运行时长限制（分钟）

**-I**
> 以交互方式运行

**-o, --output** _file_
> 标准输出文件

**-e, --error** _file_
> 标准错误文件

**-R** _resource_
> 资源需求字符串

# CAVEATS

可用队列和资源限制取决于集群配置。作业可能需要在队列中等待，直到资源可用。交互式作业（-I）会占用终端直到完成。

# SEE ALSO

[bjobs](/man/bjobs)(1), [bkill](/man/bkill)(1), [bhist](/man/bhist)(1)
