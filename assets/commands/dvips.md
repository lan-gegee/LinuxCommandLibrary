# TAGLINE

将 DVI 转换为 PostScript

# TLDR

**将 DVI 转换为 PostScript**

```dvips [document.dvi] -o [document.ps]```

**转换指定页**

```dvips -p [5] -l [10] [document.dvi] -o [output.ps]```

**输出到标准输出**

```dvips [document.dvi] -o -```

**按指定纸张大小转换**

```dvips -t [letter] [document.dvi] -o [output.ps]```

**以横向模式转换**

```dvips -t landscape [document.dvi] -o [output.ps]```

**经由 ps2pdf 生成 PDF**

```dvips [document.dvi] -o - | ps2pdf - [document.pdf]```

# SYNOPSIS

**dvips** [_options_] _file.dvi_

# PARAMETERS

**-o** _file_
> 输出文件名（- 表示标准输出）。

**-p** _num_
> 要输出的第一页。

**-l** _num_
> 要输出的最后一页。

**-t** _paper_
> 纸张类型：letter、a4、landscape。

**-D** _dpi_
> 以每英寸点数表示的分辨率。

**-x** _mag_
> 放大倍数。

**-c** _copies_
> 打印份数。

**-e** _num_
> 最大像素漂移量。

**-Z**
> 压缩位图字体。

**-Ppdf**
> 针对 PDF 转换进行优化。

# DESCRIPTION

**dvips** 将 TeX 和 LaTeX 生成的 DVI（DeVice Independent）文件转换为 PostScript。输出可直接打印，或使用 ps2pdf 等工具转换为 PDF。

该程序处理 DVI 指令、嵌入字体并生成 PostScript 代码。它支持字体替换、纸张大小选择以及针对不同输出设备的多种优化选项。

# CAVEATS

需要已安装 Type 1 或位图字体。一些现代 TeX 工作流直接使用 pdflatex 或 xelatex，绕过 DVI。PostScript 输出可能很大；使用 -Z 进行压缩。字体路径必须在 texmf.cnf 中配置。

# HISTORY

dvips 由 **Tomas Rokicki** 于 **20 世纪 80 年代末**编写，此后一直是 TeX 发行版的标准组成部分。尽管直接生成 PDF 已更为常见，它仍被广泛使用。该程序作为 TeX Live 的一部分持续维护。

# INSTALL

```apt: sudo apt install texlive-binaries```

```apk: sudo apk add texlive-dvi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[latex](/man/latex)(1), [ps2pdf](/man/ps2pdf)(1), [pdflatex](/man/pdflatex)(1), [tex](/man/tex)(1)
