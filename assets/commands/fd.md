# TAGLINE

快速且用户友好的文件查找工具

# TLDR

按名称**查找文件**

```fd [pattern]```

按指定**扩展名**查找

```fd -e [txt] [pattern]```

**在目录中**查找

```fd [pattern] [directory]```

**包含隐藏文件**

```fd -H [pattern]```

对结果**执行命令**

```fd [pattern] -x [command]```

# SYNOPSIS

**fd** [_options_] [_pattern_] [_path_...]

# PARAMETERS

_PATTERN_
> 搜索模式（默认为正则表达式）。

_PATH_
> 要搜索的目录（默认：当前目录）。

**-e** _EXT_, **--extension** _EXT_
> 按文件扩展名过滤。

**-t** _TYPE_, **--type** _TYPE_
> 按类型过滤：f（文件）、d（目录）、l（符号链接）。

**-H**, **--hidden**
> 包含隐藏文件。

**-I**, **--no-ignore**
> 不遵守 .gitignore。

**-x** _CMD_, **--exec** _CMD_
> 对每个结果执行命令。

**-X** _CMD_, **--exec-batch** _CMD_
> 用所有结果一起执行命令。

**-d** _N_, **--max-depth** _N_
> 最大搜索深度。

**-g**, **--glob**
> 使用 glob 模式而非正则表达式。

**-E** _PATTERN_, **--exclude** _PATTERN_
> 排除匹配模式的条目。

**-S** _SIZE_, **--size** _SIZE_
> 按大小过滤（如 +1m、-100k）。

**--changed-within** _DATE_
> 按修改时间过滤。

**-c**, **--color** _WHEN_
> 何时使用颜色（auto、always、never）。

# DESCRIPTION

**fd** 是 find 的现代替代品，用 Rust 编写。它提供直观的语法、彩色输出、智能的默认行为，相比传统 find 有显著的性能提升。

默认情况下，fd 忽略隐藏文件并遵守 .gitignore 规则。它使用正则表达式模式而非 glob，支持并行执行命令，输出也更友好。

fd 旨在以更简单的语法覆盖 find 80% 的使用场景，同时通过并行化实现更快的速度。

# CAVEATS

默认使用正则表达式（而非 glob）。默认忽略隐藏和被 gitignore 的文件。并非 find 的完整替代品。

# HISTORY

fd 由 **David Peter** 创建，作为 find 更简单、更快速的替代品。它用 Rust 编写，注重用户体验，具有合理的默认值和现代化的终端输出。

# INSTALL

```apt: sudo apt install fd-find```

```dnf: sudo dnf install fd-find```

```pacman: sudo pacman -S fd```

```apk: sudo apk add fd```

```zypper: sudo zypper install fd```

```brew: brew install fd```

```nix: nix profile install nixpkgs#fd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[find](/man/find)(1), [rg](/man/rg)(1), [locate](/man/locate)(1)
