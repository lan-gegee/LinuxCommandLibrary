# TAGLINE

为来自文件或标准输入的行编号

# TLDR

对文件中的**非空行编号**

```nl [path/to/file]```

从 **stdin** 读取

```[command] | nl```

对**包括空行在内的所有行**编号

```nl -b a [path/to/file]```

只对匹配某个**正则表达式模式**的行编号

```nl -b p'[pattern]' [path/to/file]```

为行号指定一个特定的**增量**

```nl -i [increment] [path/to/file]```

指定行号**格式**（左/右对齐，是否补零）

```nl -n [rz|ln|rn]```

指定行号**宽度**（默认为 6）

```nl -w [col_width] [path/to/file]```

在数字与文本之间使用一个特定的**分隔符**

```nl -s "[separator]" [path/to/file]```

# SYNOPSIS

**nl** [_options_] [_file_]

# PARAMETERS

**-b, --body-numbering _style_**
> 正文编号样式：a（全部）、t（非空行，默认）、n（无）、p_regex_（模式）。

**-h, --header-numbering _style_**
> 页眉行的编号样式（默认：n）。

**-f, --footer-numbering _style_**
> 页脚行的编号样式（默认：n）。

**-i, --line-increment _n_**
> 行号增量（默认：1）。

**-l, --join-blank-lines _n_**
> 将 n 个连续空行合并为一组计数。

**-n, --number-format _format_**
> 格式：ln（左侧，不补零）、rn（右侧，不补零，默认）、rz（右侧，补零）。

**-p, --no-renumber**
> 不在逻辑页处重置行号。

**-w, --number-width _n_**
> 行号列的宽度（默认：6）。

**-s, --number-separator _string_**
> 数字与文本之间的字符串（默认：TAB）。

**-v, --starting-line-number _n_**
> 首个行号（默认：1）。

**-d, --section-delimiter _chars_**
> 逻辑页分隔符字符（默认：\\:）。

# DESCRIPTION

**nl** 为来自文件或标准输入的行编号。默认情况下它只对非空行编号，输出中的空行会原样保留且不带行号。

该命令能识别由特殊字符序列分隔的逻辑页区块（页眉、正文、页脚），从而为每个区块使用不同的编号样式。不过最常见的用法只是简单地为文件内容添加行号。

输出格式可以自定义：数字可以左对齐或右对齐，可用空格或零填充，并可用任意字符串与正文分隔。

# CAVEATS

与 **cat -n** 不同，后者会对包括空行在内的所有行编号。逻辑页功能（区块）很少用到，但如果输入中包含分隔符字符（默认为 \\:），可能导致意外行为。

# HISTORY

nl 起源于 System V Unix，并被 POSIX 规范化。自项目创立之初起它就是 GNU coreutils 的一部分。

# INSTALL

```apt: sudo apt install coreutils```

```dnf: sudo dnf install coreutils```

```pacman: sudo pacman -S coreutils```

```apk: sudo apk add coreutils```

```zypper: sudo zypper install coreutils```

```brew: brew install coreutils```

```nix: nix profile install nixpkgs#coreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cat](/man/cat)(1), [pr](/man/pr)(1), [head](/man/head)(1), [tail](/man/tail)(1)
