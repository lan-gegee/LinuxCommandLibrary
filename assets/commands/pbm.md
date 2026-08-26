# TAGLINE

Portable Bitmap（PBM）图像文件格式

# TLDR

**查看 PBM 文件的**尺寸和类型

```pnmfile [image.pbm]```

**将 PBM 转换为 ASCII 字符画**

```pbmtoascii [image.pbm]```

**将任意图像转换为 PBM**（1 位）

```anytopnm [input] | pamditherbw | pnmtopnm > [output.pbm]```

**将 PBM 转换为 PNG**

```pnmtopng [image.pbm] > [image.png]```

# SYNOPSIS

PBM 格式由 **Netpbm** 软件包中的 **pbm*** 工具读写。

# DESCRIPTION

**PBM**（Portable Bitmap）是 Netpbm 格式中最简单的一种，用于存储 1 位（黑白）光栅图像。它有两种变体：纯 ASCII 形式（魔数 **P1**）和二进制形式（魔数 **P4**）。文件头记录格式、宽度和高度；随后是像素数据，其中 **0** 表示白色，**1** 表示黑色。

PBM 是一种无损格式，定位为图像处理流水线的最小公分母：几乎所有 Netpbm 工具都能读写它，因此在串联转换工具时常用作中间格式。

# CAVEATS

只能存储黑和白（每像素 1 位）；灰度请用 PGM，彩色请用 PPM。二进制形式更紧凑，但 ASCII 形式便于人工阅读。文件不压缩，因此可能比等效的 PNG 大得多。

# HISTORY

PBM 起源于 **Jef Poskanzer** 于 **1988 年**开发的 PBMplus 工具包，目前作为 **Netpbm** 项目的一部分维护。

# INSTALL

```nix: nix profile install nixpkgs#pbm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pgm](/man/pgm)(5), [ppm](/man/ppm)(5), [pnm](/man/pnm)(5), [netpbm](/man/netpbm)(1), [pnmtopng](/man/pnmtopng)(1)
