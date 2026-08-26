# TAGLINE

将 IP 地址转换为反向 DNS ARPA 名称。

# TLDR

将 **IP 地址**转换为其对应的 ARPA 名称

```arpaname [ip_address]```

将 **IPv6 地址**转换为 ARPA 格式

```arpaname [2001:db8::1]```

# SYNOPSIS

**arpaname** _ip_address_...

# DESCRIPTION

**arpaname** 将 IP 地址（IPv4 和 IPv6）转换为其对应的反向 DNS ARPA 域名。这些名称用于反向 DNS 查询，即把 IP 地址映射回主机名。

对于 IPv4 地址，输出位于 **in-addr.arpa** 域；对于 IPv6 地址，输出位于 **ip6.arpa** 域，每个十六进制数字逆序排列并以点分隔。

# CAVEATS

这是一个简单的转换工具，不会执行 DNS 查询。它只是把 IP 地址格式化为 ARPA 记法。要执行真正的反向 DNS 查询，请使用带 **-x** 选项的 **dig** 或 **host**。

# HISTORY

**arpaname** 是 BIND（Berkeley Internet Name Domain）工具集的一部分，BIND 是使用最广泛的 DNS 软件。ARPA 名称遵循 RFC 1035（针对 IPv4）和 RFC 3596（针对 IPv6）定义的格式。

# INSTALL

```apt: sudo apt install bind9```

```apk: sudo apk add bind-tools```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[dig](/man/dig)(1), [host](/man/host)(1), [nslookup](/man/nslookup)(1)

# RESOURCES

```[Source code](https://gitlab.isc.org/isc-projects/bind9)```

```[Homepage](https://www.isc.org/bind/)```

```[Documentation](https://bind9.readthedocs.io)```

<!-- verified: 2026-06-15 -->
