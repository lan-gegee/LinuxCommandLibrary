# TAGLINE

扫描网络中的 NetBIOS 名称信息

# TLDR

**扫描网络中的 NetBIOS 名称**

```nbtscan [192.168.1.0/24]```

**扫描单个主机**

```nbtscan [192.168.1.10]```

**详细输出**

```nbtscan -v [192.168.1.0/24]```

**人类可读输出**

```nbtscan -h [192.168.1.0/24]```

**显示全部名称**

```nbtscan -f [192.168.1.0/24]```

**设置超时时间**

```nbtscan -t [5] [192.168.1.0/24]```

# SYNOPSIS

**nbtscan** [_options_] _target_

# PARAMETERS

_TARGET_
> IP 地址或网段范围。

**-v**
> 详细模式。

**-h**
> 人类可读输出。

**-f**
> 显示完整的 NBT 资源记录。

**-t** _SECS_
> 以秒计的超时时间。

**--help**
> 显示帮助信息。

# DESCRIPTION

**nbtscan** 用 NetBIOS Name Service（UDP 端口 **137**）查询扫描目标 IP 地址或 CIDR 网段并解析响应，打印 NetBIOS 计算机名、登录用户、工作组/域、MAC 地址（如有）以及注册的服务代码。它相当于 Windows 上 **nbtstat -A** 的全网段版本，可用于清点局域网内的 Windows 和 Samba 主机。

默认输出每台主机一行，适合管道传给 shell 处理；**-v** 显示每一条 NetBIOS 名称表记录，**-f** 打印完整表，包括映射到工作站、文件服务器、域控制器等的类型代码（00、03、20、1B、1C 等）。**-h** 为每台主机输出更易读的分节信息。

# CAVEATS

目标主机必须启用 TCP/IP 上的 NetBIOS；现代 Windows 网络可能已禁用它而改用基于 TCP/445 的 SMB 直连。扫描整个网段会产生明显的流量，且经常触发 IDS 告警；扫描前请先获得授权。UDP/137 常在网络边界被封锁，因此外部扫描通常一无所获。

# HISTORY

**nbtscan** 由 **Alla Bezroutchko** 编写（早期版本由 Steve Friedl 维护），作为 Windows **nbtstat -A** 的快速 Unix 端替代品。自 2000 年代初以来，几乎所有的渗透测试与取证 Linux 发行版都收录了该工具。

# INSTALL

```apt: sudo apt install nbtscan```

```pacman: sudo pacman -S nbtscan```

```apk: sudo apk add nbtscan```

```nix: nix profile install nixpkgs#nbtscan```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nmblookup](/man/nmblookup)(1), [nmap](/man/nmap)(1), [smbclient](/man/smbclient)(1)
