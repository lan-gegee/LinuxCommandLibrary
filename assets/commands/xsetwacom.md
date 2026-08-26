# TAGLINE

配置 Wacom 数位板设置

# TLDR

**列出**所有 Wacom 设备

```xsetwacom list devices```

**列出**可用参数

```xsetwacom list parameters```

**获取**设备的全部当前设置

```xsetwacom get "[device_name]" all```

**映射**数位板输入到指定屏幕

```xsetwacom set "[device_name]" MapToOutput [screen]```

将输入**模式**设为 Relative（鼠标式）或 Absolute（笔式）

```xsetwacom set "[device_name]" Mode [Relative|Absolute]```

**旋转**数位板输入

```xsetwacom set "[device_name]" Rotate [none|half|cw|ccw]```

使用贝塞尔控制点（0-100）设置**压感曲线**

```xsetwacom set "[device_name]" PressureCurve [0] [0] [100] [100]```

**映射**数位板按钮到按键组合

```xsetwacom set "[device_name]" Button [button_number] "key [keystroke]"```

# SYNOPSIS

**xsetwacom** [_options_] _command_ [_device_name_] [_parameter_] [_value_]

# PARAMETERS

**list** devices
> 列出所有已识别的 Wacom 输入设备。

**list** parameters
> 列出适用于 get 或 set 命令的所有参数。

**list** modifiers
> 列出可用于按键和按钮操作的修饰键。

**set** _DEVICE_ _PARAM_ _VALUE_
> 为给定设备设置参数值。

**get** _DEVICE_ _PARAM_
> 获取参数的当前值。使用 "all" 显示全部设置。

**-s**, **--shell**
> 以可复现相同设置的 shell 命令形式显示输出。

**-x**, **--xconf**
> 以 xorg.conf 选项的形式显示输出。

# COMMON PARAMETERS

**Mode** [Relative|Absolute]
> Relative 模式使设备表现得像鼠标。Absolute 模式将位置直接映射到屏幕。

**MapToOutput** _SCREEN_
> 将数位板输入区域映射到特定的屏幕输出（例如 "HDMI-1"）或 X11 几何描述（WIDTHxHEIGHT+X+Y）。

**Rotate** [none|half|cw|ccw]
> 旋转输入。none：不旋转；half：180 度；cw：顺时针 90 度；ccw：逆时针 90 度。

**Button** _NUMBER_ _MAPPING_
> 将按钮映射到鼠标按键编号或按键操作。

**PressureCurve** _x1_ _y1_ _x2_ _y2_
> 定义压感响应的贝塞尔曲线控制点（0-100）。

**Area** _x1_ _y1_ _x2_ _y2_
> 以设备坐标设置数位板输入区域（左上角和右下角）。

**Threshold** _LEVEL_
> 触发按键事件所需的最小压力。范围 0-2047，默认 27。

**Touch** [on|off]
> 启用或禁用设备的触摸输入。

**TabletPCButton** [on|off]
> 开启时，触控笔必须接触屏幕才会生成按钮事件。Tablet PC 上默认开启。

**Suppress** _LEVEL_
> 发送输入事件前所需的最小坐标变化量。

# DESCRIPTION

**xsetwacom** 是一个在运行时查询和修改 Wacom 驱动设置的命令行工具。它可以配置输入模式、屏幕映射、旋转、压感响应、按钮映射和触摸行为。

设备名称可通过 `xsetwacom list devices` 或 `xinput list` 查看。并非所有参数都适用于所有设备类型；使用 `xsetwacom list parameters` 可以查看支持的参数。

# CAVEATS

仅支持 X11；不适用于 Wayland。设置不会在重启或设备重新连接后保留。持久配置请使用 xorg.conf.d 片段。设备重新连接后设备名称可能变化。

# INSTALL

```apt: sudo apt install xserver-xorg-input-wacom```

```pacman: sudo pacman -S xf86-input-wacom```

```apk: sudo apk add xf86-input-wacom```

```zypper: sudo zypper install xf86-input-wacom```

```nix: nix profile install nixpkgs#xf86-input-wacom```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xinput](/man/xinput)(1), [xrandr](/man/xrandr)(1), [xdotool](/man/xdotool)(1)
