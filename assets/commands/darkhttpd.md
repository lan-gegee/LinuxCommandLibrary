# TAGLINE

简单、快速且安全的静态 Web 服务器

# TLDR

**在默认端口伺服当前目录**

```darkhttpd .```

**在自定义端口伺服指定目录**

```darkhttpd [/path/to/webroot] --port [8080]```

**绑定到指定地址**

```darkhttpd . --addr [127.0.0.1]```

**设置自定义索引文件**

```darkhttpd . --index [home.html]```

**禁用目录列表**

```darkhttpd . --no-listing```

**伺服并记录日志**到 stdout

```darkhttpd . --log -```

**以虚拟主机方式伺服**

```darkhttpd . --forward [example.com] [http://backend:8000]```

**以守护进程方式运行**（后台）

```darkhttpd . --daemon --pidfile [/var/run/darkhttpd.pid]```

# SYNOPSIS

**darkhttpd** _docroot_ [_--port port_] [_--addr address_] [_--daemon_] [_--log file_] [_--index file_] [_options_]

# PARAMETERS

**--port** _port_
> 监听端口（root 运行时默认 80，否则为 8080）。

**--addr** _address_
> 要绑定的地址（默认：所有接口）。

**--daemon**
> fork 到后台运行。

**--pidfile** _file_
> 守护化后将 PID 写入文件。

**--log** _file_
> 将请求记录到文件（- 表示 stdout）。

**--index** _file_
> 目录请求时伺服的默认索引文件（默认：index.html）。

**--no-listing**
> 禁用目录列表（目录列表默认开启）。

**--timeout** _seconds_
> 连接超时时间（默认：60）。

**--uid** _uid_
> 将权限降至此用户 ID。

**--gid** _gid_
> 将权限降至此组 ID。

**--chroot**
> chroot 到文档根目录。

**--maxconn** _n_
> 限制同时连接的数量。

**--forward** _host_ _url_
> 将 Host 头匹配的请求 301 重定向到给定 URL。

**--forward-all** _url_
> 将所有请求 301 重定向到给定 URL（全捕获）。

**--forward-https** _host_ _url_
> 将该主机的 HTTP 请求 301 重定向到 HTTPS。

**--no-keepalive**
> 禁用 HTTP keep-alive。

**--no-server-id**
> 响应中省略 Server 标识头。

**--mimetypes** _file_
> 从文件加载 MIME 类型。

**--default-mimetype** _type_
> 扩展名未知的文件以此 MIME 类型伺服。

**--hide-dotfiles**
> 不伺服以点开头的文件或目录。

**--single-file** _file_
> 只伺服指定的单个文件而非目录。

**--auth** _user:password_
> 启用 HTTP Basic 认证。

**--syslog**
> 使用 syslog 而非文件记录请求日志。

**--header** _header_
> 添加自定义响应头（可重复使用）。

# DESCRIPTION

**darkhttpd** 是一个简单、快速且安全的静态 Web 服务器。它用 C 编写且无任何依赖，编译后是单个很小的二进制文件，能以极少的资源占用伺服静态文件。

该服务器的设计理念就是简单：从文档根目录以正确的 MIME 类型伺服文件，处理 HTTP/1.1 keep-alive 连接，并支持 chroot 和权限降级等安全特性。它没有配置文件，所有选项都是命令行参数。

目录列表默认开启，可用 **--no-listing** 关闭。可用 **--index** 指定自定义索引文件来覆盖默认的 **index.html**。服务器会发送正确的缓存头，并支持可断点续传的 range 请求。

面向生产用途时，darkhttpd 支持守护化、创建 PID 文件和日志记录。chroot 与 uid/gid 选项提供安全隔离。它虽不为高流量网站而设计，但对于本地开发、嵌入式系统或看重简洁性的静态内容伺服场景表现出色。

# CAVEATS

仅支持静态文件；不支持 CGI、PHP 或动态内容。没有 SSL/TLS；HTTPS 需借助反向代理。没有配置文件；所有设置都通过命令行。仅限于 HTTP/1.1 特性。不适合高并发的生产负载。

# HISTORY

**darkhttpd** 由 Emil Mikulic 于 **2003 年**创建，是一款简单、可移植的 HTTP 服务器。其设计哲学强调极简与安全胜过功能丰富。单文件的 C 源码几乎能在任何类 Unix 系统上无依赖编译，因此在嵌入式系统和极简环境中广受欢迎。

# INSTALL

```dnf: sudo dnf install darkhttpd```

```pacman: sudo pacman -S darkhttpd```

```apk: sudo apk add darkhttpd```

```zypper: sudo zypper install darkhttpd```

```brew: brew install darkhttpd```

```nix: nix profile install nixpkgs#darkhttpd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nginx](/man/nginx)(8), [python3](/man/python3)(1), [caddy](/man/caddy)(1), [busybox](/man/busybox)(1)
