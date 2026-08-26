# TAGLINE

用于监控和管理 NVIDIA GPU 设备的命令行工具

# TLDR

**显示 GPU 状态**

```nvidia-smi```

**显示 GPU 详细信息**

```nvidia-smi -q```

**持续监控 GPU**

```nvidia-smi -l [1]```

**仅显示特定 GPU**

```nvidia-smi -i [0]```

**显示正在使用 GPU 的进程**

```nvidia-smi pmon```

**查询特定属性**

```nvidia-smi --query-gpu=name,memory.total,memory.used --format=csv```

**设置功耗上限**（瓦特）

```nvidia-smi -pl [250]```

**设置持久化模式**

```nvidia-smi -pm [1]```

**重置 GPU**

```nvidia-smi -r```

**显示驱动版本**

```nvidia-smi --query-gpu=driver_version --format=csv,noheader```

# SYNOPSIS

**nvidia-smi** [_options_]

# DESCRIPTION

**nvidia-smi**（NVIDIA System Management Interface）是一款用于监控和管理 NVIDIA GPU 设备的命令行工具。它提供关于 GPU 利用率、内存使用、温度、功耗以及运行中进程的信息。

该工具可以显示实时统计信息、查询特定的 GPU 属性、配置功耗和时钟设置，并管理计算进程。它是机器学习、渲染和科学计算环境中进行 GPU 监控的必备工具。

nvidia-smi 随 NVIDIA 驱动包一起提供，适用于 Tesla、Quadro 和 GeForce GPU（功能可用性因型号而异）。

# PARAMETERS

**-l** _sec_, **--loop=** _sec_
> 每隔 sec 秒持续更新。

**-i** _id_
> 按索引指定目标 GPU。

**-q**, **--query**
> 显示详细信息。

**-d** _type_
> 显示特定的信息类型（MEMORY、UTILIZATION、TEMPERATURE、POWER、CLOCK）。

**--query-gpu=** _attrs_
> 查询特定属性。

**--format=** _format_
> 输出格式（csv、noheader、nounits）。

**-pm** _mode_
> 设置持久化模式（0 或 1）。

**-pl** _watts_
> 设置功耗上限。

**-r**, **--gpu-reset**
> 重置 GPU。

**pmon**
> 进程监控模式。

**topo**
> 显示 GPU 拓扑结构。

**nvlink**
> 显示 NVLink 状态。

# QUERY ATTRIBUTES

**name**: GPU 名称
**memory.total**: 总显存
**memory.used**: 已用显存
**memory.free**: 空闲显存
**utilization.gpu**: GPU 利用率 %
**utilization.memory**: 显存利用率 %
**temperature.gpu**: GPU 温度
**power.draw**: 功耗

# CAVEATS

需要 NVIDIA 专有驱动。部分功能在消费级 GPU 上受限。电源管理需要 root 权限。服务器上建议启用持久化模式，以避免初始化延迟。

# HISTORY

**nvidia-smi** 自 **2000 年代初期**起就是 **NVIDIA 驱动包**的一部分。它随 NVIDIA 的 GPU 计算平台（CUDA）一同演进，逐渐增加了监控计算工作负载的功能。随着 GPU 计算在机器学习和科学应用中的兴起，该工具变得不可或缺。

# SEE ALSO

[nvtop](/man/nvtop)(1), [gpustat](/man/gpustat)(1), [nvidia-settings](/man/nvidia-settings)(1)
