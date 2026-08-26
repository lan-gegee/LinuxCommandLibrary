# TAGLINE

力反馈设备测试工具

# TLDR

在**事件设备**上运行 fftest

```fftest [/dev/input/eventX]```

# SYNOPSIS

**fftest** _device_

# DESCRIPTION

**fftest** 用于测试带有振动或触觉反馈功能的力反馈设备，如游戏手柄、方向盘和摇杆。它会向设备发送各种力反馈效果，包括恒定力、周期效果、斜坡和弹簧条件，以验证其是否正常工作。

该工具是 linuxconsole 软件包中用于输入设备测试的一部分。它通过力反馈 API 与 Linux 输入事件设备交互，帮助用户诊断硬件问题并验证驱动支持。

fftest 需要相应的设备权限，主要用于排查游戏外设故障和测试驱动实现。

# PARAMETERS

_device_
> 要测试的输入事件设备（如 /dev/input/event0）

# CAVEATS

需要对输入设备有相应权限。设备必须支持力反馈。可使用 evtest 确认正确的事件设备。

# INSTALL

```apt: sudo apt install joystick```

```dnf: sudo dnf install linuxconsoletools```

```apk: sudo apk add linuxconsoletools```

```zypper: sudo zypper install linuxconsoletools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[evtest](/man/evtest)(1), [jstest](/man/jstest)(1)

# RESOURCES

```[Source code](https://github.com/flosse/linuxconsole)```

<!-- verified: 2026-07-15 -->
