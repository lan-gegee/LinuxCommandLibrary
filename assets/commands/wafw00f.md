# TAGLINE

Web 应用防火墙检测工具

# TLDR

**检测保护某网站**的 WAF

```wafw00f [https://example.com]```

**一次运行扫描多个 URL**

```wafw00f [https://site1.com] [https://site2.com]```

**从输入文件读取目标**

```wafw00f -i [urls.txt]```

**列出所有可检测的已知 WAF**

```wafw00f -l```

**查找所有**匹配的 WAF（不在首个匹配处停止）

```wafw00f -a [https://example.com]```

输出详细调试信息（可重复使用）

```wafw00f -vv [https://example.com]```

**经由代理路由流量**（例如 Burp Suite）

```wafw00f -p [http://127.0.0.1:8080] [https://example.com]```

**将输出保存**为 CSV、JSON 或文本（格式由扩展名推断）

```wafw00f -o [result.json] [https://example.com]```

# SYNOPSIS

**wafw00f** [_options_] _url_ [_url_ ...]

# PARAMETERS

**-h**, **--help**
> 显示帮助信息并退出。

**-V**, **--version**
> 打印当前版本并退出。

**-v**, **--verbose**
> 启用详细输出。可重复使用（如 **-vv**）以获得更多细节。

**-a**, **--findall**
> 查找所有匹配签名的 WAF；不在第一个匹配后停止。

**-r**, **--noredirect**
> 不跟随 3xx 重定向。

**-t** _TEST_, **--test**=_TEST_
> 只测试某个特定的 WAF（名称来自 **-l** 的输出）。

**-l**, **--list**
> 列出 wafw00f 能够检测的所有 WAF。

**-p** _PROXY_, **--proxy**=_PROXY_
> 使用 HTTP/SOCKS5 代理，例如 _http://host:8080_、_socks5://host:1080_、_http://user:pass@host:8080_。

**-H** _FILE_, **--headers**=_FILE_
> 从文本文件传入自定义请求头，覆盖默认请求头集合。

**-i** _FILE_, **--input-file**=_FILE_
> 从文本、CSV 或 JSON 文件中读取目标。

**-o** _FILE_, **--output**=_FILE_
> 将结果写入文件。格式根据扩展名选择（csv、json、text）。

**-f** _FORMAT_, **--format**=_FORMAT_
> 强制指定输出格式，无视文件名扩展名。

# DESCRIPTION

**wafw00f** 是一款识别网站所受 Web 应用防火墙（WAF）的安全工具。其工作原理是发送特制的 HTTP 请求，并分析响应中特定 WAF 产品特有的签名与行为特征。

该工具能检测众多商业和开源 WAF，包括 Cloudflare、AWS WAF、Akamai、F5 BIG-IP、ModSecurity、Imperva、Sucuri 等。默认模式下它识别出第一个 WAF 后即停止，而全量检测模式会对所有已知 WAF 指纹进行测试，以完成彻底分析。

可以通过输入文件批量测试多个 URL，代理支持则允许将流量经由 Burp Suite 等拦截工具转发。该工具面向经授权的渗透测试和安全评估，帮助在深入测试前摸清目标防护措施。

# DETECTED WAFS

Cloudflare、AWS WAF、Akamai、F5 BIG-IP、ModSecurity、Imperva、Sucuri、Fortinet 等等。

# CAVEATS

仅限经授权的测试。某些 WAF 可能阻止检测。可能出现误报。

# HISTORY

**wafw00f** 最初由 **Sandro Gauci** 编写，约在 **2009 年**由 **EnableSecurity** 发布。此后它已成为标准的侦察工具，随 Kali Linux 一同分发并在 GitHub 上持续维护。这个名字是 "WAF" 与狗叫声组合而成的双关语。

# INSTALL

```dnf: sudo dnf install wafw00f```

```nix: nix profile install nixpkgs#wafw00f```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nmap](/man/nmap)(1), [nikto](/man/nikto)(1), [wfuzz](/man/wfuzz)(1), [burpsuite](/man/burpsuite)(1)
