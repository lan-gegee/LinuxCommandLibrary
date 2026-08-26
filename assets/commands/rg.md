# TAGLINE

具有智能默认设置的快速递归文本搜索

# TLDR

在当前目录中**搜索模式**

```rg "[pattern]"```

**在指定文件或目录中搜索**

```rg "[pattern]" [path]```

**不区分大小写地搜索**

```rg -i "[pattern]"```

**只匹配整个单词**

```rg -w "[pattern]"```

随匹配结果**显示行号**

```rg -n "[pattern]"```

显示匹配处周围的**上下文行**

```rg -C [3] "[pattern]"```

**搜索特定文件类型**

```rg -t [py] "[pattern]"```

**搜索隐藏文件和目录**

```rg --hidden "[pattern]"```

**列出包含匹配的文件**（不显示内容）

```rg -l "[pattern]"```

**统计每个文件的匹配数**

```rg -c "[pattern]"```

# SYNOPSIS

**rg** [_options_] _pattern_ [_path_...]

# PARAMETERS

**-i**, **--ignore-case**
> 不区分大小写搜索

**-S**, **--smart-case**
> 除非模式含大写字母，否则不区分大小写

**-w**, **--word-regexp**
> 只匹配整个单词

**-x**, **--line-regexp**
> 只匹配整行

**-c**, **--count**
> 显示每个文件的匹配数

**-l**, **--files-with-matches**
> 只显示包含匹配的文件名

**-L**, **--files-without-match**
> 只显示不含匹配的文件名

**-n**, **--line-number**
> 显示行号（终端输出时默认开启）

**-H**, **--with-filename**
> 在匹配结果中显示文件名

**-A** _num_, **--after-context**
> 显示匹配后的 num 行

**-B** _num_, **--before-context**
> 显示匹配前的 num 行

**-C** _num_, **--context**
> 显示匹配前后的各 num 行

**-t** _type_, **--type**
> 只搜索指定类型的文件

**-T** _type_, **--type-not**
> 排除指定类型的文件

**-g** _glob_, **--glob**
> 包含/排除匹配 glob 的文件

**--hidden**
> 搜索隐藏文件和目录

**-u**, **--unrestricted**
> 减少过滤（可叠加：-uu、-uuu）

**-F**, **--fixed-strings**
> 将模式视为字面字符串

**-e** _pattern_
> 指定模式（可多次使用）

**-r** _replacement_, **--replace**
> 用文本替换匹配内容

**-o**, **--only-matching**
> 只显示匹配的部分

# DESCRIPTION

**rg**（ripgrep）是一个快速的递归 grep 替代品，默认遵循 gitignore 规则。它在目录中搜索正则表达式模式，自动跳过隐藏文件、二进制文件和被忽略的路径。

Ripgrep 使用 Rust 的正则引擎以获得速度，支持大多数 Perl 兼容的正则语法。它专为搜索代码库而设计，自动检测并跳过二进制文件，并遵循 .gitignore 模式。

可以使用 **-e** 指定多个模式。文件类型过滤使用内置定义（运行 **rg --type-list** 查看可用类型）。配合 **-g** 的自定义 glob 提供灵活的包含/排除模式。

输出到终端时默认带颜色。脚本中请使用 **--color=never**，通过管道传给分页器时使用 **--color=always**。

# CAVEATS

默认情况下，ripgrep 跳过隐藏文件、gitignored 文件和二进制文件。使用 **--hidden**、**--no-ignore** 或 **-u** 可以进行更全面的搜索。

Ripgrep 使用 Rust 正则语法，与 PCRE 略有不同。某些高级特性如反向引用不受支持。

对于非常大的结果集，考虑使用 **-l**（仅列出文件）或 **-c**（统计数量）来减少输出量。

# HISTORY

Ripgrep 由 **Andrew Gallant**（BurntSushi）创建，首次发布于 **2016 年**。它使用 Rust 编写，结合了 The Silver Searcher（ag）的易用性与 GNU grep 的原始速度，同时增加了 gitignore 支持。它已成为最受欢迎的 grep 替代品之一。

# INSTALL

```apt: sudo apt install ripgrep```

```dnf: sudo dnf install ripgrep```

```pacman: sudo pacman -S ripgrep```

```apk: sudo apk add ripgrep```

```zypper: sudo zypper install ripgrep```

```brew: brew install ripgrep```

```nix: nix profile install nixpkgs#ripgrep```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[grep](/man/grep)(1), [ag](/man/ag)(1), [ack](/man/ack)(1), [git-grep](/man/git-grep)(1)
