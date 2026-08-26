# TAGLINE

可通过 VNC 访问的虚拟 X server

# TLDR

**在 display :1 上启动 VNC 服务器**

```Xvnc :1```

**以指定几何尺寸启动**

```Xvnc :1 -geometry [1280x1024]```

**指定颜色深度启动**

```Xvnc :1 -depth [24]```

**使用密码文件启动**

```Xvnc :1 -PasswordFile [~/.vnc/passwd]```

**在特定端口上启动**

```Xvnc :1 -rfbport [5901]```

**使用 vncserver 脚本（推荐）**

```vncserver :1```

# SYNOPSIS

**Xvnc** [:_display_] [_options_]

# PARAMETERS

**-geometry** _WxH_
> 桌面尺寸（默认：1024x768）。

**-depth** _n_
> 颜色深度：16、24 或 32（默认：24）。

**-rfbport** _port_
> VNC 监听端口（默认：5900+display 编号）。

**-PasswordFile** _file_
> 用于身份验证的密码文件。

**-SecurityTypes** _types_
> 逗号分隔的安全类型列表。

**-localhost**
> 只接受来自 localhost 的连接。

**-AlwaysShared**
> 允许多个同时连接。

**-NeverShared**
> 新连接建立时断开现有客户端。

# DESCRIPTION

**Xvnc** 既是 X server 也是 VNC 服务器。它创建一个没有物理屏幕的虚拟 X display，只能通过 VNC 客户端访问。应用程序在 Xvnc 上的运行方式与在普通 X display 上相同。

服务器在 TCP 端口 5900+display 编号上监听 VNC 连接。与共享现有 display 的 x11vnc 不同，Xvnc 会创建全新的独立虚拟 display。

vncserver 脚本是启动 Xvnc 的推荐方式，它会处理环境设置并运行初始应用程序。多个 Xvnc 实例可以在不同的 display 编号上运行。

# CAVEATS

3D 无硬件加速。每个会话使用单独的 display 编号。密码文件必须用 vncpasswd 创建。远程访问需要配置防火墙规则。

# HISTORY

**Xvnc** 由 AT&T 剑桥实验室作为 VNC（Virtual Network Computing）的一部分开发。现在有多种实现，包括 TightVNC、TigerVNC 和 RealVNC，各自具有额外的特性和优化。

# SEE ALSO

[vncserver](/man/vncserver)(1), [vncviewer](/man/vncviewer)(1), [vncpasswd](/man/vncpasswd)(1), [x11vnc](/man/x11vnc)(1)
