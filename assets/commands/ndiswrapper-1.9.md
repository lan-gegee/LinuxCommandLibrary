# TAGLINE

特定版本的 ndiswrapper

# TLDR

**安装 Windows 驱动**

```ndiswrapper-1.9 -i [driver.inf]```

**列出已安装的驱动**

```ndiswrapper-1.9 -l```

**移除驱动**

```ndiswrapper-1.9 -r [drivername]```

**写入 modprobe 配置**

```ndiswrapper-1.9 -m```

# SYNOPSIS

**ndiswrapper-1.9** [_options_]

# PARAMETERS

**-i** _INF_
> 从 INF 文件安装驱动。

**-l**
> 列出已安装的驱动。

**-r** _NAME_
> 移除驱动。

**-m**
> 为 modprobe 写入模块别名配置。

**-ma**
> 为当前存在的所有网卡写入模块配置。

**-mi**
> 写入模块安装配置。

**-e** _NAME_
> 移除驱动（-r 的别名）。

**-da** _DEVICE_:_DRIVER_
> 将设备（PCI/USB ID）分配给驱动。

**-v**
> 详细输出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ndiswrapper-1.9** 是特定版本的 ndiswrapper。它在 Linux 上使用 Windows WiFi 驱动。

该工具封装 NDIS 网络驱动。保留此版本是为了兼容性。

# CAVEATS

版本特定的二进制文件。旧式工具。尽可能使用最新版 ndiswrapper。

# HISTORY

ndiswrapper-1.9 是 **ndiswrapper** 的一个特定版本，为兼容某些驱动而保留。

# INSTALL

```pacman: sudo pacman -S ndiswrapper```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ndiswrapper](/man/ndiswrapper)(1), [iwconfig](/man/iwconfig)(1), [modprobe](/man/modprobe)(1)
