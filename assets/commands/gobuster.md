# TAGLINE

目录与 DNS 爆破工具

# TLDR

**目录爆破**

```gobuster dir -u [https://example.com] -w [wordlist.txt]```

**DNS 子域枚举**

```gobuster dns -d [example.com] -w [subdomains.txt]```

**虚拟主机发现**

```gobuster vhost -u [https://example.com] -w [wordlist.txt]```

**指定文件扩展名**

```gobuster dir -u [https://example.com] -w [wordlist.txt] -x [php,html,txt]```

**指定自定义线程数**

```gobuster dir -u [https://example.com] -w [wordlist.txt] -t [50]```

**跟随重定向**

```gobuster dir -u [https://example.com] -w [wordlist.txt] -r```

# SYNOPSIS

**gobuster** _mode_ [_options_]

# PARAMETERS

**dir**
> 目录/文件爆破模式。

**dns**
> DNS 子域枚举模式。

**vhost**
> 虚拟主机发现模式。

**fuzz**
> 通用模糊测试模式，在 URL、请求头或请求体中使用 **FUZZ** 关键字占位符。

**s3**
> 枚举开放的 Amazon S3 存储桶。

**gcs**
> 枚举开放的 Google Cloud Storage 存储桶。

**tftp**
> 枚举 TFTP 服务器上的文件。

**-u** _url_
> 目标 URL。

**-w** _file_
> 字典文件。

**-t** _n_
> 线程数。

**-x** _extensions_
> 要搜索的文件扩展名。

**-r**
> 跟随重定向。

**-k**
> 跳过 TLS 证书验证。

**-o** _file_
> 输出文件。

**-s** _codes_
> 视为有效的状态码。

**-b** _codes_
> 要加入黑名单的状态码。

# DESCRIPTION

**gobuster** 是一个用 Go 编写的高速目录与 DNS 爆破工具。它通过基于字典的枚举来发现隐藏的目录、文件和子域。

该工具专为 Web 应用安全测试设计，帮助识别可能暴露漏洞或敏感信息的隐藏内容。它支持多种模式，包括目录枚举、DNS 子域爆破和虚拟主机发现。

# CAVEATS

仅限授权的安全测试使用。可能触发 WAF 规则。大字典在远程主机上速度较慢。请遵守速率限制。

# HISTORY

**gobuster** 由 **OJ Reeves** 创建，作为 DirBuster 等工具的高速替代品。它采用 Go 编写以获得并发能力和性能，如今已成为渗透测试和漏洞赏金挖掘中的标准工具。

# INSTALL

```apt: sudo apt install gobuster```

```dnf: sudo dnf install gobuster```

```pacman: sudo pacman -S gobuster```

```brew: brew install gobuster```

```nix: nix profile install nixpkgs#gobuster```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dirb](/man/dirb)(1), [ffuf](/man/ffuf)(1), [wfuzz](/man/wfuzz)(1), [feroxbuster](/man/feroxbuster)(1)

# RESOURCES

```[Source code](https://github.com/OJ/gobuster)```

<!-- verified: 2026-07-17 -->
