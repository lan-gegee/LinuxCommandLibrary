# TAGLINE

追踪 X11 客户端与服务器之间的协议通信

# TLDR

**追踪 X11 客户端**并打印所有协议消息

```xtrace [xeyes]```

**转发到指定的**真实 display

```xtrace --display [:0] [firefox]```

**设置自定义的伪** display 名

```xtrace --fakedisplay [:42] [xclock]```

被启动的客户端退出后**让 xtrace 继续运行**

```xtrace --keeprunning [xterm]```

**等待后续客户端**连接后再退出

```xtrace --waitforclient --fakedisplay [:42]```

将追踪输出**写入文件**

```xtrace --outfile [trace.log] [xeyes]```

为每条协议消息**显示相对时间戳**

```xtrace --relative-timestamps [xclock]```

# SYNOPSIS

**xtrace** [_options_] [_command_ [_arguments_ ...]]

# PARAMETERS

**-d**, **--display** _DISPLAY_
> 接收转发的真实 X server（默认为 **$DISPLAY**）。

**-D**, **--fakedisplay** _DISPLAY_
> xtrace 监听的伪 display 名（默认 **:9**）。

**-k**, **--keeprunning**
> 被启动的客户端断开连接后继续运行。

**-s**, **--stopwhendone**
> 所有客户端断开连接后终止（默认行为）。

**-W**, **--waitforclient**
> 即使被启动的程序未连接就退出也不结束运行。

**-c**, **--copyauthentication**
> 从真实 display 复制 X 认证 cookie（默认）。

**-n**, **--nocopyauthentication**
> 不向伪 display 复制认证数据。

**-f** _file_
> 从 _file_ 读取认证数据。

**-F** _file_
> 将生成的认证数据写入 _file_。

**-o**, **--outfile** _FILE_
> 将追踪输出写入 _FILE_ 而不是 stdout。

**-b**, **--buffered**
> 缓冲追踪输出以提高性能。

**-w**, **--readwritedebug**
> 为每次读写操作附带字节数。

**--timestamps**
> 为每条记录添加绝对墙上时间戳前缀。

**--relative-timestamps**
> 为每条记录添加距上一条记录的时间间隔前缀。

**--monotonic-timestamps**
> 为每条记录添加单调时钟来源的时间戳前缀。

# DESCRIPTION

**xtrace** 是一个调试工具，用于检查 X 客户端（如 GUI 应用程序）与 X server（如 **Xorg** 或 **Xwayland**）之间的 X11 线路协议流量。它在选定的 display 编号上启动一个伪 X server，把每个连接转发到 **$DISPLAY**（或 **--display**）指向的真实 X server，并打印流经线路的每个请求、应答、事件和错误的人类可读日志。

被启动程序的 **$DISPLAY** 环境变量会被改写为伪 display，因此它会透明地经由 xtrace 连接。这样就能看到应用程序启动时发出了哪些 X 请求、服务器投递了哪些事件、协议错误发生在哪里——而无需修改应用程序本身。

当未给出命令时（通常与 **--waitforclient** 组合），xtrace 只在伪 display 上监听并记录之后连接的任何客户端，这适用于连接由其他方式启动的应用程序。

# CAVEATS

xtrace 只追踪 X11 协议；它看不到绕过线路的 GLX、DRI3、共享内存（**MIT-SHM**）缓冲或其他通道。输出可能非常冗长——建议启用缓冲（**-b**）并进行有针对性的运行。在 Wayland 下只能追踪 XWayland 客户端。

# HISTORY

**xtrace** 由 **Bernhard R. Link** 编写，在 Debian 和 Ubuntu 中打包为 **xtrace** 软件包。它常被 X11 开发者和软件包维护者用来调试客户端和工具包中的协议级问题。

# INSTALL

```apt: sudo apt install xtrace```

```nix: nix profile install nixpkgs#xtrace```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xauth](/man/xauth)(1), [Xorg](/man/Xorg)(1), [xdpyinfo](/man/xdpyinfo)(1), [xev](/man/xev)(1), [strace](/man/strace)(1)
