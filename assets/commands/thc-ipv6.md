# TAGLINE

IPv6 安全测试工具包

# TLDR

在网络中**扫描存活的 IPv6 主机**

```atk6-alive6 [eth0]```

**跟踪到 IPv6 主机的路由**

```atk6-trace6 [eth0] [target]```

**将 MAC 地址转换为** IPv6 链路本地地址

```atk6-address6 [00:11:22:33:44:55]```

**用路由器通告泛洪目标**

```atk6-flood_router6 [eth0] [target]```

**伪造邻居通告**（中间人攻击）

```atk6-parasite6 [eth0]```

**伪装成路由器进行通告**

```atk6-fake_router6 [eth0] [network/64]```

**测试已知 IPv6 漏洞**

```atk6-exploit6 [eth0] [target]```

# SYNOPSIS

**atk6-**_tool_ [_options_] [_interface_] [_arguments_]

# TOOLS

**alive6**
> 检测本地网段上存活的主机

**trace6**
> 使用 ICMP6 或 TCP-SYN 的快速 IPv6 traceroute

**address6**
> 在 MAC、IPv4 和 IPv6 地址之间转换

**fake_router6**
> 在网络上伪装成路由器进行通告

**flood_router6**
> 用随机路由器通告泛洪目标

**flood_advertise6**
> 用随机邻居通告泛洪目标

**parasite6**
> 用于中间人攻击的 ICMP 邻居欺骗器

**redir6**
> 用于中间人攻击的 ICMPv6 重定向欺骗器

**dos-new-ip6**
> 通过告知新设备其 IP 冲突来发起 DoS

**denial6**
> 用 DAD 攻击阻止新的 IPv6 接口

**fake_mld6**
> 加入网络上的组播组

**exploit6**
> 测试已知的 IPv6 实现漏洞

**ndpexhaust26**
> 用 ICMPv6 泛洪耗尽 NDP 表

**rsmurf6**
> 基于 IPv6 的远程 smurf 攻击

# DESCRIPTION

**thc-ipv6** 是一个用于测试 IPv6 和 ICMPv6 协议弱点的工具包。它包含多种工具，可用于 IPv6 网络上的网络侦察、拒绝服务、中间人攻击和漏洞测试。

在基于 Debian 的系统上，这些工具以 **atk6-** 为前缀（例如 **atk6-alive6**）。每个工具有各自的选项；用 **-h** 运行可查看帮助。该工具包利用了 IPv6 区别于 IPv4 的特性，包括邻居发现、路由器通告和组播。

库文件 **thc-ipv6-lib.c** 让开发者能用少量代码构造自定义的 IPv6/ICMPv6 数据包工具。环境变量 **THC_IPV6_PPPOE** 和 **THC_IPV6_6IN4** 用于配置隧道支持。

# CAVEATS

这些工具仅限用于获得授权的安全测试。IPv6 攻击可能中断网段内所有用户的网络连接。许多攻击需要 root 权限和直接的网络访问。某些工具可能导致存在漏洞的系统崩溃。对 IPv6 攻击的检测和日志记录因网络基础设施而异。

# HISTORY

THC-IPv6 由德国黑客团体 **The Hacker's Choice**（THC）的 **van Hauser**（Marc Heuse）创建。该工具包的开发目的是在各组织开始部署 IPv6 时展示其安全弱点。它揭示了 IPv6 引入了 IPv4 网络中不存在的新攻击面，尤其是围绕邻居发现和路由器通告协议的部分。

# INSTALL

```dnf: sudo dnf install thc-ipv6```

```pacman: sudo pacman -S thc-ipv6```

```nix: nix profile install nixpkgs#thc-ipv6```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nmap](/man/nmap)(1), [ip](/man/ip)(8), [ping6](/man/ping6)(8), [traceroute6](/man/traceroute6)(8)
