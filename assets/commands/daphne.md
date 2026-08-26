# TAGLINE

面向 ASGI 应用的 HTTP、HTTP2 和 WebSocket 协议服务器

# TLDR

**运行 Django Channels 应用**

```daphne [myproject.asgi]:application```

**在指定的主机和端口上运行**

```daphne -b [0.0.0.0] -p [8000] [myproject.asgi]:application```

**使用 Unix 套接字运行**

```daphne -u [/tmp/daphne.sock] [myproject.asgi]:application```

**以多个 worker 线程运行**

```daphne --threads [4] [myproject.asgi]:application```

**以 SSL 运行**

```daphne -e ssl:443:privateKey=[key.pem]:certKey=[cert.pem] [myproject.asgi]:application```

**启用详细日志**

```daphne -v 2 [myproject.asgi]:application```

# SYNOPSIS

**daphne** [_options_] _application_

# PARAMETERS

**-b**, **--bind** _address_
> 要绑定的 IP 地址（默认：127.0.0.1）。

**-p**, **--port** _port_
> 监听端口（默认：8000）。

**-u**, **--unix-socket** _path_
> Unix 套接字路径（TCP 的替代方案）。

**--fd** _fd_
> 要监听的文件描述符。

**-e**, **--endpoint** _spec_
> Twisted endpoint 描述串。

**--threads** _n_
> worker 线程数量。

**-v**, **--verbosity** _level_
> 日志详细程度（0-2）。

**--access-log** _path_
> 访问日志文件路径。

**--websocket_timeout** _seconds_
> 允许 WebSocket 保持连接的最长时间（-1 表示无限）。

**--websocket_connect_timeout** _seconds_
> 允许连接完成握手的最长时间（-1 表示无限）。

**--ping-interval** _seconds_
> WebSocket 空闲多少秒后发送保活 ping。

**--ping-timeout** _seconds_
> 保活 ping 无响应多少秒后关闭 WebSocket。

**--application-close-timeout** _seconds_
> 客户端断开后，ASGI 应用在被强制终止前可用的退出时间（秒）（默认：10）。

**--proxy-headers**
> 启用 X-Forwarded-For 处理。

**--proxy-headers-host** _header_
> 在代理后用于检测主机的请求头。

**--root-path** _path_
> ASGI scope 的根路径前缀（用于反向代理场景）。

# DESCRIPTION

**Daphne** 是面向 ASGI（Asynchronous Server Gateway Interface，异步服务器网关接口）应用的 HTTP、HTTP2 和 WebSocket 协议服务器，尤其配合 Django Channels 使用。它让 Django 应用能够处理 WebSocket 连接和其他异步协议。

与处理同步 HTTP 请求的 WSGI 服务器（Gunicorn、uWSGI）不同，Daphne 支持实时特性所需的长连接：WebSocket、Server-Sent Events 和 HTTP 长轮询。

Daphne 构建在 Twisted 的网络引擎之上。它通常与 Django Channels 搭配，用于聊天应用、实时通知等实时功能。在生产环境中，它一般运行在 nginx 等反向代理之后。

# CAVEATS

不适合用来伺服静态文件；请使用 nginx 或 whitenoise。生产部署应使用多个 worker（通过进程管理器）。WebSocket 连接空闲时也会占用资源。大多数部署场景下，SSL 终止更适合交给反向代理处理。

# HISTORY

Daphne 由 **Andrew Godwin** 作为 **Django Channels** 项目的一部分创建，首次发布于 **2016 年**前后。它的开发目的是为 Django 带来 WebSocket 支持，使该框架能够处理实时应用。Django Channels 后来成为 Django 官方项目，Daphne 则是其参考 ASGI 服务器。

# INSTALL

```apk: sudo apk add py3-daphne```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[uvicorn](/man/uvicorn)(1), [hypercorn](/man/hypercorn)(1), [gunicorn](/man/gunicorn)(1), [nginx](/man/nginx)(1)
