# TAGLINE

通过 TCP/IP 远程访问无线网卡的服务器

# TLDR

**在指定信道和端口上启动接口的无线服务器**

```sudo airserv-ng -d [wlan0mon] -c [6] -p [666]```

**在默认端口上启动服务器**

```sudo airserv-ng -d [wlan0mon]```

**以详细调试输出启动**

```sudo airserv-ng -d [wlan0mon] -v [3]```

# SYNOPSIS

**airserv-ng** [_options_]

# PARAMETERS

**-d** _IFACE_
> 要提供服务的无线接口（必需）。

**-c** _CHAN_
> 将接口锁定到特定信道。

**-p** _PORT_
> 要监听的 TCP 端口（默认：666）。

**-v** _LEVEL_
> 调试级别。级别 1 显示客户端连接/断开（默认），更高级别显示更多细节。

**-h**
> 显示帮助信息。

# DESCRIPTION

**airserv-ng** 是一个无线网卡服务器，允许多个无线应用程序通过客户端-服务器式的 TCP 网络连接独立使用同一块无线网卡。所有与操作系统和无线网卡驱动相关的代码都封装在服务器中。

客户端以 **host:port** 作为接口名来连接，而非使用本地设备。这使得可以在一台机器上运行 aircrack-ng 工具，而无线网卡物理连接在另一台机器上。

# CAVEATS

没有内置的认证或加密；请使用 SSH 隧道实现安全的远程访问。网络延迟可能影响实时的数据包注入。通常应先将无线网卡置于监听模式再启动服务器。

# HISTORY

**airserv-ng** 作为 **aircrack-ng** 套件的一部分而创建，用于支持分布式无线测试场景，即无线硬件与分析软件分别运行在不同机器上。

# INSTALL

```apt: sudo apt install aircrack-ng```

```dnf: sudo dnf install aircrack-ng```

```pacman: sudo pacman -S aircrack-ng```

```apk: sudo apk add aircrack-ng```

```zypper: sudo zypper install aircrack-ng```

```brew: brew install aircrack-ng```

```nix: nix profile install nixpkgs#aircrack-ng```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aircrack-ng](/man/aircrack-ng)(1), [airodump-ng](/man/airodump-ng)(1), [aireplay-ng](/man/aireplay-ng)(1), [airmon-ng](/man/airmon-ng)(1)
