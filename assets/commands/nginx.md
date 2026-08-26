# TAGLINE

Web 服务器与反向代理

# TLDR

**启动 nginx**

```nginx```

**测试配置文件**

```nginx -t```

**重新加载配置**

```nginx -s reload```

**停止 nginx**

```nginx -s stop```

**优雅关闭**

```nginx -s quit```

**显示版本**

```nginx -v```

**测试配置并将其转储**到标准输出

```nginx -T```

**使用指定的配置文件**

```nginx -c [/etc/nginx/nginx.conf]```

**在启动时设置全局指令**

```nginx -g "[daemon off;]"```

# SYNOPSIS

**nginx** [_-?hqtTvV_] [_-s signal_] [_-p prefix_] [_-e filename_] [_-c filename_] [_-g directives_]

# PARAMETERS

**-?**, **-h**
> 打印命令行参数的帮助信息。

**-t**
> 测试配置文件：nginx 先检查语法，然后尝试打开配置中引用的文件。

**-T**
> 与 **-t** 相同，但还会把配置文件转储到标准输出（1.9.2+）。

**-q**
> 测试配置期间抑制非错误消息。

**-s** _SIGNAL_
> 向主进程发送信号。信号可以是以下之一：**stop**（快速关闭）、**quit**（优雅关闭）、**reload**（重新加载配置）或 **reopen**（重新打开日志文件）。

**-p** _PREFIX_
> 设置路径前缀，即存放服务器文件的目录。默认为 _/usr/local/nginx_。

**-e** _FILE_
> 使用替代的错误日志文件。特殊值 **stderr** 表示写入标准错误（1.19.5+）。

**-c** _FILE_
> 使用替代的配置文件，而非默认的 _prefix/conf/nginx.conf_。

**-g** _DIRECTIVES_
> 设置全局配置指令，例如 `nginx -g "pid /var/run/nginx.pid;"`。

**-v**
> 打印 nginx 版本。

**-V**
> 打印 nginx 版本、编译器版本以及 configure 参数。

# DESCRIPTION

**nginx**（读作 "engine x"）是一款高性能的 HTTP 与反向代理服务器，同时也是邮件（IMAP/POP3/SMTP）代理服务器。它采用事件驱动、异步架构设计，能以低且可预测的内存占用处理大量并发连接。

不带任何参数运行 **nginx** 会直接启动服务器（前台运行或以守护进程方式运行，取决于配置）。启动之后，可通过 **-s** 发送信号在运行时控制主进程，而无需重启。配置变更通过 `nginx -s reload` 应用，它会启动新的 worker 进程并优雅地关闭旧进程。

除了提供静态文件服务之外，nginx 还被广泛用作部署在应用服务器之前的反向代理、负载均衡器、TLS 终结点和 HTTP 缓存。

# CAVEATS

其行为完全由配置文件决定；重新加载前请务必用 **-t** 验证改动。帮助信息和默认值中出现的路径是相对编译时前缀而言的，在各发行版的软件包中通常不同（常见的是 _/etc/nginx/nginx.conf_）。

# HISTORY

nginx 由 **Igor Sysoev** 创建，于 **2004 年**首次公开发布，目的是解决大量并发连接带来的 C10k 问题。如今由 **F5, Inc.** 开发，支撑着互联网上相当大比例的高流量网站。

# INSTALL

```apt: sudo apt install nginx```

```dnf: sudo dnf install nginx```

```pacman: sudo pacman -S nginx```

```apk: sudo apk add nginx```

```zypper: sudo zypper install nginx```

```brew: brew install nginx```

```nix: nix profile install nixpkgs#nginx```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[apache2](/man/apache2)(8), [caddy](/man/caddy)(1), [haproxy](/man/haproxy)(1)
