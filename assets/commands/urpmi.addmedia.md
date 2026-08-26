# TAGLINE

在 Mageia Linux 中添加软件仓库

# TLDR

**添加**介质

```sudo urpmi.addmedia [medium] [ftp://ftp.site.com/path/to/Mageia/RPMS]```

从**硬盘**添加

```sudo urpmi.addmedia --distrib HD file://[path/to/repo]```

从**镜像站**添加

```sudo urpmi.addmedia --distrib ftp://[mirror_website]/mirror/mageia/distrib/[version]/[arch]```

从**镜像列表**添加

```sudo urpmi.addmedia --distrib --mirrorlist [mirrorlist]```

# SYNOPSIS

**urpmi.addmedia** [_OPTIONS_] _NAME_ _URL_

# PARAMETERS

**--distrib**
> 从发行版添加全部标准介质

**--mirrorlist** _URL_
> 使用镜像列表自动选择

**HD**
> 指定本地硬盘介质

# DESCRIPTION

**urpmi.addmedia** 用于向 Mageia Linux 添加软件仓库（介质）。介质可以来自 FTP 服务器、HTTP 服务器、本地目录或镜像列表。

在 Mageia 文档中，"medium"（介质）与"repository"（仓库）是同义词。

# CAVEATS

Mageia 专用。本地仓库必须先运行 genhdlist2。需要 root 权限。

# SEE ALSO

[urpmi](/man/urpmi)(8), [urpmi.removemedia](/man/urpmi.removemedia)(8), [urpmi.update](/man/urpmi.update)(8)
