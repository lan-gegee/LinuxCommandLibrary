# TAGLINE

生成 LaTeX 年度日程计划本

# TLDR

创建**每日计划本**

```yplan [language] [lettercase] [year] > [path/to/file.tex]```

# SYNOPSIS

**yplan** _LANGUAGE_ _CASE_ _YEAR_

# PARAMETERS

_LANGUAGE_
> 日/月名称使用的语言

_CASE_
> 大小写：大写或小写

_YEAR_
> 计划本对应的年份

# DESCRIPTION

**yplan** 为任意指定年份生成两页竖版每日计划本的 LaTeX 代码。输出可用 pdflatex 或其他 LaTeX 处理器编译。

该计划本格式专为打印和装订设计。

# CAVEATS

输出需要 LaTeX 处理。仅生成日历结构，不包含内容。

# INSTALL

```pacman: sudo pacman -S texlive-latexextra```

```apk: sudo apk add texlive-latexextra```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pdflatex](/man/pdflatex)(1), [pandoc](/man/pandoc)(1)
