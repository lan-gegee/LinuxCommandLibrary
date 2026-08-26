# TAGLINE

无损图像压缩优化器

# TLDR

**优化 PNG 文件**

```ect [image.png]```

**以最大压缩率优化**

```ect -9 [image.png]```

**优化多个文件**

```ect [*.png]```

**递归优化**

```ect -recurse [directory]```

**保留修改时间**

```ect -keep [image.png]```

**去除元数据以获得最小体积**

```ect -strip [image.png]```

**无损优化 JPEG**

```ect [image.jpg]```

# SYNOPSIS

**ect** [_options_] _files_...

# PARAMETERS

_FILES_
> 要优化的图像文件。

**-1** 到 **-9**
> 压缩级别（1 = 快，9 = 最慢/最强）。默认为 **-3**。

**-recurse**
> 递归处理目录。

**-keep**
> 保留文件修改时间。

**-strip**
> 去除元数据（EXIF、注释、色彩配置文件）。

**-progressive**
> 将 JPEG 编码为渐进式。

**-gzip**
> 优化 gzip 文件而不是将其当作图像处理。

**-zip**
> 优化 ZIP 归档。

**-quiet**
> 抑制非错误输出。

**--mt-deflate**[=_N_]
> 对 deflate 阶段进行多线程处理；可选指定为 _N_ 个线程。

**--mt-file**[=_N_]
> 并行处理多个输入文件。

**-help**
> 显示帮助信息。

# DESCRIPTION

**ECT**（Efficient Compression Tool）对 PNG、JPEG 和 gzip 文件进行无损优化以获得更小的体积。它在保持无损的同时，比许多同类工具实现更好的压缩效果。

该工具结合多种压缩策略来减小文件体积而不损失质量。对于 PNG，它优化滤波器和 DEFLATE 压缩；对于 JPEG，它优化 Huffman 表。

ECT 适用于 Web 优化，在保持完美图像质量的同时减少带宽和存储占用。

# CAVEATS

高压缩级别非常慢（级别 9 每张图像可能需要数分钟）。文件会被原地重写。如果需要绝对最小的输出，请使用 **-strip**，因为默认情况下会保留元数据。

# HISTORY

ECT 是作为一个高性能无损图像优化器开发的，将多种压缩工具（zopfli、optipng 等）的技术整合到一个高效的单体工具中。

# INSTALL

```aur: yay -S ect```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[optipng](/man/optipng)(1), [pngcrush](/man/pngcrush)(1), [jpegoptim](/man/jpegoptim)(1)
