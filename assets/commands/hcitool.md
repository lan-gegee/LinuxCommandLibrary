# TAGLINE

用于监视和配置的蓝牙主机控制器接口（HCI）工具

# TLDR

**扫描**蓝牙设备

```hcitool scan```

扫描**低功耗蓝牙（BLE）**设备

```hcitool lescan```

按 MAC 地址输出设备的**名称**

```hcitool name [bdaddr]```

获取远程蓝牙设备的**信息**

```hcitool info [bdaddr]```

检查到蓝牙设备的**链路质量**

```hcitool lq [bdaddr]```

修改**发射功率**级别

```hcitool tpl [bdaddr] [0|1]```

显示**链路策略**

```hcitool lp```

向特定设备请求**认证**

```hcitool auth [bdaddr]```

显示**本地设备**

```hcitool dev```

# SYNOPSIS

**hcitool** [_options_] _command_ [_command-parameters_]

# PARAMETERS

**-i** _hciX_
> 使用指定的 HCI 设备而不是第一个可用设备。

**scan**
> 扫描可发现的蓝牙设备

**lescan**
> 扫描低功耗蓝牙（BLE）设备

**dev**
> 列出本地蓝牙适配器

**name** _bdaddr_
> 获取远程设备名称

**info** _bdaddr_
> 获取远程设备信息

**lq** _bdaddr_
> 获取链路质量

**tpl** _bdaddr_ _type_
> 获取/设置发射功率级别

**lp**
> 显示链路策略

**auth** _bdaddr_
> 请求认证

**con**
> 显示活动连接

**cc** _bdaddr_
> 创建连接

**dc** _bdaddr_
> 断开连接

# DESCRIPTION

**hcitool** 是一款蓝牙主机控制器接口（HCI）工具，用于监视、配置连接以及向蓝牙设备发送命令。它提供对蓝牙功能的底层访问，适合诊断和高级配置。

该工具能够发现附近的设备、查询设备信息、管理连接并配置链路参数。它工作在 HCI 层，位于 A2DP、HFP 等更高层协议之下。

# CAVEATS

在现代 BlueZ 版本中已被 bluetoothctl 取代（废弃）。某些操作可能需要 root 权限。部分功能取决于蓝牙适配器的能力。

# HISTORY

hcitool 是 Linux 蓝牙协议栈 BlueZ 的一部分。它虽然仍然可用，但被视为遗留工具；现代系统上的大多数操作建议改用 BlueZ 5 的 bluetoothctl。

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

[bluetoothctl](/man/bluetoothctl)(1), [hciconfig](/man/hciconfig)(1), [rfkill](/man/rfkill)(8)

# RESOURCES

```[Source code](https://github.com/bluez/bluez/blob/master/tools/hcitool.c)```

<!-- verified: 2026-07-17 -->
