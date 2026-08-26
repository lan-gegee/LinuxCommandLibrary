# TAGLINE

连接到远程 VNC 桌面

# TLDR

**连接**到主机的显示器

```vncviewer [host]:[display_number]```

以**全屏**方式连接

```vncviewer -FullScreen [host]:[display_number]```

带**分辨率**连接

```vncviewer --geometry [width]x[height] [host]:[display_number]```

连接到指定**端口**

```vncviewer [host]::[port]```

# SYNOPSIS

**vncviewer** [_OPTIONS_] _HOST_[:_DISPLAY_|::_PORT_]

# PARAMETERS

**-FullScreen**
> 以全屏模式启动

**--geometry** _WxH_
> 窗口几何尺寸

**-ViewOnly**
> 仅查看，不接受输入

**-Shared**
> 与其他查看器共享该连接

# DESCRIPTION

**vncviewer** 是一个 VNC（Virtual Network Computing）客户端，用于连接远程 VNC 服务器。它可以通过网络查看和控制远程桌面。

显示器编号（单冒号后）会加到端口 5900 上。使用双冒号可直接指定端口。

# CAVEATS

VNC 流量默认不加密。安全连接请使用 SSH 隧道。性能取决于网络带宽和延迟。

# INSTALL

```apk: sudo apk add tigervnc-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vncserver](/man/vncserver)(1), [x11vnc](/man/x11vnc)(1)
