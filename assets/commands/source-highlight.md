# TAGLINE

将源代码转换为语法高亮输出

# TLDR

**将源文件高亮**为 HTML

```source-highlight -i [file.java] -o [file.html]```

**自动检测语言进行高亮**

```source-highlight [file.py]```

**显式指定源语言**

```source-highlight -s [cpp] -i [file.cc]```

**输出为其他格式**

```source-highlight -f [latex] -i [file.c] -o [file.tex]```

**按模式高亮多个文件**

```source-highlight *.java```

**列出支持的语言**

```source-highlight --lang-list```

**列出支持的输出格式**

```source-highlight --outlang-list```

**从 stdin 高亮**

```cat [file.py] | source-highlight -s python```

# SYNOPSIS

**source-highlight** [_options_] [_files_]

# PARAMETERS

**-i**, **--input** _file_
> 输入文件。默认：stdin。

**-o**, **--output** _file_
> 输出文件。默认：stdout 或带有相应扩展名的输入文件名。

**-s**, **--src-lang** _lang_
> 源语言。若未指定，则根据文件扩展名推测。

**-f**, **--out-format** _format_
> 输出格式（html, xhtml, latex, texinfo, ansi, odt 等）。

**--style-file** _file_
> 用于高亮颜色和样式的样式文件。

**--lang-list**
> 列出所有支持的源语言。

**--outlang-list**
> 列出所有支持的输出格式。

**--lang-def** _file_
> 使用自定义的语言定义文件。

**--outlang-def** _file_
> 使用自定义的输出语言定义文件。

**-n**, **--line-number**[=_padding_]
> 添加行号，可选指定填充宽度。

**--tab** _n_
> 设置制表符宽度（默认：8）。

**--title** _string_
> 设置文档标题。

**--css** _file_
> 为 HTML 输出使用 CSS 文件。

**-d**, **--doc**
> 创建独立文档。

**-h**, **--help**
> 显示帮助信息。

**-V**, **--version**
> 显示版本信息。

# DESCRIPTION

**source-highlight** 将源代码文件转换为各种输出格式的语法高亮文档。它动态读取语言规范，因此无需重新编译即可轻松扩展对新编程语言的支持。

该工具支持众多编程语言，包括 C、C++、Java、Python、Perl、Ruby、Shell 等。输出格式包括 HTML、XHTML、LaTeX、ANSI 终端转义序列等。

使用通配符处理多个文件时，输出文件名会通过追加相应的扩展名自动生成。该工具还可以作为 CGI 脚本用于网页端语法高亮，或与 **less** 集成，在查看源文件时自动进行语法高亮。

# CAVEATS

需要 Boost regex 库。语言检测依赖文件扩展名；对于扩展名不标准的文件请使用 **-s**。自定义语言和样式定义需要熟悉定义文件的格式。ANSI 输出在某些终端中可能无法正确显示。

# HISTORY

**GNU Source-highlight** 由 Lorenzo Bettini 创建，于 **1999 年**首次发布。它的开发目标是打造一款灵活、可扩展的语法高亮工具，无需重新编译即可支持新语言。该项目是 GNU 计划的一部分，遵循 GNU 通用公共许可证发行。开发持续至今，不断加入对新语言和新输出格式的支持。

# INSTALL

```apt: sudo apt install source-highlight```

```dnf: sudo dnf install source-highlight```

```pacman: sudo pacman -S source-highlight```

```apk: sudo apk add source-highlight```

```zypper: sudo zypper install source-highlight```

```brew: brew install source-highlight```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[highlight](/man/highlight)(1), [pygmentize](/man/pygmentize)(1), [bat](/man/bat)(1)
