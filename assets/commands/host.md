# TAGLINE

简单的 DNS 查询工具

# TLDR

**查询 IP 地址**

```host [example.com]```

**反向 DNS 查询**

```host [192.168.1.1]```

**查询指定 DNS 服务器**

```host [example.com] [8.8.8.8]```

**查询特定记录类型**

```host -t [MX] [example.com]```

**详细输出**

```host -v [example.com]```

**查询所有记录**

```host -a [example.com]```

# SYNOPSIS

**host** [**-aACdlnrsTUwv**] [**-c** _class_] [**-N** _ndots_] [**-p** _port_] [**-R** _number_] [**-t** _type_] [**-W** _wait_] [**-m** _flag_] [**-4**|**-6**] _name_ [_server_]

# DESCRIPTION

**host** 是一个简单的 DNS 查询工具。它将主机名转换为 IP 地址（反之亦然），并可查询特定的 DNS 记录类型。

该工具提供快捷的 DNS 查询，没有 dig 那样的复杂性，适合简单查找和故障排查。

# PARAMETERS

**-t** _type_
> 查询类型（A、AAAA、MX、NS、TXT、SOA 等）。

**-a**
> 等价于 -v -t ANY；以详细输出查询所有记录类型。

**-A**
> 类似 -a，但省略 RRSIG、NSEC 和 NSEC3 记录。

**-C**
> 检查各权威名称服务器之间 SOA 记录的一致性。

**-v**
> 详细输出（等价于 -d）。

**-l**
> 执行区域传送（AXFR）并列出 NS、PTR 和 A/AAAA 记录。

**-4**
> 仅使用 IPv4 传输。

**-6**
> 仅使用 IPv6 传输。

**-r**
> 非递归查询（清除 RD 位）。

**-s**
> 收到 SERVFAIL 响应后不再尝试下一个名称服务器。

**-W** _seconds_
> 查询超时秒数（默认：UDP 为 5 秒，TCP 为 10 秒）。

**-w**
> 无限等待（将查询超时设为最大值）。

**-R** _retries_
> UDP 查询重试次数。

**-T**
> 使用 TCP 而非 UDP。

**-U**
> 强制使用 UDP，即使是 ANY 查询。

**-p** _port_
> 查询端口（默认：53）。

**-N** _ndots_
> 绝对名称查找所需的点号数量。

**-c** _class_
> 查询类别（IN、HS、CH；默认：IN）。

**-m** _flag_
> 内存调试（record、usage 或 trace）。

**-V**
> 打印版本号后退出。

# CAVEATS

不如 dig 详细。缓存可能影响结果。某些记录类型需要显式查询。名称服务器默认使用系统解析器。

# HISTORY

**host** 是 **BIND**（Berkeley Internet Name Domain）的一部分，最初于 **20 世纪 80 年代**在**加州大学伯克利分校**开发。相比 dig 和 nslookup，它提供了更简化的接口，面向需要快速 DNS 查找的用户。

# INSTALL

```apt: sudo apt install bind9-host```

```apk: sudo apk add bind-tools```

```nix: nix profile install nixpkgs#host```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dig](/man/dig)(1), [nslookup](/man/nslookup)(1), [drill](/man/drill)(1), [getent](/man/getent)(1)
