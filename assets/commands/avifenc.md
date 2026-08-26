# TAGLINE

将图像编码为 AVIF 格式

# TLDR

将 PNG 图像**转换**为 AVIF

```avifenc [path/to/input.png] [path/to/output.avif]```

以**指定速度**编码（0=最慢，10=最快）

```avifenc --speed [2] [path/to/input.png] [path/to/output.avif]```

设置**质量**级别（0-100，越高越好）

```avifenc --qcolor [60] [path/to/input.png] [path/to/output.avif]```

# SYNOPSIS

**avifenc** [_options_] _input_ _output.avif_

# DESCRIPTION

**avifenc** 将图像编码为 AV1 图像文件格式（AVIF），这是一种基于 AV1 视频编解码器的现代图像格式。AVIF 具有出色的压缩效率，在同等画质下通常能获得比 JPEG 和 WebP 更小的文件。

该编码器支持 PNG、JPEG 和 Y4M 格式的输入，可以生成有损和无损的 AVIF 图像。

# PARAMETERS

**-q**, **--qcolor** _n_
> 彩色通道质量（0-100，100 为无损；默认 60）

**--qalpha** _n_
> alpha 通道质量（0-100，100 为无损；默认 100）

**-s**, **--speed** _n_
> 编码速度（0-10，默认 6）。数值越低质量越好但耗时越长

**-l**, **--lossless**
> 无损编码（将彩色和 alpha 的质量都设为 100）

**-d**, **--depth** _bits_
> 输出位深（8、10 或 12）

**-j**, **--jobs** _n_
> 并行编码任务数，或用 `all` 表示使用所有可用核心（默认：all）

**-o**, **--output** _file_
> 输出文件名（位置参数之外的另一种指定方式）

**--min** _n_, **--max** _n_
> 已弃用：最小/最大量化器（0-63，数值越低质量越好）。已被 `--qcolor` 取代

# CAVEATS

低速度值的编码可能极其缓慢。浏览器和图像查看器对 AVIF 的支持仍在增长，但尚未普及。极高的质量设置可能产生比原图更大的文件。旧的 `--min`/`--max` 量化器选项已在 libavif 1.2.0 中弃用，由 `--qcolor`/`--qalpha` 取代。

# HISTORY

AVIF 由开放媒体联盟（Alliance for Open Media）开发，于 **2019** 年定稿。它基于 AV1 视频编解码器，而 AV1 本身被设计为 HEVC/H.265 的免版税替代方案。

# INSTALL

```apt: sudo apt install libavif-bin```

```apk: sudo apk add libavif-apps```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[avifdec](/man/avifdec)(1), [cwebp](/man/cwebp)(1), [convert](/man/convert)(1)
