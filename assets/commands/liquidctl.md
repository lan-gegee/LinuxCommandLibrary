# TAGLINE

控制水冷散热器和 RGB 设备

# TLDR

**列出设备**

```liquidctl list```

**初始化设备**

```liquidctl initialize```

**设置水泵转速**

```liquidctl set pump speed [50]```

**设置风扇曲线**

```liquidctl set fan speed 20 30 30 50 40 70 50 100```

**设置 LED 颜色**

```liquidctl set led color fixed [ff0000]```

**显示设备状态**

```liquidctl status```

# SYNOPSIS

**liquidctl** [_options_] _command_ [_args_]

# PARAMETERS

_COMMAND_
> 要执行的操作。

**list**
> 列出受支持的设备。

**initialize**
> 初始化设备。

**status**
> 显示设备状态。

**set** _CHANNEL_ _MODE_ _VALUE_
> 配置设备设置。

**--match** _PATTERN_
> 匹配特定设备。

**--help**
> 显示帮助信息。

# DESCRIPTION

**liquidctl** 控制水冷散热器和 RGB 设备。它可管理水泵转速、风扇曲线和 LED 灯效。

该工具支持来自多家厂商的众多一体式水冷散热器和 RGB 控制器。

# CAVEATS

需要 root 权限或 udev 规则。设备支持情况各不相同。某些功能依赖特定硬件。

# HISTORY

liquidctl 的创建目的是为 Linux 上的 AIO 水冷散热器和 RGB 外设提供开源控制方案。

# INSTALL

```apt: sudo apt install liquidctl```

```dnf: sudo dnf install liquidctl```

```pacman: sudo pacman -S liquidctl```

```apk: sudo apk add liquidctl```

```brew: brew install liquidctl```

```nix: nix profile install nixpkgs#liquidctl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sensors](/man/sensors)(1), [fancontrol](/man/fancontrol)(1)
