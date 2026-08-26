# TAGLINE

使用灵活的条件查询和过滤 pacman 数据库中的软件包

# TLDR

列出**所有可用软件包**

```pacsift```

过滤**满足**某个依赖的软件包

```pacsift --satisfies [package]```

按名称搜索**已安装的软件包**

```pacsift --local --name [pattern]```

查找**外部**（AUR/手动安装）软件包

```pacsift --local --foreign```

查找**显式安装**的软件包

```pacsift --local --reason explicit```

组合过滤器并进行**精确**匹配

```pacsift --exact --repo [extra] --name [package]```

# SYNOPSIS

**pacsift** [_options_] [_filters_]

# PARAMETERS

**--satisfies _dep_**
> 过滤满足某个依赖的软件包

**--repo _name_**
> 按软件仓库过滤

**--local**
> 仅搜索已安装的软件包

**--sync**
> 仅搜索同步数据库

**--name _pattern_**
> 按软件包名称过滤

**--group _name_**
> 按组成员关系过滤

**--provides _pkg_**
> 过滤提供某个内容的软件包

**--depends _pkg_**
> 过滤依赖某个内容的软件包

**--exact**
> 精确匹配值

**--regex**
> 将值视为扩展的不区分大小写的正则表达式

**--invert**
> 返回不匹配的软件包

**--any**
> 返回匹配结果的并集而非交集

**--foreign**
> 显示同步数据库中不存在的软件包（例如 AUR 软件包）

**--native**
> 显示同步数据库中存在的软件包

**--reason** _reason_
> 按安装原因过滤（explicit 或 depend）

**--null**[=_sep_]
> 为 stdin 值设置替代的分隔符（默认：NUL）

# DESCRIPTION

**pacsift** 使用灵活的条件查询和过滤 pacman 数据库中的软件包。作为 **pacutils** 工具集的一部分，它提供了比基础 pacman 查询更强大的过滤功能。

该工具可以按多种属性过滤：名称模式、软件仓库、安装状态、依赖、组等。可以组合多个过滤器来缩小结果范围。

输出为软件包名称列表，适合通过管道传给其他 pacutils 命令或 pacman。

# CAVEATS

属于 pacutils 软件包的一部分，在 Arch 上默认不安装。过滤语法与 pacman 内置搜索不同。对于简单搜索，**pacman -Ss** 可能更方便。

# SEE ALSO

[pacman](/man/pacman)(8), [paclog](/man/paclog)(1), [pactree](/man/pactree)(8), [pacinfo](/man/pacinfo)(1)
