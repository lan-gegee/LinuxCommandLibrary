# TAGLINE

用于收集 URL 和 JavaScript 文件引用的快速网络爬虫

# TLDR

**爬取单个 URL**

```echo "[https://example.com]" | hakrawler```

**按指定深度爬取**

```echo "[https://example.com]" | hakrawler -d [3]```

**将子域名纳入范围**

```echo "[https://example.com]" | hakrawler -s subs```

**使用纯文本输出**

```echo "[https://example.com]" | hakrawler -plain```

**使用自定义超时并禁用重定向**

```echo "[https://example.com]" | hakrawler -t [15] -dr```

# SYNOPSIS

**hakrawler** [_options_]

# PARAMETERS

**-d** _depth_
> 爬取深度（默认为 1）。

**-s** _scope_
> 爬取范围：strict（仅同域名）、subs（包含子域名）或 fuzzy（全部）。默认为 strict。

**-plain**
> 纯文本输出模式，只打印 URL。

**-t** _seconds_
> 请求超时时间，单位为秒（默认为 10）。

**-w** _workers_
> 并发 worker 数量（默认为 8）。

**-insecure**
> 跳过 TLS 证书验证。

**-dr**
> 禁用跟随重定向。

**-h**
> 显示帮助信息。

# DESCRIPTION

**hakrawler** 是一款用于收集 URL 和 JavaScript 文件引用的快速网络爬虫。它专为 Web 应用安全测试中的信息收集而设计。

该工具从标准输入读取 URL 并输出发现的链接，便于在安全测试管道中与其他工具串联使用。

# USAGE EXAMPLES

```bash
# Basic crawl
echo "https://target.com" | hakrawler

# Crawl with plain output for piping
cat urls.txt | hakrawler -plain | sort -u

# Deep crawl including subdomains
echo "https://target.com" | hakrawler -d 3 -s subs -plain
```

# CAVEATS

仅限用于已授权的安全测试。可能触发安全控制机制。过高的并发数可能导致速率限制或 IP 封禁。

# HISTORY

hakrawler 由 **Luke Stephens**（hakluke）创建，是其安全工具套件的一部分。它面向进行 Web 侦察的漏洞赏金猎人和渗透测试人员。

# INSTALL

```nix: nix profile install nixpkgs#hakrawler```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[waybackurls](/man/waybackurls)(1), [gau](/man/gau)(1), [curl](/man/curl)(1)
