# TAGLINE

供控制台访问使用的盲文显示守护进程

# TLDR

**启动 brltty 守护进程**

```brltty```

使用指定的盲文驱动启动

```brltty -b [driver]```

使用指定设备启动

```brltty -d [usb:]```

在前台运行（非守护进程）

```brltty -n```

使用指定的文本表

```brltty -t [en-us-g2]```

启用语音支持

```brltty -e```

设置详细程度

```brltty -v [5]```

显示帮助

```brltty -h```

# SYNOPSIS

**brltty** [_options_]

# DESCRIPTION

**brltty** 是一个后台守护进程，通过可刷新盲文显示器为视障用户提供对 Linux/Unix 控制台的访问。它驱动盲文显示器，提供完整的屏幕阅读功能，并具备部分语音能力。

该守护进程支持串口、USB 或蓝牙连接，兼容数十种型号的盲文显示器。

# PARAMETERS

**-b** _driver_
> 盲文显示器驱动代码。

**-d** _device_
> 设备规格（usb:、bluetooth:、串口）。

**-t** _table_
> 文本转换表。

**-c** _table_
> 缩写表。

**-e**
> 启用语音支持。

**-s** _driver_
> 语音合成器驱动。

**-n**
> 前台运行（不守护进程化）。

**-f** _file_
> 配置文件路径。

**-v** _level_
> 详细程度（0-9）。

**-l** _level_
> 日志级别。

**-V**
> 打印版本信息。

**-h**
> 显示帮助摘要。

# CONFIGURATION

默认配置文件为 **/etc/brltty.conf**。文本表保存在 **/etc/brltty/Text/** 中。设备规格格式为 **qualifier:data**，默认值为 **usb:,bluetooth:**。

# CAVEATS

必须以 root 身份或具备相应设备访问权限运行。启动前盲文显示器必须已连接并通电。支持来自多家厂商的 70 多种盲文显示器型号。

# INSTALL

```apt: sudo apt install brltty```

```dnf: sudo dnf install brltty```

```pacman: sudo pacman -S brltty```

```apk: sudo apk add brltty```

```zypper: sudo zypper install brltty```

```nix: nix profile install nixpkgs#brltty```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[espeak](/man/espeak)(1), [screen](/man/screen)(1)
