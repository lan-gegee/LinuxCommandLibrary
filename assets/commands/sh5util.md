# TAGLINE

合并 Slurm HDF5 性能剖析数据

# TLDR

为作业**合并** HDF5 文件

```sh5util -j [job_id]```

为特定**作业步骤**合并 HDF5 文件

```sh5util -j [job_id.step_id]```

从已合并的作业文件中**提取**数据序列

```sh5util -j [job_id] -E -i [path/to/file.h5] -s [Energy|Filesystem|Network|Task]```

从所有节点提取**特定数据项**

```sh5util -j [job_id] -I -s [series] -d [data_item]```

**列出**某个数据序列中可用的数据项

```sh5util -j [job_id] -I -s [series] -L```

**合并**后保留节点文件

```sh5util -j [job_id] -S```

# SYNOPSIS

**sh5util** [**-j** _job[.step]_] [**-E**|**-I**] [_OPTIONS_]

# PARAMETERS

**-j, --jobs** _job[.step]_
> 为指定的作业或作业步骤合并 HDF5 文件

**-p, --profiledir** _dir_
> 存放节点-步骤 HDF5 文件的目录

**-o, --output** _path_
> 输出文件路径（默认：./job_$jobid.h5）

**-S, --savefiles**
> 合并后保留节点-步骤文件

**--user** _user_
> 运行被剖析作业的用户

**-E, --extract**
> 将数据序列提取为 CSV 格式

**-i, --input** _path_
> 用于提取的输入已合并 HDF5 文件

**-N, --node** _nodename_
> 只提取特定节点的数据

**-l, --level** _level_
> 数据级别：Node:Totals 或 Node:TimeSeries

**-s, --series** _series_
> 数据序列：Energy、Filesystem、Network、Task 或 Task_#

**-I, --item-extract**
> 从所有样本中提取单个数据项

**-d, --data** _item_
> 要提取的具体数据项名称

**-L, --list**
> 列出某个数据序列中可用的数据项

**-h, --help**
> 显示用法信息

# DESCRIPTION

**sh5util** 将 Slurm 的 **acct_gather_profile** 插件在各计算节点上生成的 HDF5 剖析文件合并为一个用于分析的整合文件。它支持三种模式：合并节点文件、将数据序列提取为 CSV，以及从时间序列中提取特定指标。

该工具处理 Slurm 作业剖析数据，追踪能耗、文件系统 I/O、网络活动和任务级指标。输出文件可以用 HDF5 工具分析，或转换为 CSV 以便使用标准数据分析应用程序。

# CAVEATS

需要在 Slurm 配置中启用 HDF5 剖析。节点文件必须存在于剖析目录中。节点多、运行时间长的大型作业可能产生相当大的 HDF5 文件。集群上必须配置 **acct_gather_profile** 插件。

# HISTORY

**sh5util** 属于由 **劳伦斯利弗莫尔国家实验室**（Lawrence Livermore National Laboratory）开发的 **Slurm**（Simple Linux Utility for Resource Management）工作负载管理器。Slurm 最初发布于 **2002 年**，如今已成为使用最广泛的 HPC 作业调度器之一。加入 HDF5 剖析支持是为了提供细致的作业性能分析能力。

# INSTALL

```apt: sudo apt install slurm-wlm-hdf5-plugin```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sacct](/man/sacct)(1), [sstat](/man/sstat)(1), [srun](/man/srun)(1), [sbatch](/man/sbatch)(1)
