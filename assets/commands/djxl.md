# TAGLINE

JPEG XL 解码器，支持多种输出格式

# TLDR

**将 JPEG XL 解码**为 PNG

```djxl [image.jxl] [output.png]```

**解码为 JPEG**

```djxl [image.jxl] [output.jpg]```

**解码为 PPM**

```djxl [image.jxl] [output.ppm]```

**仅显示图片信息**

```djxl --info [image.jxl]```

**以指定线程数解码**

```djxl --num_threads [4] [image.jxl] [output.png]```

**从动画中解码指定帧**

```djxl --frame [5] [animation.jxl] [frame5.png]```

# SYNOPSIS

**djxl** [_options_] _input.jxl_ [_output_]

# PARAMETERS

_INPUT_
> 要解码的 JPEG XL 文件。

_OUTPUT_
> 输出文件（格式由扩展名推断）。

**--info**
> 仅显示图片信息。

**--num_threads** _N_
> 解码线程数。

**--frame** _N_
> 从动画中提取指定帧。

**--jpeg**
> 若原始 JPEG 经无损重压缩，则精确重建原 JPEG。

**--bits_per_sample** _N_
> 输出位深。

**--help**
> 显示帮助信息。

# DESCRIPTION

**djxl** 是参考实现的 JPEG XL 解码器，可将 JPEG XL 图像转换为其他格式。它属于 libjxl 参考实现，支持包括动画、HDR 和无损 JPEG 重建在内的全部 JPEG XL 特性。

对于由 JPEG 无损重压缩而来的 JPEG XL 文件，可以使用 --jpeg 标志解码回与原始字节完全一致的 JPEG。这使 JPEG XL 可以作为一层可逆的压缩方案。

解码器支持多种输出格式，可根据文件扩展名自动识别格式，还能提取动画图像中的元数据和单个帧。

# CAVEATS

输出格式的支持情况取决于编译配置。部分 HDR 特性可能需要特定的输出格式。JPEG 重建要求原图经过无损压缩。大图可能占用大量内存。

# HISTORY

djxl 是 JPEG XL 的 **libjxl** 参考实现的一部分，由 **JPEG 委员会**主导开发并有 Google 参与。JPEG XL 于 **2022 年**标准化，是融合了 Google PIK 和 Cloudinary FUIF 特性的新一代图像格式。

# INSTALL

```apt: sudo apt install libjxl-tools```

```apk: sudo apk add libjxl-tools```

```zypper: sudo zypper install libjxl-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cjxl](/man/cjxl)(1), [djpeg](/man/djpeg)(1), [convert](/man/convert)(1)

# RESOURCES

```[Source code](https://github.com/libjxl/libjxl)```

```[Homepage](https://jpegxl.info/)```

<!-- verified: 2026-07-11 -->
