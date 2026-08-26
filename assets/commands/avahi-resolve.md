# TAGLINE

解析 mDNS 主机名和地址

# TLDR

**将**主机名解析为 IP 地址

```avahi-resolve -n [hostname.local]```

将主机名只**解析**为 IPv4 地址

```avahi-resolve -4 -n [hostname.local]```

将主机名只**解析**为 IPv6 地址

```avahi-resolve -6 -n [hostname.local]```

**将** IP 地址解析为主机名（反向查询）

```avahi-resolve -a [ip_address]```

一次**解析**多个名称

```avahi-resolve -n [host1.local] [host2.local]```

# SYNOPSIS

**avahi-resolve** [_OPTIONS_]

# DESCRIPTION

**avahi-resolve** 通过 Avahi 守护进程在 mDNS/DNS-SD 主机名与 IP 地址之间进行转换。它支持两种解析模式：正向查询（**--name**）将 **myhost.local** 之类的主机名解析为其 IP 地址，反向查询（**--address**）则将 IP 地址解析回其 mDNS 主机名。

该工具使用多播 DNS 查询本地网络，而非传统的单播 DNS 服务器。解析范围仅限于 mDNS 流量可见的本地网段。结果可以限定为仅 IPv4（**-4**）或仅 IPv6（**-6**）。

# PARAMETERS

**-n, --name** _hostname_
> 将主机名解析为 IP 地址

**-a, --address** _ip_
> 将 IP 地址解析为主机名（反向查询）

**-4**
> 只解析为 IPv4 地址

**-6**
> 只解析为 IPv6 地址

**-v, --verbose**
> 启用详细输出

# CAVEATS

仅对启用 mDNS 的主机有效（通常使用 .local 域）。Avahi 守护进程必须正在运行。网络防火墙可能阻止 mDNS 流量（UDP 端口 5353）。

# HISTORY

**avahi-resolve** 是 **Avahi** 软件包的一部分，在 Linux 上提供 mDNS/DNS-SD 名称解析功能。

# INSTALL

```apt: sudo apt install avahi-utils```

```dnf: sudo dnf install avahi-tools```

```apk: sudo apk add avahi-tools```

```zypper: sudo zypper install avahi-utils```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[avahi-resolve-host-name](/man/avahi-resolve-host-name)(1), [avahi-resolve-address](/man/avahi-resolve-address)(1), [avahi-publish](/man/avahi-publish)(1), [avahi-browse](/man/avahi-browse)(1), [avahi-daemon](/man/avahi-daemon)(8)

# RESOURCES

```[Homepage](https://avahi.org/)```

```[Source code](https://github.com/avahi/avahi)```

<!-- verified: 2026-06-17 -->
