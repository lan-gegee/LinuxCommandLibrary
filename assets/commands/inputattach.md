# TAGLINE

将串口线路连接到输入层设备

# TLDR

连接 **Pulse8 CEC** 适配器

```sudo inputattach --pulse8-cec /dev/ttyACM0```

以 19200 波特率连接 **Wacom W8001** 仅笔式数位板

```sudo inputattach --baud 19200 --w8001 /dev/ttyS0```

连接 **ELO 触摸屏**并转入后台

```sudo inputattach --daemon --elo /dev/ttyS0```

连接 **Microsoft 串口鼠标**

```sudo inputattach --microsoft /dev/ttyS0```

列出**支持的设备**

```inputattach --help```

# SYNOPSIS

**inputattach** [_options_] _mode_ _device_

# PARAMETERS

**--daemon**
> 连接后转入后台。

**--always**
> 忽略初始化失败并保持设备连接。

**--noinit**
> 跳过设备初始化。

**--baud** _RATE_
> 覆盖默认的串口波特率。

**--help**
> 显示帮助并列出所有支持的设备模式。

模式标志（选择其一）：

**--microsoft**, **--mouseman**, **--intellimouse**, **--mousesystems**
> 常见串口鼠标协议。

**--elo**, **--mtouch**, **--touchit213**, **--fujitsu**
> 串口触摸屏协议。

**--w8001**, **--wacom_iv**, **--wacom_v**
> Wacom 串口数位板协议。

**--pulse8-cec**, **--rainshadow-cec**
> 以串口设备形式呈现的 HDMI-CEC 适配器。

**--magellan**, **--spaceorb**, **--spaceball**
> 6 自由度（6-DOF）串口输入设备。

**--sunkbd**, **--lkkbd**, **--stowaway**
> 串口键盘协议。

# DESCRIPTION

**inputattach** 将串口线路接入 Linux 输入子系统。它从指定的串口设备读取原始字节，按所选协议解码，然后把得到的事件送入内核，使其成为 `/dev/input/` 下的标准输入设备。

该程序是 **linuxconsoletools** 软件包的一部分。连接完成后，设备即可供 libinput、evdev、X.Org 或任何其他 Linux 输入层消费者使用。配合 **--daemon** 时，inputattach 会脱离控制终端，因此可以从 rc 脚本或 systemd unit 启动。

对于 Wacom W8001 硬件，默认速率 38400 bps 适用于笔+触摸及纯触摸设备；仅笔式设备需要 **--baud 19200**。

# CAVEATS

通常需要 root 权限或对串口节点的写权限。模式标志必须与所连硬件匹配；协议选错会导致收不到事件或产生乱码。一旦连接，设备将一直由 inputattach 占用，直到进程退出。

# HISTORY

inputattach 作为 **linuxconsoletools**（前身为 joyutils）的一部分维护。Wacom 变体也由 **linuxwacom** 项目分发，用于串口 Wacom 数位板。

# INSTALL

```apt: sudo apt install inputattach```

```dnf: sudo dnf install linuxconsoletools```

```apk: sudo apk add linuxconsoletools```

```zypper: sudo zypper install linuxconsoletools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[evtest](/man/evtest)(1), [libinput](/man/libinput)(1)
