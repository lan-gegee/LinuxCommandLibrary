# TAGLINE

以交互方式管理蓝牙设备

# TLDR

**启动蓝牙交互模式**

```bluetoothctl```

**开启蓝牙适配器电源**

```bluetoothctl power on```

**扫描设备**

```bluetoothctl scan on```

**列出发现的设备**

```bluetoothctl devices```

**与设备配对**

```bluetoothctl pair [MAC_address]```

**连接已配对的设备**

```bluetoothctl connect [MAC_address]```

**信任设备**（自动连接）

```bluetoothctl trust [MAC_address]```

**断开设备连接**

```bluetoothctl disconnect [MAC_address]```

**移除已配对的设备**

```bluetoothctl remove [MAC_address]```

# SYNOPSIS

**bluetoothctl** [_command_]

# PARAMETERS

**power** _on_|_off_
> 开启或关闭蓝牙适配器。

**scan** _on_|_off_
> 开始或停止设备发现。

**devices**
> 列出发现的设备。

**paired-devices**
> 列出已配对的设备。

**pair** _MAC_
> 发起与设备的配对。

**trust** _MAC_
> 将设备标记为受信任（自动连接）。

**untrust** _MAC_
> 移除设备的受信任状态。

**connect** _MAC_
> 连接到已配对的设备。

**disconnect** _MAC_
> 断开与设备的连接。

**remove** _MAC_
> 将设备从已知设备中移除。

**info** _MAC_
> 显示详细的设备信息。

**block** / **unblock** _MAC_
> 屏蔽或取消屏蔽一个设备。

**discoverable** _on_|_off_
> 让适配器对其他设备可见。

**agent** _capability_
> 设置配对代理（NoInputNoOutput、DisplayOnly 等）。

# DESCRIPTION

**bluetoothctl** 是 Linux 系统上管理蓝牙设备的命令行界面，基于官方 Linux 蓝牙协议栈 BlueZ。它提供对蓝牙适配器、设备发现、配对和连接的完整控制。

在交互模式下（不带参数运行），bluetoothctl 提供带 Tab 补全的 shell，便于探索命令和设备。命令也可以直接从 shell 执行，便于脚本化。

该工具管理设备的完整生命周期：扫描发现附近设备、配对建立安全关系、信任启用自动重连、连接激活设备供使用。可通过 **select** 命令支持多个适配器。

# CAVEATS

需要 BlueZ 协议栈和 bluetoothd 守护进程正在运行。某些设备需要特定的配对代理或 PIN 码。音频设备需要单独配置 PulseAudio/PipeWire 的蓝牙模块。并非所有蓝牙协议都获得同等支持；请检查设备兼容性。

# HISTORY

**BlueZ** 是官方的 Linux 蓝牙协议栈，最初由 **Qualcomm** 的 Max Krasnyansky 编写，自 **21 世纪初**起作为开源项目维护。**bluetoothctl** 工具随 BlueZ 5（**2012 年**发布）引入，用于取代较旧的 hcitool 及其他各种命令行工具，将蓝牙管理整合到单一的现代化界面中。

# INSTALL

```dnf: sudo dnf install tlp```

```pacman: sudo pacman -S tlp```

```apk: sudo apk add tlp```

```zypper: sudo zypper install tlp```

```nix: nix profile install nixpkgs#tlp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hciconfig](/man/hciconfig)(1), [hcitool](/man/hcitool)(1), [rfkill](/man/rfkill)(8), [pulseaudio](/man/pulseaudio)(1)

# RESOURCES

```[Homepage](http://www.bluez.org/)```

```[Source code](https://github.com/bluez/bluez)```

<!-- verified: 2026-06-19 -->
