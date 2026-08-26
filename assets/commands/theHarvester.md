# TAGLINE

OSINT 邮箱与子域名收集工具

# TLDR

使用全部数据源**搜索域名的邮箱和子域名**

```theHarvester -d [example.com] -b all```

**使用特定数据源搜索**

```theHarvester -d [example.com] -b [google]```

**限制结果数量**

```theHarvester -d [example.com] -b google -l [100]```

**将结果保存到文件**

```theHarvester -d [example.com] -b all -f [report]```

对发现的主机**执行 DNS 解析**

```theHarvester -d [example.com] -b all --dns-lookup```

对发现的网页**截图**

```theHarvester -d [example.com] -b all --screenshot [path/to/output]```

**检查子域名接管**漏洞

```theHarvester -d [example.com] -b all --take-over```

# SYNOPSIS

**theHarvester** **-d** _domain_ **-b** _source_ [_options_]

# PARAMETERS

**-d** _domain_
> 要搜索的目标域名（必需）。

**-b** _source_
> 要使用的数据源：google、bing、yahoo、duckduckgo、github-code、linkedin、shodan、virustotal、certspotter、crtsh、dnsdumpster、hunter、securityTrails、**all** 等。

**-l** _limit_
> 限制搜索结果的数量。

**-f** _filename_
> 保存结果的输出文件名（HTML/XML 格式）。

**-S** _start_
> 搜索分页的起始结果编号。

**-e** _server_
> 使用指定的 DNS 服务器进行解析。

**-p**
> 通过代理服务器路由请求。

**-s**
> 使用 Shodan 查询发现的主机。

**-c**
> 通过 HTTP/HTTPS 验证发现的主机。

**-n**
> 启用 DNS 服务器查询。

**-r** [_file_]
> 对发现的地址段执行反向 DNS 解析。

**-w** _wordlist_
> 使用字典进行 DNS 爆破以发现子域名。

**--take-over**
> 检查可能存在的子域名接管漏洞。

**--screenshot** _path_
> 对发现的网页截图。

**-v**
> 显示版本信息。

# DESCRIPTION

**theHarvester** 是一款开源情报（OSINT）工具，用于渗透测试和红队评估中的侦察阶段。它收集目标域名的公开可用信息，包括电子邮箱地址、子域名、主机名、员工姓名和开放端口。

该工具会查询多种数据源，包括搜索引擎、证书数据库、DNS 数据库以及安全类服务。结果可以保存下来供进一步分析。许多高级数据源需要在 theHarvester 安装目录下的 **api-keys.yaml** 文件中配置 API 密钥。

# CAVEATS

许多数据源需要有效的 API 密钥（Shodan、Hunter.io、Censys、SecurityTrails 等）才能完整使用。没有正确的 API 密钥时，搜索返回的结果会很少甚至为空。频繁查询某些数据源时可能受到速率限制。

# HISTORY

theHarvester 由 **Christian Martorella**（laramies）创建，最初发布于约 **2007 年**。它已成为 **Kali Linux** 等渗透测试发行版中的标准侦察工具。该工具持续活跃维护，多年来已更新以支持 Python 3.12+ 和众多新数据源。

# SEE ALSO

[nmap](/man/nmap)(1), [subfinder](/man/subfinder)(1), [amass](/man/amass)(1), [recon-ng](/man/recon-ng)(1)
