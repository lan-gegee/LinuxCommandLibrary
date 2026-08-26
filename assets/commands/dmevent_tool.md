# TAGLINE

device-mapper 事件监控控制工具

# TLDR

**列出已注册的事件**

```dmevent_tool -l```

**注册设备**进行监控

```dmevent_tool -R [device_name]```

**注销设备**的监控

```dmevent_tool -U [device_name]```

**检查监控状态**

```dmevent_tool -s [device_name]```

# SYNOPSIS

**dmevent_tool** [_options_] [_device_]

# PARAMETERS

_DEVICE_
> device-mapper 设备名。

**-l**, **--list**
> 列出已注册的设备。

**-R**, **--register**
> 注册设备进行监控。

**-U**, **--unregister**
> 注销设备的监控。

**-s**, **--status**
> 显示设备监控状态。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**dmevent_tool** 用于与 device-mapper 事件守护进程（dmeventd）交互。它可以注册和注销 device-mapper 设备的事件监控，并查询其状态。

device-mapper 事件守护进程监控 DM 设备的故障、阈值越过或配置变化等事件。事件发生时，dmeventd 可以触发预设的响应，例如告警或自动修复。

该工具通常配合 LVM 精简配置、RAID 以及其他受益于事件驱动监控的 device-mapper 存储方案使用。

# CAVEATS

需要 dmeventd 正在运行。需要 root 权限。仅适用于 device-mapper 设备。事件处理取决于已配置的插件。

# HISTORY

dmevent_tool 属于 **Red Hat** 开发的 **LVM2** device-mapper 工具集。device-mapper 事件监控基础设施为 Linux 企业部署提供了响应式存储管理。

# INSTALL

```pacman: sudo pacman -S dmraid```

```apk: sudo apk add dmraid```

```zypper: sudo zypper install dmraid```

```nix: nix profile install nixpkgs#dmraid```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dmsetup](/man/dmsetup)(1), [lvm](/man/lvm)(1)
