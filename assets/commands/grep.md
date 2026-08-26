# TAGLINE

模式匹配文本搜索工具

# TLDR

**在文件中搜索模式**

```grep [pattern] [file]```

**忽略大小写搜索**

```grep -i [pattern] [file]```

**递归搜索目录**

```grep -r [pattern] [directory]```

**显示行号**

```grep -n [pattern] [file]```

**反转匹配（排除模式）**

```grep -v [pattern] [file]```

**扩展正则表达式**

```grep -E '[regex]' [file]```

**只显示包含匹配的文件名**

```grep -rl [pattern] [directory]```

**统计匹配数量**

```grep -c [pattern] [file]```

**带上下文搜索（前后各 3 行）**

```grep -C 3 [pattern] [file]```

**递归搜索但仅限特定文件类型**

```grep -r --include='[*.py]' [pattern] [directory]```

# SYNOPSIS

**grep** [_options_] _pattern_ [_files_]

# PARAMETERS

_PATTERN_
> 要匹配的正则表达式模式。

_FILES_
> 要搜索的文件。

**-i**, **--ignore-case**
> 忽略大小写匹配。

**-v**, **--invert-match**
> 选择不匹配的行。

**-r**, **--recursive**
> 递归搜索目录。

**-n**, **--line-number**
> 显示行号。

**-c**, **--count**
> 仅打印匹配计数。

**-l**, **--files-with-matches**
> 仅打印文件名。

**-E**, **--extended-regexp**
> 使用扩展正则表达式。

**-F**, **--fixed-strings**
> 匹配字面字符串。

**-o**, **--only-matching**
> 仅打印匹配到的部分。

**-A** _NUM_
> 打印匹配行之后的 NUM 行。

**-B** _NUM_
> 打印匹配行之前的 NUM 行。

**-C** _NUM_
> 打印 NUM 行上下文。

**-P**, **--perl-regexp**
> 使用 Perl 兼容正则表达式（PCRE）。

**-w**, **--word-regexp**
> 仅匹配完整单词。

**-q**, **--quiet**, **--silent**
> 不输出内容；若找到匹配则以退出码 0 退出。

**--include** _GLOB_
> 只搜索匹配 glob 模式的文件。

**--exclude** _GLOB_
> 跳过匹配 glob 模式的文件。

**--color**
> 高亮匹配项。

**--help**
> 显示帮助信息。

# DESCRIPTION

**grep** 在文件中搜索与正则表达式模式匹配的行。它是最基础的 Unix 工具之一，其名称来自 ed 编辑器中的 g/re/p（global regular expression print）命令。

该工具支持基本和扩展正则表达式、递归目录搜索以及多种输出格式。它可以搜索多个文件、显示匹配周围的上下文，并用颜色高亮结果。

# CAVEATS

基本与扩展正则表达式的语法存在差异。二进制文件可能产生意外的输出。未经优化时处理大文件可能较慢。

# HISTORY

grep 由 **Ken Thompson** 于 **1973 年** 在 **贝尔实验室（Bell Labs）** 创建。它的灵感来自 ed 中的 g/re/p 命令。GNU grep 是当今使用最广泛的实现。

# INSTALL

```apt: sudo apt install grep```

```dnf: sudo dnf install grep```

```pacman: sudo pacman -S grep```

```apk: sudo apk add grep```

```zypper: sudo zypper install grep```

```brew: brew install grep```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[egrep](/man/egrep)(1), [fgrep](/man/fgrep)(1), [rg](/man/rg)(1), [ack](/man/ack)(1), [sed](/man/sed)(1)
