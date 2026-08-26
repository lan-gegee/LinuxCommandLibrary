# TAGLINE

从 PAM 或 PNM 图像中提取矩形区域

# TLDR

**从图像裁剪区域**

```pamcut [x] [y] [width] [height] [input.pam] > [output.pam]```

**按坐标裁剪**

```pamcut -left [100] -top [50] -width [200] -height [150] [input.pam] > [output.pam]```

**从右侧裁剪**

```pamcut -right [100] -bottom [100] -width [200] -height [200] [input.pam] > [output.pam]```

**超出边界时填充**

```pamcut -pad -left [-10] -top [-10] -width [300] -height [300] [input.pam] > [output.pam]```

# SYNOPSIS

**pamcut** [_options_] [_x_ _y_ _width_ _height_] [_pamfile_]

# PARAMETERS

**-left** _x_
> 左边缘位置。

**-right** _x_
> 右边缘位置。

**-top** _y_
> 上边缘位置。

**-bottom** _y_
> 下边缘位置。

**-width** _w_
> 输出宽度。

**-height** _h_
> 输出高度。

**-pad**
> 超出边界时用黑色填充。

# DESCRIPTION

**pamcut** 从 PAM 或 PNM 图像中提取矩形区域。通过 left/right 与 top/bottom 的组合，可以从任意角落指定坐标。

# EXAMPLE

```bash
# Cut 100x100 from top-left corner
pamcut 0 0 100 100 photo.ppm > crop.ppm

# Cut center region
pamcut -left 100 -top 100 -width 200 -height 200 input.ppm > center.ppm
```

# CAVEATS

坐标从 0 开始计数。未使用 -pad 时，区域必须位于图像边界内。

# HISTORY

pamcut 是 **Netpbm** 的一部分，Netpbm 由 **Jef Poskanzer** 创建的原始 PBMplus 工具集演化而来。

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

[pnmcut](/man/pnmcut)(1), [pamcomp](/man/pamcomp)(1), [pamscale](/man/pamscale)(1)
