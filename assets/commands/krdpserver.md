# TAGLINE

基于 KDE 的 RDP 服务器，用于远程连接 KDE Plasma 桌面

# TLDR

用**用户名和密码**启动 RDP 服务器

```krdpserver -u [username] -p [password]```

共享**指定的显示器**

```krdpserver -u [username] -p [password] --monitor [n]```

# SYNOPSIS

**krdpserver** [_options_]

# PARAMETERS

**-u**, **--username** _USER_
> 用于 RDP 认证的用户名

**-p**, **--password** _PASS_
> 用于 RDP 认证的密码

**--monitor** _N_
> 按索引号共享指定显示器

**--port** _PORT_
> 监听指定端口（默认：3389）

**--certificate** _FILE_
> 用于加密连接的 TLS 证书文件

**--certificate-key** _FILE_
> TLS 证书私钥文件

# DESCRIPTION

**krdpserver** 是一个基于 KDE 的 RDP (Remote Desktop Protocol) 服务器，允许远程连接到 KDE Plasma 桌面。它让用户能够使用标准 RDP 客户端远程访问自己的 Plasma 会话。

该服务器与 KDE 的 portal 系统集成，可以共享整个桌面或特定显示器。它使用 RDP 协议，因此与 Windows 远程桌面及其他 RDP 客户端兼容。

# CAVEATS

需要 KDE Plasma 桌面环境。安全性取决于是否选择了强密码。远程访问可能需要配置防火墙规则。

# HISTORY

krdpserver 是 KDE 开发的 KRDP 项目的一部分，为 Plasma 提供原生 RDP 服务器支持。它是 Linux 上 VNC 之外的另一种远程桌面访问方案。

# INSTALL

```apt: sudo apt install krdp```

```dnf: sudo dnf install krdp```

```pacman: sudo pacman -S krdp```

```apk: sudo apk add krdp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vncserver](/man/vncserver)(1)
