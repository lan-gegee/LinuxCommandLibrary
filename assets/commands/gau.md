# TAGLINE

从多个归档来源抓取 URL

# TLDR

**抓取域名的** URL

```gau [example.com]```

**输出到文件**

```gau [example.com] -o [urls.txt]```

**指定数据源抓取**

```gau --providers [wayback,otx] [example.com]```

**包含子域名**

```gau --subs [example.com]```

**按日期过滤**

```gau --from [202201] --to [202212] [example.com]```

# SYNOPSIS

**gau** [_options_] _domains_...

# PARAMETERS

_DOMAINS_
> 要抓取 URL 的目标域名。

**-o** _FILE_, **--o** _FILE_
> 输出文件。

**--providers** _LIST_
> URL 来源：wayback、otx、commoncrawl。

**--subs**
> 包含子域名。

**--from** _DATE_
> 起始日期（YYYYMM）。

**--to** _DATE_
> 结束日期（YYYYMM）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gau**（Get All URLs）从 Wayback Machine、Common Crawl 和 AlienVault OTX 等多个来源抓取域名的已知 URL。它被用于侦察和安全研究。

该工具汇总历史 URL，这些 URL 可能暴露隐藏的端点、参数或旧漏洞。结果包括存档页面、API 端点和文件路径。

gau 通过找出曾经公开可访问的 URL，帮助发现攻击面。

# CAVEATS

结果包含已失效的历史 URL。输出可能非常庞大。受各数据源速率限制约束。

# HISTORY

gau 为安全研究和漏洞赏金挖掘而创建，让侦察工作可以方便地访问存档 URL 数据库。

# INSTALL

```brew: brew install gau```

```nix: nix profile install nixpkgs#gau```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[waybackurls](/man/waybackurls)(1), [hakrawler](/man/hakrawler)(1)
