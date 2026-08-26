# TAGLINE

调节屏幕背光亮度

# TLDR

获取当前**亮度**

```xbacklight```

**设置**亮度

```xbacklight -set [40]```

**提高**亮度

```xbacklight -inc [25]```

**降低**亮度

```xbacklight -dec [75]```

以**渐变**效果设置

```xbacklight -set [100] -time [60000] -steps [60]```

# SYNOPSIS

**xbacklight** [_OPTIONS_]

# PARAMETERS

**-get**
> 打印当前亮度百分比（未指定操作时的默认行为）。

**-set** _PERCENT_
> 将亮度设置为指定百分比。

**-inc** _PERCENT_
> 按百分比提高亮度。

**-dec** _PERCENT_
> 按百分比降低亮度。

**-time** _MS_
> 渐变时长，以毫秒为单位。

**-steps** _N_
> 渐变的步数。

**-display** _DISPLAY_
> 要使用的 X display。

**-help**
> 显示帮助信息。

# DESCRIPTION

**xbacklight** 使用 X RandR 扩展的背光属性来调节背光亮度。不带参数调用时，它以百分比形式打印当前亮度级别。**-set**、**-inc** 和 **-dec** 选项用于修改亮度。

**-time** 和 **-steps** 参数可实现平滑的渐变过渡，将亮度变化分散到指定的时长内完成。

# CAVEATS

仅支持 X11；在 Wayland 下无法使用。需要显示驱动暴露 RandR 背光属性。许多现代笔记本电脑和专有驱动（如 NVIDIA）不暴露该属性。建议改用 **brightnessctl** 或 **light** 等通过 sysfs 工作的更可靠的替代工具。

# INSTALL

```apt: sudo apt install xbacklight```

```dnf: sudo dnf install xbacklight```

```apk: sudo apk add xbacklight```

```zypper: sudo zypper install xbacklight```

```nix: nix profile install nixpkgs#xbacklight```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[brightnessctl](/man/brightnessctl)(1), [light](/man/light)(1), [xrandr](/man/xrandr)(1)
