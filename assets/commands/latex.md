# TAGLINE

用于高质量排版排印的文档准备系统

# TLDR

**编译 LaTeX 文档**

```latex [document.tex]```

**直接编译为 PDF**

```pdflatex [document.tex]```

**使用 XeLaTeX 编译**

```xelatex [document.tex]```

**使用 LuaLaTeX 编译**

```lualatex [document.tex]```

**持续编译**

```latexmk -pvc [document.tex]```

**清理辅助文件**

```latexmk -c```

# SYNOPSIS

**latex** [_options_] _file_

**pdflatex** [_options_] _file_

# PARAMETERS

**-interaction** _mode_
> 交互模式：nonstopmode、batchmode。

**-output-directory** _dir_
> 输出目录。

**-shell-escape**
> 启用 Shell 命令。

**-synctex** _n_
> 生成 SyncTeX 数据。

**-halt-on-error**
> 在第一个错误处停止。

# DESCRIPTION

**LaTeX** 是一套面向高质量排版排印的文档准备系统。它是科学论文、学位论文和技术文档领域的标准工具。

常用引擎：**pdflatex**（传统）、**xelatex**（Unicode/现代字体）、**lualatex**（支持 Lua 脚本）。大多数文档使用 pdflatex 或 lualatex。

# DOCUMENT STRUCTURE

```latex
\documentclass{article}
\usepackage{amsmath}

\title{My Document}
\author{Author Name}

\begin{document}
\maketitle

\section{Introduction}
Content here.

\end{document}
```

# CAVEATS

涉及交叉引用时通常需要多次编译。生成参考文献需要运行 bibtex/biber。可以用 latexmk 实现自动化。

# HISTORY

LaTeX 由 **Leslie Lamport** 于 **20 世纪 80 年代**创建，是为 TeX（Donald Knuth 于 1978 年开发）设计的一套宏。它至今仍是学术出版领域的标准。

# INSTALL

```dnf: sudo dnf install texlive```

```apk: sudo apk add texlive```

```zypper: sudo zypper install texlive```

```brew: brew install texlive```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pdflatex](/man/pdflatex)(1), [bibtex](/man/bibtex)(1), [latexmk](/man/latexmk)(1), [texdoc](/man/texdoc)(1)
