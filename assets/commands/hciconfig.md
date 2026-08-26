# TAGLINE

配置蓝牙设备

# TLDR

**显示所有蓝牙接口**

```hciconfig```

**显示指定接口**

```hciconfig [hci0]```

**启用接口**

```sudo hciconfig [hci0] up```

**禁用接口**

```sudo hciconfig [hci0] down```

**启用设备扫描**

```sudo hciconfig [hci0] piscan```

**重置接口**

```sudo hciconfig [hci0] reset```

**显示详细信息**

```hciconfig -a```

# SYNOPSIS

**hciconfig** [_options_] [_device_] [_command_]

# DESCRIPTION

**hciconfig** 用于配置蓝牙设备。它显示并修改 HCI（Host Controller Interface，主机控制器接口）设备设置，作用类似于网络接口领域的 ifconfig。

该工具管理蓝牙适配器的状态、可见性以及名称、设备类、扫描模式等各类参数。

# PARAMETERS

**-a**
> 显示所有信息。

**up**
> 启用设备。

**down**
> 禁用设备。

**reset**
> 重置设备。

**piscan**
> 同时启用页面扫描和查询扫描。

**noscan**
> 禁用扫描。

**iscan**
> 仅启用查询扫描。

**pscan**
> 仅启用页面扫描。

**name** _name_
> 设置本地名称。

**class** _class_
> 设置设备类。

**auth**
> 启用认证。

**noauth**
> 禁用认证。

# CAVEATS

已被 bluetoothctl 取代（废弃）。配置操作需要 root 权限。更改在重启后可能不会保留。接口命名可能有所不同。

# HISTORY

**hciconfig** 属于 **BlueZ**，即 Linux 官方的蓝牙协议栈。BlueZ 由 **Maxim Krasnyansky** 和 **Marcel Holtmann** 创建，现由社区维护并获得 Intel 的贡献。尽管 hciconfig 正在被逐步淘汰，它在底层蓝牙配置方面仍然有用。

# INSTALL

```apt: sudo apt install bluez```

```dnf: sudo dnf install bluez```

```pacman: sudo pacman -S bluez```

```apk: sudo apk add bluez-deprecated```

```zypper: sudo zypper install bluez```

```brew: brew install bluez```

```nix: nix profile install nixpkgs#bluez```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bluetoothctl](/man/bluetoothctl)(1), [hcitool](/man/hcitool)(1), [btmgmt](/man/btmgmt)(1), [rfkill](/man/rfkill)(1)
