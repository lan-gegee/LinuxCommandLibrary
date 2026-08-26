# TAGLINE

将 Abekas YUV 格式转换为 PPM

# TLDR

**将 Abekas YUV 转换为 PPM**

```yuvtoppm [width] [height] [input.yuv] > [output.ppm]```

# SYNOPSIS

**yuvtoppm** _width_ _height_ [_file_]

# PARAMETERS

_width_
> 图像宽度。

_height_
> 图像高度。

# DESCRIPTION

**yuvtoppm** 将 Abekas YUV 格式转换为 PPM。Abekas 是专业视频设备厂商。属于 Netpbm 工具集。

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

[ppmtoyuv](/man/ppmtoyuv)(1), [yuvsplittoppm](/man/yuvsplittoppm)(1)
