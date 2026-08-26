# TAGLINE

将 PDF 文件转换为 PostScript

# TLDR

**将 PDF 转换为 PostScript**

```pdf2ps [input.pdf] [output.ps]```

**转换指定页面**

```pdf2ps -f [1] -l [5] [input.pdf] [output.ps]```

**为 Level 2 PostScript 打印机转换**

```pdf2ps -level2 [input.pdf] [output.ps]```

**指定纸张大小**

```pdf2ps -paper [A4] [input.pdf] [output.ps]```

**通过管道直接输出到打印机**

```pdf2ps [input.pdf] - | lpr```

# SYNOPSIS

**pdf2ps** [_options_] _input.pdf_ [_output.ps_]

# PARAMETERS

**-f** _num_
> 要转换的第一页（默认：1）。

**-l** _num_
> 要转换的最后一页（默认：文档最后一页）。

**-level1**, **-level2**, **-level3**
> 设置输出的 PostScript 语言级别。Level 1 兼容性最好，Level 2 增加了彩色与压缩支持，Level 3 支持最新特性。

**-paper** _size_
> 设置纸张大小（例如 letter、A4、legal）。

**-r** _dpi_
> 设置光栅化内容的分辨率（每英寸点数）。

**-q**
> 安静模式。抑制 Ghostscript 的常规消息。

# DESCRIPTION

**pdf2ps** 将 PDF 文件转换为 PostScript。某些打印机和打印流程需要 PostScript。输出质量与兼容性取决于所选的 PostScript 级别。

# POSTSCRIPT LEVELS

```
Level 1 - Most compatible
Level 2 - Color, compression
Level 3 - Latest features
```

# EXAMPLE

```bash
# Basic conversion
pdf2ps document.pdf document.ps

# Print via PostScript
pdf2ps document.pdf - | lpr
```

# CAVEATS

输出文件可能很大。级别会影响兼容性。如需更好的输出质量，可以考虑 Poppler 的 pdftops。

# HISTORY

pdf2ps 是 **Ghostscript** 的一部分。这款 PostScript/PDF 解释器最初由 **Artifex Software** 开发。

# INSTALL

```apt: sudo apt install ghostscript```

```dnf: sudo dnf install ghostscript```

```pacman: sudo pacman -S ghostscript```

```apk: sudo apk add ghostscript```

```zypper: sudo zypper install ghostscript```

```brew: brew install ghostscript```

```nix: nix profile install nixpkgs#ghostscript```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pdftops](/man/pdftops)(1), [ps2pdf](/man/ps2pdf)(1), [gs](/man/gs)(1), [lpr](/man/lpr)(1), [pdftotext](/man/pdftotext)(1), [enscript](/man/enscript)(1)
