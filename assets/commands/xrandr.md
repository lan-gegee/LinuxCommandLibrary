# TAGLINE

配置 X11 显示输出

# TLDR

**查询**当前显示配置

```xrandr -q```

**自动配置**显示器

```xrandr --auto```

设置**分辨率和刷新率**

```xrandr --output DP1 --mode 1920x1080 -r 60```

将显示器置于另一显示器**相对位置**

```xrandr --output HDMI2 --mode 1280x1024 --right-of DP1```

**禁用**某个输出

```xrandr --output VGA1 --off```

设置**亮度**

```xrandr --output LVDS1 --brightness 0.5```

**旋转**显示

```xrandr --output HDMI1 --rotate left```

**镜像**多个显示器

```xrandr --output HDMI1 --same-as LVDS1```

# SYNOPSIS

**xrandr** [_--output output_] [_--mode mode_] [_--rate rate_] [_--pos position_] [_options_]

# DESCRIPTION

**xrandr** 用于设置 X screen 各输出的尺寸、方向和镜像。它还可以动态调整屏幕大小、添加/删除显示模式以及更改显示属性，无需重启 X。

# PARAMETERS

**-q, --query**
> 显示当前屏幕配置

**--output OUTPUT**
> 选择要配置的输出

**--mode MODE**
> 设置分辨率模式（WIDTHxHEIGHT）

**-r, --rate RATE**
> 设置刷新率（Hz）

**--pos XxY**
> 设置输出的位置

**--left-of OUTPUT**
> 置于指定输出的左侧

**--right-of OUTPUT**
> 置于指定输出的右侧

**--above OUTPUT**
> 置于指定输出上方

**--below OUTPUT**
> 置于指定输出下方

**--same-as OUTPUT**
> 镜像指定输出

**--rotate ROTATION**
> 旋转输出（normal、left、right、inverted）

**--reflect REFLECTION**
> 镜像翻转输出（x、y、xy、normal）

**--brightness LEVEL**
> 设置亮度（0.0 到 1.0）

**--gamma R:G:B**
> 设置伽马校正

**--off**
> 禁用输出

**--auto**
> 以首选模式启用输出

**--primary**
> 设为主输出

**-d, --display DISPLAY**
> 指定要使用的 X display

**--dpi DPI**
> 为屏幕设置 DPI

# CAVEATS

更改是临时的，重启 X 后会重置。若要持久化设置，可将 xrandr 命令加入 ~/.xprofile 或使用显示管理器的设置。某些模式可能不适用于所有硬件。

# HISTORY

**xrandr** 是 X.Org 项目的一部分，实现了 RandR（Resize and Rotate）扩展，可在不重启 X server 的情况下动态配置显示。

# INSTALL

```apt: sudo apt install x11-xserver-utils```

```dnf: sudo dnf install xrandr```

```apk: sudo apk add xrandr```

```zypper: sudo zypper install xrandr```

```nix: nix profile install nixpkgs#xrandr```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xset](/man/xset)(1), [xdpyinfo](/man/xdpyinfo)(1), [arandr](/man/arandr)(1)
