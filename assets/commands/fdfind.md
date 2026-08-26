# TAGLINE

快速且用户友好的文件查找工具

# TLDR

**按名称查找文件**

```fdfind [pattern]```

**按扩展名查找**

```fdfind -e [txt] [pattern]```

**只查找目录**

```fdfind -t d [pattern]```

**只查找文件**

```fdfind -t f [pattern]```

**搜索隐藏文件**

```fdfind -H [pattern]```

**在指定目录中搜索**

```fdfind [pattern] [/path/to/search]```

**对结果执行命令**

```fdfind [pattern] -x [command]```

**区分大小写搜索**

```fdfind -s [Pattern]```

# SYNOPSIS

**fdfind** [_options_] [_pattern_] [_path_...]

# PARAMETERS

**-e**, **--extension** _ext_
> 按扩展名过滤。

**-t**, **--type** _type_
> 按类型过滤（f、d、l、x）。

**-H**, **--hidden**
> 包含隐藏文件。

**-I**, **--no-ignore**
> 不遵守 ignore 文件。

**-s**, **--case-sensitive**
> 区分大小写搜索。

**-x**, **--exec** _cmd_
> 对每个结果执行命令。

**-X**, **--exec-batch** _cmd_
> 用所有结果一起执行命令。

**-d**, **--max-depth** _num_
> 最大搜索深度。

**-E**, **--exclude** _pattern_
> 排除匹配的模式。

# DESCRIPTION

**fdfind**（即 fd）是一个简单、快速且用户友好的 find 替代品，用 Rust 编写。它默认使用正则表达式模式并遵守 .gitignore 文件，非常适合搜索代码仓库。

该命令提供彩色输出、忽略隐藏和被 gitignore 文件的合理默认行为，以及并行执行以获得更好的性能。在基于 Debian 的系统上，二进制文件命名为 fdfind，以避免与另一个软件包冲突。

# CAVEATS

默认使用正则表达式模式，而非 glob 语法。除非显式启用，否则会忽略隐藏和 .gitignore 文件。可能无法覆盖 find 的全部使用场景。

# INSTALL

```apt: sudo apt install fd-find```

```dnf: sudo dnf install fd-find```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fd](/man/fd)(1), [find](/man/find)(1), [ripgrep](/man/ripgrep)(1)

# RESOURCES

```[Source code](https://github.com/sharkdp/fd)```

<!-- verified: 2026-07-15 -->
