# TAGLINE

在 Linux 上使用 Windows WiFi 驱动

# TLDR

**安装 Windows 驱动**

```ndiswrapper -i [driver.inf]```

**列出已安装的驱动**

```ndiswrapper -l```

**移除驱动**

```ndiswrapper -r [drivername]```

**写入 modprobe 配置**

```ndiswrapper -m```

**显示硬件信息**

```ndiswrapper -v```

**加载模块**

```modprobe ndiswrapper```

# SYNOPSIS

**ndiswrapper** [_options_]

# PARAMETERS

**-i** _INF_
> 从指定的 .inf 文件安装驱动（同时将其引用的 .sys/.bin 复制到 /etc/ndiswrapper）。

**-l**
> 列出已安装的驱动及其匹配的硬件/PCI ID。

**-r** _NAME_
> 移除已安装的驱动。

**-m**
> 为无线接口写入 modprobe 别名（写入 /etc/modprobe.d）。

**-ma**
> 写入模块别名配置。

**-mi**
> 写入模块安装配置。

**-v**
> 显示驱动和硬件（设备 ID）信息。

**-d** _DEVID_:_DRIVER_
> 对具有指定 PCI/USB ID 的设备使用 DRIVER。

**-e** _DRIVER_
> 从系统中移除某个驱动。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ndiswrapper** 让 Linux 能够使用 Windows WiFi 驱动。它封装 NDIS 驱动供 Linux 使用。

该工具让不受支持的无线网卡得以工作。加载 Windows 的 .sys 和 .inf 文件。

# CAVEATS

旧式工具。如今大多数网卡已有原生驱动。需要提供 Windows 驱动文件。

# HISTORY

ndiswrapper 的诞生是为了在缺乏原生驱动的年代于 Linux 上使用 **Windows 网络驱动**。

# INSTALL

```pacman: sudo pacman -S ndiswrapper```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[iwconfig](/man/iwconfig)(1), [modprobe](/man/modprobe)(1), [lspci](/man/lspci)(1)
