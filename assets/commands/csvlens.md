# TAGLINE

带搜索和导航功能的 CSV 文件查看器

# TLDR

**查看** CSV 文件，列对齐且支持导航

```csvlens [path/to/file.csv]```

在 CSV 中**搜索**特定模式

```csvlens [path/to/file.csv] -f [pattern]```

使用逗号以外的指定分隔符**查看**

```csvlens [path/to/file.csv] -d '[delimiter]'```

仅**查看**指定列

```csvlens [path/to/file.csv] -c [1,3,5]```

# SYNOPSIS

**csvlens** [_options_] [_file_]

# PARAMETERS

**-f, --filter** _PATTERN_
> 过滤匹配模式的行

**-d, --delimiter** _CHAR_
> 指定分隔符（默认：逗号）

**-c, --columns** _LIST_
> 只显示指定的列（以逗号分隔的序号）

**-H, --no-header**
> 把第一行当作数据而非表头

**-n, --line-number**
> 显示行号

**--tab**
> 使用制表符作为分隔符

**--semi**
> 使用分号作为分隔符

**-h, --help**
> 显示帮助并退出

**-V, --version**
> 显示版本并退出

# DESCRIPTION

**csvlens** 是一款命令行 CSV 文件查看器，专为高效浏览和搜索 CSV 数据而设计。它提供列对齐显示、交互式搜索过滤，以及类似 less 或 vim 的键盘导航。

该工具会自动检测并对齐列以便阅读，支持逗号之外的多种分隔符，并且无需修改原文件即可过滤数据。对于传统编辑器难以应付的大型 CSV 文件，它尤其有用。

# KEYBINDINGS

**↑/↓** 或 **k/j**
> 在行之间上下移动

**←/→** 或 **h/l**
> 水平滚动

**/**
> 搜索/过滤模式

**n/N**
> 下一个/上一个搜索结果

**g/G**
> 跳到第一行/最后一行

**q**
> 退出

# CAVEATS

超大 CSV 文件仍可能受可用内存限制而出现性能瓶颈。Unicode 和特殊字符的处理取决于终端能力。某些包含内嵌换行的复杂 CSV 格式可能无法正确渲染。

# HISTORY

**csvlens** 的开发初衷是满足终端中快速轻量 CSV 查看器的需求。它的灵感来自 less、grep 等传统 Unix 工具，同时增加了针对 CSV 的格式化和导航特性。

# INSTALL

```pacman: sudo pacman -S csvlens```

```brew: brew install csvlens```

```nix: nix profile install nixpkgs#csvlens```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cat](/man/cat)(1), [less](/man/less)(1), [grep](/man/grep)(1), [awk](/man/awk)(1)
