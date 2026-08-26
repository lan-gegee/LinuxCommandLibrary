# TAGLINE

DNS 查询与故障排查工具

# TLDR

**查询** DNS

```dig [example.com]```

指定记录类型

```dig [example.com] [A]```

**简短**输出

```dig [example.com] +short```

**反向**查询

```dig -x [8.8.8.8]```

**查询**指定的域名服务器

```dig [@8.8.8.8] [example.com]```

# SYNOPSIS

**dig** [_@server_] [_name_] [_type_]

# DESCRIPTION

**dig**（Domain Information Groper）是一个 DNS 查询工具。它向 DNS 服务器查询各种记录类型，提供详细的响应，是 DNS 故障排查和分析的首选工具。

该命令已在很大程度上取代了 nslookup 等较旧的工具。

# PARAMETERS

**@**_server_
> 查询指定的 DNS 服务器

**+short**
> 简短输出（仅答案）

**+noall +answer**
> 只显示 answer 部分

**-x** _ip_
> 反向查询

**-t** _type_
> 记录类型（A、AAAA、MX、NS 等）

**+trace**
> 跟踪 DNS 委派路径

**+dnssec**
> 请求 DNSSEC 记录

**-4** / **-6**
> 仅使用 IPv4 / IPv6

# RECORD TYPES

**A**
> IPv4 地址

**AAAA**
> IPv6 地址

**MX**
> 邮件交换

**NS**
> 域名服务器

**TXT**
> 文本记录

**CNAME**
> 规范名称（别名）

**SOA**
> 权威起始记录

**PTR**
> 反向查询指针

**SRV**
> 服务定位

**ANY**
> 所有可用记录

# WORKFLOW

```bash
# Basic lookup (A record)
dig example.com

# Specific record type
dig example.com MX
dig example.com AAAA

# Short answer only
dig example.com +short

# Multiple queries
dig example.com A AAAA MX

# Query specific DNS server
dig @8.8.8.8 example.com
dig @1.1.1.1 example.com

# Reverse lookup
dig -x 8.8.8.8

# Trace delegation
dig example.com +trace

# Show only answer
dig example.com +noall +answer

# Query all records
dig example.com ANY
```

# DNS SERVERS

常用公共 DNS：
- **8.8.8.8** - Google DNS
- **1.1.1.1** - Cloudflare DNS
- **9.9.9.9** - Quad9

# ADVANCED QUERIES

```bash
# Check DNSSEC
dig example.com +dnssec

# Query specific port
dig -p 5353 example.com

# Batch file queries
dig -f domains.txt

# TCP instead of UDP
dig +tcp example.com

# Show query time
dig example.com +stats
```

# OUTPUT SECTIONS

**QUESTION** - 发送的查询
**ANSWER** - 响应记录
**AUTHORITY** - 权威域名服务器
**ADDITIONAL** - 附加信息

# CAVEATS

需要网络连接。默认使用系统 DNS。输出对新手较为复杂。部分 ISP 会劫持 DNS。DNSSEC 校验需要正确配置。大型查询可能超时。

# HISTORY

**dig** 由 USC 信息科学研究所的 **Steve Hotz** 于 **1989** 年开发，后来成为 BIND 的一部分以及标准的 DNS 调试工具。

# INSTALL

```apt: sudo apt install bind9-dnsutils```

```apk: sudo apk add bind-tools```

```nix: nix profile install nixpkgs#dig```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[host](/man/host)(1), [nslookup](/man/nslookup)(1), [drill](/man/drill)(1)
