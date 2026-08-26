# TAGLINE

阅读未安装 Debian 软件包中的 man page

# TLDR

从**软件包**阅读 man page

```debman -p [package] [command]```

指定**软件包版本**

```debman -p [package]=[version] [command]```

从 **.deb 文件**阅读 man page

```debman -f [path/to/file.deb] [command]```

# SYNOPSIS

**debman** [_options_] _command_

# DESCRIPTION

**debman** 无需安装即可阅读 Debian 软件包中的 man page。它会下载软件包、提取其中的 man page，并使用系统的 man 查看器显示。

适用于安装前查阅软件包文档，或查看当前系统上没有的软件包文档。

# PARAMETERS

**-p** _package_
> 下载并从指定的软件包读取

**-f** _file_
> 从本地 .deb 文件读取

_command_
> 要显示的 man page

# CAVEATS

下载软件包需要网络连接（使用 -f 时除外）。属于 debian-goodies 软件包。

# SEE ALSO

[man](/man/man)(1), [apt-get](/man/apt-get)(8), [dpkg](/man/dpkg)(1)

# RESOURCES

```[Source code](https://salsa.debian.org/debian/debian-goodies)```

<!-- verified: 2026-07-11 -->
