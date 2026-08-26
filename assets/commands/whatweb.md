# TAGLINE

Web 技术指纹识别工具

# TLDR

**扫描网站**

```whatweb [https://example.com]```

**详细输出**

```whatweb -v [url]```

**激进扫描**（对每个目标发送额外请求）

```whatweb -a 3 [url]```

**将结果保存为 JSON**

```whatweb --log-json=[output.json] [url]```

**扫描多个 URL**

```whatweb [url1] [url2]```

**使用自定义 User-Agent 和线程数扫描**

```whatweb --user-agent "[custom-agent]" -t [10] [url]```

**仅在同一站点内跟随重定向**

```whatweb --follow-redirect=same-site [url]```

# SYNOPSIS

**whatweb** [_options_] _urls_

# PARAMETERS

**-v**
> 详细输出，显示插件的详细结果。

**-a**, **--aggression** _LEVEL_
> 激进级别：**1**（隐蔽，单个请求，默认）、**3**（激进，匹配时发送额外请求）、**4**（重度，对每个目标发送大量请求）。级别 2 未使用。

**--log-verbose** _FILE_
> 将详细输出记录到文件。

**--log-json** _FILE_
> 以 JSON 格式记录输出。

**--log-xml** _FILE_
> 以 XML 格式记录输出。

**-q**, **--quiet**
> 安静模式；不在标准输出显示结果。

**--user-agent** _UA_
> 设置自定义 User-Agent 字符串。

**-t**, **--max-threads** _N_
> 并发线程数。默认：25。

**--follow-redirect** _WHEN_
> 何时跟随重定向：never、http-only、meta-only、same-site 或 always（默认）。

**--cookie** _COOKIE_
> 提供 cookie（如 'name=value; name2=value2'）。

**--proxy** _HOST:PORT_
> 通过 HTTP 代理发送请求。

# DESCRIPTION

**whatweb** 是一款识别网站所用技术的 Web 扫描器，可识别内容包括内容管理系统、Web 框架、服务器软件、JavaScript 库和分析平台。它向目标 URL 发送请求并分析响应，从而识别具体的产品和版本。

该工具采用基于插件的架构，拥有超过 1,800 个用于识别不同技术的插件。四个激进级别控制扫描强度，从分析单次页面请求的被动模式，到发送额外请求探测特定技术的主动测试。

输出可以格式化为 JSON、XML、详细文本或 SQL 以便存入数据库。一次运行即可扫描多个 URL，并且支持身份验证、自定义请求头和代理配置，可用于登录页之后或经由中间服务器的测试。

# CAVEATS

只在你被授权扫描的系统上使用。激进模式（`-a 3` 和 `-a 4`）会发送大量请求，通常会被 WAF 和 IDS/IPS 标记。需要 Ruby 2.x 或更新版本。在高度定制的网站上插件结果可能出现误报。

# HISTORY

**whatweb** 由 **Andrew Horton**（urbanadventurer）和 **Brendan Coles** 创建，是一款开源的 Web 指纹识别框架。源码：github.com/urbanadventurer/WhatWeb。

# INSTALL

```dnf: sudo dnf install whatweb```

```nix: nix profile install nixpkgs#whatweb```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wappalyzer](/man/wappalyzer)(1), [nmap](/man/nmap)(1), [nikto](/man/nikto)(1), [curl](/man/curl)(1), [httpx](/man/httpx)(1)
