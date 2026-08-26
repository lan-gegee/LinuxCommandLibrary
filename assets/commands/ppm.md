# TAGLINE

Portable Pixmap 彩色图像格式

# TLDR

**PPM 格式概览**

```ppm```

**转换为 PPM**

```anytopnm [image] | ppmtopgm```

**查看 PPM 信息**

```pamfile [image.ppm]```

# SYNOPSIS

**ppm** [_file_]

# PARAMETERS

_FILE_
> PPM 图像文件。

# DESCRIPTION

**PPM**（Portable Pixmap）是 Netpbm 家族中的彩色图像格式。每个像素以 RGB 三元组存储，取值范围从 0 到指定的最大值。该格式有两种变体：plain（ASCII 文本，人类可读）和 raw（二进制，紧凑）。

PPM 是 Netpbm 流水线中彩色图像的通用交换格式。大量工具可以在 PPM 与其他格式之间互相转换，通过串联简单的单一用途工具即可完成图像处理。同一家族中，PGM 处理灰度图，PBM 处理位图。

# CAVEATS

属于 Netpbm 格式家族。PPM 用于彩色图像，PGM 用于灰度图像，PBM 用于位图。

# HISTORY

PPM 作为 **Netpbm** 可移植图像格式家族的一部分而创建。

# SEE ALSO

[pnm](/man/pnm)(5), [pgm](/man/pgm)(5), [pbm](/man/pbm)(5), [pamfile](/man/pamfile)(1)
