# TAGLINE

简单的串口设备终端模拟器

# TLDR

**连接串口设备**

```tio [/dev/ttyUSB0]```

**以指定波特率连接**

```tio -b [115200] [/dev/ttyUSB0]```

**带参数连接**

```tio -b [9600] -d [8] -s [1] -p [none] [/dev/ttyUSB0]```

**启用本地回显**

```tio -e [/dev/ttyUSB0]```

**将会话记录到文件**

```tio -l [session.log] [/dev/ttyUSB0]```

# SYNOPSIS

**tio** [_options_] _device_

# PARAMETERS

**-b** _rate_
> 波特率（默认 115200）。

**-d** _bits_
> 数据位（5、6、7、8）。

**-s** _bits_
> 停止位（1、2）。

**-p** _parity_
> 校验位（none、odd、even）。

**-e**
> 启用本地回显。

**-l** _file_
> 记录到文件。

**-t**
> 启用时间戳。

**-m** _map_
> 映射特殊字符。

# DESCRIPTION

**tio** 是一款简单的串口设备终端模拟器，定位为 minicom 和 screen 在串口通信上的现代化、易用替代品。它以合理的默认值（115200 波特率，8N1）连接串口，并支持在设备插入或变为可用时自动重连。

该工具提供基本的串口通信特性，包括可配置的波特率、数据位、停止位和校验位设置、本地回显、会话日志以及时间戳。前缀键 **Ctrl+t** 提供会话内命令入口，其中 **Ctrl+t q** 用于退出。

# CAVEATS

按 **Ctrl+t q** 退出终端会话。

# INSTALL

```apt: sudo apt install tio```

```dnf: sudo dnf install tio```

```apk: sudo apk add tio```

```zypper: sudo zypper install tio```

```brew: brew install tio```

```nix: nix profile install nixpkgs#tio```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[minicom](/man/minicom)(1), [screen](/man/screen)(1), [picocom](/man/picocom)(1)
