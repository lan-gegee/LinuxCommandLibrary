# TAGLINE

搜索预建的数据库以查找匹配模式的文件

# TLDR

按模式**查找**文件

```locate "[pattern]"```

**不区分大小写**查找

```locate -i "[pattern]"```

按**精确文件名**查找（仅 basename）

```locate -b "\[filename]"```

将输出**限制**为指定数量的结果

```locate -l [10] "[pattern]"```

**统计**匹配条目的数量

```locate -c "[pattern]"```

**显示**数据库统计信息

```locate -S```

**更新**数据库

```sudo updatedb```

# SYNOPSIS

**locate** [_options_] _pattern_...

# DESCRIPTION

**locate** 搜索预建的数据库来查找匹配模式的文件，对于简单的文件名搜索比 find 快得多。数据库通常由 cron 任务每天更新一次。

# PARAMETERS

**-i, --ignore-case**
> 不区分大小写搜索

**-l, --limit N**
> 将输出限制为 N 条

**-c, --count**
> 打印匹配的数量

**-e, --existing**
> 仅打印仍存在的文件

**-b, --basename**
> 只匹配 basename

**-r, --regexp**
> 使用基本正则表达式

**--regex**
> 使用扩展正则表达式

**-d, --database** _DBPATH_
> 在指定的数据库中搜索而不是默认数据库

**-S, --statistics**
> 打印每个数据库的统计信息并退出

**-w, --wholename**
> 匹配完整路径名（默认行为）

# CAVEATS

数据库定期更新，因此最近创建的文件可能查不到。运行 `updatedb` 可手动刷新数据库。

# INSTALL

```apk: sudo apk add findutils-locate```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[find](/man/find)(1), [updatedb](/man/updatedb)(1), [mlocate](/man/mlocate)(1), [plocate](/man/plocate)(1)
