# TAGLINE

快速递归的 Web 内容发现工具

# TLDR

扫描 URL 中的目录和文件

```feroxbuster --url [https://example.com]```

**使用自定义词典**

```feroxbuster --url [https://example.com] --wordlist [path/to/wordlist.txt]```

**带指定扩展名扫描**

```feroxbuster --url [https://example.com] --extensions [php,html,txt]```

**递归扫描**到指定深度

```feroxbuster --url [https://example.com] --depth [3]```

**多线程扫描**

```feroxbuster --url [https://example.com] --threads [100]```

**过滤掉特定状态码**

```feroxbuster --url [https://example.com] --filter-status [404,403]```

**将结果输出到文件**

```feroxbuster --url [https://example.com] --output [results.txt]```

**通过代理扫描**

```feroxbuster --url [https://example.com] --proxy [http://127.0.0.1:8080]```

# SYNOPSIS

**feroxbuster** [_-u url_] [_-w wordlist_] [_-x extensions_] [_-t threads_] [_-d depth_] [_-o output_] [_options_]

# PARAMETERS

**-u**, **--url** _url_
> 要扫描的目标 URL。

**-w**, **--wordlist** _file_
> 要使用的词典（默认：内置 seclists）。

**-x**, **--extensions** _ext_
> 要检查的文件扩展名（逗号分隔）。

**-t**, **--threads** _n_
> 并发线程数（默认：50）。

**-d**, **--depth** _n_
> 最大递归深度（默认：4，0 表示无限）。

**-o**, **--output** _file_
> 结果输出文件。

**-n**, **--no-recursion**
> 禁用递归扫描。

**-f**, **--add-slash**
> 为每个请求追加 /。

**-C**, **--filter-status** _codes_
> 过滤掉特定的 HTTP 状态码。

**-S**, **--filter-size** _size_
> 过滤掉特定大小的响应。

**-W**, **--filter-words** _count_
> 过滤掉特定单词数的响应。

**-L**, **--filter-lines** _count_
> 过滤掉特定行数的响应。

**--proxy** _url_
> 用于请求的代理。

**-H**, **--headers** _header_
> 自定义请求头（可多次使用）。

**-k**, **--insecure**
> 禁用 TLS 证书验证。

**-q**, **--quiet**
> 最少输出。

**--json**
> 以 JSON 格式输出。

# DESCRIPTION

**feroxbuster** 是一个用 Rust 编写的快速递归内容发现工具。它通过从词典发送 HTTP 请求来暴力枚举 Web 服务器上的目录和文件，并通过响应分析找出隐藏的资源。

速度是其核心特性之一：Rust 的性能结合异步请求，可实现每秒扫描数千个路径。该工具支持递归扫描，会自动深入已发现的目录，直到可配置的深度。

高级过滤选项可根据状态码、响应大小、单词数、行数或正则表达式隐藏响应，减少误报。当服务器对不存在的路径返回通用页面时尤其有用。

交互模式提供实时统计信息，并允许在扫描过程中暂停、恢复、添加新 URL 以及调整设置。结果按状态码着色，便于快速判读。

Feroxbuster 通过代理支持与 Burp Suite 等工具集成，并可保存状态以便恢复中断的扫描。输出格式包括纯文本、JSON 以及与其他安全工具兼容的格式。

# CAVEATS

只可用于你获得测试授权的系统。高线程数可能触发限流或 IP 封禁。大词典配合递归会产生巨大流量。某些 WAF 能检测并拦截该工具的模式。

# HISTORY

**feroxbuster** 由 Ben "epi" Risher 创建，首个版本发布于 **2020 年**前后。名称由 "ferox"（拉丁语意为凶猛/狂野）和 "buster" 组合而成。为追求性能采用 Rust 编写，很快便作为 dirb、gobuster、dirsearch 等工具的现代替代品流行起来。

# INSTALL

```zypper: sudo zypper install feroxbuster```

```brew: brew install feroxbuster```

```nix: nix profile install nixpkgs#feroxbuster```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gobuster](/man/gobuster)(1), [dirsearch](/man/dirsearch)(1), [ffuf](/man/ffuf)(1), [dirb](/man/dirb)(1)

# RESOURCES

```[Source code](https://github.com/epi052/feroxbuster)```

<!-- verified: 2026-07-15 -->
