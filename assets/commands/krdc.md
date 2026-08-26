# TAGLINE

KDE 远程桌面客户端

# TLDR

**启动**远程桌面客户端

```krdc```

**连接到 VNC 服务器**

```krdc vnc://[hostname:display]```

**连接到 RDP 服务器**

```krdc rdp://[hostname]```

在自定义端口上**连接到 RDP 服务器**

```krdc rdp://[hostname:port]```

以**全屏模式启动**并连接到主机

```krdc --fullscreen vnc://[hostname]```

# SYNOPSIS

**krdc** [_options_] [_URL_]

# PARAMETERS

**--fullscreen**
> 以全屏模式启动。仅在指定单个 URL 时有效。

**-h**, **--help**
> 显示列出可用选项的帮助文本。

**--version**
> 显示版本信息。

**--author**
> 显示作者信息。

**--license**
> 显示许可证信息。

# DESCRIPTION

**KRDC** (KDE Remote Desktop Client) 是一个图形应用，可以查看并控制另一台运行兼容服务器的机器上的桌面会话。它在帧缓冲层面工作，因此兼容多种窗口系统，包括 X11、Wayland、macOS 和 Windows。

KRDC 支持两种协议：用于跨平台远程访问的 **VNC** (Virtual Network Computing)，以及用于连接 Windows 机器和其他支持 RDP 的主机的 **RDP** (Remote Desktop Protocol)。RDP 支持需要 **xfreerdp** (FreeRDP) 作为运行时依赖。

该客户端提供常用连接的书签管理、最近会话历史、按主机保存的设置，以及可配置的连接速度配置（LAN、DSL/Cable、Modem），用以调整画质与压缩。密码可通过 **KWallet** 集成安全存储。

# CONFIGURATION

连接设置按主机存储，可通过配置对话框访问。对话框提供三个标签页：**General**、**VNC Defaults** 和 **RDP Defaults**。速度配置通过控制颜色深度和压缩来平衡画质与带宽。按主机设置避免了重新连接时重复弹出配置提示。

# CAVEATS

KRDC 是图形应用，需要正在运行的显示服务器（X11 或 Wayland）。RDP 连接需要单独安装 **xfreerdp**。VNC 连接默认不加密；在不可信网络上使用时应通过 SSH 建立隧道以保证安全。

# HISTORY

KRDC 由 **Tim Jansen** 作为 KDE 项目的一部分编写。**Urs Wolfer** 在 **Google Summer of Code 2007** 期间完成了一次大规模重写，使代码库现代化并改进了协议支持。自 KDE 3.x 以来它一直是 **KDE Applications** 套件的标准组件，目前作为 KDE Gear 发行版的一部分持续活跃开发。

# INSTALL

```apt: sudo apt install krdc```

```dnf: sudo dnf install krdc```

```pacman: sudo pacman -S krdc```

```apk: sudo apk add krdc```

```zypper: sudo zypper install krdc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rdesktop](/man/rdesktop)(1), [xfreerdp](/man/xfreerdp)(1), [vncviewer](/man/vncviewer)(1), [ssh](/man/ssh)(1)
