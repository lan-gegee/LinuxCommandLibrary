# TAGLINE

将光栅图像转换为 EPS 或 PDF

# TLDR

**将图像转换为 PDF**

```sam2p [input.png] [output.pdf]```

**转换为 EPS**

```sam2p [input.png] [output.eps]```

**使用 ZIP 压缩转换**

```sam2p -c:zip [input.png] [output.pdf]```

**使用 JPEG 压缩转换**

```sam2p -c:jpeg [input.png] [output.pdf]```

**缩放图像以适应页面**

```sam2p -e:scale [input.png] [output.pdf]```

**设置页边距**

```sam2p -m:1cm [input.png] [output.pdf]```

# SYNOPSIS

**sam2p** [_options_] _input_ _output_

# PARAMETERS

**-c:**_method_
> 压缩方法：none、zip、lzw、rle、fax、dct、jpeg。

**-1**, **-ps:1**
> 生成 PostScript Level 1 输出。

**-2**, **-ps:2**
> 生成 PostScript Level 2 输出（PS 的默认值）。

**-3**, **-ps:3**
> 生成 PostScript Level 3 输出。

**-pdf:b2**
> 生成带内联图像的 PDF 1.2（PDF 的默认值）。

**-e:scale**
> 缩放图像以适应页面。

**-e:rotate**
> 缩放并旋转图像以适应页面。

**-m:**_dimen_
> 设置所有页边距（如 -m:1cm、-m:0.5in）。

**-m:**_spec_**:**_dimen_
> 设置特定边距：l（左）、r（右）、t（上）、b（下）。

**-m:dpi:**_res_
> 设置输出分辨率。

**-j:quiet**
> 抑制警告，只显示错误。

# DESCRIPTION

**sam2p** 将光栅（位图）图像转换为输出体积尽可能小的 Adobe PostScript 或 PDF 文件。它可以完全控制标准兼容性、压缩方式和位深。

支持的输入格式包括 PNM、PBM、PGM、PPM、XPM、GIF、LBM、TGA、PCX、JPEG、TIFF、PNG、BMP、PS、EPS 和 PDF。输出格式包括 PS（1-3 级）、EPS、PDF 以及多种光栅格式。

# INSTALL

```aur: yay -S sam2p```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[convert](/man/convert)(1), [img2pdf](/man/img2pdf)(1), [a2ping](/man/a2ping)(1), [epstopdf](/man/epstopdf)(1), [ps2pdf](/man/ps2pdf)(1)
