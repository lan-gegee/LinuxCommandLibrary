# TAGLINE

发现 Web 应用中隐藏的 HTTP 参数

# TLDR

**查找某 URL 的 GET 参数**

```arjun -u [https://example.com/page]```

**查找 POST 参数**

```arjun -u [https://example.com/api] -m POST```

**使用自定义字典扫描**

```arjun -u [https://example.com] -w [path/to/wordlist.txt]```

从文件**扫描多个 URL**

```arjun -i [urls.txt]```

使用 **JSON 请求体**进行参数发现

```arjun -u [https://example.com/api] -m JSON```

**设置自定义请求头**

```arjun -u [https://example.com] --headers "[Cookie: session=abc]"```

将结果**输出**到 JSON 文件

```arjun -u [https://example.com] -o [results.json]```

**设置线程数**

```arjun -u [https://example.com] -t [20]```

# SYNOPSIS

**arjun** [_-u url_] [_-i file_] [_-m method_] [_-w wordlist_] [_-o output_] [_-t threads_] [_options_]

# PARAMETERS

**-u**, **--url** _url_
> 要扫描参数的目标 URL。

**-i**, **--input** _file_
> 包含待扫描 URL 的文件（每行一个）。

**-m**, **--method** _method_
> 要使用的 HTTP 方法（GET、POST、JSON、XML）。默认：GET。

**-w**, **--wordlist** _file_
> 参数名使用的自定义字典。

**-o** _file_
> 将结果保存到 JSON 输出文件。

**-oT** _file_
> 将结果保存到文本输出文件。

**-oB** [_proxy_]
> 将结果发送到 Burp Suite 代理。

**-t**, **--threads** _n_
> 并发线程数（默认：5）。

**--json**
> 以 JSON 而非表单数据发送 POST 数据。

**--headers** _headers_
> 自定义请求头，格式为 "Header: value"。

**--passive**
> 使用被动来源查找参数。

**--stable**
> 使用更可靠但更慢的检测方式。

**-d**, **--delay** _seconds_
> 请求之间的延迟。

**--include** _params_
> 始终包含在请求中的参数。

**-T**, **--timeout** _seconds_
> HTTP 请求超时时间，单位秒（默认：15）。

**-c** _n_, **--chunks** _n_
> 每个请求发送的参数数量。

**-q**, **--quiet**
> 除结果外抑制输出。

# DESCRIPTION

**Arjun** 是一款面向 Web 应用安全测试的参数发现工具。它通过发送精心构造的请求并分析响应差异来识别隐藏或未公开的 HTTP 参数，差异表明该参数有效。

该工具综合多种技术检测参数：提交不同参数名时监控响应长度、状态码和内容变化。这使它能找到会触发特定服务器行为的参数，即使应用并未明确公布它们。

Arjun 内置了常见参数名词典，同时支持自定义字典进行针对性测试。它可以发现 GET 请求（查询字符串）、POST 表单数据和 JSON 请求体中的参数。被动模式会查询网页存档和搜索引擎等外部来源获取已知参数。

该工具常用于渗透测试和漏洞赏金挖掘，用于发现在初步侦察阶段可能遗漏的攻击面。发现的参数可能揭示隐藏功能、调试模式或额外的攻击向量。

# CAVEATS

只应用于你有权测试的应用。高线程数或不加延迟可能触发速率限制或 WAF 拦截。检测基于启发式算法，可能出现误报或漏报。大型字典会显著增加扫描时间。

# HISTORY

**Arjun** 由 Somdev Sangwan（s0md3v）开发并以开源安全工具形式发布。它凭借发现隐藏参数的高效性在漏洞赏金和渗透测试社区广受欢迎。该工具用 Python 编写，目前仍在积极维护并更新新的检测技术。

# INSTALL

```aur: yay -S arjun```

```brew: brew install arjun```

```nix: nix profile install nixpkgs#arjun```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[ffuf](/man/ffuf)(1), [wfuzz](/man/wfuzz)(1), [burpsuite](/man/burpsuite)(1), [httpx](/man/httpx)(1), [paramspider](/man/paramspider)(1)
