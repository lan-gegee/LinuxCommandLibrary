# TAGLINE

DHCP 与 DHCPv6 客户端守护进程

# TLDR

**在指定接口上获取租约**

```sudo dhcpcd [eth0]```

**释放**所有地址租约并退出

```sudo dhcpcd -k```

**请求**新租约（重新绑定）

```sudo dhcpcd -n```

**仅配置 IPv4**

```sudo dhcpcd -4 [eth0]```

**仅配置 IPv6**

```sudo dhcpcd -6 [eth0]```

**测试模式**（不实际配置，只打印变量）

```sudo dhcpcd -T [eth0]```

# SYNOPSIS

**dhcpcd** [_options_] [_interface_]

# DESCRIPTION

**dhcpcd** 是一个 DHCP 和 DHCPv6 客户端守护进程，用于自动配置网络接口。它从网络中的 DHCP 服务器获取 IP 地址、默认路由和 DNS 服务器，还能处理 IPv6 路由通告以实现无状态自动配置。

守护进程在后台运行，随接口的启用和禁用管理网络配置。它会自动处理租约的续约、重新绑定和释放。借助配置钩子，可以在网络状态变化时运行自定义脚本。

dhcpcd 常被许多 Linux 发行版用作默认的网络配置工具，尤其是那些不带 NetworkManager 的发行版。它轻量、严格遵循 RFC 标准，并且能很好地融入嵌入式和服务器环境。

# PARAMETERS

**-k, --release**
> 释放当前租约并退出

**-n, --rebind**
> 请求新租约（重新绑定）

**-x, --exit**
> 退出守护进程

**-d, --debug**
> 调试模式（不 fork）

**-B, --nobackground**
> 不在后台运行

**-4, --ipv4only**
> 只配置 IPv4

**-6, --ipv6only**
> 只配置 IPv6

**-b, --background**
> 立即转入后台

**-S, --static** _value_
> 配置静态 DHCP 值（如 ip_address、routers、domain_name_servers）

**-s, --inform** _address_
> 发送 DHCP INFORM 而不是 DISCOVER/REQUEST

**-T, --test**
> 测试模式，不实际配置接口

# CONFIGURATION

**/etc/dhcpcd.conf**
> 主配置文件，控制接口行为、静态地址、钩子和客户端选项。

# CAVEATS

可能与 NetworkManager 或 systemd-networkd 冲突。配置文件位于 /etc/dhcpcd.conf。需要 root 权限。

# INSTALL

```apt: sudo apt install dhcpcd-base```

```dnf: sudo dnf install dhcpcd```

```pacman: sudo pacman -S dhcpcd```

```apk: sudo apk add dhcpcd```

```zypper: sudo zypper install dhcpcd```

```nix: nix profile install nixpkgs#dhcpcd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dhclient](/man/dhclient)(8), [nmcli](/man/nmcli)(1), [ip](/man/ip)(8)
