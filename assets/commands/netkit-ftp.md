# TAGLINE

netkit FTP 客户端

# TLDR

**连接到 FTP 服务器**

```netkit-ftp [ftp.example.com]```

**以被动模式连接**（在防火墙后很有用）

```netkit-ftp -p [ftp.example.com]```

**以详细输出模式连接**

```netkit-ftp -v [ftp.example.com]```

**连接时不自动登录**

```netkit-ftp -n [ftp.example.com]```

**以非交互式多文件传输方式连接**

```netkit-ftp -i [ftp.example.com]```

**启用调试**

```netkit-ftp -d [ftp.example.com]```

# SYNOPSIS

**netkit-ftp** [_options_] [_host_]

# PARAMETERS

_HOST_
> FTP 服务器主机名。

**-4**
> 仅使用 IPv4 联系主机。

**-6**
> 仅使用 IPv6 联系主机。

**-p**
> 数据传输使用被动模式。当以 pftp 调用时默认启用。

**-i**
> 在多文件传输期间关闭交互式提示。

**-n**
> 初始连接时不尝试自动登录（跳过 .netrc 查找）。

**-g**
> 禁用文件名通配符展开。

**-v**
> 详细输出；显示远程服务器的所有响应以及数据传输统计信息。

**-d**
> 启用调试。

# DESCRIPTION

**netkit-ftp** 是经典的互联网文件传输程序。它为标准文件传输协议（FTP）提供交互式命令行界面，允许用户在本地与远程网络站点之间传输文件。它支持通过 .netrc 文件自动登录、用于穿越防火墙的被动模式，以及交互式文件名通配符展开。

# CAVEATS

传输不加密，包括密码在内。这是一款已不再活跃维护的旧式工具。如需安全传输，请考虑 **sftp** 或 **lftp**。

# HISTORY

netkit-ftp 是 **netkit** 的一部分，自早期互联网时代起就提供标准的 Unix 网络工具。

# SEE ALSO

[ftp](/man/ftp)(1), [sftp](/man/sftp)(1), [lftp](/man/lftp)(1)
