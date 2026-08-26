# TAGLINE

Deluge BitTorrent 客户端的守护进程组件

# TLDR

**启动 Deluge 守护进程**

```deluged```

**在指定端口启动守护进程**

```deluged -p [58846]```

**以前台方式启动**

```deluged -d```

**使用指定的配置目录**

```deluged -c [~/.config/deluge]```

**启动并将日志写入文件**

```deluged -l [/var/log/deluged.log]```

**启用 debug 级日志**

```deluged -L debug```

# SYNOPSIS

**deluged** [_options_]

# PARAMETERS

**-p**, **--port** _PORT_
> 守护进程监听端口（默认：58846）。

**-i**, **--interface** _IP_
> 要监听的网络接口。

**-d**, **--do-not-daemonize**
> 以前台方式运行。

**-c**, **--config** _DIR_
> 配置目录。

**-l**, **--logfile** _FILE_
> 将日志写入指定文件。

**-L**, **--loglevel** _LEVEL_
> 日志级别：none、error、warning、info、debug。

**-P**, **--pidfile** _FILE_
> PID 文件位置。

**--help**
> 显示帮助信息。

# DESCRIPTION

**deluged** 是 Deluge BitTorrent 客户端的守护进程组件。它负责所有 BitTorrent 协议操作，并在后台运行，允许客户端连接进行管理。

这种守护进程架构让 Deluge 可以运行在无头服务器上，客户端远程连接即可。多个客户端（GTK、web、console）可以同时连接同一个守护进程。即使客户端断开，下载也会继续进行。

deluged 在可配置的端口上监听客户端连接并处理认证，确保对种子管理功能的访问安全可控。

# CONFIGURATION

**~/.config/deluge/**
> 配置目录，包含 core.conf、auth 认证文件和状态文件。

# CAVEATS

远程访问需要正确的端口配置。防火墙规则可能需要调整。要实现安全的远程访问必须配置认证。资源占用取决于活跃种子的数量。

# HISTORY

deluged 是 Deluge BitTorrent 客户端的核心组件，自 **2006 年**开始开发。守护进程/客户端分离是一项关键设计决策，使其能够灵活部署于从桌面应用到专用做种机的各种场景。

# INSTALL

```dnf: sudo dnf install deluge```

```pacman: sudo pacman -S deluge```

```apk: sudo apk add deluge```

```zypper: sudo zypper install deluge```

```nix: nix profile install nixpkgs#deluge```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[deluge](/man/deluge)(1), [deluge-console](/man/deluge-console)(1)
