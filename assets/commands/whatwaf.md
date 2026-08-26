# TAGLINE

Web 应用防火墙检测与绕过

# TLDR

**检测 WAF**

```whatwaf -u [https://example.com]```

**从文件读取 URL**

```whatwaf -l [urls.txt]```

**使用 Tor**

```whatwaf -u [url] --tor```

**指定 payload**

```whatwaf -u [url] --payload "[<script>]"```

**JSON 输出**

```whatwaf -u [url] --json```

# SYNOPSIS

**whatwaf** [_-u url_] [_-l file_] [_--tor_] [_options_]

# PARAMETERS

**-u** _URL_
> 目标 URL。

**-l** _FILE_
> URL 列表文件。

**--tor**
> 使用 Tor 网络。

**--payload** _PAY_
> 自定义 payload。

**--json**
> JSON 输出。

**--tamper** _SCRIPT_
> Tamper 脚本。

# DESCRIPTION

**whatwaf** 是一款安全工具，用于检测保护网站的 Web 应用防火墙（WAF），并给出潜在的绕过技术。它向目标发送各种 payload 并分析响应，从而识别所使用的 WAF 产品。

除检测之外，whatwaf 还针对识别出的 WAF 提供 tamper 脚本和规避建议，帮助渗透测试人员了解在授权评估中需要绕过哪些防护。可以指定自定义 payload 进行针对性测试。

该工具支持从 URL 文件批量扫描、通过 Tor 网络路由实现匿名测试，以及 JSON 输出以便与其他安全工具集成。它仅用于经授权的安全测试和研究。

# CAVEATS

仅限经授权的测试。可能触发告警。需要 Python。

# HISTORY

**WhatWaf** 的创建目的是识别 Web 应用防火墙并给出绕过技术建议。

# SEE ALSO

[wafw00f](/man/wafw00f)(1), [nmap](/man/nmap)(1), [sqlmap](/man/sqlmap)(1)
