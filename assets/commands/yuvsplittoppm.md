# TAGLINE

将 YUV 分量文件合并为 PPM 图像

# TLDR

**将 YUV 分量文件合并为 PPM 图像**

```yuvsplittoppm [base] [width] [height] > [output.ppm]```

**使用 CCIR 601（MPEG）色彩缩放合并**

```yuvsplittoppm -ccir601 [base] [width] [height] > [output.ppm]```

# SYNOPSIS

**yuvsplittoppm** [_-ccir601_] _basename_ _width_ _height_

# PARAMETERS

_basename_
> 分量文件的基本名称。将读取 _basename_.Y、_basename_.U 和 _basename_.V。

_width_
> 图像宽度（像素）。

_height_
> 图像高度（像素）。

**-ccir601**
> 使用 CCIR 601（MPEG）范围而非默认的 JFIF（JPEG）范围解释 YUV 值。

# DESCRIPTION

**yuvsplittoppm** 读取分别包含 Y、U、V 颜色分量的三个原始文件，并在标准输出上生成 PPM 图像。文件名由 _basename_ 加上 `.Y`、`.U` 和 `.V` 后缀构成。由于这些文件是不带头的原始数据，必须在命令行上给出图像尺寸。

它是 [ppmtoyuvsplit](/man/ppmtoyuvsplit)(1) 的逆操作，属于 Netpbm 工具集。

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

[ppmtoyuvsplit](/man/ppmtoyuvsplit)(1), [yuvtoppm](/man/yuvtoppm)(1), [rgb3toppm](/man/rgb3toppm)(1)
