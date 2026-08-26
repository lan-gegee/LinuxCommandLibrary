# TAGLINE

适用于 Unix 的 Python WSGI HTTP 服务器

# TLDR

**运行 WSGI 应用程序**

```gunicorn [myapp:app]```

**在指定的主机和端口上运行**

```gunicorn --bind [0.0.0.0:8000] [myapp:app]```

**使用多个 worker 运行**

```gunicorn --workers [4] [myapp:app]```

**自动重启 worker 运行**

```gunicorn --reload [myapp:app]```

**开启访问日志运行**

```gunicorn --access-logfile [access.log] [myapp:app]```

**以守护进程方式运行**（后台）

```gunicorn --daemon --pid [gunicorn.pid] [myapp:app]```

**使用 Unix 套接字运行**

```gunicorn --bind unix:[/tmp/gunicorn.sock] [myapp:app]```

**使用异步 worker**（gevent）

```gunicorn --worker-class [gevent] --workers [4] [myapp:app]```

# SYNOPSIS

**gunicorn** [_options_] _APP_MODULE_

# PARAMETERS

**-b**, **--bind** _ADDRESS_
> 要绑定的套接字（HOST:PORT、unix:PATH 或 fd://FD）。

**-w**, **--workers** _INT_
> worker 进程数量（默认为 1）。

**-k**, **--worker-class** _STRING_
> worker 类型：sync、gevent、eventlet、tornado、gthread。

**--threads** _INT_
> 每个 worker 的线程数（用于 gthread worker）。

**-t**, **--timeout** _INT_
> worker 超时时间，单位为秒（默认为 30）。

**--graceful-timeout** _INT_
> worker 优雅重启的超时时间。

**--reload**
> 代码变更时重启 worker（仅用于开发）。

**-D**, **--daemon**
> 以守护进程方式运行。

**-p**, **--pid** _FILE_
> PID 文件路径。

**--access-logfile** _FILE_
> 访问日志文件（- 表示标准输出）。

**--error-logfile** _FILE_
> 错误日志文件（- 表示标准错误）。

**--log-level** _LEVEL_
> 日志级别：debug、info、warning、error、critical。

**-c**, **--config** _FILE_
> 配置文件路径。

**--preload**
> 在 fork worker 之前加载应用程序代码。

**--max-requests** _INT_
> 处理这么多请求后重启 worker（0 表示禁用）。有助于防止内存泄漏。

**--max-requests-jitter** _INT_
> 添加到 max-requests 的随机抖动量，使重启时机错开。

**--keep-alive** _INT_
> Keep-Alive 连接上等待请求的秒数（默认为 2）。

**-n**, **--name** _STRING_
> ps 输出中显示的进程名。

**-u**, **--user** _USER_
> 让 worker 进程以此用户身份运行。

**-g**, **--group** _GROUP_
> 让 worker 进程以此组身份运行。

# DESCRIPTION

**Gunicorn**（Green Unicorn）是一个面向 Unix 系统的 Python WSGI HTTP 服务器，专为在生产环境中服务 Web 应用而设计，采用 pre-fork worker 模型。主进程管理一个 worker 进程池，每个 worker 进程独立处理传入的请求。应用程序以 **module:variable** 形式指定（例如 Flask 使用 `myapp:app`，Django 使用 `myproject.wsgi:application`），推荐的 worker 数量为 **(2 x CPU 核心数) + 1**，以在并发能力与内存占用之间取得平衡。

默认的同步 worker 每个进程一次只处理一个请求，适合 CPU 密集型应用。对于并发连接众多的 I/O 密集型工作负载，`gevent` 或 `eventlet` 等异步 worker 类使用协作式多线程，在更少的进程内复用数千个连接，而 `gthread` worker 则使用操作系统线程。超过可配置超时时间的 worker 会被主进程自动终止并重启，从而对挂起的请求提供容错能力。

在生产环境中，Gunicorn 通常运行在 Nginx 等反向代理之后，由代理负责 SSL 终止、静态文件服务和请求缓冲。代理与 Gunicorn 之间通过 HTTP 或 Unix 域套接字通信。

# CAVEATS

不支持 Windows。没有缓冲代理时，同步 worker 会被慢速客户端阻塞。--reload 仅用于开发。--preload 可能与某些框架产生冲突。worker 超时后无论正在做什么都会被终止。

# HISTORY

**Gunicorn** 由 Benoît Chesneau 创建，首个版本发布于约 **2010 年**。其名称是 "Green Unicorn" 的合成词。它的设计初衷是将 Ruby 的 Unicorn 服务器移植到 Python，把 pre-fork 架构带入 Python 世界。Gunicorn 已成为 Python Web 应用最流行的 WSGI 服务器之一。

# INSTALL

```pacman: sudo pacman -S gunicorn```

```apk: sudo apk add py3-gunicorn```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[uvicorn](/man/uvicorn)(1), [uwsgi](/man/uwsgi)(1), [nginx](/man/nginx)(8), [flask](/man/flask)(1), [django-admin](/man/django-admin)(1)
