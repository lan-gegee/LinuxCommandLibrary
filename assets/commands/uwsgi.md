# TAGLINE

面向 Python Web 框架的应用服务器

# TLDR

带 HTTP 服务器**运行 WSGI 应用**

```uwsgi --http :8080 --wsgi-file [app.py]```

**以多进程和多线程运行**

```uwsgi --http :8080 --wsgi-file [app.py] --master --processes [4] --threads [2]```

**使用 Unix 套接字运行**以配合 Nginx

```uwsgi --socket [/tmp/uwsgi.sock] --wsgi-file [app.py] --chmod-socket=666```

**运行 Django 应用**

```uwsgi --http :8080 --module [myproject.wsgi]:application```

**从配置文件启动**

```uwsgi --ini [uwsgi.ini]```

**启用统计服务器**

```uwsgi --http :8080 --wsgi-file [app.py] --stats 127.0.0.1:9191```

# SYNOPSIS

**uwsgi** [_options_]

# PARAMETERS

**--http** _address_
> 在指定的 地址:端口 上启用 HTTP 服务器

**--socket** _address_
> 绑定到指定的 UNIX/TCP 套接字，使用 uwsgi 协议

**--wsgi-file** _file_
> 从 Python 文件加载 WSGI 应用

**--module** _module_
> 从指定的模块加载 WSGI 应用

**--master**
> 启用主进程来管理 worker

**--processes** _n_
> 启动 n 个 worker 进程

**--threads** _n_
> 每个 worker 进程运行 n 个线程

**--chdir** _path_
> 加载应用前切换到指定目录

**--virtualenv** _path_
> 使用指定的 Python virtualenv

**--ini** _file_
> 从 INI 文件加载配置

**--stats** _address_
> 在指定地址启用统计服务器

**--chmod-socket**
> 设置套接字文件权限

# DESCRIPTION

**uWSGI** 是一个实现了 WSGI 规范的应用服务器，用于服务 Python Web 应用。它是 Nginx 等 Web 服务器与 Django、Flask、Pyramid 等 Python 框架之间的桥梁。

该服务器支持多种协议：用于直接服务的 HTTP、用于与 Nginx 高效通信的 uwsgi 二进制协议，以及用于本地进程间通信的套接字。它还处理进程管理、负载均衡和缓存。

配置可以通过命令行选项或 INI/YAML/JSON 文件提供。主进程模式支持平滑重载和 worker 的自动重启。

# CAVEATS

uWSGI 自 **2022 年 10 月**起处于维护模式。新项目可考虑 Gunicorn 等替代品。uwsgi 协议（小写）不同于 uWSGI 应用服务器。在 Nginx 后面运行时，套接字权限需要仔细配置。

# HISTORY

uWSGI 最初是作为支持多种语言和协议的全栈应用服务器开发的。尽管其名称来源于 WSGI，但它后来扩展到支持 Ruby（Rack）、Perl（PSGI）等语言。该项目在 Python 部署领域得到了广泛采用。

# INSTALL

```dnf: sudo dnf install uwsgi```

```pacman: sudo pacman -S uwsgi```

```apk: sudo apk add uwsgi```

```zypper: sudo zypper install uwsgi```

```brew: brew install uwsgi```

```nix: nix profile install nixpkgs#uwsgi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gunicorn](/man/gunicorn)(1), [nginx](/man/nginx)(8), [python](/man/python)(1), [pip](/man/pip)(1)
