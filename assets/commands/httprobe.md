# TAGLINE

从标准输入读取域名列表，探测可用的 HTTP 和 HTTPS 服务器

# TLDR

**从标准输入探测域名**

```cat [subdomains.txt] | httprobe```

**以并发方式探测**

```cat [subdomains.txt] | httprobe -c [50]```

**探测指定的端口**

```cat [subdomains.txt] | httprobe -p [http:8080] -p [https:8443]```

**跳过默认端口**

```cat [subdomains.txt] | httprobe -s```

**设置超时时间**

```cat [subdomains.txt] | httprobe -t [5000]```

**优先使用 HTTPS**

```cat [subdomains.txt] | httprobe --prefer-https```

# SYNOPSIS

**httprobe** [_options_]

# PARAMETERS

**-c** _n_
> 并发级别（默认 20）。

**-p** _proto:port_
> 添加要探测的端口（例如 http:8080）。

**-s**
> 跳过默认端口（80、443）。

**-t** _ms_
> 超时时间（毫秒）（默认 10000）。

**--prefer-https**
> 当两者都可用时只输出 HTTPS。

# DESCRIPTION

**httprobe** 从标准输入读取域名列表，并探测其中可用的 HTTP 和 HTTPS 服务器。它会输出能响应请求的域名对应的 URL。常见于漏洞赏金工作流：在完成子域名枚举后、进一步测试前，用它筛选出存活的 Web 服务器。

# CAVEATS

使用 Go 编写，后续维护很少；ProjectDiscovery 的 **httpx** 是维护更活跃的替代品，具备更多探测与指纹识别功能。

# HISTORY

**httprobe** 由 **Tom Hudson**（"tomnomnom"）编写。他是一位安全研究员，以一系列小巧、可组合的 Go 工具著称（包括 **anew**、**waybackurls** 和 **gf**），这些工具在漏洞赏金和信息收集流水线中被广泛使用。

# INSTALL

```dnf: sudo dnf install httprobe```

```nix: nix profile install nixpkgs#httprobe```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[httpx](/man/httpx)(1), [curl](/man/curl)(1), [subfinder](/man/subfinder)(1)

# RESOURCES

```[Source code](https://github.com/tomnomnom/httprobe)```

<!-- verified: 2026-07-19 -->
