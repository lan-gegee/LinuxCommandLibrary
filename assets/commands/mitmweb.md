# TAGLINE

带 Web 界面的中间人代理

# TLDR

**以默认设置启动 mitmweb**

```mitmweb```

**指定代理和 Web 界面端口**

```mitmweb --listen-port [8080] --web-port [8081]```

**将拦截的流保存到文件**

```mitmweb -w [flows.mitm]```

**加载之前保存的流**

```mitmweb -r [flows.mitm]```

**以上游代理模式运行**

```mitmweb --mode upstream:[http://proxy:8080]```

**以透明代理模式运行**

```mitmweb --mode transparent```

**以反向代理模式运行**

```mitmweb --mode reverse:[https://target.example.com]```

**禁用自动打开浏览器**

```mitmweb --no-web-open-browser```

# SYNOPSIS

**mitmweb** [_options_]

# PARAMETERS

**--web-port** _PORT_
> Web 界面端口（默认：8081）。

**--web-open-browser**
> 启动时自动打开浏览器（默认：true）。

**--no-web-open-browser**
> 不自动打开浏览器。

**--listen-port** _PORT_
> 代理监听端口（默认：8080）。

**-w** _FILE_
> 将流写入文件。

**-r** _FILE_
> 从文件读取流。

**--mode** _MODE_
> 代理模式：regular、transparent、socks5、reverse:SPEC、upstream:SPEC、wireguard。

**--set** _OPTION=VALUE_
> 设置任意选项（例如 --set ignore_hosts=example.com）。

**-s** _SCRIPT_
> 运行 Python 插件脚本。

**--ssl-insecure**
> 不验证上游服务器 SSL/TLS 证书。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mitmweb** 是 mitmproxy 的基于 Web 的界面。它通过浏览器 UI 拦截、检查、修改和回放 HTTP/HTTPS 流量。Web 界面提供流列表、详情视图和交互式的请求/响应编辑。

默认情况下，mitmweb 在 8080 端口启动代理，在 8081 端口启动 Web 界面。它支持与 mitmproxy 相同的代理模式：regular、transparent、SOCKS5、反向代理、上游代理和 WireGuard。

客户端必须配置为使用该代理；对于 HTTPS 拦截，还必须在客户端安装 mitmproxy CA 证书。通过代理访问 http://mitm.it 可以下载证书。

# CAVEATS

HTTPS 拦截需要在客户端设备上安装 mitmproxy CA 证书。透明模式需要操作系统级的流量重定向（如 iptables）。未经身份验证时不应将 Web 界面暴露给不可信网络。

# HISTORY

**mitmweb** 是 **mitmproxy** 项目的一部分，由 Aldo Cortesi 创建。mitmproxy 项目始于 **2010 年**，添加 mitmweb 是为了提供控制台版 mitmproxy 界面的浏览器替代方案。

# INSTALL

```pacman: sudo pacman -S mitmproxy```

```apk: sudo apk add mitmproxy```

```nix: nix profile install nixpkgs#mitmproxy```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mitmproxy](/man/mitmproxy)(1), [mitmdump](/man/mitmdump)(1), [wireshark](/man/wireshark)(1), [tshark](/man/tshark)(1)
