# TAGLINE

识别网站上使用的技术

# TLDR

**扫描单个 URL**

```wappalyzer -i https://example.com```

**从文件读取 URL 扫描**

```wappalyzer -i [urls.txt] -t [10]```

**将结果导出为 JSON**

```wappalyzer -i https://example.com -oJ [results.json]```

使用 webanalyze（Go 版本）

```webanalyze -host https://example.com```

**更新技术指纹**

```webanalyze -update```

**从文件扫描多个主机**

```webanalyze -hosts [urls.txt] -output json```

# SYNOPSIS

**wappalyzer** [_options_] -i _url_|_file_

**webanalyze** [_options_]

# PARAMETERS (wappalyzer)

**-i** _url_|_file_
> 输入 URL 或包含 URL 的文件。

**-t** _num_
> 线程数。

**-oJ** _file_
> 将 JSON 输出到文件。

**-oC** _file_
> 将 CSV 输出到文件。

# PARAMETERS (webanalyze)

**-host** _url_
> 要分析的单个主机。

**-hosts** _file_
> 包含主机列表的文件。

**-output** _format_
> 输出格式：stdout、csv、json。

**-update**
> 更新技术指纹。

**-worker** _num_
> 工作进程数。

# DESCRIPTION

**wappalyzer** 用于识别网站上使用的技术，包括 CMS 平台、JavaScript 框架、分析工具和服务器软件。它通过对 HTML、响应头、Cookie 和 JavaScript 变量进行模式匹配来实现识别。

存在多个 CLI 实现：Python 的 wappalyzer 包（需要 Firefox/geckodriver）、webanalyze（基于 Go，独立运行）和 wappybird（多线程）。它们都使用来自 Wappalyzer 项目的指纹。

这些工具适用于安全评估、竞争分析和技术清点。既可以处理单个 URL，也可以从文件批量扫描。

# CAVEATS

Python 版需要 Firefox 和 geckodriver。指纹需要定期更新。动态内容可能需要基于浏览器的扫描。批量扫描可能受到速率限制。

# HISTORY

**Wappalyzer** 起初是一个用于识别 Web 技术的浏览器扩展。随后出现了各种 CLI 工具以支持自动化和集成。在官方项目停止开源指纹之后，社区分支持续维护着更新的检测规则。

# SEE ALSO

[whatweb](/man/whatweb)(1), [httpie](/man/httpie)(1), [curl](/man/curl)(1)
