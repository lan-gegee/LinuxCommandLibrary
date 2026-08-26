# TAGLINE

启动 X Window System 服务器

# TLDR

**以默认窗口管理器启动 X**

```xinit```

**以指定窗口管理器启动 X**

```xinit /usr/bin/[openbox]```

**在不同的显示器上启动 X**

```xinit -- :1```

**使用指定的服务器启动 X**

```xinit -- /usr/bin/Xorg :0```

**带服务器选项启动 X**

```xinit -- -depth 24```

# SYNOPSIS

**xinit** [_client_] [_options_] [_--_] [_server_] [_display_] [_options_]

# PARAMETERS

**client**
> 要启动的客户端程序（必须以 / 或 . 开头）

**--**
> 客户端参数与服务器参数之间的分隔符

**server**
> 要运行的 X server 程序（必须以 / 或 . 开头）

**display**
> 显示器编号（:0、:1 等）

# ENVIRONMENT

**DISPLAY**
> 设置为客户端应连接的显示器名称。

**XINITRC**
> 指定一个包含启动初始窗口所需 shell 命令的初始化文件。覆盖 ~/.xinitrc。

# CONFIGURATION FILES

**~/.xinitrc**
> 用于启动客户端程序的 shell 脚本；最后一个程序应在前台运行

**~/.xserverrc**
> 用于启动 X server 的 shell 脚本

**/etc/X11/xinit/xinitrc**
> 系统级默认客户端脚本

**/etc/X11/xinit/xserverrc**
> 系统级默认服务器脚本

# DESCRIPTION

**xinit** 启动 X Window System 服务器和一个初始客户端程序。它通常用于没有显示管理器的系统，或需要运行多个窗口系统的场合。

不带参数时，xinit 会读取 ~/.xinitrc 来确定要启动哪些客户端，否则使用默认值（xterm）。对于服务器，它会检查 ~/.xserverrc 或使用默认的 X server。

.xinitrc 中的程序除最后一个外都应在后台运行，最后一个（通常是窗口管理器）保持会话存活。当前台客户端退出时，xinit 会杀死 X server 并终止。

# CAVEATS

xinit 是一个底层工具；**startx** 为一般用途提供了更友好的接口。.xinitrc 中的程序除最终的窗口管理器外都必须放入后台。生产系统更推荐使用 GDM 或 SDDM 等显示管理器。

# HISTORY

xinit 自 X Window System 早期版本起就是 X11 的一部分。X Window System 由 MIT 自 **1984** 年起开发，xinit 提供了在没有显示管理器的情况下启动 X 会话的基本机制。

# INSTALL

```apt: sudo apt install xinit```

```apk: sudo apk add xinit```

```zypper: sudo zypper install xinit```

```brew: brew install xinit```

```nix: nix profile install nixpkgs#xinit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[startx](/man/startx)(1), [Xorg](/man/Xorg)(1), [xterm](/man/xterm)(1)
