# TAGLINE

查询 CRUX Linux 软件包数据库

# TLDR

列出**已安装的软件包**及版本

```pkginfo -i```

列出软件包拥有的**文件**

```pkginfo -l [package]```

查找匹配模式的文件**属于哪个包**

```pkginfo -o [pattern]```

打印文件的 **footprint**

```pkginfo -f [path/to/file]```

# SYNOPSIS

**pkginfo** [**-i**|**--installed**] [**-l**|**--list** _pkg_] [**-o**|**--owner** _pattern_] [**-f** _file_]

# PARAMETERS

**-i, --installed**
> 列出所有已安装的软件包及版本

**-l, --list _package_**
> 列出软件包拥有的文件

**-o, --owner _pattern_**
> 查找拥有匹配模式文件的软件包

**-f _file_**
> 打印软件包文件的 footprint

**-r, --root _path_**
> 使用备用的根目录

# DESCRIPTION

**pkginfo** 查询 CRUX Linux 系统上的软件包数据库。它可以列出已安装的软件包、显示软件包内容，以及确定特定文件属于哪个软件包。

该工具从 pkgadd 和 pkgrm 维护的软件包数据库读取信息，为系统管理和故障排查提供必要信息。

# CAVEATS

CRUX 专用工具。模式匹配使用 shell 通配符。footprint 比较有助于验证软件包完整性。数据库位置固定为 /var/lib/pkg/db。

# HISTORY

**pkginfo** 是 **pkgutils** 的一部分，后者是 CRUX Linux 原生的软件包管理系统。它提供简单的查询功能，符合 CRUX 的极简主义理念。

# INSTALL

```apk: sudo apk add py3-pkginfo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pkgadd](/man/pkgadd)(8), [pkgrm](/man/pkgrm)(8), [pkgmk](/man/pkgmk)(8)
