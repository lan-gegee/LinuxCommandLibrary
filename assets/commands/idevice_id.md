# TAGLINE

列出已连接 iOS 设备的标识符

# TLDR

**列出已连接的设备**

```idevice_id -l```

**显示设备 UDID**

```idevice_id```

**以简单模式列出**

```idevice_id -l -n```

**调试输出**

```idevice_id -d -l```

# SYNOPSIS

**idevice_id** [_options_]

# PARAMETERS

**-l**, **--list**
> 列出设备 UDID。

**-n**, **--network**
> 包含网络设备。

**-d**, **--debug**
> 调试输出。

**-u** _UDID_
> 目标设备。

**--help**
> 显示帮助信息。

# DESCRIPTION

**idevice_id** 列出已连接 iOS 设备的标识符。它通过 USB 或网络检测 iPhone、iPad 和 iPod。

该工具提供其他 libimobiledevice 命令所需的 UDID。它是 iOS 设备管理的第一步。

# CAVEATS

属于 libimobiledevice。需要 USB 访问权限。可能需要先配对。

# HISTORY

idevice_id 是 **libimobiledevice** 的一部分，后者是一个开源的 iOS 设备通信库。

# INSTALL

```apt: sudo apt install libimobiledevice-utils```

```dnf: sudo dnf install libimobiledevice-utils```

```apk: sudo apk add libimobiledevice-progs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[idevicepair](/man/idevicepair)(1), [ideviceinfo](/man/ideviceinfo)(1), [idevicename](/man/idevicename)(1)
