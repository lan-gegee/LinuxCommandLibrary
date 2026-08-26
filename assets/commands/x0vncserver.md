# TAGLINE

通过 VNC 共享现有的 X 显示

# TLDR

以**密码文件**启动

```x0vncserver -display :0 -passwordfile [path/to/file]```

在特定**端口**上启动

```x0vncserver -display :0 -rfbport [port]```

# SYNOPSIS

**x0vncserver** [_OPTIONS_]

# PARAMETERS

**-display** _DISPLAY_
> 要共享的 X display

**-passwordfile** _FILE_
> 用于身份验证的密码文件

**-rfbport** _PORT_
> 监听的 VNC 端口

**-SecurityTypes** _TYPES_
> 以逗号分隔的接受安全类型列表（如 `VncAuth,Plain`）。

**-Geometry** _WxH+X+Y_
> 将共享区域限制为显示的一个子矩形。

**-Log** _DEST:LEVEL_
> 配置日志（如 `stderr:100`、`*:stderr:30`）。

**-SendCutText** / **-AcceptCutText**
> 启用/禁用服务器与客户端之间的剪贴板转发。

**-QueryConnect**
> 接受每个传入连接前先询问本地用户。

# DESCRIPTION

**x0vncserver** 是 TigerVNC 的服务器组件，通过 VNC 共享已有的 X display。与创建新虚拟显示的 vncserver 不同，x0vncserver 共享的是物理显示。

这样就能远程访问显示器上实际正在显示的画面。

# CAVEATS

需要 X11 display。必须先用 vncpasswd 设置密码。安全性取决于网络配置。建议考虑 SSH 隧道以实现安全访问。

# INSTALL

```dnf: sudo dnf install tigervnc```

```pacman: sudo pacman -S tigervnc```

```apk: sudo apk add tigervnc```

```zypper: sudo zypper install tigervnc```

```nix: nix profile install nixpkgs#tigervnc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vncserver](/man/vncserver)(1), [vncpasswd](/man/vncpasswd)(1), [x11vnc](/man/x11vnc)(1)
