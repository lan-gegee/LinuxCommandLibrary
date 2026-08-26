# TAGLINE

控制设备亮度

# TLDR

**列出**可调节亮度的设备

```brightnessctl -l```

打印**当前亮度**

```brightnessctl get```

打印**指定设备**的亮度

```brightnessctl get -d '[device_name]'```

将亮度**设置为**百分比

```brightnessctl set [50]%```

按百分比**增加**亮度

```brightnessctl set +[10]%```

按百分比**降低**亮度

```brightnessctl set [10]%-```

# SYNOPSIS

**brightnessctl** [_options_] _command_ [_arguments_]

# DESCRIPTION

**brightnessctl** 在 Linux 系统上读取并控制设备的亮度。它通过 sysfs 接口支持显示屏背光、键盘背光以及其他可调亮度的设备。

该工具可以使用绝对值或百分比调整亮度，并支持增减操作。

# SUBCOMMANDS

**list**（或 **-l**）
> 列出所有可调节亮度的设备。

**get**（或 **g**）
> 获取当前亮度值。

**set**（或 **s**）
> 将亮度设置为某个数值或百分比。

**max**（或 **m**）
> 获取最大亮度值。

# PARAMETERS

**-d, --device** _name_
> 指定设备（支持通配符）。

**-c, --class** _class_
> 设备类别（backlight、leds）。

**-s, --save**
> 在更改前保存状态。

**-r, --restore**
> 恢复已保存的状态。

**-q, --quiet**
> 不输出信息。

# CAVEATS

需要相应权限（通常是加入 video 组）。并非所有设备都支持细粒度亮度控制。最小亮度可能不为零。

# INSTALL

```apt: sudo apt install brightnessctl```

```dnf: sudo dnf install brightnessctl```

```pacman: sudo pacman -S brightnessctl```

```apk: sudo apk add brightnessctl```

```zypper: sudo zypper install brightnessctl```

```nix: nix profile install nixpkgs#brightnessctl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xbacklight](/man/xbacklight)(1), [light](/man/light)(1), [backlight_control](/man/backlight_control)(1)

# RESOURCES

```[Source code](https://github.com/Hummer12007/brightnessctl)```

<!-- verified: 2026-06-22 -->
