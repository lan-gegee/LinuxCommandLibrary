# TAGLINE

开源的 XSS 漏洞扫描器与参数分析器

# TLDR

**扫描 URL** 的 XSS 漏洞

```dalfox url [https://example.com?q=test]```

**使用自定义载荷文件扫描**

```dalfox url [https://example.com?q=test] --custom-payload [payloads.txt]```

**从文件扫描多个 URL**

```dalfox file [urls.txt]```

**从其他工具管道传入 URL**

```cat [urls.txt] | dalfox pipe```

**使用 blind XSS 回调**

```dalfox url [https://example.com?q=test] --blind [https://your.xss.ht]```

**将结果输出**到 JSON 文件

```dalfox url [https://example.com?q=test] -o [results.json] --format json```

# SYNOPSIS

**dalfox** _mode_ [_target_] [_options_]

# PARAMETERS

_MODE_
> 运行模式：url、file、pipe、sxss、server、payload。

_TARGET_
> 要扫描的 URL 或包含 URL 的文件。

**--custom-payload** _FILE_
> 使用自定义载荷文件。

**--blind** _URL_
> Blind XSS 回调 URL。

**-o**, **--output** _FILE_
> 输出文件路径。

**--format** _FORMAT_
> 输出格式：plain、json、xml。

**--cookie** _STRING_
> 为请求设置 Cookie。

**-H**, **--header** _STRING_
> 添加自定义请求头。

**--proxy** _URL_
> 要使用的 HTTP 代理。

**-w**, **--worker** _N_
> 并发 worker 数量。

**--silence**
> 抑制除结果外的所有输出。

**--mining-dict**
> 启用基于字典的参数挖掘。

**--mining-dom**
> 启用基于 DOM 的参数挖掘。

**--only-custom-payload**
> 仅测试自定义载荷，跳过内置载荷。

**--remote-payloads** _SOURCE_
> 使用远程载荷（portswigger、payloadbox）。

**--skip-xss-scanning**
> 跳过 XSS 扫描，只执行参数分析。

**--poc-type** _TYPE_
> PoC 输出格式（plain、curl、httpie、http-request）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**dalfox** 是一个功能强大的开源 XSS（跨站脚本）漏洞扫描器和参数分析器。它专注于通过自动化测试发现反射型 XSS、存储型 XSS 和基于 DOM 的 XSS 漏洞。

该工具先进行参数分析以识别注入点，然后用全面的载荷数据库进行测试。它借助外部回调服务器支持 blind XSS 检测，并可通过管道输入与其他安全工具集成。

dalfox 提供 DOM 渲染分析、WAF 检测与绕过以及智能载荷变异等功能。它专为进行授权安全评估的渗透测试人员和安全研究人员设计。

# CAVEATS

只能对获得明确授权的系统进行测试。可能出现误报；请人工验证发现的结果。高请求速率可能触发限流或封禁。某些 XSS 类型需要基于浏览器的验证。

# HISTORY

dalfox 由 **hahwul** 创建并于 **2020 年**发布。名字意为 "Finder Of XSS"，其中 "dal" 在韩语中是"月亮"的意思。它被设计为现有 XSS 扫描器的快速灵活替代品，强调自动化与准确性。

# INSTALL

```brew: brew install dalfox```

```nix: nix profile install nixpkgs#dalfox```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nikto](/man/nikto)(1), [sqlmap](/man/sqlmap)(1), [nuclei](/man/nuclei)(1), [httpx](/man/httpx)(1)
