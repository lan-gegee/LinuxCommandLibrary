# TAGLINE

极速的 Python ASGI Web 服务器

# TLDR

**运行 ASGI 应用**

```uvicorn [main:app]```

**启用自动重载运行**

```uvicorn [main:app] --reload```

**绑定到指定的主机和端口**

```uvicorn [main:app] --host [0.0.0.0] --port [8000]```

**以多个 worker 运行**

```uvicorn [main:app] --workers [4]```

**以 SSL 运行**

```uvicorn [main:app] --ssl-keyfile [key.pem] --ssl-certfile [cert.pem]```

**使用特定的事件循环**（性能场景用 uvloop）

```uvicorn [main:app] --loop uvloop```

**通过 Unix 套接字运行**

```uvicorn [main:app] --uds [/tmp/uvicorn.sock]```

**指定日志级别**

```uvicorn [main:app] --log-level [debug]```

# SYNOPSIS

**uvicorn** _app_ [_--host host_] [_--port port_] [_--reload_] [_--workers num_] [_options_]

# PARAMETERS

**--host** _HOST_
> 将套接字绑定到主机（默认：127.0.0.1）。

**--port** _PORT_
> 将套接字绑定到端口（默认：8000）。

**--uds** _PATH_
> 绑定到 Unix 域套接字。

**--fd** _NUM_
> 绑定到来自文件描述符的套接字。

**--reload**
> 启用代码变更时自动重载。

**--reload-dir** _PATH_
> 重载时要监视的目录。

**--reload-include** _PATTERN_
> 重载时要包含的模式。

**--reload-exclude** _PATTERN_
> 重载时要排除的模式。

**--workers** _NUM_
> worker 进程的数量。

**--loop** _IMPL_
> 事件循环：auto、uvloop、asyncio。

**--http** _IMPL_
> HTTP 实现：auto、h11、httptools。

**--ws** _IMPL_
> WebSocket 实现：auto、websockets、wsproto。

**--interface** _TYPE_
> 接口类型：auto、asgi3、asgi2、wsgi。

**--log-level** _LEVEL_
> 日志级别：critical、error、warning、info、debug、trace。

**--access-log** / **--no-access-log**
> 启用/禁用访问日志。

**--ssl-keyfile** _PATH_
> SSL 密钥文件。

**--ssl-certfile** _PATH_
> SSL 证书文件。

# DESCRIPTION

**uvicorn** 是一个速度极快的 Python ASGI 服务器。它服务于 FastAPI、Starlette 等实现了 ASGI 规范的异步 Web 框架。

ASGI（Asynchronous Server Gateway Interface，异步服务器网关接口）支持以 async/await 方式处理 HTTP、WebSocket 及其他协议。Uvicorn 实现了服务器一侧，与异步应用代码相连接。

开发模式（--reload）会监视文件并在发生变更时重启。这使快速迭代成为可能，无需手动重启服务器。

生产部署使用多个 worker（--workers）来利用 CPU 核心。每个 worker 都是独立处理请求的独立进程。进程管理机制会处理 worker 崩溃的情况。

其性能来源于可选的 uvloop（基于 libuv 的事件循环）和 httptools（HTTP 解析）。这些基于 C 的库显著优于纯 Python 实现。

WebSocket 支持实现了实时的双向通信。服务器负责处理连接升级并将消息路由到应用代码。

# CAVEATS

worker 之间不共享任何状态——状态必须使用外部存储。重载模式不应在生产环境中使用。Windows 上没有 uvloop。SSL 终止放在反向代理处通常更好。文件上传受内存限制。

# HISTORY

**uvicorn** 由 **Tom Christie**（Django REST framework 和 Starlette 的作者）于 **2017 年**前后创建。它实现了让异步 Python Web 框架成为可能的 ASGI 规范。名称引用了 UV（高能光线）以及 Python Web 服务器中常见的后缀 -corn。

# INSTALL

```pacman: sudo pacman -S uvicorn```

```apk: sudo apk add uvicorn```

```brew: brew install uvicorn```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gunicorn](/man/gunicorn)(1), [hypercorn](/man/hypercorn)(1), [daphne](/man/daphne)(1)
