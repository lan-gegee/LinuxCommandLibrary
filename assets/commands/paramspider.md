# TAGLINE

通过挖掘网络归档发现 URL 参数

# TLDR

**查找域名的参数**

```paramspider -d [example.com]```

**排除指定的文件扩展名**

```paramspider -d [example.com] --exclude [woff,css,js,png,jpg]```

**为参数值使用自定义占位符**

```paramspider -d [example.com] -p "[FUZZ]"```

**设置输出目录**

```paramspider -d [example.com] -o [results/]```

**从文件批量爬取多个域名**

```paramspider -l [domains.txt]```

# SYNOPSIS

**paramspider** -d _domain_ [_options_]

# PARAMETERS

**-d**, **--domain** _domain_
> 目标域名。

**-l**, **--list** _file_
> 包含域名列表的文件。

**-o**, **--output** _dir_
> 输出目录（默认为 ./results）。

**--exclude** _exts_
> 排除具有特定扩展名的 URL（逗号分隔）。

**-p**, **--placeholder** _str_
> 参数值的占位符（默认为 FUZZ）。

**--level** _level_
> 查找嵌套参数（例如 high）。

**-q**, **--quiet**
> 安静模式，不在屏幕上输出 URL。

**-s**, **--subs**
> 包含子域名。

# DESCRIPTION

**paramspider** 通过挖掘网络归档来发现 URL 参数。它会查询 archive.org 的 Wayback Machine，找出目标域名历史上带有参数的 URL。

在安全测试过程中，可用于发现隐藏参数、端点和潜在注入点。

# OUTPUT FORMAT

```
https://example.com/page?id=FUZZ
https://example.com/search?q=FUZZ&page=FUZZ
```

# CAVEATS

需要联网。结果来自已存档的 URL。可能会找到过时的参数。请负责任地使用。

# HISTORY

ParamSpider 由 **Devansh Batham** 开发，是一款供漏洞赏金猎人和渗透测试人员发现参数的工具。

# SEE ALSO

[waybackurls](/man/waybackurls)(1), [gau](/man/gau)(1), [arjun](/man/arjun)(1)
