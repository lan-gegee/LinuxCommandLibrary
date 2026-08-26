# TAGLINE

通过串口访问远程设备的极简终端程序

# TLDR

使用指定波特率打开**串口**

```microcom -p [/dev/ttyXYZ] -s [baud_rate]```

建立到指定主机的 **telnet 连接**

```microcom -t [hostname]:[port]```

# SYNOPSIS

**microcom** [_options_]

# PARAMETERS

**-p, --port _device_**
> 要连接的串口设备（例如 /dev/ttyUSB0）

**-s, --speed _baud_**
> 串口通信的波特率（例如 9600、115200）

**-t, --telnet _host:port_**
> 通过 telnet 连接到指定的主机和端口

**-c, --can _interface_**
> 连接到 CAN 总线接口

**-l, --logfile _file_**
> 将会话记录到文件

# DESCRIPTION

**microcom** 是一个极简的终端程序，用于从控制台通过串口、CAN 总线或 telnet 连接访问远程设备。对于基本的串口通信需求，它是 minicom 等程序的简单轻量替代品。

该程序在终端与远程设备之间传递数据，适用于访问嵌入式系统、路由器、网络设备以及其他带有串口控制台的设备。

按 **Ctrl+\\** 再按 **q**（或配置的转义序列）退出 microcom。

# CAVEATS

串口访问通常需要相应权限（在大多数 Linux 系统上需加入 **dialout** 组）。设备必须配置正确的波特率、校验位和停止位以匹配远程设备。没有内置 XMODEM 或 ZMODEM 等文件传输协议。

# INSTALL

```apt: sudo apt install microcom```

```zypper: sudo zypper install microcom```

```nix: nix profile install nixpkgs#microcom```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[minicom](/man/minicom)(1), [screen](/man/screen)(1), [picocom](/man/picocom)(1), [cu](/man/cu)(1)
