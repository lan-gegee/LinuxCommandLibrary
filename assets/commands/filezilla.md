# TAGLINE

图形化 FTP/SFTP 客户端

# TLDR

**启动 FileZilla**

```filezilla```

**连接服务器**

```filezilla [ftp://user@host]```

**以 SFTP 连接**

```filezilla [sftp://user@host]```

**启动时打开站点管理器**

```filezilla -s```

**连接已保存的站点**

```filezilla -c [0/sitename]```

# SYNOPSIS

**filezilla** [_options_] [_url_]

# PARAMETERS

_URL_
> 要连接的服务器 URL。

**-c** _PATH_, **--site** _PATH_
> 连接到站点管理器中已保存的条目（路径形式，如 0/name）。不能与 -s 同时使用。

**-s**, **--sitemanager**
> 启动时打开站点管理器。

**-a** _PATH_, **--local** _PATH_
> 设置本地起始目录。

**-l** _TYPE_, **--logontype** _TYPE_
> 通过 FTP URL 连接时的登录类型（ask 或 interactive）。

**-v**, **--version**
> 显示版本信息。

**-h**, **--help**
> 显示帮助信息。

# CONFIGURATION

**~/.config/filezilla/sitemanager.xml**
> 已保存的 FTP/SFTP 站点配置和连接配置档。

**~/.config/filezilla/filezilla.xml**
> 应用的一般设置和偏好项。

# DESCRIPTION

**filezilla** 是图形化的 FTP、SFTP 和 FTPS 客户端。它提供拖放式文件传输、目录比较、书签以及传输队列管理。

该应用支持多条并发连接、中断传输后的续传，以及可配置的传输速度限制。站点管理器保存连接配置档，方便快速访问常用站点。

借助传输队列和多线程引擎，FileZilla 能高效地处理大文件和大型目录。

# CAVEATS

GUI 应用需要图形显示环境。保存下来的密码可能有安全风险。特别大的目录列起目录来可能很慢。

# HISTORY

FileZilla 由 **Tim Kosse** 于 2001 年创建，最初只是一个学校项目。它后来成为最受欢迎的开源 FTP 客户端之一，之后又陆续加入了对 SFTP 和 FTPS 的支持。

# INSTALL

```apt: sudo apt install filezilla```

```dnf: sudo dnf install filezilla```

```pacman: sudo pacman -S filezilla```

```apk: sudo apk add filezilla```

```zypper: sudo zypper install filezilla```

```nix: nix profile install nixpkgs#filezilla```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sftp](/man/sftp)(1), [ftp](/man/ftp)(1), [lftp](/man/lftp)(1)

# RESOURCES

```[Homepage](https://filezilla-project.org/)```

<!-- verified: 2026-07-15 -->
