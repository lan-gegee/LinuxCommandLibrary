# TAGLINE

通过 HTTP 传输并经 SSH 加固的 TCP/UDP 隧道

# TLDR

**启动服务器**

```chisel server --port [8080]```

**带认证启动服务器**

```chisel server --authfile [users.json]```

**客户端连接并转发端口**

```chisel client [server:8080] [local:3000:remote:80]```

**反向隧道**

```chisel client [server:8080] R:[remote:8001:local:80]```

**SOCKS5 代理**

```chisel client [server:8080] socks```

**通过 HTTPS 连接**

```chisel client https://[server] [8080:localhost:80]```

# SYNOPSIS

**chisel** server [_options_]
**chisel** client [_options_] _server_ _remote_...

# DESCRIPTION

**chisel** 是一种通过 HTTP 传输、经 SSH 加固的快速 TCP/UDP 隧道。单个可执行文件同时包含客户端和服务器功能。它使用 WebSocket 多路复用连接，允许通过单一 HTTP 连接承载多条隧道。

该工具适用于穿越防火墙、访问 NAT 后的服务以及创建反向隧道。它支持正向和反向端口转发以及 SOCKS5 代理模式。认证可通过用户名/密码对或认证文件配置。使用 Go 编写。

# SERVER OPTIONS

**-p**, **--port** _PORT_
> 监听端口（默认 **8080**）。

**--host** _HOST_
> 监听接口（默认全部）。

**--authfile** _FILE_
> JSON 文件路径，将 **user:pass** 凭据映射到允许的远程目标。

**--auth** _USER:PASS_
> 单个内联凭据对。

**--reverse**
> 允许客户端请求反向隧道（**R:**）。

**--socks5**
> 允许客户端通过特殊的 **socks** 远程目标请求 SOCKS5 端点。

**--backend** _URL_
> 将打到服务器上的非 chisel HTTP 请求转发到此后端 URL（适合让 chisel 与 web 服务器共存）。

**--keepalive** _DURATION_
> WebSocket keepalive 间隔（默认 **25s**）。

**--key**, **--keygen**, **--keyfile**
> 管理服务器的持久化 SSH 主机密钥。

**--tls-key**, **--tls-cert**, **--tls-ca**, **--tls-domain**
> 启用原生 TLS 终结和客户端证书校验。

# CLIENT OPTIONS

**--auth** _USER:PASS_
> 向服务器进行认证。

**--fingerprint** _HASH_
> 固定预期的服务器 SSH 密钥指纹。

**--proxy** _URL_
> 通过上游 HTTP **CONNECT** 或 SOCKS5 代理拨号。

**--header** _NAME: VAL_
> 添加到 WebSocket 握手的额外 HTTP header（可重复）。

**--hostname** _HOST_
> 覆盖 HTTP **Host** header。

**--sni** _NAME_
> 覆盖握手时使用的 TLS **ServerName**。

**--keepalive** _DURATION_
> WebSocket keepalive 间隔。

**--max-retry-count** _N_, **--max-retry-interval** _DURATION_
> 限制重连尝试次数和退避时间。

**--tls-ca** _FILE_, **--tls-skip-verify**, **--tls-key** _FILE_, **--tls-cert** _FILE_
> 控制 TLS 校验和客户端证书认证。

# REMOTE SYNTAX

```
[<local-host>:]<local-port>[:<remote-host>:<remote-port>][/udp]
```

默认值：local-host = **0.0.0.0**，remote-host = **0.0.0.0**，协议 = **tcp**。加前缀 **R:** 表示反向隧道。特殊值：**socks**（SOCKS5 端点，需要服务器启用 **--socks5**）和 **stdio:host:port**（附加到 stdio 的隧道）。

# CAVEATS

可用于绕过防火墙。WebSocket 支持情况因 PaaS 提供商而异。安装：curl https://i.jpillora.com/chisel! | bash

# INSTALL

```brew: brew install chisel```

```nix: nix profile install nixpkgs#chisel```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ssh](/man/ssh)(1), [socat](/man/socat)(1), [ngrok](/man/ngrok)(1)
