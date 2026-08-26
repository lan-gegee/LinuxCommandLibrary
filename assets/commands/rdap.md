# TAGLINE

查询域名和 IP 注册数据

# TLDR

**查询域名**

```rdap [example.com]```

**查询 IP 地址**

```rdap [192.0.2.1]```

**查询 ASN**

```rdap [AS15169]```

**JSON 输出**

```rdap -j [example.com]```

**WHOIS 风格输出**

```rdap -w [example.com]```

**详细输出**

```rdap -v [example.com]```

**使用指定的 RDAP 服务器**

```rdap -s [https://rdap.verisign.com/com/v1] [example.com]```

# SYNOPSIS

**rdap** [_options_] _query_

# PARAMETERS

**-j**, **--json**
> 以美化排版输出 JSON

**-r**, **--raw**
> 输出原始服务器响应

**-w**, **--whois**
> 输出 WHOIS 风格（仅限域名查询）

**-v**, **--verbose**
> 在 stderr 上打印详细消息

**-s**, **--server**=_URL_
> 使用指定的 RDAP 服务器

**-T**, **--timeout**=_SECS_
> 指定秒数后超时（默认：30）

**-k**, **--insecure**
> 禁用 SSL 证书校验

**--text**
> 输出纯文本树形格式（默认）

**-t**, **--type**=_TYPE_
> RDAP 查询类型（通常会自动检测）：domain、ip、autnum、entity、nameserver、url

# DESCRIPTION

**rdap** 向注册数据访问协议（RDAP）服务器查询域名、IP 和 ASN 注册信息。RDAP 是 WHOIS 的现代替代者，提供结构化数据并支持身份验证。

# EXAMPLES

```bash
# Domain lookup
rdap example.com

# IP address lookup
rdap 8.8.8.8

# ASN lookup
rdap AS15169

# JSON output
rdap -j google.com

# Specific server
rdap -s https://rdap.verisign.com/com/v1 example.com

# IPv6 address
rdap 2001:4860:4860::8888
```

# QUERY TYPES

查询类型通常会自动检测，但可以用 **--type** 指定：

```
domain     - Domain registration
ip         - IP address/network
autnum     - Autonomous System Number
entity     - Registrant entity
nameserver - Name server
url        - Direct RDAP URL
```

# CAVEATS

并非所有 TLD 都支持 RDAP。部分数据可能需要身份验证。它是 WHOIS 的继任者。

# HISTORY

RDAP 由 **IETF** 自 2012 年起开发，作为 WHOIS 协议的结构化、安全替代方案。

# INSTALL

```apt: sudo apt install rdap```

```zypper: sudo zypper install rdap```

```brew: brew install rdap```

```nix: nix profile install nixpkgs#rdap```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[whois](/man/whois)(1), [dig](/man/dig)(1), [host](/man/host)(1)
