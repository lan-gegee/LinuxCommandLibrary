# TAGLINE

统计 LaTeX 文档中的字数

# TLDR

**统计字数**

```texcount [document.tex]```

**简要输出**

```texcount -brief [document.tex]```

**包含子统计**

```texcount -sub [document.tex]```

**HTML 输出**

```texcount -html [document.tex]```

**统计多个文件**

```texcount -merge [file1.tex] [file2.tex]```

**详细输出**

```texcount -v [document.tex]```

# SYNOPSIS

**texcount** [_-brief_] [_-sub_] [_-html_] [_options_] _files_

# PARAMETERS

**-brief**
> 简短输出。

**-sub**
> 按章节细分统计。

**-html**
> HTML 输出。

**-merge**
> 合并多个文件的统计结果。

**-v**
> 详细输出。

**-inc**
> 包含被 \input 的文件。

# DESCRIPTION

**texcount** 通过正确解析 TeX 语法来统计 LaTeX 文档的字数，而不是简单地对所有以空白分隔的词元计数。它区分正文字词、标题字词、题注字词和数学公式，提供排除宏名和格式化命令后的准确计数。

**-sub** 选项可按节、章或其他结构元素细分统计，便于跟踪文档各部分的进度。多个文件可用 **-merge** 一起处理，**-inc** 会跟随 \\input 和 \\include 指令统计被包含的文件。输出格式包括纯文本、HTML 以及展示每个词如何被分类的详细模式。

# CAVEATS

仅适用于 LaTeX。自定义宏可能造成混淆。需要 Perl。

# HISTORY

**TeXcount** 的创建目的是通过正确解析 TeX 语法，为 LaTeX 文档提供准确的字数统计。

# INSTALL

```pacman: sudo pacman -S texlive-binextra```

```apk: sudo apk add texlive-binextra```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wc](/man/wc)(1), [latex](/man/latex)(1), [detex](/man/detex)(1)
