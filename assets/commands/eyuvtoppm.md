# TAGLINE

Encoder YUV 转 PPM 转换器

# TLDR

**将 EYUV 转换为 PPM**

```eyuvtoppm --width [width] --height [height] [input.eyuv] > [output.ppm]```

# SYNOPSIS

**eyuvtoppm** [**--width** _width_] [**--height** _height_] [_eyuvfile_]

# PARAMETERS

**--width** _width_
> 图像宽度（像素，必须为偶数）。必填。

**--height** _height_
> 图像高度（像素，必须为偶数）。必填。

_eyuvfile_
> 输入 EYUV 文件；省略时从标准输入读取。

**-quiet**
> 抑制提示信息（libnetpbm 通用选项）。

# DESCRIPTION

**eyuvtoppm** 将 Encoder YUV（EYUV）视频格式文件转换为 PPM（Portable Pixmap）格式。EYUV 是一种 Berkeley YUV 格式，用于视频编码工作流，存储未压缩的 YUV 色彩空间数据。

该工具是 Netpbm 图像处理工具集的一部分。由于 EYUV 文件不包含图像尺寸元数据，因此必须显式指定 **--width** 和 **--height** 选项。输出 PPM 格式是一种简单、未压缩的格式，在图像处理和转换领域得到广泛支持。

# INSTALL

```apt: sudo apt install netpbm```

```dnf: sudo dnf install netpbm```

```pacman: sudo pacman -S netpbm```

```apk: sudo apk add netpbm```

```zypper: sudo zypper install netpbm```

```brew: brew install netpbm```

```nix: nix profile install nixpkgs#netpbm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ppmtoeyuv](/man/ppmtoeyuv)(1), [yuvtoppm](/man/yuvtoppm)(1)

# RESOURCES

```[Source code](https://sourceforge.net/projects/netpbm/)```

```[Documentation](https://netpbm.sourceforge.net/doc/eyuvtoppm.html)```

<!-- verified: 2026-07-15 -->
