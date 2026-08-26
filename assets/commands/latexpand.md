# TAGLINE

通过展开 \input 和 \include 指令将 LaTeX 源码扁平化为单文件

# TLDR

**展开 LaTeX 文件中的 include**

```latexpand [input.tex] > [output.tex]```

**保留注释**

```latexpand --keep-comments [input.tex]```

**内联参考文献**

```latexpand --expand-bbl [input.bbl] [input.tex]```

**输出到文件**

```latexpand -o [output.tex] [input.tex]```

**找不到被包含文件时报错**

```latexpand --fatal [input.tex]```

**内联展开 \usepackage 指令**

```latexpand --expand-usepackage [input.tex]```

**同时展开 biber 参考文献**

```latexpand --biber [input.bcf] [input.tex]```

# SYNOPSIS

**latexpand** [_options_] _file_

# PARAMETERS

**-o**, **--output** _file_
> 输出到文件而不是标准输出。

**--verbose**
> 显示正在进行的操作。

**--keep-comments**
> 在输出中保留注释（以 % 开头的行以及 \end{document} 之后的内容）。默认情况下注释会被剔除。

**--empty-comments**
> 为清晰起见保留空注释（行尾多余的 %）。

**--keep-includes**
> 不展开 \input 和 \include 指令。

**--expand-usepackage**
> 当能在 $TEXINPUTS 或当前目录中找到匹配的 .sty 文件时，展开 \usepackage 指令。

**--expand-bbl** _file_
> 用给定的 .bbl 文件就地内联替换参考文献。

**--biber** _file_
> 内联 biber 的 .bcf/参考文献数据（适用于采用 biber 后端的 biblatex）。

**-d**, **--define** _key=val_
> 定义用于替换的宏。可以多次指定。

**--explain**
> 在输出中生成解释性注释，说明展开了哪些内容。

**--show-graphics**
> 在 stderr 上列出被包含的图形文件。

**--graphics_extensions** _LIST_
> 可能的图形文件扩展名列表（以冒号分隔）。

**--fatal**
> 如果找不到某个被包含的文件，则以错误退出（默认行为是发出警告）。

**--makeatletter**
> 在导言区插入一个 \makeatletter，以帮助解决某些包含问题。

**--in-encoding** _FMT_
> 使用 PerlIO 语法指定输入文件编码（例如 :encoding(UTF-8)）。

**--out-encoding** _FMT_
> 使用 PerlIO 语法指定输出文件编码。

**--help**
> 显示帮助。

# DESCRIPTION

**latexpand** 展开 LaTeX 文档中的 **\input** 和 **\include** 命令，生成一个扁平化的单一文件。适用于要求单文件提交的场合（如 arXiv 期刊投稿），或需要交给不支持 include 的工具处理的情况。它是一个通过 CTAN 和 TeX Live 分发的 Perl 脚本。

# INSTALL

```pacman: sudo pacman -S texlive-binextra```

```apk: sudo apk add texlive-binextra```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pdflatex](/man/pdflatex)(1), [latexmk](/man/latexmk)(1)
