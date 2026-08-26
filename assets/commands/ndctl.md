# TAGLINE

管理 Linux 上非易失性内存条（NVDIMM）的工具

# TLDR

创建 **fsdax 模式的命名空间**

```ndctl create-namespace --mode=fsdax```

将命名空间的**模式改为** raw

```ndctl create-namespace --reconfigure=[namespaceX.Y] --mode=raw```

**检查并修复** sector 模式的命名空间

```ndctl check-namespace --repair [namespaceX.Y]```

**列出所有**命名空间、区域和总线

```ndctl list --namespaces --regions --buses --idle```

以**详细信息列出**命名空间

```ndctl list -vvv --namespace=[namespaceX.Y]```

**监视** SMART 健康事件

```ndctl monitor --bus=ACPI.NFIT```

**销毁**或重置命名空间

```ndctl destroy-namespace --force [namespaceX.Y]```

# SYNOPSIS

**ndctl** _command_ [_options_] [_namespace_]

# COMMANDS

**create-namespace**
> 以指定模式创建新命名空间

**destroy-namespace**
> 移除命名空间或将其重置为初始状态

**check-namespace**
> 检查命名空间的一致性

**list**
> 列出命名空间、区域、总线和 dimm

**monitor**
> 监视 SMART 健康事件

**enable-namespace**
> 启用已禁用的命名空间

**disable-namespace**
> 禁用活动命名空间

**enable-region**
> 启用区域

**disable-region**
> 禁用区域

# PARAMETERS

**--mode _mode_**
> 命名空间模式：fsdax、devdax、sector、raw

**--reconfigure _namespace_**
> 重新配置现有命名空间

**--repair**
> 修复检查中发现的错误

**--force, -f**
> 强制执行操作而不确认

**--bus _bus_**
> 在指定总线上操作

**--region _region_**
> 在指定区域上操作

**--idle**
> 列表包含已禁用/空闲的对象

**-v, -vv, -vvv**
> 提高详细程度

# DESCRIPTION

**ndctl** 是一款用于管理 Linux 上非易失性内存条（NVDIMM）的工具。NVDIMM 是断电后仍能保留数据的持久内存模块，可提供存储级内存能力。

该工具管理命名空间（逻辑存储单元）、区域（物理 NVDIMM 分组），并监视 NVDIMM 的健康状况。不同的命名空间模式支持不同用途：fsdax 用于文件系统 DAX，devdax 用于设备 DAX，sector 用于传统块设备访问。

# CAVEATS

对活动命名空间的操作可能需要先卸载文件系统。销毁命名空间不可逆。NVDIMM 支持需要相应的硬件和内核配置。健康监视需要 ACPI NFIT 支持。

# HISTORY

**ndctl** 由 Intel 和 Linux 社区作为 **pmem**（持久内存）项目的一部分开发。它提供用户态工具来管理 NVDIMM，遵循 ACPI NFIT 和 NVDIMM 驱动子系统制定的标准。

# INSTALL

```apt: sudo apt install ndctl```

```dnf: sudo dnf install ndctl```

```pacman: sudo pacman -S ndctl```

```apk: sudo apk add ndctl```

```zypper: sudo zypper install ndctl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[daxctl](/man/daxctl)(1), [cxl](/man/cxl)(1)
