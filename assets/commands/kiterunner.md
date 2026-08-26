# TAGLINE

通过上下文感知扫描发现 API 端点

# TLDR

**扫描 API**

```kr scan [url] -w [wordlist.txt]```

**爆破端点**

```kr brute [url] -w [wordlist.txt]```

**使用指定字典**

```kr scan [url] -A apiroutes-210228```

**携带请求头扫描**

```kr scan [url] -w [list] -H "Authorization: Bearer [token]"```

**输出到文件**

```kr scan [url] -w [list] -o [results.txt]```

# SYNOPSIS

**kr** _command_ [_options_] _target_

# PARAMETERS

**scan** _URL_
> 上下文感知的 API 端点发现，使用包含正确 HTTP 方法、请求头和参数的数据集。

**brute** _URL_
> 使用自定义字典进行传统的目录爆破。

**kb replay** _REQUEST_
> 重放之前发现的请求，可选通过代理进行。

**-w** _WORDLIST_
> 字典文件。

**-A**, **--assetnote-wordlist** _NAME_
> 使用 wordlist.assetnote.io 提供的字典。可附加 `;N` 以限制为前 N 行。

**-H** _HEADER_
> 添加 HTTP 请求头。

**-o** _FILE_
> 输出文件。

**-x**, **--max-connection-per-host** _N_
> 每个主机的最大并发连接数（建议 5-10）。

**--disable-precheck**
> 扫描前跳过主机存活探测。

**--help**
> 显示帮助信息。

# DESCRIPTION

**kiterunner** 是一款专为在 Web 应用上发现 API 端点而设计的上下文感知内容发现工具。与传统目录爆破工具只是把路径拼接到基础 URL 后面不同，kiterunner 理解 API 路由约定，发送模拟真实 API 调用的请求，包括为每个候选路由使用恰当的 HTTP 方法、请求头和内容类型。

该工具附带 Assetnote 精选的字典，专门针对 Rails、Django、Express 和 Spring 等常见 API 框架。它同时提供用于智能 API 感知发现的 `scan` 模式和用于传统目录枚举的 `brute` 模式，让安全专业人员在侦察和渗透测试工作中更加灵活。

# CAVEATS

安全测试工具。仅限授权使用。基于 Go 实现。

# HISTORY

kiterunner 由 **Assetnote** 创建，用于安全评估过程中的 API 端点发现。

# INSTALL

```nix: nix profile install nixpkgs#kiterunner```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ffuf](/man/ffuf)(1), [gobuster](/man/gobuster)(1), [dirsearch](/man/dirsearch)(1)
