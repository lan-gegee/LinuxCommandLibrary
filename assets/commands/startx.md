# TAGLINE

启动 X Window System 会话

# TLDR

**启动** X 会话

```startx```

**以指定颜色深度启动** X

```startx -- -depth [16]```

**以指定 DPI 值启动** X

```startx -- -dpi [100]```

**以指定窗口管理器启动** X

```startx [path/to/window_manager]```

**使用指定的服务器布局启动** X

```startx -- -layout [Multihead]```

# SYNOPSIS

**startx** [ [ _client_ ] _options_ ... ] [ **--** [ _server_ ] [ _display_ ] _options_ ... ]

# PARAMETERS

**--**
> 客户端参数与服务器参数之间的分隔符。

**-depth _value_**
> 服务器选项：设置颜色深度（如 8、16、24）。

**-dpi _value_**
> 服务器选项：设置显示器的 DPI。

**-layout _name_**
> 服务器选项：使用 xorg.conf 中特定的服务器布局。

# DESCRIPTION

**startx** 是 xinit 的前端，提供了一种启动 X 会话的便捷方式。它读取用户的 .xinitrc 文件（若不存在则使用系统默认）来决定运行哪些客户端程序；同样地，它读取 .xserverrc（或系统默认）来决定要启动的 X 服务器。

通常 startx 会运行一个窗口管理器或桌面环境并建立 X 显示。**--** 之前的参数传给客户端，**--** 之后的参数传给服务器。

# ENVIRONMENT

**XINITRC**
> xinitrc 文件的路径。未设置时使用 ~/.xinitrc 或 /etc/X11/xinit/xinitrc。

**XSERVERRC**
> xserverrc 文件的路径。未设置时使用 ~/.xserverrc 或 /etc/X11/xinit/xserverrc。

**DISPLAY**
> 由 startx 设置，表示客户端应连接的显示器名称。

**XAUTHORITY**
> 若尚未定义，则设置为 ~/.Xauthority。

# CONFIGURATION

**~/.xinitrc**
> 用户启动脚本，由 startx 执行以启动窗口管理器或桌面环境。

**~/.xserverrc**
> 用户的服务器启动脚本，用于决定启动哪个 X 服务器。

**/etc/X11/xinit/xinitrc**
> 系统级默认启动脚本，在没有用户 .xinitrc 时使用。

**/etc/X11/xinit/xserverrc**
> 系统级默认服务器脚本，在没有用户 .xserverrc 时使用。

# CAVEATS

需要安装 X 服务器。用户主目录中的 .xinitrc 文件决定哪些程序随 X 一起启动。使用 GDM、SDDM 或 LightDM 等显示管理器时无需此命令。

# INSTALL

```apt: sudo apt install xinit```

```apk: sudo apk add xinit```

```zypper: sudo zypper install xinit```

```brew: brew install xinit```

```nix: nix profile install nixpkgs#xinit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xinit](/man/xinit)(1), [Xorg](/man/Xorg)(1), [xrandr](/man/xrandr)(1), [xterm](/man/xterm)(1)
