# TAGLINE

轻量级 Subversion 仓库服务器

# TLDR

**以守护进程方式启动**并提供仓库服务

```svnserve -d -r [/path/to/repos]```

为便于调试而**在前台启动**

```svnserve -d --foreground -r [/path/to/repos]```

**监听指定端口**

```svnserve -d -r [/path/to/repos] --listen-port [3690]```

**监听指定网卡**

```svnserve -d -r [/path/to/repos] --listen-host [192.168.1.1]```

**以 inetd 模式运行**

```svnserve -i```

**以隧道模式运行**（配合 SSH）

```svnserve -t```

**使用自定义配置文件**

```svnserve -d -r [/path/to/repos] --config-file [/etc/svnserve.conf]```

# SYNOPSIS

**svnserve** [_options_]

# PARAMETERS

**-d**, **--daemon**
> 以守护进程方式运行，在 svn 端口（3690）接受 TCP 连接。

**-i**, **--inetd**
> 以 inetd 模式通过标准输入/标准输出来运行。

**-t**, **--tunnel**
> 以隧道模式运行，用于 SSH 访问（已完成预认证）。

**-X**, **--listen-once**
> 接受一个连接，提供服务后退出。

**-r**, **--root** _path_
> 设置所服务仓库的虚拟根目录。

**--listen-port** _port_
> 监听指定端口（默认 3690）。

**--listen-host** _host_
> 监听指定的接口或主机名。

**--foreground**
> 保持在前台运行（配合 -d），便于调试。

**--tunnel-user** _name_
> 在隧道模式下覆盖已认证的用户名。

**--config-file** _file_
> 使用指定的配置文件。

**--pid-file** _file_
> 将进程 ID 写入文件。

**--log-file** _file_
> 将日志写入指定文件。

**--threads**
> 使用线程而不是 fork 子进程。

**--min-threads** _n_
> 线程池中的最小线程数。

**--max-threads** _n_
> 线程池中的最大线程数。

**-h**, **--help**
> 显示用法信息。

**--version**
> 显示版本信息。

# DESCRIPTION

**svnserve** 是一个轻量级的 Subversion 仓库服务器，使用 Subversion 自定义的网络协议。它通过 svn:// 和 svn+ssh:// URL 方案提供对仓库的访问。

服务器支持多种运行模式：作为监听 TCP 端口 3690 的独立守护进程、作为 inetd/xinetd 服务，或者作为由 SSH 启动的隧道进程。隧道模式允许在不暴露 svn 端口的情况下进行安全访问。

-r 选项设置虚拟根目录，将客户端访问限制在该路径下的仓库内，同时简化 URL。认证可以按仓库配置，也可以通过共享配置文件全局配置。

对于高流量环境，svnserve 支持使用线程池代替"每个连接 fork 一个进程"的方式。

# CAVEATS

除非通过 SSH 隧道传输或配置了 SASL，否则默认使用明文认证。没有内置 SSL 支持；加密请使用 SSH 隧道或 svn+ssh://。访问控制不如基于 Apache 的服务方式细粒度。守护进程模式要求防火墙放行端口 3690。

# HISTORY

**svnserve** 从早期版本起就包含在 Subversion 中，作为基于 Apache 的仓库服务方式的轻量替代。它为小型部署提供更快的搭建速度和更低的开销。svn:// 协议的设计追求简单，而 svn+ssh:// 则借助 SSH 实现认证和加密。

# INSTALL

```apt: sudo apt install subversion```

```dnf: sudo dnf install subversion```

```pacman: sudo pacman -S subversion```

```apk: sudo apk add subversion```

```zypper: sudo zypper install subversion```

```brew: brew install subversion```

```nix: nix profile install nixpkgs#subversion```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[svnadmin](/man/svnadmin)(1), [svn](/man/svn)(1), [sshd](/man/sshd)(8)
