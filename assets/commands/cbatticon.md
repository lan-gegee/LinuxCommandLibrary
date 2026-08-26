# TAGLINE

轻量级系统托盘电池指示器

# TLDR

在系统托盘显示**电池图标**

```cbatticon```

设置以秒为单位的**刷新间隔**（默认：5）

```cbatticon -u [10]```

列出可用的**图标类型**

```cbatticon -t```

以**指定图标类型**显示

```cbatticon -i [standard|notification|symbolic]```

列出可用的**电源**

```cbatticon -p```

为**指定电池**显示图标

```cbatticon [BAT0]```

设置**危急电量**命令

```cbatticon -r [5] -c [poweroff]```

# SYNOPSIS

**cbatticon** [_options_] [_battery_]

# DESCRIPTION

**cbatticon** 是一个轻量级的系统托盘电池指示器。它使用可配置的图标显示电池状态，并能在电量达到危急水平时执行命令。

该工具专为不自带电池监控功能的最小化窗口管理器和桌面环境设计。

# PARAMETERS

**-u**, **--update-interval** _seconds_
> 刷新间隔，单位为秒（默认：5）。

**-i**, **--icon-type** _type_
> 图标样式：standard、notification 或 symbolic。

**-t**, **--list-icon-types**
> 列出可用的图标类型。

**-p**, **--list-power-supplies**
> 列出可用的电源。

**-r**, **--critical-level** _percent_
> 设置危急电量百分比（默认：5%）。

**-c**, **--command-critical-level** _cmd_
> 达到危急电量时执行的命令。

**-o**, **--command-low-level** _cmd_
> 达到低电量时执行的命令。

**-l**, **--low-level** _percent_
> 设置低电量百分比。

**-x**, **--command-left-click** _cmd_
> 左键点击托盘图标时执行的命令。

**-d**, **--debug**
> 显示调试信息。

# CAVEATS

需要系统托盘才能显示。在不支持托盘的 Wayland 合成器上可能无法工作。危急电量命令以用户权限运行。

# INSTALL

```apt: sudo apt install cbatticon```

```pacman: sudo pacman -S cbatticon```

```apk: sudo apk add cbatticon```

```nix: nix profile install nixpkgs#cbatticon```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[upower](/man/upower)(1), [acpi](/man/acpi)(1)
