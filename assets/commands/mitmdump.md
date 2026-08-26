# TAGLINE

mitmproxy 的命令行配套工具，一个强大的 HTTPS 代理

# TLDR

**以默认端口启动代理**

```mitmdump```

**在指定端口启动**

```mitmdump -p [8888]```

**将流量保存到文件**

```mitmdump -w [traffic.mitm]```

**读取并回放流量**

```mitmdump -r [traffic.mitm]```

**运行脚本**

```mitmdump -s [script.py]```

**按 URL 过滤请求**

```mitmdump --set flow_detail=3 "~u example.com"```

**透明代理模式**

```mitmdump --mode transparent```

**忽略特定主机**

```mitmdump --ignore-hosts "^example\.com$"```

# SYNOPSIS

**mitmdump** [_-p port_] [_-w file_] [_-r file_] [_-s script_] [_--mode mode_] [_options_] [_filter_]

# PARAMETERS

**-p** _PORT_, **--listen-port** _PORT_
> 代理监听端口（默认：8080）。

**-w** _FILE_
> 将流写入文件。

**-r** _FILE_
> 从文件读取流。

**-s** _SCRIPT_
> 运行 Python 脚本。

**--mode** _MODE_
> 代理模式：regular、transparent、socks5、reverse、upstream。

**--listen-host** _HOST_
> 监听主机。

**--ssl-insecure**
> 不验证服务器 SSL 证书。

**--ignore-hosts** _PATTERN_
> 忽略匹配正则表达式的主机。

**--intercept** _FILTER_
> 拦截匹配过滤器的流。

**--modify-body** _SPEC_
> 修改响应体。

**--modify-headers** _SPEC_
> 修改头部。

**--set** _KEY=VALUE_
> 设置选项值。

**--flow-detail** _LEVEL_
> 输出详细级别（0-3）。

**-q**, **--quiet**
> 抑制输出。

**-k**, **--insecure**
> 不验证上游 SSL。

# DESCRIPTION

**mitmdump** 是 mitmproxy 的命令行配套工具。mitmproxy 是一款用于调试、测试和安全分析的强大 HTTPS 代理。mitmdump 捕获并操纵 HTTP/HTTPS 流量。

该工具充当中间人（man-in-the-middle）代理。对于 HTTPS，它会即时生成证书，从而能够检查加密流量。客户端必须信任 mitmproxy 的 CA 证书。

流量可以保存（-w）并回放（-r）用于分析或测试。保存的流包含带时间信息的完整请求/响应数据。

Python 脚本（-s）支持以编程方式操纵流量。脚本定义 request()、response() 和 clientconnect() 等钩子，实时修改或分析流量。

过滤表达式选择特定的流：~u 匹配 URL，~m 匹配方法，~b 匹配正文内容，~h 匹配头部。过滤器可用 &（与）、|（或）和 !（非）组合。

模式包括：regular（显式代理）、transparent（网络级拦截）、reverse（转发到指定服务器）和 upstream（链到另一个代理）。

# CAVEATS

HTTPS 拦截需要 CA 信任。某些应用固定证书。透明模式需要配置 iptables/pf。大流量会占用大量内存。记录全部流量会影响性能。

# HISTORY

**mitmproxy** 和 mitmdump 由 **Aldo Cortesi** 于 **2010 年**前后创建。该项目从安全研究工具发展为广泛使用的代理套件。它是移动应用调试、API 开发和安全测试的必备工具。

# INSTALL

```pacman: sudo pacman -S mitmproxy```

```apk: sudo apk add mitmproxy```

```nix: nix profile install nixpkgs#mitmproxy```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mitmproxy](/man/mitmproxy)(1), [charles](/man/charles)(1), [wireshark](/man/wireshark)(1), [tcpdump](/man/tcpdump)(1)
