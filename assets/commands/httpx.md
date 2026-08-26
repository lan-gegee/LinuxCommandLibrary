# TAGLINE

用于探测 Web 服务器的快速 HTTP 工具包

# TLDR

**探测存活主机**

```cat [hosts.txt] | httpx```

**探测并显示页面标题**

```httpx -l [hosts.txt] -title```

**显示状态码**

```httpx -l [hosts.txt] -status-code```

**探测指定端口**

```httpx -l [hosts.txt] -ports [80,443,8080]```

**跟随重定向**

```httpx -l [hosts.txt] -follow-redirects```

**输出 JSON**

```httpx -l [hosts.txt] -json -o [output.json]```

# SYNOPSIS

**httpx** [_options_]

# PARAMETERS

**-l**, **-list** _FILE_
> 包含待处理主机列表的输入文件。

**-u**, **-target** _HOST_
> 直接探测指定的目标主机，而不是读取列表。

**-title**
> 显示页面标题。

**-sc**, **-status-code**
> 显示响应状态码。

**-td**, **-tech-detect**
> 显示检测到的技术（基于 Wappalyzer 数据集）。

**-ip**
> 显示解析出的主机 IP。

**-p**, **-ports** _PORTS_
> 要探测的端口，使用 nmap 风格的语法（例如 `http:1,2-10,https:443`）。

**-x** _METHOD_
> 要探测的 HTTP 方法；使用 `all` 可尝试所有方法。

**-H** _HEADER_
> 随每个请求发送的自定义 HTTP 头。

**-fr**, **-follow-redirects**
> 跟随 HTTP 重定向。

**-mc**, **-match-code** _CODES_
> 只显示匹配指定状态码的响应（例如 `-mc 200,301`）。

**-fc**, **-filter-code** _CODES_
> 排除匹配指定状态码的响应。

**-t**, **-threads** _N_
> 并发线程数（默认 50）。

**-rl**, **-rate-limit** _N_
> 每秒最大请求数（默认 150）。

**-timeout** _SECONDS_
> 请求超时时间（默认 10）。

**-retries** _N_
> 失败后的重试次数。

**-silent**
> 只打印结果，隐藏横幅和统计信息。

**-json**
> 以 JSONL（JSON lines）格式保存输出。

**-o**, **-output** _FILE_
> 写入结果的文件。

**-help**
> 显示帮助信息。

# DESCRIPTION

**httpx** 是一款基于 Go 的 `retryablehttp` 库构建的快速多用途 HTTP 工具包，用于同时对一批主机运行大量探测。它会检查哪些主机存活，并能报告状态码、页面标题、响应头、TLS 信息、检测到的技术、屏幕截图等。

默认情况下，它先以 **HTTPS** 协议探测，只有在 HTTPS 无法访问时才回退到 **HTTP**；使用 **-no-fallback** 可以两种协议都尝试。该工具为侦察和安全测试工作流而构建，能够并发处理大量主机列表，并可与其余 ProjectDiscovery 工具链（**nuclei**、**subfinder** 等）配合使用。

# CAVEATS

仅用于对获得授权的系统进行侦察和安全测试。从源码构建需要 Go；也有预编译二进制可用。选项采用单横线风格（例如 `-json`，而非 `--json`）。

# HISTORY

httpx 由 **ProjectDiscovery** 创建，是其开源安全侦察工具套件的组成部分，与 **nuclei**、**subfinder** 等工具属于同一体系。

# INSTALL

```apk: sudo apk add py3-httpx```

```brew: brew install httpx```

```nix: nix profile install nixpkgs#httpx```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nuclei](/man/nuclei)(1), [nmap](/man/nmap)(1), [httprobe](/man/httprobe)(1)

# RESOURCES

```[Source code](https://github.com/projectdiscovery/httpx)```

```[Homepage](https://projectdiscovery.io)```

```[Documentation](https://docs.projectdiscovery.io/opensource/httpx)```

<!-- verified: 2026-07-19 -->
