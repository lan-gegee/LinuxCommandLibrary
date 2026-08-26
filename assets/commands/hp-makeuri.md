# TAGLINE

为 HP 打印机生成设备 URI

# TLDR

**生成设备 URI**

```hp-makeuri [192.168.1.100]```

**USB 设备**

```hp-makeuri -b usb```

**网络探测**

```hp-makeuri -g```

**指定端口**

```hp-makeuri -p [9100] [ip-address]```

# SYNOPSIS

**hp-makeuri** [_options_] [_ip-address_]

# PARAMETERS

_IP-ADDRESS_
> 打印机 IP 地址。

**-b** _BUS_
> 总线类型（usb、net）。

**-g**
> 猜测/探测设备。

**-p** _PORT_
> 网络端口。

**-s** _SERIAL_
> 按序列号过滤。

**--help**
> 显示帮助信息。

# DESCRIPTION

**hp-makeuri** 为 HP 打印机生成设备 URI。它创建 CUPS 打印机配置所需的正确 URI 格式。

该工具会探测网络或 USB 打印机并构造有效的设备标识符。URI 配合 lpadmin 和 CUPS 使用。

# CAVEATS

属于 HPLIP 软件包。网络打印机需要网络连通性。USB 设备需要相应权限。

# HISTORY

hp-makeuri 是 **HPLIP**（HP Linux Imaging and Printing）中负责设备 URI 生成的组件。

# INSTALL

```apt: sudo apt install hplip```

```dnf: sudo dnf install hplip```

```pacman: sudo pacman -S hplip```

```zypper: sudo zypper install hplip```

```nix: nix profile install nixpkgs#hplip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hp-setup](/man/hp-setup)(1), [lpadmin](/man/lpadmin)(1)
