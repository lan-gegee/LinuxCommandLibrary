# TAGLINE

Portage 软件包信息查询工具

# TLDR

**列出**所有已安装的软件包

```equery list '*'```

在 Portage 树和 **overlay** 中搜索软件包

```equery list -po [package1] [package2]```

列出**依赖于**某软件包的所有软件包

```equery depends [package]```

列出某软件包**所依赖的**全部软件包

```equery depgraph [package]```

列出某软件包安装的全部**文件**

```equery files --tree [package]```

显示软件包的 **USE 标志**

```equery uses [package]```

查找某个文件**属于**哪个软件包

```equery belongs [/path/to/file]```

# SYNOPSIS

**equery** _command_ [_options_] [_package_]

# DESCRIPTION

**equery** 是 Gentoo Linux 上功能强大的查询工具，用于查看 Portage 软件包的相关信息。它提供关于已安装软件包的详细信息，包括依赖关系、所属文件、USE 标志设置等。该工具既能查询本地已安装软件包数据库，也能搜索包含 overlay 在内的 Portage 树。

作为 gentoolkit 软件包的一部分，equery 提供了比原始 Portage 查询更友好的界面，便于排查软件包关系、诊断安装问题以及了解系统状态。它是 Gentoo 系统管理与软件包管理的必备工具。

# PARAMETERS

**list** _pattern_
> 列出匹配模式的软件包

**depends** _package_
> 显示反向依赖

**depgraph** _package_
> 显示依赖图

**files** _package_
> 列出已安装的文件

**uses** _package_
> 显示软件包的 USE 标志

**belongs** _file_
> 查找文件所属的软件包

**hasuse** _flag_
> 查找具有特定 USE 标志的软件包

**size** _package_
> 显示软件包占用的磁盘空间

**-p**, **--portage-tree**
> 包含 Portage 树

**-o**, **--overlay-tree**
> 包含 overlay

**--tree**
> 以树形显示

# CAVEATS

Gentoo Linux 专属。属于 gentoolkit 软件包。只查询本地数据库，不查询远程仓库。

# SEE ALSO

[emerge](/man/emerge)(1), [eix](/man/eix)(1)
