# TAGLINE

通过 Web 共享终端会话

# TLDR

**通过 Web 共享 bash shell**

```ttyd bash```

**在指定端口上共享**

```ttyd -p [8080] bash```

**启用身份验证共享**

```ttyd -c [username]:[password] bash```

**以只读模式共享**

```ttyd -R bash```

**通过 Web 共享 vim 编辑器**

```ttyd vim [file.txt]```

**与多个客户端共享 tmux 会话**

```ttyd tmux new -A -s [session_name]```

**使用 SSL 加密共享**

```ttyd --ssl --ssl-cert [cert.pem] --ssl-key [key.pem] bash```

**绑定到指定网络接口**

```ttyd -i [eth0] bash```

# SYNOPSIS

**ttyd** [_options_] _command_ [_arguments_...]

# PARAMETERS

**-p**, **--port** _port_
> 监听端口（默认：7681，设为 0 表示随机）

**-i**, **--interface** _interface_
> 要绑定的网络接口（例如 eth0）或 Unix 套接字路径

**-c**, **--credential** _user:pass_
> Basic 身份验证凭据

**-u**, **--uid** _uid_
> 运行命令使用的用户 ID

**-g**, **--gid** _gid_
> 运行命令使用的组 ID

**-R**, **--readonly**
> 不允许客户端写入 TTY

**-W**, **--writable**
> 允许客户端写入（多客户端时默认只读）

**-s**, **--signal** _signal_
> 退出时发送的信号（默认：1，SIGHUP）

**--ssl**
> 启用 SSL/TLS 加密

**--ssl-cert** _file_
> SSL 证书文件路径

**--ssl-key** _file_
> SSL 密钥文件路径

**-O**, **--once**
> 只接受一个客户端，断开后退出

**-d**, **--debug** _level_
> 设置日志级别（0-9，默认：7）

# DESCRIPTION

**ttyd** 使用 WebSocket 通过 Web 共享终端会话。它会启动一个 web 服务器（默认端口 7681），提供可从任何浏览器访问的终端界面。这样无需配置 SSH 即可实现远程终端访问、协作和演示。

任何命令都可以被共享，不限于 shell。运行 **ttyd vim** 可提供基于 web 的 vim 编辑器。结合 **tmux** 可以让多个用户同时共享同一个会话。

该工具支持通过 **-c** 进行 Basic 身份验证、使用 SSL 加密实现安全连接，并可将客户端限制为只读模式。它支持 Unicode 和 CJK 字符，并可通过 ZMODEM 传输文件。

ttyd 可在 Linux、macOS、FreeBSD、OpenBSD 和 Windows 上运行。

# CAVEATS

默认情况下 ttyd 不提供身份验证；在生产环境中务必使用 **-c** 或防火墙规则。未配合 tmux 时，多个客户端连接会各自获得独立会话。默认端口 7681 可能需要配置防火墙才能从外部访问。

# HISTORY

**ttyd** 由 **Shuanglei Tao**（tsl0922）创建，于 **2016 年**前后首次发布。它用 C 编写，使用 libwebsockets 处理 WebSocket 通信，使用 xterm.js 实现浏览器端终端。该项目受 shellinabox 等较早工具启发，但采用了现代 web 技术。

# INSTALL

```dnf: sudo dnf install ttyd```

```pacman: sudo pacman -S ttyd```

```apk: sudo apk add ttyd```

```zypper: sudo zypper install ttyd```

```brew: brew install ttyd```

```nix: nix profile install nixpkgs#ttyd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tmux](/man/tmux)(1), [screen](/man/screen)(1), [gotty](/man/gotty)(1), [ssh](/man/ssh)(1)
