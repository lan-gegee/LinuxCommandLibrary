# TAGLINE

NVIDIA 数据中心 GPU 管理接口

# TLDR

**显示 GPU 发现**信息

```dcgmi discovery -l```

**显示 GPU 健康**状态

```dcgmi health -g [group_id]```

**对 GPU 运行诊断**

```dcgmi diag -r [1]```

**显示实时统计信息**

```dcgmi dmon```

**创建 GPU 组**

```dcgmi group -c [group_name]```

**将 GPU 加入组**

```dcgmi group -g [group_id] -a [gpu_id]```

**显示 GPU 拓扑**

```dcgmi topo -g [group_id]```

# SYNOPSIS

**dcgmi** _subsystem_ [_options_]

# PARAMETERS

_SUBSYSTEM_
> 管理子系统：discovery、health、diag、dmon、group、topo 等。

**discovery** **-l**
> 列出已发现的 GPU。

**health** **-g** _GROUP_
> 检查 GPU 组的健康状态。

**diag** **-r** _LEVEL_
> 运行诊断（级别 1-4）。

**dmon**
> 实时监控面板。

**group** **-c** _NAME_
> 创建命名的 GPU 组。

**topo** **-g** _GROUP_
> 显示互连拓扑。

**fieldgroup** **-c** _NAME_
> 创建用于指标采集的命名字段组。

**modules** **-l**
> 列出可用的 DCGM 模块及其状态。

**policy** **-g** _GROUP_
> 查看或设置 GPU 策略条件。

**stats** **-j** _JOB_ID_
> 显示作业级别的 GPU 统计信息。

**--host** _HOST_:_PORT_
> 连接到远程 DCGM 主机守护进程（默认：localhost:5555）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**dcgmi** 是 NVIDIA 数据中心 GPU 管理器（DCGM）的命令行界面。它为数据中心和 HPC 环境中的 NVIDIA GPU 提供监控、管理和诊断能力。

该工具让管理员能够监控 GPU 健康状态、运行诊断、跟踪性能指标，并管理 GPU 组以实施策略。它可与作业调度器和集群管理系统集成，实现自动化 GPU 管理。

DCGM 跟踪数百项 GPU 指标，包括温度、功耗、内存使用和错误计数。诊断子系统能在硬件问题导致故障之前发现它们，支持主动维护。

# CAVEATS

要求主机上运行 NVIDIA DCGM 服务。仅支持受支持的 NVIDIA 数据中心 GPU。某些诊断需要 GPU 处于空闲状态。部分操作需要提升的权限。

# HISTORY

DCGM 由 **NVIDIA** 开发，约于 **2016 年**发布，面向企业级 GPU 部署。dcgmi 提供 DCGM 功能的命令行访问方式，与 API 和图形界面对数据中心 GPU 集群管理形成互补。

# SEE ALSO

[nvidia-smi](/man/nvidia-smi)(1), [nvtop](/man/nvtop)(1), [gpustat](/man/gpustat)(1)
