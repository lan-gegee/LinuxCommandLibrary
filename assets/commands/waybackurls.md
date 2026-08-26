# TAGLINE

从 Wayback Machine 获取已归档的 URL

# TLDR

**获取某个域名的 URL**

```echo "[example.com]" | waybackurls```

**从多个域名获取**

```cat [domains.txt] | waybackurls```

**排除子域名**

```echo "[example.com]" | waybackurls -no-subs```

**在输出中包含日期**

```echo "[example.com]" | waybackurls -dates```

**以 JSON 格式输出**

```echo "[example.com]" | waybackurls -json```

**将去重后的 URL 保存到文件**

```echo "[example.com]" | waybackurls | sort -u > [urls.txt]```

**查找特定类型的文件**

```echo "[example.com]" | waybackurls | grep "\.js$"```

# SYNOPSIS

**waybackurls** [_options_]

# PARAMETERS

**-no-subs**
> 结果中不包含子域名。

**-dates**
> 在输出中包含归档日期。

**-json**
> 以 JSON 格式输出结果。

# DESCRIPTION

**waybackurls** 从 Wayback Machine（互联网档案馆）获取指定域名的所有已知 URL。它从标准输入读取域名，并将发现的 URL 输出到标准输出。

该工具查询 Wayback Machine 的 CDX API 来检索历史 URL 数据，其中包含可能已不存在的 URL，从而揭示网站过去的结构以及潜在的敏感端点。

常见用例包括安全评估期间的侦察、查找旧端点、发现 JavaScript 文件以及识别已被移除的内容。结果中经常能发现 API 端点、管理后台和被遗忘的页面。

通过 Go 安装：`go install github.com/tomnomnom/waybackurls@latest`

# CAVEATS

结果取决于 Wayback Machine 的归档覆盖范围。可能返回大量重复或相似的 URL。大量请求可能受到速率限制。URL 在现网站点上可能已无法访问。

# HISTORY

**waybackurls** 由 Tom Hudson（tomnomnom）创建，是其漏洞赏金工具集的一部分。它简化了对历史 URL 数据的访问，否则需要手动进行 CDX API 查询。该工具在安全侦察领域被广泛使用。

# INSTALL

```nix: nix profile install nixpkgs#waybackurls```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gau](/man/gau)(1), [hakrawler](/man/hakrawler)(1), [subfinder](/man/subfinder)(1), [httpx](/man/httpx)(1)
