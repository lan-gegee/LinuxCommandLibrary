# TAGLINE

端口敲门（port knocking）的客户端组件

# TLDR

**按顺序敲击一系列端口**

```knock [hostname] [port1] [port2] [port3]```

以指定协议**敲击**端口

```knock [hostname] [port]:tcp [port]:udp```

**使用 UDP 作为默认协议**敲击

```knock -u [hostname] [port1] [port2] [port3]```

**每次敲击之间加入延迟**（毫秒）

```knock -d [500] [hostname] [port1] [port2]```

敲击时**显示详细**输出

```knock -v [hostname] [port1] [port2] [port3]```

# SYNOPSIS

**knock** [_options_] _hostname_ _port_[:_protocol_]...

# PARAMETERS

**-u**, **--udp**
> 使用 UDP 而非 TCP

**-4**
> 强制使用 IPv4

**-6**
> 强制使用 IPv6

**-v**, **--verbose**
> 显示详细信息

**-d**, **--delay** _MS_
> 敲击之间的延迟（毫秒）

# DESCRIPTION

**knock** 是端口敲门的客户端组件。端口敲门是一种安全技术：防火墙只有在收到针对关闭端口的一串预定义连接尝试（"敲门"）之后，才会打开特定端口。

客户端按顺序向指定端口发送数据包。当服务器端（knockd）检测到正确的序列时，就会执行配置的命令，通常是为客户端 IP 地址打开防火墙端口。

# CAVEATS

端口序列必须保密。网络问题可能导致敲门序列失败。它不是正确身份验证的替代品，而是一层额外的安全防护。

# HISTORY

端口敲门作为一种安全技术出现于 **21 世纪初**，用于向端口扫描器隐藏服务。knock/knockd 实现是应用最广泛的端口敲门方案之一。

# INSTALL

```apt: sudo apt install knockd```

```dnf: sudo dnf install knock```

```pacman: sudo pacman -S knockd```

```apk: sudo apk add knock```

```zypper: sudo zypper install knockd```

```brew: brew install knock```

```nix: nix profile install nixpkgs#knock```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[knockd](/man/knockd)(1), [iptables](/man/iptables)(8), [nmap](/man/nmap)(1)
