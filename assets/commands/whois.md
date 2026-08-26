# TAGLINE

查询域名和 IP 注册信息

# TLDR

**查询域名注册信息**

```whois [example.com]```

**查询 IP 地址信息**

```whois [8.8.8.8]```

**查询指定的 WHOIS 服务器**

```whois -h [whois.verisign-grs.com] [example.com]```

**查询 AS 编号**

```whois [AS15169]```

**禁用递归查询**

```whois -r [example.com]```

# SYNOPSIS

**whois** [_options_] _object_

# PARAMETERS

**-h** _host_, **--host** _host_
> 查询指定的 WHOIS 服务器，而不是根据对象猜测。

**-p** _port_, **--port** _port_
> 连接到给定的 TCP 端口（默认：43）。

**-H**
> 隐藏某些注册机构显示的法律免责声明。

**-r**
> 禁用对联系信息的递归查询（RIPE 风格的服务器）。

**-I**
> 先查询 whois.iana.org，然后跟随其转介。

**-a**
> 同时搜索所有镜像数据库（RIPE）。

**-T** _type_
> 将搜索限制为给定类型的对象（如 _inetnum_、_person_）。

**-B**
> 禁用对象过滤；在结果中包含电子邮件地址。

**-R**
> 不跟随转介；显示本地副本中的对象。

**--verbose**
> 详细输出；显示正在查询哪台服务器。

# DESCRIPTION

**whois** 查询数据库以获取域名注册信息、IP 地址分配和自治系统（AS）编号。它提供域名所有者、注册日期、域名服务器和联系信息等详情。

对于域名，whois 会根据 TLD 联系相应的注册机构来获取注册数据。对于 IP 地址，它会查询区域互联网注册机构（ARIN、RIPE、APNIC 等）。

返回的数据包括注册人信息（通常受隐私保护）、注册和到期日期、域名服务器以及注册商详情。

不同注册机构的数据格式和详细程度各不相同。一些域名使用隐私服务来隐藏实际的注册人信息。

# CAVEATS

如今许多域名注册都使用隐私保护服务，显示的是代理信息而非实际注册人详情。

可能存在速率限制。过多的查询可能导致被 WHOIS 服务器临时封锁。

各注册机构之间的数据格式差异很大。以编程方式解析 WHOIS 输出相当困难。

RDAP（注册数据访问协议）正以其结构化、标准化的格式逐渐取代 WHOIS。

# INSTALL

```apt: sudo apt install whois```

```dnf: sudo dnf install whois```

```pacman: sudo pacman -S whois```

```apk: sudo apk add whois```

```zypper: sudo zypper install whois```

```brew: brew install whois```

```nix: nix profile install nixpkgs#whois```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dig](/man/dig)(1), [host](/man/host)(1), [nslookup](/man/nslookup)(1), [rdap](/man/rdap)(1)
