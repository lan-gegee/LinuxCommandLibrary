# TAGLINE

生成像素值直方图图像

# TLDR

**生成直方图可视化**

```pnmhistmap [input.pnm] > [histogram.pgm]```

**指定输出尺寸**

```pnmhistmap -width [256] -height [100] [input.pnm] > [histogram.pgm]```

# SYNOPSIS

**pnmhistmap** [_options_] [_file_]

# PARAMETERS

**-width** _n_
> 输出宽度。

**-height** _n_
> 输出高度。

**-white**
> 使用白色背景。

**-verbose**
> 打印统计信息。

# DESCRIPTION

**pnmhistmap** 生成一幅可视化的直方图图像，展示 PNM 图像中像素值的分布情况。输出是一幅 PNM 图像：横轴表示采样值，纵轴表示拥有该值的像素数量。

对于彩色图像，会为每个通道分别绘制直方图。**-width** 和 **-height** 选项控制输出图像的尺寸。**-white** 标志用白色背景取代默认的黑色背景，**-verbose** 则打印有关分布的统计信息。属于 Netpbm 工具集。

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

[pgmhist](/man/pgmhist)(1), [ppmhist](/man/ppmhist)(1)
