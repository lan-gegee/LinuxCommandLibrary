# TAGLINE

支持格式转换的 JPEG 解压缩器

# TLDR

**将 JPEG 解压**为 PPM

```djpeg [image.jpg] > [output.ppm]```

**解压为 BMP** 格式

```djpeg -bmp [image.jpg] > [output.bmp]```

**解压为 GIF** 格式

```djpeg -gif [image.jpg] > [output.gif]```

**按比例缩放输出**

```djpeg -scale [1/2] [image.jpg] > [output.ppm]```

**仅输出灰度图**

```djpeg -grayscale [image.jpg] > [output.ppm]```

**显示详细信息**

```djpeg -verbose [image.jpg] > [output.ppm]```

# SYNOPSIS

**djpeg** [_options_] [_file_]

# PARAMETERS

_FILE_
> 输入的 JPEG 文件（省略时从 stdin 读取）。

**-bmp**
> 输出 BMP 格式。

**-gif**
> 输出 GIF 格式。

**-ppm**
> 输出 PPM 格式（默认）。

**-targa**
> 输出 Targa 格式。

**-scale** _M/N_
> 按比例缩放输出。

**-grayscale**
> 仅输出灰度图。

**-colors** _N_
> 量化为 N 种颜色。

**-verbose**, **-debug**
> 显示调试信息。

# DESCRIPTION

**djpeg** 将 JPEG 图像解压为多种未压缩或无损格式。它是 libjpeg/libjpeg-turbo 软件包的一部分，提供带格式转换功能的命令行 JPEG 解码。

该工具读取 JPEG 文件并输出 PPM、BMP、GIF 或 Targa 格式。解压时进行缩放非常高效，因为它使用 DCT 系数缩放，而不是先完全解压再调整大小。

djpeg 适用于批处理、脚本编写，以及将 JPEG 图像转换为便于其他工具进一步处理的格式。

# CAVEATS

输出默认写入 stdout（需重定向到文件）。GIF 的颜色量化可能损失画质。并非所有 JPEG 特性都得到同等支持。处理渐进式 JPEG 需要缓冲。

# HISTORY

djpeg 是 **libjpeg** 项目的一部分，该项目由 **Independent JPEG Group（IJG）** 自 **1991 年**起开发。libjpeg-turbo 是一个高性能分支，通过 SIMD 优化提供了兼容的 djpeg。

# INSTALL

```apt: sudo apt install libjpeg-turbo-progs```

```dnf: sudo dnf install libjpeg-turbo-utils```

```apk: sudo apk add libjpeg-turbo-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cjpeg](/man/cjpeg)(1), [jpegtran](/man/jpegtran)(1), [convert](/man/convert)(1)

# RESOURCES

```[Source code](https://github.com/libjpeg-turbo/libjpeg-turbo)```

```[Homepage](https://libjpeg-turbo.org/)```

<!-- verified: 2026-07-11 -->
