# TAGLINE

获取或设置 iOS 设备的名称

# TLDR

**获取设备名称**

```idevicename```

**设置设备名称**

```idevicename "New Name"```

**指定目标设备**

```idevicename -u [udid]```

**调试输出**

```idevicename -d```

# SYNOPSIS

**idevicename** [_options_] [_name_]

# PARAMETERS

_NAME_
> 要设置的新设备名称。

**-u** _UDID_
> 按 UDID 指定目标设备。

**-n**
> 使用网络连接。

**-d**, **--debug**
> 调试输出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**idevicename** 获取或设置 iOS 设备的名称。不带参数时显示当前名称。

该工具修改的是在 iTunes 和 Finder 中可见的设备名称。它要求设备已完成配对并被信任。

# CAVEATS

属于 libimobiledevice。设备必须已配对。名称修改后会自动同步。

# HISTORY

idevicename 是 **libimobiledevice** 的组成部分，用于管理 iOS 设备属性。

# INSTALL

```apt: sudo apt install libimobiledevice-utils```

```dnf: sudo dnf install libimobiledevice-utils```

```apk: sudo apk add libimobiledevice-progs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[idevice_id](/man/idevice_id)(1), [ideviceinfo](/man/ideviceinfo)(1), [idevicepair](/man/idevicepair)(1)
