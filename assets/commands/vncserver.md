# TAGLINE

启动 VNC 远程桌面服务器

# TLDR

在下一个**可用**的显示器上启动

```vncserver```

以指定的**分辨率**启动

```vncserver -geometry [1920]x[1080]```

在指定的**显示器**编号上启动

```vncserver :[display_number]```

**终止**指定显示器

```vncserver -kill :[display_number]```

**列出**正在运行的 VNC 服务器

```vncserver -list```

# SYNOPSIS

**vncserver** [_OPTIONS_] [:_DISPLAY_]

# PARAMETERS

**-geometry** _WxH_
> 指定桌面尺寸（默认：1920x1200）。

**-depth** _depth_
> 像素深度（16、24 或 32；默认：24）。

**-kill** _:DISPLAY_
> 终止之前在指定显示器上启动的 VNC 服务器。

**-list**
> 列出所有正在运行的 VNC 服务器实例。

**-localhost** [_yes|no_]
> 只接受来自 localhost 的连接。与 SSH 隧道配合使用很有用。

**-SecurityTypes** _types_
> 以逗号分隔的安全类型列表（None、VncAuth、Plain、TLSVnc、X509Vnc 等）。

**-desktop** _name_
> 显示给连接客户端的桌面名称。

**-fg**
> 将服务器作为前台进程运行。

**-autokill** [_yes|no_]
> 会话脚本退出时自动终止服务器（默认：yes）。

**-xstartup** _script_
> 运行自定义的启动脚本，而不是默认的会话脚本。

**-noxstartup**
> 启动服务器后不运行任何启动脚本。

**-rfbport** _port_
> 用于 VNC 连接的 TCP 端口（默认：5900 + 显示器编号）。

# DESCRIPTION

**vncserver** 启动一个 VNC（Virtual Network Computing）桌面服务器。它会创建一个新的 X display，可以使用 VNC 查看器远程访问。

每个服务器实例运行在独立的显示器编号上。若未指定，则使用第一个可用的显示器。

# CAVEATS

首次使用前必须用 **vncpasswd** 设置密码。显示器编号会加到基础端口 5900 上（例如显示器 :1 使用端口 5901）。防火墙可能需要放行 VNC 端口。VNC 流量默认不加密；安全连接请使用 SSH 隧道或 TLS 安全类型。

# INSTALL

```dnf: sudo dnf install tigervnc```

```pacman: sudo pacman -S tigervnc```

```apk: sudo apk add tigervnc```

```zypper: sudo zypper install tigervnc```

```nix: nix profile install nixpkgs#tigervnc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vncviewer](/man/vncviewer)(1), [vncpasswd](/man/vncpasswd)(1), [x11vnc](/man/x11vnc)(1), [ssh](/man/ssh)(1)
