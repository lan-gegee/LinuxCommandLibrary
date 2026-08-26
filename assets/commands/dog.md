# TAGLINE

带彩色输出的命令行 DNS 客户端

# TLDR

**查询 A 记录**

```dog [example.com]```

**查询指定记录**类型

```dog [example.com] [MX]```

**使用指定的 DNS** 服务器

```dog [example.com] @[8.8.8.8]```

**查询多种记录**类型

```dog [example.com] A AAAA MX```

**以 JSON 格式输出**

```dog [example.com] --json```

**使用 DNS over** HTTPS

```dog [example.com] --https @[https://cloudflare-dns.com/dns-query]```

**使用 DNS over** TLS

```dog [example.com] --tls @[1.1.1.1]```

**只打印第一个结果**（适合脚本使用）

```dog [example.com] --short```

# SYNOPSIS

**dog** [_options_] [_domain_] [_type_...] [@_server_]

参数与顺序无关：dog 根据名称识别记录类型，根据前导 **@** 识别域名服务器，其余一律视为域名。

# PARAMETERS

**-q**, **--query**=_HOST_
> 要查询的主机名或域名（也可以按位置给出）。

**-t**, **--type**=_TYPE_
> 要查询的记录类型：A、AAAA、CAA、CNAME、HINFO、MX、NS、PTR、SOA、SRV、TXT。可重复使用。

**-n**, **--nameserver**=_ADDR_
> 接收查询的域名服务器地址（也可以用 @_ADDR_ 的形式给出）。

**--class**=_CLASS_
> 查询的网络类别：IN（默认）、CH 或 HS。

**-U**, **--udp**
> 通过普通 UDP 发送查询（默认方式）。

**-T**, **--tcp**
> 通过 TCP 发送查询。

**-S**, **--tls**
> 使用 DNS-over-TLS 发送查询。

**-H**, **--https**
> 使用 DNS-over-HTTPS 发送查询。

**--edns**=_SETTING_
> 控制 EDNS：**disable**、**hide** 或 **show**。

**--txid**=_NUMBER_
> 使用指定的事务 ID 而不是随机值。

**-Z**=_TWEAKS_
> 少见的协议级微调选项，如 **aa**、**ad**、**cd** 或 **bufsize=**_N_。

**-1**, **--short**
> 只显示第一个结果，不输出其他内容。

**-J**, **--json**
> 以 JSON 格式打印响应。

**--color**, **--colour**=_WHEN_
> 何时对输出着色：**always**、**automatic** 或 **never**。

**--seconds**
> 以秒而不是人类可读的时间单位打印时长。

**--time**
> 打印响应到达所耗费的时间。

**--help**
> 显示帮助信息。

**-v**, **--version**
> 显示版本信息。

# DESCRIPTION

**dog** 是一个带彩色输出的命令行 DNS 客户端，具备现代特性。它是 dig 的替代品，拥有更友好的界面，并支持加密 DNS 协议。

该工具支持 DNS over HTTPS（DoH）和 DNS over TLS（DoT），可进行安全的 DNS 查询。输出默认着色以提升可读性，同时提供 JSON 输出供脚本使用。

相比 dig，dog 提供了更简化的界面，同时保留了高级用户所需的功能。可以同时查询多种记录类型，响应的格式也十分清晰。

# CAVEATS

上游开发自 **2021 年**起已陷入停滞，项目主页（dns.lookup.dog）也已下线，因此发行版软件包可能落后于代码仓库。当输出目标不是终端时会自动禁用彩色显示，但在脚本中若要确保如此，可显式传入 **--color=never**。DoH 与 DoT 要求解析器支持相应协议。dog 并未覆盖 dig 的每一个角落：没有区域传送（AXFR）、没有批量 `-f` 文件模式，也没有等价于 `+trace` 的功能。

# HISTORY

dog 由 **Benjamin Sago**（ogham）创建，他也是 `exa` 文件列表工具的作者。dog 于 **2020 年**首次发布，采用 Rust 编写，定位为比 dig 更友好的替代品，具备彩色输出、参数顺序无关以及内置加密 DNS 传输支持等特性。它还启发了 **doggo**——基于 Go 的同理念重实现，目前维护得更为活跃。

# INSTALL

```pacman: sudo pacman -S dog```

```apk: sudo apk add dog```

```zypper: sudo zypper install dog```

```nix: nix profile install nixpkgs#dog```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dig](/man/dig)(1), [doggo](/man/doggo)(1), [drill](/man/drill)(1), [nslookup](/man/nslookup)(1)

# RESOURCES

```[Source code](https://github.com/ogham/dog)```

<!-- verified: 2026-07-14 -->
