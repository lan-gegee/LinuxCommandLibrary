# TAGLINE

支持加密协议的现代 DNS 客户端

# TLDR

使用系统解析器查询 **A 记录**

```doggo [example.com]```

向选定的解析器查询**特定记录类型**

```doggo [example.com] [MX] @[9.9.9.9]```

使用 **DNS over HTTPS**

```doggo [example.com] @https://[cloudflare-dns.com/dns-query]```

使用 **DNS over TLS**

```doggo [example.com] @tls://[1.1.1.1]```

一次查询**所有常见记录类型**

```doggo [example.com] --any```

输出 **JSON** 以便脚本处理

```doggo [example.com] --json```

对 IP 地址进行**反向查询**，简短输出

```doggo --reverse [8.8.8.8] --short```

通过 Globalping 网络**从其他国家**发起查询

```doggo [example.com] --gp-from [Germany] --gp-limit [2]```

# SYNOPSIS

**doggo** [_query options_] [_arguments_...]

参数可以自由书写：无论顺序如何，doggo 都能识别主机名、记录类型、网络类别以及 **@**_resolver_。

# PARAMETERS

**-q**, **--query**=_HOSTNAME_
> 要查询 DNS 记录的主机名。

**-t**, **--type**=_TYPE_
> DNS 记录类型（A、AAAA、MX、NS、TXT 等）。

**-n**, **--nameserver**=_ADDR_
> 用于接收查询的特定域名服务器地址。

**-c**, **--class**=_CLASS_
> DNS 记录的网络类别（IN、CH、HS）。

**-x**, **--reverse**
> 对 IPv4 或 IPv6 地址进行反向查询；自动设置类型为 PTR、类别为 IN。

**--any**
> 查询所有支持的记录类型（A、AAAA、CNAME、MX、NS、PTR、SOA、SRV、TXT、CAA）。

**-A**, **--authoritative**
> 通过域名的 SOA 记录找到其区域，并向委派的权威域名服务器发起查询。

**--strategy**=_STRATEGY_
> 如何在多个域名服务器之间选择：**all**、**random**、**first** 或 **internal**。

**--ndots**=_INT_
> ndots 值；系统域名服务器场景下取自 `/etc/resolv.conf`，否则为 1。

**--search**
> 使用 `resolv.conf` 中的搜索列表（默认开启；**--search=false** 可禁用）。

**--timeout**=_DURATION_
> 解析超时时间，如 `5s`、`400ms`、`1m`。

**-4**, **--ipv4** / **-6**, **--ipv6**
> 将查询限制为仅 IPv4 或仅 IPv6。

**--tls-hostname**=_HOSTNAME_
> 当 DoT 域名服务器以 IP 形式给出时，用于证书校验的主机名。

**--skip-hostname-verification**
> 跳过 DoT 查询的 TLS 主机名校验。

**--aa**, **--ad**, **--cd**, **--rd**, **--do**, **--z**
> 设置 AA（权威应答）、AD（已认证数据）、CD（禁用检查）、RD（期望递归，默认开启）、DO（DNSSEC OK）以及 Z 头部标志位。

**--nsid**, **--cookie**, **--padding**, **--ede**
> EDNS 选项：请求名称服务器标识符（NSID）、DNS Cookie、EDNS 填充或扩展 DNS 错误（EDE）。

**--ecs**=_SUBNET_
> 发送 EDNS Client Subnet，例如 `192.0.2.0/24`，以获得感知地理位置的响应。

**--bufsize**=_BYTES_
> EDNS UDP 缓冲区大小（512-65535）；设置后即启用 EDNS。EDNS 开启时默认为 1232。

**-J**, **--json**
> 以 JSON 格式输出。

**--short**
> 简短输出：仅显示响应部分。

**--color**
> 彩色输出（默认开启；**--color=false** 可禁用）。

**--time**
> 显示服务器响应所耗费的时间。

**--debug**
> 启用调试日志。

**--gp-from**=_LOCATION_, **--gp-limit**=_INT_
> 从指定位置的 Globalping 探针发起查询，并可限制探针数量。

**completions** [_bash_|_zsh_|_fish_]
> 打印给定 Shell 的补全脚本。

# TRANSPORT

通过 **@** 后面的 URL 风格 scheme 选择解析器。未给出 scheme 时使用普通 UDP。

**@udp://1.1.1.1**
> 发往 53 端口的 UDP 查询（默认方式）。

**@tcp://1.1.1.1**
> 发往 53 端口的 TCP 查询。

**@tls://1.1.1.1**
> 发往 853 端口的 DNS over TLS（DoT）。

**@https://cloudflare-dns.com/dns-query**
> DNS over HTTPS（DoH）。

**@quic://**
> DNS over QUIC（DoQ）。

**@sdns://**
> 通过 DNS stamp 使用 DNSCrypt 或 DoH。

# DESCRIPTION

**doggo** 是一个用 Go 编写的命令行 DNS 客户端，定位为更友好的 `dig`。它默认打印表格化的彩色结果，也可以输出 JSON 供脚本使用。

除普通 UDP 和 TCP 外，它还支持现代加密传输协议：DNS over HTTPS、DNS over TLS、DNS over QUIC 以及 DNSCrypt。只需给解析器加上 URL scheme 前缀即可完成选择，这让所有协议共用一套无需选项的语法。

doggo 会读取 `/etc/resolv.conf` 获取系统域名服务器、ndots 值和搜索列表，因此裸主机名的解析行为与其他程序一致。头部标志位、EDNS 选项和 DNSSEC 都可以在命令行上切换，而 **--gp-from** 可以让同一条查询从世界各地的 Globalping 探针发出，用来比较不同地区的解析结果。

# CAVEATS

加密传输协议只在解析器支持时才可用。**--short** 会隐藏 question、authority 和 additional 部分，虽然方便，但调试时经常需要的信息也会被丢掉。彩色输出默认开启，因此在使用 **--json** 以外的方式解析输出时应传入 **--color=false**。Globalping 查询由第三方服务执行，而非从你自己的机器发出。

# HISTORY

doggo 由 **Karan Sharma** 创建，于 **2020 年**首次发布。它的灵感来自 Rust 编写的 DNS 客户端 **dog**，但改用 Go 编写，因此以单个静态二进制文件的形式发布。此后它在灵感来源的基础上发展出更多功能：DNSCrypt、DNS over QUIC、Globalping 集成以及一个 Web 前端，而且与 dog 不同，它至今仍在积极维护。

# INSTALL

```pacman: sudo pacman -S doggo```

```apk: sudo apk add doggo```

```zypper: sudo zypper install doggo```

```brew: brew install doggo```

```nix: nix profile install nixpkgs#doggo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dig](/man/dig)(1), [dog](/man/dog)(1), [drill](/man/drill)(1), [nslookup](/man/nslookup)(1), [host](/man/host)(1)

# RESOURCES

```[Source code](https://github.com/mr-karan/doggo)```

```[Homepage](https://doggo.mrkaran.dev)```

```[Documentation](https://doggo.mrkaran.dev/docs/)```

<!-- verified: 2026-07-14 -->
