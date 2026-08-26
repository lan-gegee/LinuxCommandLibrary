# TAGLINE

使用 Ghostscript 和 pdfTeX 裁剪 PDF 页面的白边

# TLDR

对每页**自动检测并移除**白边

```pdfcrop [path/to/input_file.pdf] [path/to/output_file.pdf]```

为每页设置**指定数值的边距**

```pdfcrop [path/to/input_file.pdf] --margins '[left] [top] [right] [bottom]' [path/to/output_file.pdf]```

四边使用相同值设置**统一边距**

```pdfcrop [path/to/input_file.pdf] --margins [300] [path/to/output_file.pdf]```

使用**自定义边界框**进行裁剪

```pdfcrop [path/to/input_file.pdf] --bbox '[left] [top] [right] [bottom]' [path/to/output_file.pdf]```

为**奇数页和偶数页**使用不同的边界框

```pdfcrop [path/to/input_file.pdf] --bbox-odd '[left] [top] [right] [bottom]' --bbox-even '[left] [top] [right] [bottom]' [path/to/output_file.pdf]```

使用**较低分辨率**加快边距检测

```pdfcrop [path/to/input_file.pdf] --resolution 72 [path/to/output_file.pdf]```

# SYNOPSIS

**pdfcrop** [_options_] _input.pdf_ [_output.pdf_]

# PARAMETERS

**--margins** _"l t r b"_
> 裁剪后添加边距（单位为 bp）

**--clip**
> 将内容裁剪到边界框内

**--bbox** _"l t r b"_
> 对所有页面使用指定的边界框

**--bbox-odd** _"l t r b"_
> 奇数页的边界框

**--bbox-even** _"l t r b"_
> 偶数页的边界框

**--resolution** _dpi_
> 边界框检测使用的分辨率（默认：72）

**--restricted**
> 开启受限模式（Web 使用更安全）

**--verbose**
> 打印额外的处理信息

**--debug**
> 启用调试模式，输出更多信息

**--gscmd** _command_
> 指定要使用的 Ghostscript 命令

**--pdftexcmd** _command_
> 指定要使用的 pdftex 命令

**--help**
> 显示帮助信息

**--version**
> 显示版本信息

# DESCRIPTION

**pdfcrop** 使用 Ghostscript 进行边界检测、pdfTeX 执行实际裁剪，自动检测并移除 PDF 页面的白边。它会分析每一页以找到实际内容的边界框，生成一个空白空间最小的 PDF。

该工具特别适合处理扫描文档、去除期刊文章的多余白边，或优化适配电子阅读器屏幕的 PDF。它可以自动处理所有页面，也可以应用自定义边界框。

# CAVEATS

需要安装 Ghostscript 和 pdfTeX。对于边缘附近内容非常浅的页面，自动检测可能效果不佳。处理时间随分辨率增加而变长；在精度要求不高时可使用较低分辨率以加快速度。

# HISTORY

最初由 Heiko Oberdiek 作为 **texlive** 的一部分开发。在学术和出版流程中广泛用于文档准备。现作为 TeX 工具 ho-tex 集合的一部分维护。

# INSTALL

```pacman: sudo pacman -S texlive-binextra```

```apk: sudo apk add texlive-binextra```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pdfjam](/man/pdfjam)(1), [pdfbook2](/man/pdfbook2)(1), [gs](/man/gs)(1), [pdflatex](/man/pdflatex)(1)
