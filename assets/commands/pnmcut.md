# TAGLINE

从 PNM 图像中提取矩形区域

# TLDR

**裁切矩形区域**

```pnmcut [x] [y] [width] [height] [input.pnm] > [output.pnm]```

**从左上角开始裁切**

```pnmcut -left [0] -top [0] -width [100] -height [100] [input.pnm] > [output.pnm]```

**使用右下角坐标裁切**

```pnmcut -left [10] -top [10] -right [200] -bottom [150] [input.pnm] > [output.pnm]```

**超出边界时填充**

```pnmcut -pad [x] [y] [width] [height] [input.pnm] > [output.pnm]```

# SYNOPSIS

**pnmcut** [_options_] _x_ _y_ _width_ _height_ [_pnmfile_]

# PARAMETERS

**-left** _n_
> 左侧起始列。

**-right** _n_
> 右侧结束列。

**-top** _n_
> 顶部起始行。

**-bottom** _n_
> 底部结束行。

**-width** _n_
> 宽度（像素）。

**-height** _n_
> 高度（像素）。

**-pad**
> 超出边界时用黑色填充。

# DESCRIPTION

**pnmcut** 从 PNM 图像中提取一个矩形区域。坐标从左上角开始，以零为起始索引。

属于 Netpbm 图像处理工具集。

# EXAMPLES

```bash
# Cut 100x100 from position 50,50
pnmcut 50 50 100 100 image.ppm > crop.ppm

# Using named parameters
pnmcut -left 100 -top 100 -width 200 -height 150 image.ppm > crop.ppm

# Cut with padding
pnmcut -pad -10 -10 120 120 image.ppm > padded.ppm

# Chain with conversion
jpegtopnm photo.jpg | pnmcut 0 0 640 480 | pnmtojpeg > thumb.jpg
```

# CAVEATS

功能更丰富的 pamcut 已取代本命令。负坐标表示从相对的一侧边缘开始计算。

# HISTORY

pnmcut 是 **Jef Poskanzer** 所作 **Netpbm** 的一部分，提供基础的裁切功能。

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

[pamcut](/man/pamcut)(1), [pnmpaste](/man/pnmpaste)(1), [pnmcrop](/man/pnmcrop)(1), [netpbm](/man/netpbm)(1)
