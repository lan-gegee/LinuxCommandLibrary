# TAGLINE

用户态 Xbox 手柄驱动

# TLDR

**为已连接的手柄启动驱动**

```sudo xboxdrv```

**以守护进程方式运行**

```sudo xboxdrv --daemon --detach```

**运行时使用 PID 文件**

```sudo xboxdrv --daemon --detach --pid-file [/var/run/xboxdrv.pid]```

**使用配置文件**

```sudo xboxdrv -c [/etc/default/xboxdrv]```

**安静模式**

```sudo xboxdrv --silent```

**列出已连接的手柄**

```sudo xboxdrv --list-controller```

**将扳机键映射为按钮**而不是轴

```sudo xboxdrv --trigger-as-button```

**为摇杆设置自定义死区**

```sudo xboxdrv --deadzone [4000]```

# SYNOPSIS

**xboxdrv** [_options_]

# PARAMETERS

**-D**, **--daemon**
> 以守护进程方式运行，监听 USB 事件。

**--detach**
> 守护进程化时脱离终端。

**--pid-file** _file_
> 将 PID 写入文件。

**-c**, **--config** _file_
> 使用配置文件。

**--silent**
> 抑制常规输出。

**--list-controller**
> 列出已连接的手柄。

**-l**, **--led** _num_
> 设置 LED 状态（0 为关闭，1-4 为玩家编号）。

**--deadzone** _value_
> 设置模拟摇杆死区。

**--trigger-as-button**
> 将扳机键映射为按钮。

# DESCRIPTION

**xboxdrv** 是 Linux 上 Xbox 和 Xbox 360 手柄的用户态驱动。它作为 xpad 内核驱动的替代方案，提供额外的功能，如按键重映射、死区配置和多手柄支持。

该驱动通过 uinput 创建虚拟输入设备，使手柄可以在游戏和应用程序中正常工作。守护进程模式会自动处理手柄的连接/断开事件。

配置文件允许针对每个手柄进行设置和复杂的映射。该驱动支持有线 USB 手柄以及配合 Xbox 360 无线接收器使用的无线手柄。

# CAVEATS

已被内核 xpad 驱动取代（Linux 6.1+），不再推荐使用。需要 uinput 内核模块。访问 USB 需要 root 权限或 udev 规则。可能与 xpad 内核模块冲突。

# HISTORY

**xboxdrv** 诞生于 Linux 内核对 Xbox 手柄支持尚不完善的时期。它提供了内核驱动所缺少的功能。随着内核支持的改进，xboxdrv 停止了开发，用户被建议改用内核驱动。

# INSTALL

```apt: sudo apt install xboxdrv```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jstest](/man/jstest)(1), [evtest](/man/evtest)(1), [udevadm](/man/udevadm)(8)
