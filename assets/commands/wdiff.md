# TAGLINE

逐词比较文件的工具

# TLDR

**逐词比较文件**

```wdiff [file1.txt] [file2.txt]```

**仅显示统计信息**

```wdiff -s [file1.txt] [file2.txt]```

**忽略大小写**

```wdiff -i [file1.txt] [file2.txt]```

**使用彩色输出**

```wdiff -w $'\033[1;31m' -x $'\033[0m' -y $'\033[1;32m' -z $'\033[0m' [file1] [file2]```

**只显示差异（隐藏相同的单词）**

```wdiff -3 [file1.txt] [file2.txt]```

**避免标记跨行**

```wdiff -n [file1.txt] [file2.txt]```

# SYNOPSIS

**wdiff** [_-s_] [_-i_] [_options_] _file1_ _file2_

# PARAMETERS

**-s**, **--statistics**
> 显示单词计数统计和变化百分比。

**-i**, **--ignore-case**
> 忽略大小写差异。

**-3**, **--no-common**
> 隐藏相同（未改变）的单词；只显示差异。

**-1**, **--no-deleted**
> 在输出中不显示被删除的单词。

**-2**, **--no-inserted**
> 在输出中不显示被插入的单词。

**-n**, **--avoid-wraps**
> 防止标记跨越行边界。

**-a**, **--auto-pager**
> 自动将输出通过分页器输出。

**-t**, **--terminal**
> 使用 termcap 字符串进行终端强调。

**-l**, **--less-mode**
> 为 less 分页器优化的重叠打印格式。

**-p**, **--printer**
> 用于打印机输出的重叠打印强调。

**-d**, **--diff-input**
> 接受 unified diff 格式作为输入。

**-w** _STRING_
> 删除标记的起始符号（默认 `[-`）。

**-x** _STRING_
> 删除标记的结束符号（默认 `-]`）。

**-y** _STRING_
> 插入标记的起始符号（默认 `{+`）。

**-z** _STRING_
> 插入标记的结束符号（默认 `+}`）。

# DESCRIPTION

**wdiff** 以逐词方式比较两个文件，而不是像传统 diff 那样逐行比较。这使得它特别适合比较散文和文本文档——这类文档中的修改通常只涉及段落中的个别单词，而非整行。

默认情况下，被删除的单词用 `[-...-]` 标记包围，被插入的单词用 `{+...+}` 标记包围，使更改在输出中一目了然。这些标记可以自定义为 ANSI 转义码，生成用颜色高亮增删内容的彩色输出。

统计模式显示删除、插入和相同单词的数量以及变化百分比。在需要忽略大小写差异的场景下可以使用忽略大小写的比较。

# CAVEATS

大文件可能较慢。复杂格式会丢失。忽略行的结构。

# HISTORY

**wdiff** 作为 GNU 项目的一部分创建，现作为独立的 GNU 软件包维护。它提供适合散文和自然语言文本的词级差异对比，弥补了基于行的 diff 输出难以阅读的问题。

# INSTALL

```apt: sudo apt install wdiff```

```dnf: sudo dnf install wdiff```

```pacman: sudo pacman -S wdiff```

```zypper: sudo zypper install wdiff```

```brew: brew install wdiff```

```nix: nix profile install nixpkgs#wdiff```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[diff](/man/diff)(1), [colordiff](/man/colordiff)(1), [dwdiff](/man/dwdiff)(1)
