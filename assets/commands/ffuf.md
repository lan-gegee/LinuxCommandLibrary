# TAGLINE

用 Go 编写的快速 Web 模糊测试工具

# TLDR

**目录模糊测试**

```ffuf -u [https://target.com/FUZZ] -w [wordlist.txt]```

**POST 参数模糊测试**

```ffuf -u [https://target.com/api] -w [wordlist.txt] -X POST -d "param=FUZZ"```

**按状态码过滤**

```ffuf -u [https://target.com/FUZZ] -w [wordlist.txt] -fc [404]```

**匹配响应大小**

```ffuf -u [https://target.com/FUZZ] -w [wordlist.txt] -ms [1234]```

**多个字典文件**

```ffuf -u [https://target.com/FUZZ1/FUZZ2] -w [list1.txt]:FUZZ1 -w [list2.txt]:FUZZ2```

**通过 Host 头发现虚拟主机**

```ffuf -u [https://target.com] -w [vhosts.txt] -H "Host: FUZZ.target.com"```

**带扩展名的递归发现**

```ffuf -u [https://target.com/FUZZ] -w [wordlist.txt] -recursion -e [.php,.html,.txt]```

# SYNOPSIS

**ffuf** [_options_]

# PARAMETERS

**-u** _URL_
> 包含 FUZZ 关键字的目标 URL。

**-w** _WORDLIST_
> 字典文件。

**-X** _METHOD_
> HTTP 方法。

**-d** _DATA_
> POST 数据。

**-H** _HEADER_
> 自定义请求头。

**-fc** _CODES_
> 按状态码过滤掉响应。

**-fs** _SIZE_
> 按大小过滤掉响应。

**-fw** _COUNT_
> 按单词数过滤掉响应。

**-fl** _COUNT_
> 按行数过滤掉响应。

**-mc** _CODES_
> 匹配状态码（默认 200-299,301,302,307,401,403,405,500）。

**-ms** _SIZE_
> 匹配响应大小。

**-e** _EXTENSIONS_
> 以逗号分隔的扩展名，会附加到每个单词后面。

**-recursion**
> 递归扫描发现的目录。

**-recursion-depth** _N_
> 最大递归深度。

**-t** _N_
> 并发线程数（默认 40）。

**-rate** _N_
> 速率限制，以每秒请求数计（0 = 不限制）。

**-o** _FILE_
> 将结果写入文件。

**-of** _FORMAT_
> 输出格式（json、csv、html、md 等）。

**-c**
> 彩色输出。

**-s**
> 静默模式，仅显示结果。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ffuf**（Fuzz Faster U Fool）是一个用 Go 编写的快速 Web 模糊测试工具。它通过在标记位置替换为字典条目并发送请求，来发现隐藏内容、参数和漏洞。

该工具擅长内容发现、参数模糊测试和虚拟主机枚举。过滤选项支持按状态码、大小、单词数或行数来匹配或排除响应。

ffuf 凭借其速度和灵活性，成为渗透测试和安全评估中的流行工具。

# CAVEATS

只能对已授权的目标使用。线程数过高可能压垮服务器。结果需要人工验证。

# HISTORY

ffuf 由 **joohoi** 创建，是一个快速灵活的 Web 模糊测试工具。它使用 Go 编写以追求性能，现已成为 Web 应用安全测试的标准工具。

# INSTALL

```apt: sudo apt install ffuf```

```dnf: sudo dnf install ffuf```

```apk: sudo apk add ffuf```

```brew: brew install ffuf```

```nix: nix profile install nixpkgs#ffuf```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gobuster](/man/gobuster)(1), [dirb](/man/dirb)(1), [wfuzz](/man/wfuzz)(1)
