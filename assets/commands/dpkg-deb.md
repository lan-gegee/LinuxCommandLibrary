# TAGLINE

Debian 归档操作工具

# TLDR

显示软件包**信息**

```dpkg-deb -I [path/to/file.deb]```

显示软件包**名称与版本**

```dpkg-deb -W [path/to/file.deb]```

**列出**软件包内容

```dpkg-deb -c [path/to/file.deb]```

**解压**内容到目录

```dpkg-deb -x [path/to/file.deb] [path/to/directory]```

**解压**内容及控制信息

```dpkg-deb --raw-extract [path/to/file.deb] [path/to/directory]```

从目录**构建**软件包

```dpkg-deb -b [path/to/directory]```

**显示特定 control 文件**字段

```dpkg-deb -f [path/to/file.deb] [field_name]```

# SYNOPSIS

**dpkg-deb** _action_ [_options_] _archive_|_directory_

# DESCRIPTION

**dpkg-deb** 用于打包、解包 Debian 归档（.deb 文件）并获取其信息。它是直接操作 .deb 文件格式的底层工具，不涉及软件包数据库。

借助该工具，你可以在安装前检查软件包的内容和元数据、从软件包中提取文件而不必安装，或从结构正确的目录树构建新的 .deb 归档。与 dpkg 本身不同，dpkg-deb 纯粹针对归档文件操作，不会修改系统的软件包数据库。

常见用例包括：出于安全审计目的检查陌生软件包、从软件包中提取特定文件，以及在开发工作流中构建自定义 .deb 软件包。

# PARAMETERS

**-I, --info** _archive_
> 显示软件包信息

**-W, --show** _archive_
> 显示软件包名称和版本

**-c, --contents** _archive_
> 列出归档内容

**-x, --extract** _archive_ _dir_
> 解压文件到目录

**-X, --vextract** _archive_ _dir_
> 解压并列出文件

**-e, --control** _archive_ [_dir_]
> 解压控制信息文件

**-R, --raw-extract** _archive_ _dir_
> 解压全部内容（数据和控制信息）

**-f, --field** _archive_ [_field_]
> 显示 control 文件字段的值

**-b, --build** _dir_ [_archive_]
> 从目录构建软件包

# CAVEATS

比 dpkg 更底层；安装请使用 dpkg。构建软件包需要正确的 debian/ 目录结构。属于 dpkg 包的一部分。

# INSTALL

```apt: sudo apt install dpkg```

```dnf: sudo dnf install dpkg```

```pacman: sudo pacman -S dpkg```

```apk: sudo apk add dpkg```

```zypper: sudo zypper install dpkg```

```brew: brew install dpkg```

```nix: nix profile install nixpkgs#dpkg```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dpkg](/man/dpkg)(1), [dpkg-query](/man/dpkg-query)(1), [apt](/man/apt)(1), [ar](/man/ar)(1)
