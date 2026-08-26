# TAGLINE

文件传输协议（FTP）客户端

# TLDR

**连接到服务器**

```ftp [ftp.example.com]```

**带用户名连接**

```ftp [username]@[ftp.example.com]```

**非交互模式**

```ftp -n [ftp.example.com]```

**下载文件**

```ftp> get [remote_file] [local_file]```

**上传文件**

```ftp> put [local_file] [remote_file]```

# SYNOPSIS

**ftp** [_options_] [_host_]

# PARAMETERS

_HOST_
> FTP 服务器主机名或 IP。

**-n**
> 不自动登录。

**-i**
> 多文件传输时不进行交互提示。

**-v**
> 详细模式。

**-p**
> 被动模式。

**get** _FILE_
> 下载文件。

**put** _FILE_
> 上传文件。

**mget** _FILES_
> 下载多个文件。

**--help**
> 显示帮助信息。

# CONFIGURATION

**~/.netrc**
> 存储 FTP 凭据以实现自动登录（格式：machine host login user password pass）。

# DESCRIPTION

**ftp** 是标准的文件传输协议客户端，用于在本地与远程系统之间传输文件。它提供交互式命令界面进行文件操作。

该客户端支持目录导航、文件列表、二进制/ASCII 传输模式和批量传输。被动模式有助于穿过防火墙。注意该协议以明文传输凭据。

ftp 在访问遗留系统和公共 FTP 归档时仍然有用。

# CAVEATS

**不安全** —— 密码以明文发送。处理敏感数据请使用 SFTP 或 FTPS。主动模式可能遇到防火墙问题。

# HISTORY

ftp 是最古老的互联网协议之一，在 **RFC 959**（1985 年）中标准化。虽然大部分场景已被安全替代方案取代，它在匿名文件归档领域仍有广泛部署。

# INSTALL

```dnf: sudo dnf install ftp```

```apk: sudo apk add inetutils-ftp```

```zypper: sudo zypper install ftp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sftp](/man/sftp)(1), [lftp](/man/lftp)(1), [curl](/man/curl)(1)

# RESOURCES

```[Documentation](https://manpages.debian.org/ftp)```

<!-- verified: 2026-07-15 -->
