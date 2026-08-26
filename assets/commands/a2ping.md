# TAGLINE

在 PostScript、EPS 和 PDF 格式之间转换

# TLDR

**转换** PostScript 文件为 PDF

```a2ping [input.ps] [output.pdf]```

**转换** EPS 文件为 PDF 并收紧边界框

```a2ping --bboxfrom=compute-gs [input.eps] [output.pdf]```

转换为**指定的输出格式**

```a2ping --outformat=[pdf|eps|ps] [input.ps] [output]```

# SYNOPSIS

**a2ping** [_options_] _inputfile_ [_outputfile_]

# DESCRIPTION

**a2ping** 是一个 Perl 脚本，可在多种页面描述格式之间转换，包括 PostScript（PS）、Encapsulated PostScript（EPS）、PDF 及相关格式。它充当 Ghostscript 和其他工具的智能包装器，自动检测输入格式并执行适当的转换。

该工具特别适合在正确处理边界框的前提下转换 EPS 图形，是为 LaTeX 文档准备插图的理想选择。它能计算精确的边界框、处理字体嵌入，并针对不同用途优化输出。

# PARAMETERS

**--outformat=**_format_
> 输出格式：pdf、eps、eps2、eps3、ps、ps2、ps3

**--bboxfrom=**_method_
> 边界框来源：adsc（来自 DSC 注释）、compute-gs（用 Ghostscript 计算）

**--resolution=**_dpi_
> 设置输出分辨率，单位为 dpi

**--compress=**_method_
> 压缩方式：none、zip、best

**--gsextra=**_options_
> 向 Ghostscript 传递额外选项

**--help**
> 显示帮助信息

# CAVEATS

大多数转换需要安装 Ghostscript。某些复杂的 PostScript 特性可能无法完美转换。该工具主要为单页文档设计；多页文档的处理情况可能有所不同。

# HISTORY

**a2ping** 由 Peter Szabo 编写，于 **2003 年**首次发布。它的开发是为了解决将 EPS 文件转换为 PDF 时边界框不正确的常见难题，尤其面向用 LaTeX 撰写科学文献的用户。该工具后来成为 TeX Live 发行版的组成部分。

# INSTALL

```pacman: sudo pacman -S texlive-binextra```

```apk: sudo apk add texlive-binextra```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gs](/man/gs)(1), [ps2pdf](/man/ps2pdf)(1), [epstopdf](/man/epstopdf)(1), [convert](/man/convert)(1)

# RESOURCES

```[Source code](https://github.com/pts/a2ping)```

```[Documentation](https://ctan.org/pkg/a2ping)```

<!-- verified: 2026-06-10 -->
