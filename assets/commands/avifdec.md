# TAGLINE

将 AVIF 图像解码为标准格式

# TLDR

将 AVIF **解码**为 PNG

```avifdec [input.avif] [output.png]```

以指定质量解码为 **JPEG**

```avifdec -q [85] [input.avif] [output.jpg]```

仅**显示**图像信息

```avifdec -i [input.avif]```

以 **16 位色深**解码（仅限 PNG）

```avifdec -d 16 [input.avif] [output.png]```

使用**多线程**解码

```avifdec -j [4] [input.avif] [output.png]```

# SYNOPSIS

**avifdec** [_options_] _input.avif_ _output_

# DESCRIPTION

**avifdec** 将 AVIF（AV1 Image File Format）图像解码为 PNG、JPEG 或 Y4M 等标准格式。AVIF 是一种现代图像格式，压缩率和画质均优于 JPEG。

该工具是 libavif 的一部分，可用于查看 AVIF 图像并将其转换为支持更广泛的格式。

# PARAMETERS

**-c** _codec_
> 要使用的 AV1 编解码器（aom、dav1d、libgav1）。默认：从可用编解码器中自动选择

**-d** _depth_
> 输出位深，8 或 16（仅限 PNG；JPEG 始终为 8bpc）

**-q** _quality_
> 输出 JPEG 质量，0-100（默认：90）

**-j** _jobs_
> 工作线程数，或用 'all' 表示使用所有核心（默认：all）

**-i**, **--info**
> 显示图像信息而不保存到磁盘

**--png-compress** _level_
> PNG 压缩级别，0-9（0=不压缩，9=最大压缩）

**--chroma-upsampling** _mode_
> 420/422 的色度上采样：automatic、fastest、best、nearest、bilinear（默认：automatic）

**--ignore-icc**
> 忽略内嵌的 ICC 色彩配置文件

**--index** _n_
> 解码指定的帧索引，或用 'all' 表示每一帧（默认：0）

**--no-strict**
> 禁用严格的校验检查

**-r**
> 输出原始 RGB 值，而不是与 alpha 预乘

# FEATURES

- HDR 支持（10 位、12 位）
- 广色域
- ICC 配置文件保留
- EXIF 元数据提取
- 动画帧选择

# CAVEATS

输出格式支持取决于编译期选项。大图可能消耗大量内存。HDR 内容在不支持 HDR 的查看器中可能无法正确显示。

# HISTORY

**avifdec** 由 Joe Drago 和开放媒体联盟（Alliance for Open Media）作为 libavif 的一部分开发，于 **2019** 年前后发布，以支持 AOM 标准化的新 AVIF 格式。

# INSTALL

```apt: sudo apt install libavif-bin```

```apk: sudo apk add libavif-apps```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[avifenc](/man/avifenc)(1), [imagemagick](/man/imagemagick)(1), [convert](/man/convert)(1)
