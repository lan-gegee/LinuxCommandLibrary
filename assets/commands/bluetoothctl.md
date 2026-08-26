# TAGLINE

从命令行控制蓝牙设备

# TLDR

进入**交互式** Shell

```bluetoothctl```

列出**设备**

```bluetoothctl devices```

打开/关闭控制器的**电源**

```bluetoothctl power on```

与设备**配对**

```bluetoothctl pair AA:BB:CC:DD:EE:FF```

**连接**到设备

```bluetoothctl connect AA:BB:CC:DD:EE:FF```

**断开**设备连接

```bluetoothctl disconnect AA:BB:CC:DD:EE:FF```

**移除**设备

```bluetoothctl remove AA:BB:CC:DD:EE:FF```

# SYNOPSIS

**bluetoothctl** [_OPTIONS_] [_COMMAND_]

# DESCRIPTION

**bluetoothctl** 用于管理 Linux 上的蓝牙设备。它提供一个交互式 Shell，用于发现、配对、连接和管理蓝牙设备。

# PARAMETERS

**-a**, **--agent** _capability_
> 以指定的能力注册代理处理程序。

**-e**, **--endpoints**
> 注册媒体端点。

**-m**, **--monitor**
> 启用监视输出。

**-t**, **--timeout** _seconds_
> 非交互模式的超时时间。

**-v**, **--version**
> 显示版本。

**-h**, **--help**
> 显示帮助。

**list**
> 列出可用的控制器。

**show** [_ctrl_]
> 显示控制器信息。

**select** _ctrl_
> 设置默认控制器。

**devices** [_filter_]
> 列出已知设备（过滤条件：Paired、Bonded、Trusted、Connected）。

**power** _on|off_
> 打开或关闭蓝牙控制器电源。

**scan** _on|off_
> 启动或停止设备发现。

**pair** _address_
> 按 MAC 地址与设备配对。

**connect** _address_
> 连接到已配对的设备。

**disconnect** _address_
> 断开与设备的连接。

**remove** _address_
> 从已知列表中移除设备。

**trust** _address_
> 将设备标记为受信任。

**untrust** _address_
> 取消设备的受信任状态。

**info** _address_
> 显示设备信息。

**block** _address_
> 阻止某台设备连接。

**unblock** _address_
> 解除对先前被阻止设备的阻止。

**discoverable** _on|off_
> 设置控制器是否可被发现。

**agent** _on|off|capability_
> 注册或注销代理。

**help**
> 显示可用命令。

# CAVEATS

需要蓝牙服务正在运行。某些操作要求设备处于配对模式。MAC 地址格式为 AA:BB:CC:DD:EE:FF。

# HISTORY

**bluetoothctl** 是 Linux 官方蓝牙协议栈 **BlueZ** 的一部分。

# INSTALL

```apt: sudo apt install bluez```

```dnf: sudo dnf install bluez```

```pacman: sudo pacman -S bluez```

```apk: sudo apk add bluez```

```zypper: sudo zypper install bluez```

```brew: brew install bluez```

```nix: nix profile install nixpkgs#bluez```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hcitool](/man/hcitool)(1), [rfkill](/man/rfkill)(8)
