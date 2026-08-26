# TAGLINE

HTTP 与 HTTPS 流量的交互式中间人代理

# TLDR

**以默认端口（8080）启动 mitmproxy**

```mitmproxy```

**在指定端口启动**

```mitmproxy -p [8888]```

**以反向代理模式启动**

```mitmproxy -m reverse:https://[example.com]```

**以透明代理模式启动**

```mitmproxy -m transparent```

**加载 Python 脚本**用于流量处理

```mitmproxy -s [path/to/script.py]```

**从文件读取流**

```mitmproxy -r [flows.mitm]```

**忽略特定主机**

```mitmproxy --ignore-hosts '^example\.com$'```

**启动 Web 界面**而非控制台

```mitmweb```

# SYNOPSIS

**mitmproxy** [_options_]

**mitmdump** [_options_]

**mitmweb** [_options_]

# PARAMETERS

**-p** _PORT_, **--listen-port** _PORT_
> 代理服务端口（默认：8080）

**-m** _MODE_, **--mode** _MODE_
> 代理模式：regular、transparent、socks5、reverse:SPEC、upstream:SPEC

**-T**, **--transparent**
> 启用透明代理模式

**--socks**
> 启用 SOCKS5 代理模式

**-R** _URL_, **--reverse** _URL_
> 反向代理到上游服务器（http[s]://host[:port]）

**-s** _SCRIPT_
> 用于流处理的 Python 脚本路径

**-r** _FILE_
> 从文件读取流

**-w** _FILE_
> 将流写入文件

**--ignore-hosts** _REGEX_
> 匹配要忽略（不拦截）主机的正则表达式

**--allow-hosts** _REGEX_
> 匹配要拦截主机的正则表达式

**--anticache**
> 去除缓存头部以防止 304 响应

**--insecure**
> 不验证上游 SSL/TLS 证书

**--cert** _SPEC_
> 添加 SSL 证书（路径或目录）

**--cadir** _DIR_
> CA 文件位置（默认：~/.mitmproxy）

**--no-http2**
> 禁用 HTTP/2 支持

**-q**, **--quiet**
> 安静模式

**-n**, **--no-server**
> 不启动代理服务器

**--options**
> 以 YAML 转储所有选项

**-h**, **--help**
> 显示帮助消息

# DESCRIPTION

**mitmproxy** 是 HTTP 和 HTTPS 流量的交互式中间人代理。它允许通过控制台界面检查、修改和回放 Web 流量。该套件包含三个工具：**mitmproxy**（控制台 UI）、**mitmweb**（Web UI）和 **mitmdump**（仅命令行）。

代理的工作方式是拦截连接并向客户端出示自己的证书。在客户端安装 mitmproxy CA 证书可避免 SSL 警告。流量可以被过滤、用 Python 脚本修改，或保存供日后分析。

代理模式包括 regular（显式代理）、transparent（网络级拦截）、reverse（转发到上游）和 SOCKS5。Python 插件可以修改请求和响应、实现自定义逻辑，或与其他工具集成。

# CAVEATS

拦截 HTTPS 需要客户端信任 mitmproxy CA 证书，证书位于 **~/.mitmproxy** 中。透明模式需要额外的系统配置（Linux 上为 iptables）。某些应用实现了证书固定，会拒绝经由 mitmproxy 的连接。未经授权拦截流量可能违反法律。

# HISTORY

mitmproxy 由 **Aldo Cortesi** 创建，于 **2010 年**首次发布。它用 **Python** 编写，已成为 Web 应用安全测试和调试的标准工具。该项目引入了 Web 界面（mitmweb）和强大的脚本 API 等创新功能。它在安全研究人员、开发者和 QA 工程师中被广泛用于分析 HTTP 流量。

# INSTALL

```pacman: sudo pacman -S mitmproxy```

```apk: sudo apk add mitmproxy```

```nix: nix profile install nixpkgs#mitmproxy```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[burpsuite](/man/burpsuite)(1), [wireshark](/man/wireshark)(1), [tcpdump](/man/tcpdump)(1), [charles](/man/charles)(1)
