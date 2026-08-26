# TAGLINE

将 GIF 图片转换为 PNM 格式

# TLDR

**将 GIF 转换为 PNM**

```giftopnm [input.gif] > [output.pnm]```

**转换指定帧**

```giftopnm --image [2] [input.gif] > [output.pnm]```

**显示注释**

```giftopnm --comments [input.gif]```

**输出动画 GIF 的所有帧**

```giftopnm --all-images [input.gif] > [output.pnm]```

以**详细模式**输出并显示图像细节

```giftopnm --verbose [input.gif] > [output.pnm]```

# SYNOPSIS

**giftopnm** [_options_] [_file_]

# PARAMETERS

**--image** _num_
> 选择指定的图像/帧。

**--comments**
> 打印图像注释。

**--all-images**
> 输出所有帧。

**--verbose**
> 显示关于 GIF 输入的信息。

**--repair**
> 尝试恢复损坏的 GIF 数据。

# DESCRIPTION

**giftopnm** 将 GIF 图片转换为 Portable Any Map（PNM）格式家族，包括 PBM（位图）、PGM（灰度）和 PPM（彩色）格式。它是 Netpbm 图像处理工具集的核心组件。

该工具会根据输入 GIF 的颜色特性自动选择合适的输出格式。对于动画 GIF，它可以提取单个帧或按顺序输出所有帧。PNM 格式未经压缩，是图像处理管线中理想的中间格式。

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

[ppmtogif](/man/ppmtogif)(1), [pamtogif](/man/pamtogif)(1), [pnmtopng](/man/pnmtopng)(1), [pnmtojpeg](/man/pnmtojpeg)(1), [gifsicle](/man/gifsicle)(1), [convert](/man/convert)(1)
