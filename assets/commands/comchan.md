# TAGLINE

极简的终端串口监视器

# TLDR

以 9600 波特率**连接**串口

```comchan -p /dev/ttyUSB0 -r 9600```

**自动检测**串口并以 115200 波特率连接

```comchan --auto -r 115200```

启用实时绘图后**连接**

```comchan -p /dev/ttyACM0 -r 9600 --plot```

**启用**详细输出和日志记录

```comchan -p /dev/ttyUSB0 -r 9600 -v -l```

**生成**默认配置文件

```comchan --generate-config```

# SYNOPSIS

**comchan** [_OPTIONS_]

# PARAMETERS

**-p**, **--port** _PORT_
> 指定串口（例如 /dev/ttyUSB0、/dev/ttyACM0、COM3）。

**-r**, **--baud** _RATE_
> 设置波特率（例如 9600、115200）。

**--auto**
> 自动检测已连接的串口。

**-v**, **--verbose**
> 显示详细的连接信息。

**-l**, **--log**
> 将输出保存到日志文件。

**--plot**
> 启用基于终端的传感器数据实时绘图。

**--generate-config**
> 在 ~/.config/comchan/comchan.toml 生成默认配置文件。

**--help**
> 显示帮助信息。

# DESCRIPTION

**comchan**（Communication Channel）是一个用 Rust 编写的快速、极简的串口监视器，用于在终端中与 Arduino、ESP32、Teensy 和树莓派等串口设备通信。它支持读写串口数据、自动检测已连接的设备、基于终端的传感器数据实时绘图（可同时可视化多个传感器）、彩色日志输出，并可在 Linux、macOS 和 Windows 上跨平台运行。

# CONFIGURATION

配置存储在 **~/.config/comchan/comchan.toml**。支持 **port**（或 "auto"）、**baud**（默认：9600）、**data_bits**、**stop_bits**、**parity**（none/odd/even）、**flow_control**（none/software/hardware）、**timeout_ms**、**reset_delay_ms**、**verbose** 和 **plot**。命令行标志会覆盖配置文件中的值。

# CAVEATS

在 Linux 上，用户可能需要适当的权限才能访问串口（通常需要加入 **dialout** 或 **uucp** 组）。**--plot** 功能要求串口设备提供数值数据才能正确绘图。

# HISTORY

**comchan** 由 **Vaishnav Sabari Girish** 创建，采用 Rust 编写并以 MIT 许可证发布。可通过 cargo、AUR 和 Homebrew 获取，遵循 Unix "做好一件事"的哲学。

# INSTALL

```aur: yay -S comchan```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[minicom](/man/minicom)(1), [picocom](/man/picocom)(1), [screen](/man/screen)(1), [tio](/man/tio)(1), [cu](/man/cu)(1)
