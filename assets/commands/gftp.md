# TAGLINE

图形化 FTP 和 SFTP 客户端

# TLDR

**启动 gFTP**

```gftp```

**连接服务器**

```gftp [ftp.example.com]```

指定端口连接

```gftp [ftp://server:2121]```

通过 SSH 连接

```gftp [ssh://user@server]```

# SYNOPSIS

**gftp** [_options_] [_url_]

# PARAMETERS

_URL_
> 要连接的服务器 URL。

**--help**
> 显示帮助信息。

**--version**
> 显示版本。

# DESCRIPTION

**gftp** 是 Linux 上的图形化 FTP、SFTP 和 HTTP 客户端。它提供双窗格文件管理器界面，用于在本地和远程系统之间传输文件。

该应用程序支持多种协议、书签、队列管理和递归传输，并支持中断传输的断点续传。

gftp 是命令行文件传输工具之外的友好替代选择。

# CAVEATS

GTK 应用程序需要 X/Wayland。FTP 凭据以明文发送。部分功能取决于具体协议。

# HISTORY

gFTP 由 **Brian Masney** 于 1998 年创建，是一个基于 GTK 的 Linux FTP 客户端，后来加入了对 SFTP 和其他协议的支持。

# INSTALL

```dnf: sudo dnf install gftp```

```nix: nix profile install nixpkgs#gftp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ftp](/man/ftp)(1), [sftp](/man/sftp)(1), [filezilla](/man/filezilla)(1)

# RESOURCES

```[Source code](https://github.com/masneyb/gftp)```

<!-- verified: 2026-07-15 -->
