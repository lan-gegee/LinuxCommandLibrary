# TAGLINE

Linux 硬件识别系统

# TLDR

**运行硬件发现**

```discover```

**发现特定**类型的设备

```discover [video]```

**列出所有硬件**类别

```discover --list```

**显示详细信息**

```discover -v [device_type]```

将输出**格式化为**机器可读数据

```discover --format data [network]```

# SYNOPSIS

**discover** [_options_] [_type_...]

# PARAMETERS

_TYPE_
> 要发现的设备类型：video、network、audio 等。

**--list**
> 列出可用的设备类型。

**-v**, **--verbose**
> 详细输出。

**--data-version** _VERSION_
> 输出数据格式版本。

**--format** _FORMAT_
> 输出格式（human、data 等）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**discover** 是一个 Linux 硬件识别系统，用于识别硬件设备并将其映射到内核模块、X 驱动或其他软件组件。它查询系统总线以检测已连接的硬件。

该工具被安装与配置系统用于自动检测硬件并加载合适的驱动。它维护着一个将设备 ID 映射到驱动名称和配置数据的数据库。

discover 可以识别 PCI、USB 等多种总线上的设备，提供自动硬件配置所需的信息。

# CAVEATS

数据库可能不包含最新硬件。某些设备需要厂商专有的检测方式。结果取决于内核支持和权限。可能遗漏非标准总线上的设备。

# HISTORY

discover 为 **Progeny** 和 **Debian** 发行版开发，是自动硬件检测和配置系统的一部分。它出现于 21 世纪初，当时自动硬件检测对用户友好的 Linux 安装变得日益重要。

# INSTALL

```apt: sudo apt install discover```

```pacman: sudo pacman -S discover```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lspci](/man/lspci)(8), [lsusb](/man/lsusb)(8), [hwinfo](/man/hwinfo)(8), [udevadm](/man/udevadm)(8)
