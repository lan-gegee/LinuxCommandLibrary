# TAGLINE

GNOME 远程桌面查看器

# TLDR

**启动 vinagre**

```vinagre```

**连接到 VNC 服务器**

```vinagre [vnc://hostname:5900]```

**连接到 RDP 服务器**

```vinagre [rdp://hostname]```

**使用显示编号连接**

```vinagre [vnc://hostname:1]```

**以全屏模式打开**

```vinagre -f [vnc://hostname]```

**在新窗口中连接**

```vinagre -n [vnc://hostname]```

# SYNOPSIS

**vinagre** [_options_] [_server_]

# PARAMETERS

**-f**, **--fullscreen**
> 以全屏模式打开。

**-n**, **--new-window**
> 为连接创建新窗口。

**-F** _file_
> 从 .vnc 文件打开连接。

**--geometry** _WxH+X+Y_
> 设置初始窗口几何尺寸。

**--help**
> 显示帮助。

**--version**
> 显示版本。

# URI FORMAT

**vnc://host::port**：通过 VNC 连接（默认端口 5900）。

**vnc://host:display**：按显示编号连接（自动加 5900）。

**rdp://host**：通过 RDP 协议连接。

**spice://host**：通过 SPICE 协议连接。

**ssh://host**：通过 SSH 连接。

# DESCRIPTION

**vinagre** 是 GNOME 的远程桌面查看器，支持 VNC、RDP、SPICE 和 SSH 协议。它提供标签页式连接、收藏/书签功能，并集成 GNOME keyring 存储密码。

该应用可使用 Avahi/mDNS 浏览网络中的 VNC 服务器。支持在标签页或独立窗口中同时建立多个连接。连接设置可保存为收藏以便快速访问。

Vinagre 取代了更早的 GNOME VNC 客户端，之后它自身又在较新的 GNOME 版本中被 GNOME Connections 取代。

# CAVEATS

已被弃用，建议改用 GNOME Connections。部分协议需要可选依赖。RDP 支持可能需要 freerdp。网络浏览需要 Avahi。以 GNOME 为中心；其他桌面环境可能更适合使用替代工具。

# HISTORY

**vinagre** 随 GNOME 2.22 推出，作为官方远程桌面客户端。名字是葡萄牙语的"醋"。它将 VNC、RDP 等多种协议统一到一个界面中。GNOME 3 之后开发放缓，最终由 GNOME Connections 接替。

# INSTALL

```dnf: sudo dnf install vinagre```

```zypper: sudo zypper install vinagre```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[remmina](/man/remmina)(1), [vncviewer](/man/vncviewer)(1), [xfreerdp](/man/xfreerdp)(1)
