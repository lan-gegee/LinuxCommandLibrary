# TAGLINE

通过搜索预构建的数据库而非扫描文件系统来查找文件

# TLDR

**按名称查找文件**

```locate [pattern]```

**不区分大小写搜索**

```locate -i [pattern]```

**更新数据库**

```sudo updatedb```

**只显示现存的文件**

```locate -e [pattern]```

**限制结果数量**

```locate -l [10] [pattern]```

**统计匹配数量**

```locate -c [pattern]```

# SYNOPSIS

**locate** [_options_] _pattern_...

# PARAMETERS

**-i**, **--ignore-case**
> 不区分大小写匹配。

**-l** _n_, **--limit** _n_
> 输出限制为 n 条。

**-c**, **--count**
> 只打印计数。

**-e**, **--existing**
> 仅限现存的文件。

**-b**, **--basename**
> 仅匹配基名（basename）。

**-r**, **--regexp**
> 使用正则表达式模式。

**-d** _path_
> 使用指定的数据库。

# DESCRIPTION

**mlocate**（merging locate）通过搜索预构建的数据库而不是扫描文件系统来查找文件。这使搜索速度极快。

数据库通常由 cron 每日更新，也可手动运行 updatedb 更新。

# DATABASE

```
Default: /var/lib/mlocate/mlocate.db
Config:  /etc/updatedb.conf

# Update database
sudo updatedb
```

# CAVEATS

数据库可能已过时。新文件要等 updatedb 运行后才会出现。部分路径默认被排除。需要 updatedb 才能获得最新结果。

# HISTORY

mlocate 由 **Miloslav Trmač** 创建，是对 GNU locate 的改进，采用更高效且能跟踪文件变化的数据库格式。

# INSTALL

```nix: nix profile install nixpkgs#mlocate```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[updatedb](/man/updatedb)(8), [find](/man/find)(1), [fd](/man/fd)(1), [plocate](/man/plocate)(1)
