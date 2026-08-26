# TAGLINE

提供有关 lintian 标签的信息

# TLDR

**显示标签信息**

```lintian-info [tag-name]```

**列出所有标签**

```lintian-info --list-tags```

**显示标签描述**

```lintian-info -t [tag-name]```

**搜索标签**

```lintian-info --tags [pattern]```

**显示检查信息**

```lintian-info --check [check-name]```

# SYNOPSIS

**lintian-info** [_options_] [_tag_]

# PARAMETERS

_TAG_
> Lintian 标签名称。

**-t** _TAG_
> 显示标签描述。

**--list-tags**
> 列出所有可用标签。

**--tags** _PATTERN_
> 搜索匹配的标签。

**--check** _NAME_
> 显示检查信息。

**--help**
> 显示帮助信息。

# DESCRIPTION

**lintian-info** 提供有关 lintian 标签的信息。标签用于标识 Debian 软件包中的特定问题。

该工具解释每个标签的含义，以及如何修复它所代表的问题。

# CAVEATS

是 lintian 软件包的一部分。标签数据库在不同版本之间可能不同。专注于 Debian。

# HISTORY

lintian-info 是 **lintian** 软件包的一部分，为其庞大的标签集合提供文档说明。

# INSTALL

```aur: yay -S lintian```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lintian](/man/lintian)(1), [debuild](/man/debuild)(1)
