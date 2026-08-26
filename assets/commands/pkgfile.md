# TAGLINE

在 Arch 仓库中搜索文件所属的软件包

# TLDR

**同步** pkgfile 数据库

```sudo pkgfile --update```

搜索**拥有某文件的**软件包

```pkgfile [filename]```

**列出**软件包提供的文件

```pkgfile --list [package]```

列出软件包中的**可执行文件**

```pkgfile --list --binaries [package]```

**不区分大小写**搜索

```pkgfile --ignorecase [filename]```

仅在 **bin/sbin** 目录中搜索

```pkgfile --binaries [filename]```

搜索并显示**版本**

```pkgfile --verbose [filename]```

在**指定仓库**中搜索

```pkgfile --repo [core] [filename]```

# SYNOPSIS

**pkgfile** [**--update**] [**--list**] [**--binaries**] [**--verbose**] [**--repo** _repo_] _target_

# PARAMETERS

**-u, --update**
> 同步 pkgfile 数据库

**-l, --list**
> 列出软件包中的文件

**-b, --binaries**
> 仅搜索/列出可执行文件

**-i, --ignorecase**
> 不区分大小写匹配

**-v, --verbose**
> 显示软件包版本

**-R, --repo** _repo_
> 在特定仓库中搜索

**-g, --glob**
> 启用 shell 风格的 glob 模式匹配

**-r, --regex**
> 启用正则表达式匹配

**-d, --directories**
> 在搜索结果中包含目录

**-q, --quiet**
> 抑制错误消息

**-0, --null**
> 用空字节分隔输出

# DESCRIPTION

**pkgfile** 在官方 Arch Linux 仓库中搜索包含特定文件的软件包。它维护自己的文件到软件包映射数据库，以实现快速查询。

该工具常用于查找缺失命令或文件由哪个软件包提供。它还可以列出软件包包含的所有文件，便于在安装前了解软件包的内容。

# CAVEATS

使用前必须先同步数据库。只搜索官方仓库，不包括 AUR。数据库更新需要 root 权限。首次下载大型数据库可能耗时。

# HISTORY

**pkgfile** 为 Arch Linux 而生，提供快速的文件到软件包查询。它与 `pacman -F` 功能类似，但拥有为此目的优化的专用数据库。

# INSTALL

```pacman: sudo pacman -S pkgfile```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pacman](/man/pacman)(8), [pactree](/man/pactree)(1), [makepkg](/man/makepkg)(8)
