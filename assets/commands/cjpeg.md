# TAGLINE

JPEG 图像压缩器

# TLDR

以默认质量将 BMP 图像**压缩**为 JPEG

```cjpeg [image.bmp] > [output.jpg]```

以指定**质量等级**（1-100，越高越好）**压缩** PPM 图像

```cjpeg -quality [85] [image.ppm] > [output.jpg]```

创建用于网页优化的**渐进式 JPEG**

```cjpeg -progressive [image.bmp] > [output.jpg]```

以**灰度**输出进行压缩

```cjpeg -grayscale [image.ppm] > [output.jpg]```

**优化 Huffman 表**以获得更小的文件

```cjpeg -optimize [image.bmp] > [output.jpg]```

使用 outfile 选项**直接设置输出文件**

```cjpeg -outfile [output.jpg] [image.bmp]```

# SYNOPSIS

**cjpeg** [_options_] [_input_file_]

# PARAMETERS

**-quality** _N_
> 设置压缩质量等级（1-100）。值越高质量越好，但文件更大。默认为 75。

**-progressive**
> 创建渐进式 JPEG 文件，可在下载过程中逐步显示。

**-grayscale**
> 即使输入为彩色也强制输出灰度图像。

**-optimize**
> 优化 Huffman 编码表。文件更小但压缩更慢。

**-outfile** _name_
> 指定输出文件名，而不是写入 stdout。

**-targa**
> 输入文件为 Targa 格式（自动检测失败时有用）。

**-smooth** _N_
> 平滑输入图像以减少抖动伪影（1-100）。

**-maxmemory** _N_
> 将内存用量限制为 N KB。

**-restart** _N_
> 每 N 行 MCU 输出一个重启标记（若使用 B 后缀则为 N 个块）。

**-arithmetic**
> 使用算术编码代替 Huffman 编码（文件更小，兼容性较差）。

**-baseline**
> 强制输出基线（baseline）JPEG（8 位、非渐进）。

**-verbose** 或 **-debug**
> 启用调试输出。

# DESCRIPTION

**cjpeg** 是来自 Independent JPEG Group（IJG）libjpeg 库的图像压缩工具，在优化版 libjpeg-turbo 中同样可用。它将光栅图像文件压缩为 JPEG/JFIF 格式。

该工具读取多种格式的输入图像，包括 BMP、PPM、PGM 和 Targa，然后输出压缩后的 JPEG 数据。默认情况下，输出到标准输出，便于管道和重定向操作。输入格式会根据文件头自动检测。

对于网页使用，**-progressive** 选项可创建在下载过程中逐步渲染的图像。**-optimize** 标志通过更好的 Huffman 表减小文件大小，但编码速度较慢。质量设置在 75-85 左右通常能在文件大小与视觉保真度之间取得良好平衡。

# CAVEATS

默认输出到 stdout，需要重定向或使用 **-outfile** 才能保存。**-arithmetic** 选项生成的文件与某些旧解码器不兼容。极低的质量设置（低于 20）会产生严重的可见伪影。

# HISTORY

cjpeg 起源于 Independent JPEG Group 的免费 JPEG 软件，由 Tom Lane 于 **1991** 年首次发布。它成为 Unix 上标准的 JPEG 压缩工具。始于 **2009** 年的 libjpeg-turbo 项目使用 SIMD 指令提供显著更快的编解码优化版本。

# INSTALL

```apt: sudo apt install libjpeg-turbo-progs```

```dnf: sudo dnf install libjpeg-turbo-utils```

```apk: sudo apk add libjpeg-turbo-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[djpeg](/man/djpeg)(1), [jpegtran](/man/jpegtran)(1), [convert](/man/convert)(1), [ffmpeg](/man/ffmpeg)(1)

# RESOURCES

```[Source code](https://github.com/libjpeg-turbo/libjpeg-turbo)```

```[Homepage](https://libjpeg-turbo.org/)```

<!-- verified: 2026-06-22 -->
