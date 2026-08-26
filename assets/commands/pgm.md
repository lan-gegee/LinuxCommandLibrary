# TAGLINE

Netpbm 家族中的灰度图像格式

# TLDR

**查看 PGM 格式信息**

```pamfile [image.pgm]```

**将 JPEG 转换为 PGM**

```jpegtopnm [image.jpg] | ppmtopgm > [output.pgm]```

**从文本创建 PGM**

```echo "P2 3 2 255 0 128 255 64 192 32" > [output.pgm]```

**显示 PGM 图像**

```display [image.pgm]```

# SYNOPSIS

PGM 格式规范及相关工具集

# DESCRIPTION

**PGM**（Portable Graymap）是 Netpbm 家族中的一种灰度图像格式。它将图像存储为从 0（黑）到 maxval（白）的灰度值。

格式简单，分为 ASCII 或二进制两种，易于程序读写。

# FORMAT

```
P2              # ASCII format (P5 for binary)
width height
maxval          # Maximum gray value (usually 255)
pixel_values    # Space-separated (ASCII) or raw (binary)
```

# EXAMPLE FILE

```
P2
# comment
3 2
255
0   128  255
64  192  32
```

# CONVERSIONS

```bash
# JPEG to PGM
jpegtopnm photo.jpg | ppmtopgm > photo.pgm

# PNG to PGM
pngtopam image.png | pamtopnm | ppmtopgm > image.pgm

# PGM to PNG
pnmtopng image.pgm > image.png
```

# CAVEATS

ASCII 格式体积较大但人类可读；二进制格式更高效。PGM 是 Netpbm 工具集的一部分。

# HISTORY

PGM 由 **Jef Poskanzer** 设计，是 **Netpbm**（前身为 Pbmplus）图像处理工具集的一部分。

# SEE ALSO

[ppm](/man/ppm)(5), [pbm](/man/pbm)(5), [pnm](/man/pnm)(5), [netpbm](/man/netpbm)(1)
