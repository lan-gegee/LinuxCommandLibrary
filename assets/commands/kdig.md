# TAGLINE

Knot DNS 项目的高级 DNS 查询工具

# TLDR

**查询 A 记录**

```kdig [example.com] A```

**查询指定服务器**

```kdig [example.com] @[8.8.8.8]```

**使用 TCP 查询**

```kdig +tcp [example.com]```

**使用 TLS 查询（DoT）**

```kdig +tls [example.com] @[1.1.1.1]```

**执行区域传送**

```kdig [example.com] AXFR @[ns1.example.com]```

**带 DNSSEC 验证查询**

```kdig +dnssec [example.com]```

**反向 DNS 查询**

```kdig -x [192.0.2.1]```

# SYNOPSIS

**kdig** [_common-settings_] [_query_...]

# PARAMETERS

**@**_server_
> 要查询的域名服务器。

**-t** _type_
> 查询类型（A、AAAA、MX、NS 等）。

**-x** _address_
> 对 IP 地址进行反向查询。

**+tcp**
> 使用 TCP 而非 UDP。

**+tls**
> 使用 TLS（DNS over TLS）。

**+https**
> 使用 HTTPS（DNS over HTTPS）。

**+dnssec**
> 请求 DNSSEC 记录。

**+short**
> 显示简短输出。

# DESCRIPTION

**kdig** 是 Knot DNS 项目的高级 DNS 查询工具。它支持现代 DNS 协议，包括 DNS over TLS（DoT）和 DNS over HTTPS（DoH）。相比传统的 dig，它为 DNS 故障排查和测试提供了更多功能。

# INSTALL

```apt: sudo apt install knot-dnsutils```

```dnf: sudo dnf install knot-utils```

```apk: sudo apk add knot-utils```

```zypper: sudo zypper install knot-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dig](/man/dig)(1), [host](/man/host)(1), [nslookup](/man/nslookup)(1)
