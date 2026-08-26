# TAGLINE

伪造 ARP 应答以进行中间人拦截。

# TLDR

针对目标主机**毒化**所有主机

```sudo arpspoof -i wlan0 host_ip```

毒化指定的**目标**

```sudo arpspoof -i wlan0 -t target_ip host_ip```

**双向**毒化

```sudo arpspoof -i wlan0 -r -t target_ip host_ip```

# SYNOPSIS

**arpspoof** [_-i interface_] [_-c own_|_host_|_both_] [_-t target_] [_-r_] _host_

# DESCRIPTION

**arpspoof** 通过伪造 ARP 应答来拦截网络数据包。它发送虚假的 ARP 响应，将流量重定向到攻击者的机器，从而实现中间人攻击，用于网络分析和安全测试。

# PARAMETERS

**-i** _interface_
> 要使用的网络接口

**-c** _own_|_host_|_both_
> 清理恢复 ARP 配置时使用哪个硬件地址（默认：own）

**-t** _target_
> 要毒化的目标 IP 地址（省略时毒化所有主机）。可重复使用以指定多个目标

**-r**
> 同时毒化 host 和 target 以捕获双向流量（仅在与 -t 一起使用时有效）

**host**
> 要冒充的主机的 IP 地址（通常是网关）

# CAVEATS

这是一个渗透测试工具，可能中断网络流量。只在你拥有或获得明确测试授权的网络上使用。需要 root 权限并启用 IP 转发，流量才能正常流动。

# HISTORY

**arpspoof** 是 **dsniff** 软件包的一部分，该软件包是一组面向渗透测试和安全分析的网络审计工具。

# INSTALL

```apt: sudo apt install dsniff```

```dnf: sudo dnf install dsniff```

```pacman: sudo pacman -S dsniff```

```nix: nix profile install nixpkgs#dsniff```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[dsniff](/man/dsniff)(8), [tcpdump](/man/tcpdump)(8), [ettercap](/man/ettercap)(8)

# RESOURCES

```[Source code](https://github.com/tecknicaltom/dsniff)```

```[Homepage](https://www.monkey.org/~dugsong/dsniff/)```

<!-- verified: 2026-06-16 -->
