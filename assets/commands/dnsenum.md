# TAGLINE

DNS 枚举与侦察工具

# TLDR

为域名**枚举 DNS 信息**

```dnsenum [domain.com]```

**使用指定的 DNS** 服务器

```dnsenum --dnsserver [8.8.8.8] [domain.com]```

**结合暴力破解枚举**

```dnsenum --enum -f [wordlist.txt] [domain.com]```

**将输出保存到文件**

```dnsenum -o [output.xml] [domain.com]```

为暴力破解**指定线程数**

```dnsenum --threads [10] [domain.com]```

**跳过反向**查询

```dnsenum --noreverse [domain.com]```

# SYNOPSIS

**dnsenum** [_options_] _domain_

# PARAMETERS

_DOMAIN_
> 要枚举的目标域名。

**--dnsserver** _SERVER_
> 要查询的 DNS 服务器。

**--enum**
> 快捷方式，等价于 --threads 5 -s 15 -w。

**-f** _FILE_
> 用于暴力破解的子域名字典文件。

**--threads** _N_
> 并行查询的线程数。

**-o** _FILE_
> 将输出以 XML（magictree）格式写入 FILE。

**--noreverse**
> 跳过反向查询。

**--private**
> 显示并保存私有（RFC 1918）IP 地址。

**-p** _N_, **--pages** _N_
> 要抓取的 Google 搜索结果页数（默认 5）。

**-s** _N_, **--scrap** _N_
> 从 Google 抓取的最大子域名数量。

**-r**, **--recursion**
> 对发现的子域名递归执行枚举。

**-w**, **--whois**
> 对 C 类网络段执行 whois 查询。

**--help**
> 显示帮助信息。

# DESCRIPTION

**dnsenum** 是一款 DNS 枚举工具，用于收集域名 DNS 基础设施的相关信息。它通过多次查询来发现主机、域名服务器、邮件服务器和潜在的子域名。

该工具会尝试区域传送、执行反向查询，并能使用字典对子域名进行暴力枚举。它还会抓取搜索引擎获取更多子域名信息，并整合多个来源的结果。

dnsenum 常用于渗透测试和安全评估中，以摸清一个组织的 DNS 足迹并发现潜在攻击面。

# CAVEATS

只能对获得授权的域名进行测试。配置正确的服务器通常会阻止区域传送。暴力枚举可能被检测并封锁。搜索抓取可能触发限速。

# HISTORY

dnsenum 是一款基于 Perl 的工具，由安全社区开发。它已成为 Kali Linux 等渗透测试发行版中的标准侦察工具，提供全面的 DNS 枚举能力。

# INSTALL

```dnf: sudo dnf install dnsenum```

```apk: sudo apk add dnsenum```

```nix: nix profile install nixpkgs#dnsenum```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dig](/man/dig)(1), [nslookup](/man/nslookup)(1), [fierce](/man/fierce)(1), [dnsrecon](/man/dnsrecon)(1)

# RESOURCES

```[Source code](https://github.com/fwaeytens/dnsenum)```

<!-- verified: 2026-07-11 -->
