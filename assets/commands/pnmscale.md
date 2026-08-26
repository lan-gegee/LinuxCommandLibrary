# TAGLINE

缩放 PNM 图像（已被 pamscale 取代）

# TLDR

**按倍数缩放**

```pnmscale [0.5] [input.pnm] > [output.pnm]```

**缩放到指定宽度**

```pnmscale -width [640] [input.pnm] > [output.pnm]```

**缩放到指定尺寸**

```pnmscale -width [800] -height [600] [input.pnm] > [output.pnm]```

**按 X 和 Y 倍数缩放**

```pnmscale -xscale [2] -yscale [1.5] [input.pnm] > [output.pnm]```

# SYNOPSIS

**pnmscale** [_options_] [_pnmfile_]

# PARAMETERS

**-width** _n_
> 输出宽度。

**-height** _n_
> 输出高度。

**-xscale** _n_
> 水平缩放倍数。

**-yscale** _n_
> 垂直缩放倍数。

**-reduce** _n_
> 按整数倍缩小。

**-xysize** _x_ _y_
> 适配到指定尺寸内（在 pamscale 中是 -xyfit 的同义词）。

**-pixels** _n_
> 缩放到给定的总像素数。

# DESCRIPTION

**pnmscale** 放大或缩小 PNM 图像，缩小图像时使用像素混合来获得平滑效果。自 Netpbm 10.20（2004 年 1 月）起，本命令已被 **pamscale** 取代，并于 Netpbm 10.46（2009 年 3 月）被移除。新的工作请使用 **pamscale**，它向后兼容并支持 PAM 图像。

属于 Netpbm 工具集。

# EXAMPLES

```bash
# Half size
pnmscale 0.5 image.ppm > half.ppm

# Specific width, maintain aspect
pnmscale -width 640 image.ppm > resized.ppm

# Exact dimensions
pnmscale -width 800 -height 600 image.ppm > exact.ppm

# Integer reduction (faster)
pnmscale -reduce 4 huge.ppm > quarter.ppm

# Chain with conversion
jpegtopnm photo.jpg | pnmscale 0.25 | pnmtojpeg > thumb.jpg
```

# CAVEATS

已被 pamscale 取代；新的工作请使用 pamscale。像素混合可能引起模糊。整数倍缩小（-reduce）比小数倍缩放更快。

# HISTORY

pnmscale 是 **Jef Poskanzer** 所作 **Netpbm** 的一部分，后来被功能更多的 pamscale 所取代。

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

[pamscale](/man/pamscale)(1), [pnmenlarge](/man/pnmenlarge)(1), [pnmcut](/man/pnmcut)(1), [netpbm](/man/netpbm)(1)
