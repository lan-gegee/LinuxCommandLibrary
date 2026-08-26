# TAGLINE

支持自定义格式的 pacman 数据库查询工具

# TLDR

列出软件包的**依赖**

```expac [-S|--sync] '%D' [package]```

列出**可选依赖**

```expac [-S|--sync] "%o" [package]```

以 MiB 为单位列出软件包的**下载大小**

```expac [-S|--sync] [-H|--humansize] M '%k\t%n' [package1] [package2]```

按大小列出标记为待**升级**的软件包

```expac [-S|--sync] [-H|--humansize] M '%k\t%n' $(pacman -Qqu) | sort [-sh|--sort --human-numeric-sort]```

列出**显式安装**的软件包及其可选依赖

```expac [-d|--delim] '\n\n' [-l|--listdelim] '\n\t' [-Q|--query] '%n\n\t%O' $(pacman -Qeq)```

# SYNOPSIS

**expac** [_options_] _format_ [_targets_]

# DESCRIPTION

**expac** 使用类似 printf 的格式字符串从 alpm 数据库提取数据。它为基于 pacman 的软件包查询提供灵活的输出格式化。

该工具是解析 pacman 输出的轻量级替代方案，可直接访问软件包元数据，包括依赖、大小、描述和安装日期。%n（名称）、%v（版本）、%D（依赖）等格式说明符可用于生成自定义报告。

适合用于脚本编写、软件包分析和生成自定义软件包报告。与其他工具结合进行过滤和处理时尤为强大。

# PARAMETERS

**-S, --sync**
> 查询同步数据库

**-Q, --query**
> 查询本地数据库

**-H, --humansize** _unit_
> 人类可读的大小（K、M、G）

**-d, --delim** _string_
> 软件包之间的分隔符（默认：换行符）

**-l, --listdelim** _string_
> 列表项之间的分隔符（默认：两个空格）

**-t, --timefmt** _format_
> 传递给 strftime(3) 的时间输出格式字符串（默认：%c）

**-1, --readone**
> 在第一个匹配后停止

**-p, --file** _pkgfile_
> 查询软件包文件而非数据库

# FORMAT SPECIFIERS

常用格式说明符：%n（名称）、%v（版本）、%d（描述）、%D（依赖）、%E（依赖，不含版本）、%O（可选依赖）、%o（可选依赖，不含描述）、%N（被谁依赖）、%P（提供）、%H（冲突）、%G（组）、%m（安装大小）、%k（下载大小）、%r（仓库）、%u（URL）、%a（架构）、%l（安装日期）、%w（安装原因）、%F（文件列表）。

# CAVEATS

仅适用于 Arch Linux 及其衍生发行版。格式字符串使用 % 说明符。属于 pacman 生态的一部分。使用 -H 可以将大小格式化为人类可读的单位（K、M、G、T）。

# INSTALL

```pacman: sudo pacman -S expac```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pacman](/man/pacman)(8), [pactree](/man/pactree)(8)
