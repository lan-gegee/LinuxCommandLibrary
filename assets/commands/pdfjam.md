# TAGLINE

使用 LaTeX 和 pdfpages 操作 PDF 页面

# TLDR

**合并 PDF**

```pdfjam [file1.pdf] [file2.pdf] -o [output.pdf]```

**选择页面**

```pdfjam [input.pdf] [1,3,5-7] -o [output.pdf]```

**旋转页面**

```pdfjam --angle [90] [input.pdf] -o [output.pdf]```

**每张纸两页**

```pdfjam --nup 2x1 [input.pdf] -o [output.pdf]```

**缩放页面**

```pdfjam --scale [0.8] [input.pdf] -o [output.pdf]```

**设置纸张大小**

```pdfjam --paper [a4paper] [input.pdf] -o [output.pdf]```

**横向方向**

```pdfjam --landscape [input.pdf] -o [output.pdf]```

# SYNOPSIS

**pdfjam** [_options_] _files_ [_page-ranges_] [_--outfile file_]

# PARAMETERS

**-o**, **--outfile** _FILE_
> 输出文件名。

**--nup** _COLxROW_
> 每张纸的页数。

**--angle** _DEGREES_
> 旋转角度。

**--scale** _FACTOR_
> 缩放系数。

**--paper** _SIZE_
> 纸张大小。

**--landscape**
> 横向方向。

**--frame** _true|false_
> 页面周围加边框。

**--delta** _X Y_
> 偏移调整。

**--offset** _X Y_
> 页面偏移。

**--suffix** _STRING_
> 输出文件名后缀。

# DESCRIPTION

**pdfjam** 使用 LaTeX 和 pdfpages 操作 PDF 页面。它可以组合、重排和变换 PDF 文档。

页面选择支持如 1-5 的范围或如 1,3,5 的列表。负数表示从末尾倒数计数。

N-up 打印将多页放在一张纸上。常见布局有 2x1、2x2 和 3x3。

旋转可用于横向文档或纠正方向。支持任意角度。

缩放调整页面大小。结合纸张大小设置，可以将内容适配到不同格式。

输出默认沿用修改后的输入文件名。suffix 选项在原文件名上追加后缀。

# CAVEATS

需要 TeX Live 或类似的 LaTeX 发行版。复杂的 PDF 可能无法正确处理。某些 PDF 特性可能会丢失。

# HISTORY

**pdfjam** 由 **David Firth** 创建，是 LaTeX pdfpages 包的 shell 封装。它为 PDF 操作提供了便捷的命令行入口。

# INSTALL

```pacman: sudo pacman -S texlive-binextra```

```apk: sudo apk add texlive-binextra```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pdfunite](/man/pdfunite)(1), [pdftk](/man/pdftk)(1), [pdfpages](/man/pdfpages)(1)
