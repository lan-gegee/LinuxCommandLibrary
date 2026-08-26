# TAGLINE

支持 HTTP/1、HTTP/2 和 WebSocket 的 Python ASGI Web 服务器

# TLDR

**运行 ASGI 应用**

```hypercorn [app:app]```

**指定主机和端口**

```hypercorn [app:app] --bind [0.0.0.0:8000]```

以多个 worker **运行**

```hypercorn [app:app] --workers [4]```

为开发**启用热重载**

```hypercorn [app:app] --reload```

**使用 HTTPS（同时启用 HTTP/2）**

```hypercorn [app:app] --certfile [cert.pem] --keyfile [key.pem]```

**从 TOML 文件加载配置**

```hypercorn [app:app] --config [hypercorn.toml]```

# SYNOPSIS

**hypercorn** [_options_] _module:application_

# PARAMETERS

_module:application_
> Python 模块与 ASGI 应用变量。

**--bind**, **-b** _address_
> 要绑定的地址（host:port）。

**--workers**, **-w** _n_
> worker 进程数量。

**--reload**
> 代码变化时自动重载（仅用于开发）。

**-c**, **--config** _FILE_
> 从 TOML 文件加载配置，或通过 `python:module` / `file:path.py` 使用 Python 源文件。

**--access-logfile** _FILE_
> 访问日志的目标；用 `-` 表示 stdout。（`--access-log` 仍可用但已弃用。）

**--access-logformat** _FORMAT_
> 访问日志行的格式字符串。

**--error-logfile**, **--log-file** _FILE_
> 错误日志的目标；用 `-` 表示 stderr。（`--error-log` 仍可用但已弃用。）

**--log-level** _LEVEL_
> 错误日志详细程度（默认为 info）。

**--certfile** _FILE_
> SSL 证书文件的路径。

**--keyfile** _FILE_
> SSL 密钥文件的路径。

**--ca-certs** _FILE_
> SSL CA 证书文件的路径。

**--worker-class**, **-k** _CLASS_
> worker 类型：`asyncio`（默认）、`uvloop` 或 `trio`。

**--graceful-timeout** _SECONDS_
> 收到 SIGTERM/Ctrl-C 后等待进行中的请求完成的时间。

**--keep-alive** _SECONDS_
> 空闲连接保持打开的时长。

**--max-requests** _N_
> worker 处理完指定数量的请求后重启。

**-p**, **--pid** _FILE_
> 将 PID 写入文件。

**-D**, **--daemon**
> 以守护进程方式运行 worker。

**--quic-bind** _ADDRESS_
> 为支持 HTTP/3 而绑定的 UDP/QUIC host:port（实验性）。

**--insecure-bind** _ADDRESS_
> 额外绑定的不带 SSL 的 TCP host:port（例如用于 HTTP 到 HTTPS 的重定向）。

# DESCRIPTION

**Hypercorn** 是一个 ASGI 服务器，支持 HTTP/1、HTTP/2 和 WebSocket（基于 HTTP/1 和 HTTP/2），并通过 **--quic-bind** 实验性地支持 HTTP/3。它可以运行 FastAPI、Starlette、Quart 等 ASGI 应用，也能服务 WSGI 应用。

它构建于 `hyper` 系列的 sans-I/O 库之上（h11、h2、wsproto），可通过 **--worker-class** 在 asyncio、uvloop 或 trio 上运行事件循环，提供面向生产环境的特性，包括多 worker 进程、优雅关闭以及除 CLI 参数之外的 TOML/Python 配置方式。

# CAVEATS

向浏览器提供 HTTP/2 需要 TLS（**--certfile**/**--keyfile**）；明文 HTTP/2（h2c）可用于非浏览器客户端。**--reload** 仅用于开发。与其他 ASGI 服务器一样，建议在生产环境中置于反向代理（nginx、Caddy）之后，以处理 TLS 终止和静态文件服务。

# HISTORY

Hypercorn 由 **Philip Jones**（pgjones）创建，他也是 **Quart** 框架的作者；Hypercorn 最初是 Quart 内置的服务器，后来被拆分为独立的、不依赖特定框架的 ASGI 服务器。

# INSTALL

```pacman: sudo pacman -S hypercorn```

```apk: sudo apk add py3-hypercorn```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[uvicorn](/man/uvicorn)(1), [gunicorn](/man/gunicorn)(1), [daphne](/man/daphne)(1)

# RESOURCES

```[Source code](https://github.com/pgjones/hypercorn)```

```[Documentation](https://hypercorn.readthedocs.io/en/latest/)```

<!-- verified: 2026-07-19 -->
