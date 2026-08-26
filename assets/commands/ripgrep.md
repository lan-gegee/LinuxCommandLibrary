# TAGLINE

快速递归文本搜索工具

# TLDR

**在当前目录中递归搜索模式**

```rg "[pattern]"```

**只在特定类型的文件中搜索**

```rg -t [py] "[pattern]"```

**不区分大小写地搜索**

```rg -i "[pattern]"```

**显示匹配项周围的上下文行**

```rg -C [3] "[pattern]"```

**只列出包含匹配项的文件名**

```rg -l "[pattern]"```

**搜索时包括隐藏文件和目录**

```rg --hidden "[pattern]"```

**搜索字面字符串**（不用正则）

```rg -F "[literal string]"```

**统计每个文件的匹配数**

```rg -c "[pattern]"```

**使用多行匹配进行搜索**

```rg -U "[pattern]"```

**用字符串替换匹配项**

```rg "[pattern]" -r "[replacement]"```

# SYNOPSIS

**rg** [_options_] _pattern_ [_path_...]

# PARAMETERS

**-i**, **--ignore-case**
> 不区分大小写搜索。

**-s**, **--case-sensitive**
> 区分大小写搜索（覆盖 -i）。

**-S**, **--smart-case**
> 智能大小写：除非模式含大写字母，否则不区分大小写。

**-t**, **--type** _TYPE_
> 只搜索匹配 TYPE 的文件（例如 py、js、rust）。

**-T**, **--type-not** _TYPE_
> 排除匹配 TYPE 的文件。

**-C**, **--context** _NUM_
> 显示每个匹配项前后各 NUM 行。

**-A**, **--after-context** _NUM_
> 显示每个匹配项之后的 NUM 行。

**-B**, **--before-context** _NUM_
> 显示每个匹配项之前的 NUM 行。

**-l**, **--files-with-matches**
> 只打印包含匹配项的文件路径。

**-c**, **--count**
> 打印每个文件的匹配数。

**-F**, **--fixed-strings**
> 将模式视为字面字符串，而不是正则表达式。

**-w**, **--word-regexp**
> 只匹配完整单词。

**-x**, **--line-regexp**
> 只匹配整行内容。

**--hidden**
> 搜索隐藏文件和目录。

**-g**, **--glob** _GLOB_
> 包含或排除匹配 glob 的文件（加 ! 前缀表示排除）。

**-u**, **--unrestricted**
> 减少过滤。可重复使用（-uu 或 -uuu）以进一步放宽。

**-U**, **--multiline**
> 启用多行匹配。

**-P**, **--pcre2**
> 使用 PCRE2 正则引擎处理高级模式。

**-r**, **--replace** _STRING_
> 用 STRING 替换匹配项（支持捕获组）。

**-n**, **--line-number**
> 显示行号（连接到终端时默认开启）。

**-N**, **--no-line-number**
> 不显示行号。

**--no-ignore**
> 不遵循 .gitignore 及其他忽略文件。

**--type-list**
> 列出所有内置文件类型。

# DESCRIPTION

**ripgrep**（rg）是一款面向行的搜索工具，可递归地在目录中搜索正则表达式模式，通过 Rust 实现和并行目录遍历针对速度进行了优化。在搜索大型代码库时，它通常比传统的 grep、ag 或 ack 快数倍。

智能的默认设置让它开箱即用：它会自动遵循 .gitignore 规则、跳过二进制文件和隐藏目录，并提供带行号的彩色输出。这些默认行为免去了递归使用 grep 时常见的复杂排除模式。**--hidden** 标志会包含隐藏文件；**-u** 标志可逐步禁用过滤器：**-u** 搜索被忽略的文件，**-uu** 同时搜索隐藏文件，**-uuu** 还会搜索二进制文件。

Ripgrep 支持完整的 Unicode 正则语法、通过 **-P** 使用 PCRE2 模式、通过 **-F** 进行字面字符串匹配，以及通过 **-w** 进行单词边界匹配。文件类型过滤器（**-t**）涵盖数十种常见编程语言，并且可以自定义。使用 **--type-list** 查看所有可用类型。

# CAVEATS

正则语法默认使用 Rust 的 regex crate，与 POSIX 或 PCRE 存在一些差异（例如不加 **-P** 就不支持反向引用）。**-u** 标志需重复使用才能产生累积效果。默认情况下 ripgrep 不搜索 .gitignore 中列出的文件，当你在 Git 仓库之外搜索且存在全局 gitignore 时，这一点可能会令人意外。

# HISTORY

**ripgrep** 由 **Andrew Gallant** 于 **2016 年**创建。它将速度与智能默认设置相结合，已成为现代开发工作流中最流行的 grep 替代品之一。

# INSTALL

```dnf: sudo dnf install ripgrep```

```pacman: sudo pacman -S ripgrep```

```zypper: sudo zypper install ripgrep```

```brew: brew install ripgrep```

```nix: nix profile install nixpkgs#ripgrep```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[grep](/man/grep)(1), [ag](/man/ag)(1), [ack](/man/ack)(1), [fd](/man/fd)(1)
