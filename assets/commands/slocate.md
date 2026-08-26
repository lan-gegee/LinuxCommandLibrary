# TAGLINE

具备权限感知的文件定位数据库

# TLDR

**查找文件**

```slocate [filename]```

**不区分大小写**

```slocate -i [filename]```

**更新数据库**

```slocate -u```

**显示统计信息**

```slocate -S```

**限制结果数量**

```slocate -n [10] [filename]```

**正则表达式搜索**

```slocate -r "[pattern]"```

# SYNOPSIS

**slocate** [_-i_] [_-r_] [_-n num_] [_options_] _pattern_

# PARAMETERS

**-i**
> 不区分大小写。

**-u**
> 更新数据库。

**-S**
> 统计信息。

**-n** _NUM_
> 限制结果数量。

**-r** _REGEX_
> 正则表达式模式。

**-e** _DIR_
> 排除目录。

# DESCRIPTION

**slocate**（Secure Locate）是 **locate** 命令的权限感知版本，它在预先构建的文件路径数据库中进行搜索。与标准 locate 不同，slocate 只返回搜索用户有权访问的文件，从而防止受限目录中的文件结构信息被泄露。

该工具维护一个按文件路径索引的数据库，与使用 **find** 实时遍历文件系统相比能提供近乎即时的搜索结果。数据库通常通过 cron 定期更新，并支持 glob 风格的模式和正则表达式以实现灵活匹配。

slocate 在很大程度上已被 **mlocate** 取代，后者采用更高效的数据库格式，并且是多数现代 Linux 发行版的默认选择。两者都提供同样的安全特性：基于调用者的文件权限过滤结果。

# CAVEATS

数据库可能过期。更新需要 root 权限。已被 mlocate 取代。

# HISTORY

**slocate**（Secure Locate）由 **Kevin Lindsay** 创建，用于解决原始 GNU locate 的安全问题——后者可能泄露受限文件的信息。在现代 Linux 发行版上，它已在很大程度上被 **mlocate** 取代。

# INSTALL

```apk: sudo apk add mlocate```

```nix: nix profile install nixpkgs#mlocate```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[locate](/man/locate)(1), [mlocate](/man/mlocate)(1), [find](/man/find)(1), [updatedb](/man/updatedb)(1)
