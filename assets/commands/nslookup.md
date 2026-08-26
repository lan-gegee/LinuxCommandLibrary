# TAGLINE

向 DNS 服务器查询主机名和 IP 信息

# TLDR

**查询 IP 地址**

```nslookup [example.com]```

**使用指定 DNS 服务器查询**

```nslookup [example.com] [8.8.8.8]```

**反向 DNS 查询**

```nslookup [192.168.1.1]```

**查询特定记录类型**

```nslookup -type=[MX] [example.com]```

**查询所有记录**

```nslookup -type=[ANY] [example.com]```

**用 TCP 代替 UDP**

```nslookup -vc [example.com]```

**交互模式**

```nslookup```

**调试模式**

```nslookup -debug [example.com]```

# SYNOPSIS

**nslookup** [_options_] [_host_] [_server_]

# DESCRIPTION

**nslookup** 向 DNS 服务器查询主机名和 IP 信息。它可以执行正向和反向查询、查询特定记录类型，并诊断 DNS 问题。

该工具可在交互或非交互模式下运行，交互模式允许进行多次查询。

# PARAMETERS

**-type=**_type_
> 记录类型（A、AAAA、MX、NS、TXT、SOA、PTR、ANY、CNAME、SRV）。

**-query=**_type_
> -type 的别名。

**-class=**_class_
> DNS 类别（IN、CH、HS、ANY）。默认为 IN。

**-debug**
> 显示调试信息（完整响应数据包）。

**-port=**_port_
> DNS 服务器端口（默认 53）。

**-timeout=**_seconds_
> 查询超时时间。

**-retry=**_n_
> 放弃前的重试次数。

**-vc**
> 查询使用 TCP 而不是 UDP。

**-nosearch**
> 不将搜索列表附加到非限定域名。

**-norecurse**
> 不请求服务器进行递归解析。

**-version**
> 输出版本信息并退出。

# INTERACTIVE COMMANDS

**server** _name_：设置默认 DNS 服务器（用当前服务器解析它）
**lserver** _name_：使用初始服务器设置默认服务器
**set type=**_type_：设置查询类型
**set class=**_class_：设置查询类别
**set debug** / **set nodebug**：切换调试输出
**set all**：显示当前选项设置
**exit**：退出

# CAVEATS

已被弃用，建议改用 dig。行为因实现而异。交互模式与命令行方式有所不同。部分功能取决于具体实现。

# HISTORY

**nslookup** 由 UC Berkeley 的 **Andrew Cherenson** 编写，是 BIND 的一部分。虽然大多数系统仍包含它，但 BIND 文档建议 DNS 查询改用 dig，因为其行为更加一致。

# INSTALL

```apt: sudo apt install bind9-dnsutils```

```apk: sudo apk add bind-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dig](/man/dig)(1), [host](/man/host)(1), [drill](/man/drill)(1), [getent](/man/getent)(1)
