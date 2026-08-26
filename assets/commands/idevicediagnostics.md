# TAGLINE

与 iOS 设备的诊断接口交互

# TLDR

**重启设备**

```idevicediagnostics restart```

**关闭设备**

```idevicediagnostics shutdown```

**让设备进入睡眠**

```idevicediagnostics sleep```

**获取诊断信息**

```idevicediagnostics diagnostics```

**获取电池信息**

```idevicediagnostics diagnostics GasGauge```

**按 UDID 指定目标设备**

```idevicediagnostics -u [UDID] restart```

**打印指定平面的 IORegistry**

```idevicediagnostics ioregistry IODeviceTree```

# SYNOPSIS

**idevicediagnostics** [_options_] _command_

# SUBCOMMANDS

**diagnostics** [_type_]
> 打印诊断信息，可按类型选择：All（默认）、WiFi、GasGauge 或 NAND。

**mobilegestalt** _key_ [_key_ ...]
> 打印 MobileGestalt 键的值。

**ioregistry** [_plane_]
> 打印设备的 IORegistry，可选按平面选择（IODeviceTree、IOPower、IOService）。仅限 iOS 5+。

**restart**
> 重启设备。

**shutdown**
> 关闭设备。

**sleep**
> 让设备进入睡眠。

# PARAMETERS

**-u**, **--udid** _UDID_
> 按设备的 UDID 指定目标设备。

**-n**, **--network**
> 连接到网络设备。

**-d**, **--debug**
> 启用通信调试。

**-h**, **--help**
> 打印用法信息。

**-v**, **--version**
> 打印版本信息。

# DESCRIPTION

**idevicediagnostics** 与 iOS 设备的诊断接口交互，用于获取诊断数据、MobileGestalt 数据和 IORegistry 信息，并可执行重启、关机和睡眠等操作。属于 **libimobiledevice** 套件。适用于 iOS 4 及更高版本；访问 IORegistry 需要 iOS 5 或更高版本。

# INSTALL

```apt: sudo apt install libimobiledevice-utils```

```dnf: sudo dnf install libimobiledevice-utils```

```apk: sudo apk add libimobiledevice-progs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ideviceinfo](/man/ideviceinfo)(1), [idevicecrashreport](/man/idevicecrashreport)(1), [idevicepair](/man/idevicepair)(1), [idevicebackup2](/man/idevicebackup2)(1), [idevicesyslog](/man/idevicesyslog)(1), [idevicescreenshot](/man/idevicescreenshot)(1)

