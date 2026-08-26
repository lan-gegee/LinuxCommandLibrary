# TAGLINE

用于内容发现的 Web 路径暴力破解扫描器

# TLDR

**使用默认词典扫描** URL

```dirsearch -u [https://example.com]```

**使用自定义词典**

```dirsearch -u [https://example.com] -w [path/to/wordlist.txt]```

**指定扩展名扫描**

```dirsearch -u [https://example.com] -e [php,html,js]```

从文件**扫描多个 URL**

```dirsearch -l [urls.txt]```

**设置线程数**

```dirsearch -u [https://example.com] -t [50]```

**将结果输出到文件**

```dirsearch -u [https://example.com] -o [results.txt]```

**排除特定状态码**

```dirsearch -u [https://example.com] -x [403,404,500]```

以**递归方式**进行目录发现扫描

```dirsearch -u [https://example.com] -r```

# SYNOPSIS

**dirsearch** [_-u url_] [_-l urllist_] [_-w wordlist_] [_-e extensions_] [_-t threads_] [_-o output_] [_options_]

# PARAMETERS

**-u**, **--url** _url_
> 要扫描的目标 URL。

**-l**, **--urls-file** _file_
> 包含待扫描 URL 列表的文件。

**-w**, **--wordlist** _file_
> 要使用的自定义词典（可逗号分隔多个）。

**-e**, **--extensions** _ext_
> 要附加的扩展名（逗号分隔，如 php,asp,js）。

**-t**, **--threads** _n_
> 并发线程数（默认：25）。

**-r**, **--recursive**
> 启用递归扫描。

**-R**, **--max-recursion-depth** _n_
> 最大递归深度。

**-x**, **--exclude-status** _codes_
> 从结果中排除这些状态码。

**-i**, **--include-status** _codes_
> 仅包含这些状态码。

**-o**, **--output** _file_
> 将结果保存到文件。

**--format** _type_
> 输出格式：plain、simple、json、xml、md、csv、html。

**-H**, **--header** _header_
> 自定义头部（可多次使用）。

**--cookie** _cookie_
> 为请求设置 cookie。

**--user-agent** _ua_
> 自定义 User-Agent 字符串。

**--random-agent**
> 使用随机的 User-Agent。

**-b**, **--follow-redirects**
> 跟随 HTTP 重定向。

**--timeout** _seconds_
> 连接超时时间。

**--proxy** _url_
> 使用 HTTP/SOCKS 代理。

**-q**, **--quiet**
> 安静模式（最少输出）。

# DESCRIPTION

**dirsearch** 是一个 Web 内容发现工具，对 Web 服务器上的目录和文件进行暴力破解。它针对词典中的路径发送 HTTP 请求，通过分析服务器响应来识别存在的资源。

该工具常用于渗透测试和安全评估，发现隐藏内容、备份文件、管理后台、配置文件以及其他未从主应用链接的资源。它使用响应状态码、内容长度等启发式方法判断有效性。

Dirsearch 内置了词典，也支持自定义列表进行针对性扫描。可以指定扩展名来测试多种文件类型（例如同时检查 /admin 和 /admin.php）。递归模式会继续扫描已发现的目录。

高级功能包括代理支持、自定义头部、认证、限速和多种输出格式。工具可按状态码、响应大小或内容模式过滤结果，以减少误报。

# CAVEATS

仅可用于获得测试授权的系统。高线程数可能触发限速或被封禁。某些 WAF 可能拦截 dirsearch 的默认模式。大型词典会显著增加扫描时间。在大网站上递归扫描可能非常缓慢。

# HISTORY

**dirsearch** 由 Mauro Soria 创建，作为 DirBuster 和 gobuster 等工具的 Python 替代品。自 **2014** 年以来一直积极维护，在安全社区中被广泛使用。凭借易用性和全面的功能，它在 Web 应用安全测试中颇受欢迎。

# INSTALL

```aur: yay -S dirsearch```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gobuster](/man/gobuster)(1), [ffuf](/man/ffuf)(1), [wfuzz](/man/wfuzz)(1), [nikto](/man/nikto)(1), [dirb](/man/dirb)(1)

# RESOURCES

```[Source code](https://github.com/maurosoria/dirsearch)```

<!-- verified: 2026-07-11 -->
