# TAGLINE

为源代码添加语法高亮

# TLDR

**高亮代码文件**

```pygmentize [file.py]```

**指定输出格式**

```pygmentize -f [html] [file.py]```

**输出到文件**

```pygmentize -o [output.html] [file.py]```

**指定语言**

```pygmentize -l [python] [file]```

**列出可用的词法分析器**

```pygmentize -L lexers```

**生成 CSS**

```pygmentize -S [monokai] -f html > [style.css]```

# SYNOPSIS

**pygmentize** [_options_] [_file_]

# PARAMETERS

_FILE_
> 输入文件。

**-f** _FORMATTER_
> 输出格式。

**-l** _LEXER_
> 语言词法分析器。

**-o** _FILE_
> 输出文件。

**-S** _STYLE_
> 语法高亮样式。

**-L**
> 列出可用选项。

# DESCRIPTION

**pygmentize** 是 Pygments 语法高亮库的命令行界面。它读取源代码文件并以多种格式输出语法高亮版本，包括终端 ANSI 颜色、HTML、LaTeX、RTF 和 SVG，支持超过 500 种编程语言和标记格式。

该工具根据文件扩展名自动检测输入语言，也可用 **-l** 显式指定。输出格式用 **-f** 设置；生成 CSS 样式表时用 **-S** 控制视觉主题。pygmentize 广泛用于在文档、博客和演示文稿中生成高亮代码。

# CAVEATS

需要 Python 库。支持多种输出格式。

# HISTORY

Pygments 作为 **Python 的语法高亮库**而创建。

# INSTALL

```apk: sudo apk add py3-pygments```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[highlight](/man/highlight)(1), [source-highlight](/man/source-highlight)(1)
