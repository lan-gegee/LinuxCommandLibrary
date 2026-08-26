# TAGLINE

对 JPEG 图像执行无损变换

# TLDR

将图像**水平或垂直镜像**

```jpegtran -flip [horizontal|vertical] [path/to/image.jpg] > [path/to/output.jpg]```

将图像顺时针**旋转** 90、180 或 270 度

```jpegtran -rotate [90|180|270] [path/to/image.jpg] > [path/to/output.jpg]```

沿左上到右下轴**转置**

```jpegtran -transpose [path/to/image.jpg] > [path/to/output.jpg]```

转换为**灰度图**

```jpegtran -grayscale [path/to/image.jpg] > [path/to/output.jpg]```

**裁剪**到指定尺寸

```jpegtran -crop [W]x[H]+[X]+[Y] [path/to/image.jpg] > [path/to/output.jpg]```

裁剪并保存到**指定文件**

```jpegtran -crop [W]x[H] -outfile [path/to/output.jpg] [path/to/image.jpg]```

# SYNOPSIS

**jpegtran** [_options_] [_file_]

# PARAMETERS

**-flip** _horizontal|vertical_
> 镜像图像

**-rotate** _90|180|270_
> 顺时针旋转指定角度

**-transpose**
> 沿主对角线转置

**-transverse**
> 沿反对角线转置

**-grayscale**
> 转换为灰度图

**-crop** _WxH+X+Y_
> 在偏移 X,Y 处裁剪为宽 W、高 H

**-outfile** _FILE_
> 将输出写入指定文件

**-optimize**
> 优化 Huffman 表

**-progressive**
> 创建渐进式 JPEG

# DESCRIPTION

**jpegtran** 对 JPEG 图像执行无损变换。与重新编码不同，这些操作直接作用于 DCT 系数，能完全保持图像质量。

支持的无损操作包括旋转（以 90 度为步长）、翻转、转置、灰度转换以及裁剪（按 MCU 边界进行）。该工具还可以进行优化或在基线格式与渐进式格式之间转换。

# CAVEATS

裁剪尺寸可能被调整到 MCU（最小编码单元）边界。某些变换可能需要 -trim 来丢弃边缘不完整的块。默认输出到 stdout；请重定向或使用 -outfile。

# HISTORY

jpegtran 是 libjpeg/libjpeg-turbo（JPEG 参考库）的一部分。最初的 libjpeg 由 Independent JPEG Group 自 **1991 年**起开发。

# INSTALL

```apt: sudo apt install libjpeg-turbo-progs```

```dnf: sudo dnf install libjpeg-turbo-utils```

```apk: sudo apk add libjpeg-turbo-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cjpeg](/man/cjpeg)(1), [djpeg](/man/djpeg)(1), [convert](/man/convert)(1)
