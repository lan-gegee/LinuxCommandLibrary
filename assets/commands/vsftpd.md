# TAGLINE

轻量级安全 FTP 服务器守护进程

# TLDR

以独立模式**启动 vsftpd**

```vsftpd```

**使用指定的配置文件启动**

```vsftpd [/etc/vsftpd.conf]```

通过 systemd **启动 vsftpd 服务**

```sudo systemctl start vsftpd```

**设置 vsftpd 开机自启**

```sudo systemctl enable vsftpd```

**打印版本**信息后退出

```vsftpd -v```

# SYNOPSIS

**vsftpd** [_config_file_]

# PARAMETERS

**-v**
> 打印版本信息后退出。

**-ooption=value**
> 按照配置文件的格式设置单个配置项。

# DESCRIPTION

**vsftpd**（Very Secure FTP Daemon）是一个面向类 Unix 系统的轻量级、安全的 FTP 服务器。它是 Ubuntu、Fedora 和 RHEL 等许多 Linux 发行版的默认 FTP 服务器。

该守护进程可以通过在 /etc/vsftpd.conf 中设置 **listen=YES** 以独立模式运行（推荐），也可以由 inetd/xinetd 启动。它默认监听 TCP 端口 21 以处理控制连接。

vsftpd 支持匿名 FTP、本地用户身份验证、基于 PAM 的虚拟用户、SSL/TLS 加密（FTPS）以及适用于 NAT 环境的被动模式。访问控制通过 /etc/vsftpd/ftpusers 和 /etc/vsftpd/user_list 管理。

# CONFIGURATION

**/etc/vsftpd.conf** 中的关键配置：

**listen=YES**
> 以独立模式运行

**anonymous_enable=NO**
> 禁用匿名访问

**local_enable=YES**
> 允许本地用户登录

**write_enable=YES**
> 允许上传操作

**chroot_local_user=YES**
> 将用户限制在其主目录内

**ssl_enable=YES**
> 启用 SSL/TLS 加密

**pasv_enable=YES**
> 启用被动模式

**pasv_min_port/pasv_max_port**
> 被动模式的端口范围

# CAVEATS

FTP 以明文传输凭据；为了安全请启用 SSL/TLS。被动模式需要防火墙放行数据端口范围。可考虑用 SFTP（基于 SSH）作为更安全的 FTP 替代方案。

# HISTORY

vsftpd 由 **Chris Evans** 编写，专注于安全性，成为 Linux 上部署最广泛的 FTP 服务器。其设计通过权限分离和最小攻击面来优先保证安全。

# INSTALL

```apt: sudo apt install vsftpd```

```dnf: sudo dnf install vsftpd```

```pacman: sudo pacman -S vsftpd```

```apk: sudo apk add vsftpd```

```zypper: sudo zypper install vsftpd```

```brew: brew install vsftpd```

```nix: nix profile install nixpkgs#vsftpd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sftp](/man/sftp)(1), [ftp](/man/ftp)(1)
