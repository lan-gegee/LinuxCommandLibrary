# TAGLINE

游戏杆测试工具，实时显示轴与按键状态

# TLDR

**测试游戏杆**

```jstest [/dev/input/js0]```

**以单行模式测试**，即时显示状态

```jstest --normal [/dev/input/js0]```

**以事件输出模式测试**

```jstest --event [/dev/input/js0]```

**以非阻塞事件模式测试**

```jstest --nonblock [/dev/input/js0]```

# SYNOPSIS

**jstest** [_options_] _device_

# PARAMETERS

_device_
> 游戏杆设备路径（如 /dev/input/js0）。

**--normal**
> 单行模式，即时显示轴和按键状态。

**--old**
> 与 --normal 相同，但使用 0.x 兼容接口。

**--event**
> 实时打印收到的事件。

**--nonblock**
> 与 --event 相同，但为非阻塞模式。

**--select**
> 与 --event 相同，但使用 select(2) 系统调用。

# DESCRIPTION

**jstest** 可用于测试 Linux 游戏杆 API 的全部特性，包括非阻塞访问和 select(2) 访问，以及 0.x 版本兼容模式。它从 Linux 游戏杆设备（/dev/input/js*）读取输入，并在轴值和按键状态变化时显示出来。

该工具适合验证游戏杆功能、进行校准以及排查输入问题。它兼容手柄、飞行摇杆和其他游戏控制器。

# OUTPUT

```
Driver version is 2.1.0.
Joystick (Microsoft X-Box One pad) has 8 axes (X, Y, Z, Rx, Ry, Rz, Hat0X, Hat0Y)
and 11 buttons (BtnA, BtnB, BtnX, BtnY, BtnTL, BtnTR, BtnSelect, BtnStart, BtnMode, BtnThumbL, BtnThumbR).
Testing ... (interrupt to exit)
Axes:  0:     0  1:     0  2:-32767  3:     0  4:     0  5:-32767  6:     0  7:     0
Buttons:  0:off  1:off  2:off  3:off  4:off  5:off  6:off  7:off  8:off  9:off 10:off
```

# CAVEATS

需要游戏杆驱动支持。热插拔后设备路径可能变化。可能需要先校准。部分控制器需要 xpad 或其他驱动。

# HISTORY

jstest 是 Linux **joystick** 软件包的一部分，提供基本的输入设备测试功能。它配合内核的游戏杆 API（/dev/input/js*）工作。

# INSTALL

```apt: sudo apt install joystick```

```dnf: sudo dnf install linuxconsoletools```

```apk: sudo apk add linuxconsoletools```

```zypper: sudo zypper install linuxconsoletools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[evtest](/man/evtest)(1), [inputattach](/man/inputattach)(1)
