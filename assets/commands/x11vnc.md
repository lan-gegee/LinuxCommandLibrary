# TAGLINE

面向现有 X 显示的 VNC 服务器

# TLDR

**共享当前显示**给多个客户端

```x11vnc -shared```

以只读模式**持久运行**

```x11vnc -forever -viewonly```

在指定的 display 和 screen 上**启动**

```x11vnc -display :[display].[screen]```

在第三个 display 的默认 screen 上**启动**

```x11vnc -display :2```

在第一个 display 的第二个 screen 上**启动**

```x11vnc -display :0.1```

**启用密码保护**启动

```x11vnc -passwd [mypassword] -forever```

**启用 SSL 加密**启动

```x11vnc -ssl -forever```

# SYNOPSIS

**x11vnc** [_options_]

# PARAMETERS

**-display _display_**
> 要共享的 X display（如 :0、:1.0）

**-shared**
> 允许多个客户端同时连接

**-forever**
> 最后一个客户端断开后不退出

**-viewonly**
> 客户端只能查看，不能交互

**-passwd _password_**
> 设置 VNC 密码

**-rfbauth _file_**
> 使用密码文件

**-rfbport _port_**
> 设置 VNC 端口（默认：5900）

**-noxdamage**
> 禁用 X DAMAGE 扩展

**-clip _WxH+X+Y_**
> 只共享屏幕的一部分区域

**-scale _fraction_**
> 缩放帧缓冲

**-ssl**
> 启用 SSL/TLS 加密

# DESCRIPTION

**x11vnc** 让 VNC 可以访问已存在的 X11 display。与其他创建虚拟显示的 VNC 服务器不同，x11vnc 共享的是实际运行中的桌面，可以远程控制物理显示器上的画面。

该服务器捕获显示内容并传输给 VNC 客户端。默认情况下，当所有客户端断开连接后它会终止，除非指定 **-forever**。

# CAVEATS

需要有正在运行的 X display。在使用合成窗口管理器时可能有性能问题。在不加密的情况下使用存在安全隐患；建议使用 **-ssl** 或通过 SSH 隧道传输。

# INSTALL

```apt: sudo apt install x11vnc```

```dnf: sudo dnf install x11vnc```

```pacman: sudo pacman -S x11vnc```

```apk: sudo apk add x11vnc```

```zypper: sudo zypper install x11vnc```

```brew: brew install x11vnc```

```nix: nix profile install nixpkgs#x11vnc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vncviewer](/man/vncviewer)(1), [xvnc](/man/xvnc)(1), [ssh](/man/ssh)(1)
