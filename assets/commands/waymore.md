# TAGLINE

从多个来源查找已归档的 URL

# TLDR

**查找某个域名的 URL**

```waymore -i [example.com]```

**只获取 URL**（跳过响应下载）

```waymore -i [example.com] -mode U```

**同时获取 URL 和已归档的响应**

```waymore -i [example.com] -mode B```

**将 URL 输出到指定文件**

```waymore -i [example.com] -oU [urls.txt]```

**排除子域名**

```waymore -i [example.com] -n```

运行前**检查预计耗时和请求数量**

```waymore -i [example.com] -co```

**限制每个来源的请求数**

```waymore -i [example.com] -lr [100]```

# SYNOPSIS

**waymore** [_-i domain_] [_-mode mode_] [_-oU file_] [_options_]

# PARAMETERS

**-i** _DOMAIN_
> 输入的域名或域名列表文件。

**-mode** _MODE_
> 模式：U（仅 URL）、R（仅响应）、B（两者）。默认：U。

**-n**, **--no-subs**
> 不包含目标域名的子域名。

**-oU** _FILE_
> 发现的 URL 的输出文件。

**-oR** _DIR_
> 下载响应的输出目录。

**-xcc**
> 排除 Common Crawl 结果。

**-xav**
> 排除 Alien Vault OTX 结果。

**-lr** _NUM_
> 限制每个来源的请求数（0 = 不限制）。

**-co**, **--check-only**
> 仅检查预计请求数和耗时，不实际运行。

**-ow**, **--output-overwrite**
> 覆盖输出文件而不是追加。

**-f** _REGEX_
> 用关键字正则表达式过滤 URL。

**-v**, **--verbose**
> 详细输出。

# DESCRIPTION

**waymore** 是一款侦察工具，通过查询多个网络存档来源来发现某个域名的 URL 和已归档的响应，这些来源包括 Wayback Machine、Common Crawl、Alien Vault OTX、URLScan、VirusTotal、GhostArchive 和 Intelligence X。相比只查询单一存档的工具，它的覆盖范围更广。

该工具有三种模式：URL 模式（U）从存档索引中提取目标域名的已知 URL；响应模式（R）检索实际归档的页面内容；both 模式（B）则两者兼顾。可以对结果进行过滤，排除特定来源或匹配关键字模式。

多线程处理加速大规模查询，输出可保存到文件以便进一步分析。该工具常用于安全研究和漏洞赏金项目，用于发现被遗忘的端点、旧的 API 路径和已被移除的内容。

# CAVEATS

受存档来源的速率限制。大型域名可能耗费大量时间；建议先用 -co 进行预估。需要 Python 3。通过 config.yml 配置 API 密钥和默认值。

# HISTORY

**waymore** 由 **xnl-h4ck3r** 创建，用于网络侦察，可在多个存档来源中搜索 URL。

# INSTALL

```nix: nix profile install nixpkgs#waymore```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[waybackurls](/man/waybackurls)(1), [gau](/man/gau)(1), [hakrawler](/man/hakrawler)(1)
