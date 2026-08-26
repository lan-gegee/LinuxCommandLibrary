# TAGLINE

将原始 RGB 数据转换为 PPM 格式

# TLDR

**将原始 RGB 数据转换为 PPM**

```rawtoppm [width] [height] [input.raw] > [output.ppm]```

**以交错格式转换**

```rawtoppm -interrow [width] [height] [input.raw] > [output.ppm]```

# SYNOPSIS

**rawtoppm** [_options_] _width_ _height_ [_file_]

# PARAMETERS

_width_
> 图像宽度（像素）。

_height_
> 图像高度（像素）。

**-headerskip** _bytes_
> 跳过头部字节。

**-interrow**
> 按行交错的 RGB。

**-interpixel**
> 按像素交错的 RGB。

# DESCRIPTION

**rawtoppm** 将原始 RGB 颜色数据转换为便携式像素图（PPM）格式，它把字节流解释为按指定尺寸排列的红、绿、蓝像素值。该工具支持颜色通道的不同内存布局：默认期望按像素交错的数据（RGBRGB...），而 **-interrow** 读取按行交错的数据，即每个颜色平面以完整一行的形式存储后才轮到下一个。

由于原始数据不包含元数据，必须同时指定宽度和高度作为参数。**-headerskip** 选项可跳过文件开头的非图像数据。该命令属于 Netpbm 图像处理工具集。

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

[rawtopgm](/man/rawtopgm)(1), [ppmtorgb3](/man/ppmtorgb3)(1)
