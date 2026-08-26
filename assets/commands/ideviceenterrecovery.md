# TAGLINE

让 iOS 设备进入恢复模式

# TLDR

**进入恢复模式**

```ideviceenterrecovery [udid]```

**按名称进入恢复模式**

```ideviceenterrecovery -n [device-name]```

**调试模式**

```ideviceenterrecovery -d [udid]```

# SYNOPSIS

**ideviceenterrecovery** [_options_] _udid_

# PARAMETERS

_UDID_
> 设备 UDID。

**-n** _NAME_
> 按设备名称指定目标。

**-d**, **--debug**
> 调试输出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ideviceenterrecovery** 让 iOS 设备进入恢复模式。恢复模式用于固件恢复和故障排查。

该工具通过 USB 发送进入恢复模式的命令。设备必须已完成配对并被信任。

# CAVEATS

设备必须已配对。恢复模式需要手动退出。属于 libimobiledevice。

# HISTORY

ideviceenterrecovery 是 **libimobiledevice** 的组成部分，用于在 Linux 上管理 iOS 设备。

# INSTALL

```apt: sudo apt install libimobiledevice-utils```

```dnf: sudo dnf install libimobiledevice-utils```

```apk: sudo apk add libimobiledevice-progs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[idevice_id](/man/idevice_id)(1), [idevicepair](/man/idevicepair)(1)
