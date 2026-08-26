# TAGLINE

纯 Python 的 WSGI 生产级服务器

# TLDR

**在默认端口 8080 上运行 WSGI 应用**

```waitress-serve [myapp:app]```

**绑定到指定的主机和端口**

```waitress-serve --host=[127.0.0.1] --port=[8080] [myapp:app]```

**监听多个地址**

```waitress-serve --listen=[127.0.0.1:8080] --listen=[127.0.0.1:8443] [myapp:app]```

**使用应用工厂函数**

```waitress-serve --call [myapp:create_app]```

**监听 Unix 套接字**

```waitress-serve --unix-socket=[/tmp/app.sock] [myapp:app]```

**设置工作线程数**

```waitress-serve --threads=[8] [myapp:app]```

**在 URL 前缀下运行应用（位于反向代理之后时）**

```waitress-serve --url-prefix=[/api] [myapp:app]```

# SYNOPSIS

**waitress-serve** [_--host addr_] [_--port port_] [_options_] _module:app_

# PARAMETERS

**--host** _ADDR_
> 要监听的主机名或 IP 地址。默认：`0.0.0.0`。

**--port** _PORT_
> 要监听的 TCP 端口。默认：`8080`。

**--listen** _HOST:PORT_
> 绑定到特定的 host:port 对。可重复使用以监听多个地址。支持 `*` 作为通配主机。

**--threads** _N_
> 处理请求的工作线程数。默认：`4`。

**--unix-socket** _PATH_
> Unix 域套接字的路径（Windows 上不可用）。

**--unix-socket-perms** _OCTAL_
> Unix 套接字的八进制权限。默认：`600`。

**--url-scheme** _SCHEME_
> `wsgi.url_scheme` 的值。默认：`http`。

**--url-prefix** _PREFIX_
> `SCRIPT_NAME` 的值（用于挂载在子路径下的应用）。默认：空。

**--ident** _STRING_
> 在 `Server` 响应头中发送的服务器标识。默认：`waitress`。

**--call**
> 将位置参数视为返回 WSGI 应用的可调用工厂，而不是直接将其作为应用使用。

**--connection-limit** _N_
> 同时连接的最大数量。默认：`100`。

**--channel-timeout** _SECONDS_
> 非活动连接的超时时间。默认：`120`。

**--trusted-proxy** _IP_
> 可提供转发头的受信任反向代理的 IP 地址。

# DESCRIPTION

**waitress-serve** 是一个面向 Python Web 应用的生产级 WSGI 服务器，完全用纯 Python 实现，不依赖 C 扩展。它可以为 Flask、Django、Pyramid 等框架提供服务，并能运行在任何平台上，包括 Windows、Linux 和 macOS。

该服务器采用多线程架构，工作线程数量可配置，用于处理并发请求。它接受来自 TCP 端口或 Unix 套接字的连接，并支持 URL 前缀配置，适用于挂载在反向代理之后子路径上的应用。

Waitress 的设计目标是让生产部署简单可靠，只需极少配置即可提供稳健的性能。它常与 Nginx 等反向代理配合使用，由代理负责静态文件服务和 SSL 卸载。

# CAVEATS

仅支持 WSGI。不支持 ASGI。请配置在代理之后使用。

# HISTORY

**Waitress** 由 **Pylons Project** 创建，是一个生产级的纯 Python WSGI 服务器。

# INSTALL

```apk: sudo apk add py3-waitress```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gunicorn](/man/gunicorn)(1), [uwsgi](/man/uwsgi)(1), [uvicorn](/man/uvicorn)(1), [hypercorn](/man/hypercorn)(1), [flask](/man/flask)(1)
