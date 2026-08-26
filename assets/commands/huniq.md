# TAGLINE

无需排序即可过滤重复行

# TLDR

**保留唯一行**，维持首次出现的顺序

```echo -e "foo\nbar\nfoo\nbaz" | huniq```

**统计出现次数**

```echo -e "foo\nbar\nfoo\nbaz" | huniq -c```

处理以 NUL **分隔的**记录

```find . -print0 | huniq -0```

**自定义分隔符**

```huniq -d [,]```

# SYNOPSIS

**huniq** [**-c**|**--count**] [**-0**|**--null**|**-d** *DELIM*|**--delim** *DELIM*]

# DESCRIPTION

**huniq** 使用哈希集合而非排序来移除标准输入中的重复行。普通模式下输出顺序稳定（首次出现者优先）。配合 **-c** / **--count** 时会打印出现次数（计数模式下顺序不稳定）。

它旨在作为 **sort | uniq** 或 **sort -u** 的更快的替代方案，适用于不需要排序输出的场合。可通过 **cargo install huniq** 安装。

# PARAMETERS

**-c**, **--count**

> 打印各唯一行的出现次数（类似 **uniq -c**，但不排序）。

**-0**, **--null**

> 使用 NUL 作为记录分隔符。

**-d**, **--delim** *DELIM*

> 使用自定义分隔符代替换行符。

**-h**

> 显示帮助。

# CAVEATS

内存占用随唯一键数量增长（哈希表）。如果需要已排序的去重输出，请继续使用 **sort -u**。计数模式不保留输入顺序。

# INSTALL

```nix: nix profile install nixpkgs#huniq```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[uniq](/man/uniq)(1), [sort](/man/sort)(1), [awk](/man/awk)(1)

# RESOURCES

```[Source code](https://github.com/koraa/huniq)```

<!-- verified: 2026-07-19 -->
