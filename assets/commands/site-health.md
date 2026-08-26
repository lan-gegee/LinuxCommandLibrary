# TAGLINE

从命令行检查网站和域名的健康状况

# TLDR

对域名运行完整健康检查

```site-health example.com```

显示详细诊断信息而不是仪表盘

```site-health --verbose example.com```

只检查 MX、SPF 和 DMARC

```site-health --mail example.com```

输出机器可读的 JSON 报告

```site-health --format json example.com```

要求重定向后到达特定的最终 URL

```site-health --expected-url https://example.org/ example.com```

跳过可选的 /llms.txt 探测

```site-health --skip-llms-txt example.com```

打印版本号并退出

```site-health --version```

# SYNOPSIS

**site-health** [**--mail**] [**--verbose**] [**--expected-url** _url_] [**--skip-llms-txt**] [**--format** _dashboard_|_json_] [**--version**] _domain_

# PARAMETERS

**--mail**
> 只运行与邮件相关的 DNS 检查：MX（包括 Null MX）、SPF 和 DMARC。

**--verbose**
> 打印详细的故障排查诊断。使用 **--format json** 时被忽略。

**--expected-url** _url_
> 重定向后站点必须落到的绝对 `http://` 或 `https://` URL。默认为 `https://<domain>/`。

**--skip-llms-txt**
> 跳过可选的 `GET /llms.txt` 可用性检查。

**--format** _dashboard_|_json_
> 输出格式。默认 `dashboard`。`json` 在标准输出上写出一个文档。`text` 可作为 `dashboard` 的别名使用。

**--version**
> 打印 `site-health <version>` 并以 0 退出。

**_domain_**
> 要检查的单个主机名。协议前缀、路径、端口或末尾的点会被去除。多个参数属于用法错误。

# DESCRIPTION

**site-health** 是一个用 Go 编写的 CLI，用于给域名的公开 Web 与邮件姿态打分。它仅使用 Go 标准库：无需 WHOIS 客户端二进制、OpenSSL 或其他运行时依赖。

默认（site）运行会探测 DNS（A、AAAA、CNAME）、TCP 80/443、HTTP/HTTPS、重定向及规范 URL、TLS 证书、响应时间、HTML 内容（常见的服务器、PHP 和 WordPress 错误页面、停放域名标记）、域名注册到期时间与注册商、MX/SPF/DMARC，以及可选的 `/llms.txt`。在检查之前，它可能自动检测转发目标：如果 `http://`、`http://www.`、`https://www.` 和 `https://` 都汇聚到同一个站外最终 URL，该 URL 就成为期望的目标。存在多个不同目标时视为有歧义，留给 **--expected-url** 处理。

邮件模式跳过 Web 探测，打印一个更小的 MX/SPF/DMARC 仪表盘。JSON 模式输出单个对象，包含 `tool`、`version`、`domain`、`mode`（`site` 或 `mail`）、`expected_url`、`forwarding`、`checks`、`issues` 和 `summary`。退出码为 **0**（无失败项）、**1**（一项或多项检查失败）和 **2**（用法错误：缺少域名、多余参数、错误标志或无效的 **--expected-url**）。警告本身不会导致退出码 1。

# CAVEATS

需要对 DNS、HTTP(S) 和注册查询的出站网络访问；部分 TLD 和隐私保护的注册会显示不完整的注册商或到期数据。每次调用只接受一个域名。JSON 模式下 **--verbose** 被抑制。自动转发检测仅在 **--expected-url** 保持默认值 `https://<domain>/` 时运行。`/llms.txt` 检查仅供参考，可以跳过。这不是完整的漏洞扫描器、负载测试工具，也不能替代 **sslscan** / **testssl**。

# HISTORY

由 **atillalab** 使用 **Go** 编写。仓库于 **2026 年 8 月**发布。**0.8 版**是完成的 Go 重写版。采用 **MIT** 许可证。二进制名为 **site-health**。

# SEE ALSO

[whois](/man/whois)(1), [dig](/man/dig)(1), [host](/man/host)(1), [curl](/man/curl)(1), [openssl](/man/openssl)(1), [sslscan](/man/sslscan)(1), [httping](/man/httping)(1)

# RESOURCES

```[Source code](https://github.com/atillalab/site-health)```

<!-- verified: 2026-08-18 -->
