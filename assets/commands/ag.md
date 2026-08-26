# TAGLINE

快速搜索代码，类似 ack 但更快

# TLDR

递归地**搜索**模式

```ag [pattern]```

在**指定文件类型**中搜索

```ag --python [pattern]```

**不区分大小写**搜索

```ag -i [pattern]```

只显示包含匹配项的**文件名**

```ag -l [pattern]```

搜索**字面字符串**（不用正则表达式）

```ag -Q "[literal string]"```

搜索并带**上下文**行

```ag -C [3] [pattern]```

# SYNOPSIS

**ag** [_options_] _pattern_ [_path_...]

# DESCRIPTION

**ag**（The Silver Searcher）是一款类似于 ack 但速度更快的代码搜索工具。它递归地搜索源代码，自动忽略 .gitignore 和 .hgignore 中列出的文件，并跳过隐藏文件和二进制文件。

该工具专为速度优化，采用多线程和内存映射 I/O。它支持 Perl 兼容正则表达式，并能提供带上下文行的彩色输出。

# PARAMETERS

**-i**, **--ignore-case**
> 不区分大小写搜索

**-s**, **--case-sensitive**
> 区分大小写搜索

**-v**, **--invert-match**
> 反转匹配结果

**-w**, **--word-regexp**
> 只匹配完整单词

**-l**, **--files-with-matches**
> 只打印包含匹配项的文件名

**-L**, **--files-without-matches**
> 打印不包含匹配项的文件名

**-c**, **--count**
> 打印每个文件的匹配次数

**-C** _n_, **--context=**_n_
> 打印 n 行上下文

**-A** _n_, **--after=**_n_
> 打印匹配行之后的 n 行

**-B** _n_, **--before=**_n_
> 打印匹配行之前的 n 行

**-Q**, **--literal**
> 把模式当作字面字符串处理

**--python**, **--js**, **--html**, etc.
> 只搜索特定文件类型

**-g** _pattern_
> 搜索匹配模式的文件名

**--hidden**
> 搜索隐藏文件

**-u**, **--unrestricted**
> 搜索所有文件（忽略 .gitignore）

**-z**, **--search-zip**
> 在压缩文件内部搜索

# CONFIGURATION

**~/.agignore**
> 搜索时全局忽略的文件模式。

**.agignore**
> 按项目忽略的文件模式，语法与 .gitignore 类似。

# CAVEATS

在超大规模代码库上不如 **ripgrep** 快。某些正则特性可能与 grep 不同。文件类型检测基于扩展名，而非内容。

# HISTORY

**ag** 由 Geoff Greer 创建，于 **2011** 年首次发布。它的定位是更快的 ack 替代品，凭借并行化和更智能的文件过滤带来了显著的速度提升。它也启发了后来 ripgrep 之类的工具。

# INSTALL

```apt: sudo apt install silversearcher-ag```

```dnf: sudo dnf install the_silver_searcher```

```pacman: sudo pacman -S the_silver_searcher```

```apk: sudo apk add the_silver_searcher```

```brew: brew install the_silver_searcher```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[rg](/man/rg)(1), [ack](/man/ack)(1), [grep](/man/grep)(1), [git-grep](/man/git-grep)(1)
