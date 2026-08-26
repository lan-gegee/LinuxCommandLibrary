# TAGLINE

递归搜索目录的 grep

# TLDR

**递归搜索**

```rgrep "[pattern]" [path]```

**不区分大小写**

```rgrep -i "[pattern]" [path]```

**显示行号**

```rgrep -n "[pattern]" [path]```

**仅列出匹配的文件**

```rgrep -l "[pattern]" [path]```

**统计匹配数**

```rgrep -c "[pattern]" [path]```

**排除目录**

```rgrep --exclude-dir=[node_modules] "[pattern]" [path]```

# SYNOPSIS

**rgrep** [_-i_] [_-n_] [_-l_] [_options_] _pattern_ [_path_]

# PARAMETERS

**-i**
> 不区分大小写搜索。

**-n**
> 显示行号。

**-l**
> 只打印包含匹配的文件名。

**-c**
> 只打印每个文件的匹配行数。

**-v**
> 反转匹配（选择不匹配的行）。

**-w**
> 只匹配整个单词。

**-E**
> 使用扩展正则表达式（与 egrep 相同）。

**-P**
> 使用 Perl 兼容正则表达式。

**--color** _WHEN_
> 为匹配着色：auto、always 或 never。

**--exclude-dir** _DIR_
> 跳过指定目录。

**--include** _GLOB_
> 只搜索匹配模式的文件。

**--exclude** _GLOB_
> 跳过匹配模式的文件。

# DESCRIPTION

**rgrep** 是等价于 **grep -r** 的便捷封装，提供遍历目录树的递归文本搜索。它从指定路径开始遍历所有子目录，使用标准 grep 正则表达式语法在文件内容中搜索给定模式。

所有标准 grep 选项都可用于 rgrep，包括不区分大小写搜索（**-i**）、显示行号（**-n**）、仅列出匹配文件（**-l**）和反转匹配（**-v**）。**--exclude-dir** 和 **--include** 标志允许过滤要搜索的文件和目录，这对跳过 node_modules 或构建输出等大型目录非常重要。

在大多数 GNU/Linux 系统上，rgrep 作为 GNU grep 软件包的一部分默认安装。若要在大型代码库上获得更好的性能，请考虑使用 ripgrep（**rg**），它速度明显更快并自动遵循 .gitignore 规则。

# CAVEATS

默认跟随命令行中给出的符号链接。大型目录树上可能较慢。在 GNU grep 中已弃用（推荐 **grep -r**），但仍为向后兼容而保留。大型代码库上建议改用 ripgrep（**rg**）以获得更好性能。

# INSTALL

```apt: sudo apt install grep```

```dnf: sudo dnf install grep```

```pacman: sudo pacman -S grep```

```zypper: sudo zypper install grep```

```brew: brew install grep```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[grep](/man/grep)(1), [egrep](/man/egrep)(1), [fgrep](/man/fgrep)(1), [rg](/man/rg)(1)
