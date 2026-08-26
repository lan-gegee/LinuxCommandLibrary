# TAGLINE

DNS 侦察与子域名发现工具

# TLDR

**对域名进行 DNS 侦察**

```fierce --domain [example.com]```

**使用自定义 DNS**服务器

```fierce --domain [example.com] --dns-servers [8.8.8.8]```

**使用字典搜索**

```fierce --domain [example.com] --subdomain-file [wordlist.txt]```

**扩大搜索范围**

```fierce --domain [example.com] --wide```

**输出到文件**

```fierce --domain [example.com] > [output.txt]```

# SYNOPSIS

**fierce** [_options_]

# PARAMETERS

**--domain** _DOMAIN_
> 要扫描的目标域名。

**--dns-servers** _SERVERS_
> 自定义 DNS 服务器。

**--subdomain-file** _FILE_
> 用于子域名暴力破解的字典文件。

**--wide**
> 扫描已发现主机所在的整个 C 类网段。

**--traverse** _N_
> 扫描相邻的 IP。

**--delay** _SEC_
> 查询之间的延迟。

**--help**
> 显示帮助信息。

# DESCRIPTION

**fierce** 是一款 DNS 侦察工具，用于定位目标的非连续 IP 空间和主机名。它可以执行区域传送、子域名暴力破解以及相邻 IP 探测。

该工具会首先尝试 DNS 区域传送，失败后回退到基于字典的子域名枚举。发现主机后，它还会扫描附近的 IP 地址，以找出更多系统。

fierce 常用于渗透测试中的初始目标枚举和攻击面测绘。

# CAVEATS

只能对已授权的目标使用。配置得当的服务器通常会让区域传送失败。DNS 查询可能被日志记录。

# HISTORY

fierce 由 **RSnake**（Robert Hansen）创建，是一款面向渗透测试人员的 DNS 侦察工具。Python 3 重写版对原来的 Perl 脚本做了现代化改造，以融入当前的安全工作流程。

# INSTALL

```brew: brew install fierce```

```nix: nix profile install nixpkgs#fierce```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dig](/man/dig)(1), [nmap](/man/nmap)(1), [dnsenum](/man/dnsenum)(1)

# RESOURCES

```[Source code](https://github.com/mschwager/fierce)```

<!-- verified: 2026-07-15 -->
