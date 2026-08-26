# TAGLINE

从 PNM 图像生成调色板

# TLDR

**用 N 种颜色生成颜色表**

```pnmcolormap [256] [image.ppm] > [colormap.ppm]```

**使用中位切分算法**

```pnmcolormap -center [16] [image.ppm] > [colormap.ppm]```

**均匀铺开颜色**

```pnmcolormap -spreadluminosity [256] [image.ppm] > [colormap.ppm]```

**从多幅图像生成**

```pnmcolormap [256] [image1.ppm] [image2.ppm] > [colormap.ppm]```

# SYNOPSIS

**pnmcolormap** [_options_] _ncolors_ [_pnmfile_...]

# PARAMETERS

**ncolors**
> 颜色表中的最大颜色数。

**-center**
> 使用聚类中心。

**-meancolor**
> 使用聚类的平均颜色。

**-meanpixel**
> 使用按像素数加权的平均值。

**-spreadbrightness**
> 按亮度铺开。

**-spreadluminosity**
> 按光度铺开。

# DESCRIPTION

**pnmcolormap** 使用中位切分量化从图像创建颜色表（调色板）。输出是一幅小图像，其中每个像素就是调色板中的一种颜色。

与 pnmremap 搭配用于减色。

# EXAMPLES

```bash
# Create 256-color palette
pnmcolormap 256 photo.ppm > palette.ppm

# Reduce colors using map
pnmcolormap 16 image.ppm > map.ppm
pnmremap -mapfile=map.ppm image.ppm > reduced.ppm

# Combined color reduction
pnmcolormap 256 image.ppm | pnmremap -mapfile=- image.ppm > reduced.ppm
```

# CAVEATS

输出的是颜色表，而非重映射后的图像。要实际应用请使用 pnmremap。属于 Netpbm。

# HISTORY

pnmcolormap 是 **Netpbm** 的一部分，实现了中位切分颜色量化算法。

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

[pnmremap](/man/pnmremap)(1), [ppmquant](/man/ppmquant)(1), [ppmquantall](/man/ppmquantall)(1), [netpbm](/man/netpbm)(1)
