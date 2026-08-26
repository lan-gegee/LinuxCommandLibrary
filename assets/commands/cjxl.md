# TAGLINE

JPEG XL 图像编码器

# TLDR

以默认设置将图像**编码**为 JPEG XL 格式

```cjxl [input.png] [output.jxl]```

以指定**质量等级**编码（1-100，越高越好）

```cjxl -q [90] [input.png] [output.jxl]```

以**无损**压缩方式编码

```cjxl -q [100] [input.png] [output.jxl]```

以指定 **effort 等级**编码（1-9，越高越慢但文件越小）

```cjxl -e [7] [input.png] [output.jxl]```

将 JPEG 文件**无损转码**为 JPEG XL（保留原始数据）

```cjxl --lossless_jpeg=1 [input.jpg] [output.jxl]```

以指定 **distance 值**编码（0=无损，越高压缩越多）

```cjxl -d [1.0] [input.png] [output.jxl]```

# SYNOPSIS

**cjxl** [_options_] _input_ _output.jxl_

# PARAMETERS

**-q** _N_, **--quality**=_N_
> 质量设置，取值 1 到 100。100 为数学上无损。默认为 90。

**-d** _N_, **--distance**=_N_
> 目标视觉距离（0=无损，1.0=视觉无损，值越大压缩越多）。覆盖质量设置。

**-e** _N_, **--effort**=_N_
> 编码器 effort 等级，取值 1 到 9。值越大文件越小但编码越慢。默认为 7。

**--lossless_jpeg**=_N_
> 编码 JPEG 输入时，设为 1 会保留原始 JPEG 数据以便按位精确重建。

**-j**, **--jpeg_transcode**
> 无损 JPEG 转码模式（--lossless_jpeg=1 的快捷方式）。

**--num_threads**=_N_
> 使用的线程数。0 表示使用所有可用核心。

**--progressive**
> 为输出文件启用渐进式解码。

**--premultiply**=_N_
> 预乘 alpha 通道（0=否，1=是，-1=自动）。

**-h**, **--help**
> 显示帮助信息并退出。

**-v**, **--verbose**
> 启用详细输出。

# DESCRIPTION

**cjxl** 是 JPEG XL 的参考编码器。JPEG XL 是旨在同时取代 JPEG 和 PNG 的新一代图像格式，由 JPEG 委员会维护的 libjxl 项目开发。

相比传统格式，JPEG XL 提供更优的压缩效果，同时支持有损和无损模式。其独特之处在于能够对现有 JPEG 文件进行无损转码，将其大小缩减约 20%，同时允许完美重建原始 JPEG。

该编码器支持多种输入格式，包括 PNG、APNG、GIF、JPEG、PPM 和 PFM。它原生支持高位深、HDR 内容和动画。effort 参数用于在编码速度和压缩率之间权衡。

# CAVEATS

截至 2024 年，浏览器对 JPEG XL 的支持仍然有限。无损 JPEG 转码功能仅适用于标准基线 JPEG，在渐进式或算术编码的 JPEG 上可能失败。高 effort 等级会显著增加编码时间。

# HISTORY

JPEG XL 于 **2022** 年被标准化为 **ISO/IEC 18181**。该格式由 JPEG 委员会开发，融合了 Google 的 PIK 与 Cloudinary 的 FUIF 项目的技术。cjxl 编码器是 libjxl 项目自 **2019** 年起发布的参考实现的一部分。

# INSTALL

```apt: sudo apt install libjxl-tools```

```apk: sudo apk add libjxl-tools```

```zypper: sudo zypper install libjxl-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[djxl](/man/djxl)(1), [cjpeg](/man/cjpeg)(1), [convert](/man/convert)(1), [cwebp](/man/cwebp)(1)

# RESOURCES

```[Source code](https://github.com/libjxl/libjxl)```

```[Homepage](https://jpegxl.info/)```

<!-- verified: 2026-06-22 -->
