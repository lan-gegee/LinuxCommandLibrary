# TAGLINE

减少 PPM 图像的颜色数量

# TLDR

**减少到 N 种颜色**

```ppmquant [256] [input.ppm] > [output.ppm]```

**减少到 16 种颜色**

```ppmquant [16] [input.ppm] > [output.ppm]```

**配合 Floyd-Steinberg 抖动**

```ppmquant -fs [256] [input.ppm] > [output.ppm]```

**使用现有的颜色映射表**

```ppmquant -map [palette.ppm] [input.ppm] > [output.ppm]```

# SYNOPSIS

**ppmquant** [_options_] _ncolors_ [_ppmfile_]

# PARAMETERS

**ncolors**
> 颜色数量的上限。

**-fs**
> Floyd-Steinberg 抖动。

**-map** _file_
> 使用来自文件的颜色映射表。

**-spreadbrightness**
> 按亮度扩散误差。

**-spreadluminosity**
> 按光度扩散误差。

# DESCRIPTION

**ppmquant** 使用中位切分（median-cut）量化方法减少 PPM 图像中的颜色数量。对于创建 GIF 图像或减小文件大小至关重要。

在现代 Netpbm 中已被 pnmquant 取代。

# EXAMPLES

```bash
# Reduce to 256 colors
ppmquant 256 photo.ppm > reduced.ppm

# 16 colors with dithering
ppmquant -fs 16 image.ppm > dithered.ppm

# Use web-safe palette
ppmquant -map websafe.ppm image.ppm > websafe.ppm

# Convert for GIF
ppmquant 256 image.ppm | ppmtogif > image.gif
```

# CAVEATS

新项目请使用 pnmquant。抖动可能增大文件体积。属于 Netpbm。

# HISTORY

ppmquant 是 **Jef Poskanzer** 编写的 **Netpbm** 的组成部分，实现了 **Paul Heckbert** 提出的中位切分颜色量化算法。

# INSTALL

```apt: sudo apt install netpbm```

```dnf: sudo dnf install netpbm```

```pacman: sudo pacman -S netpbm```

```apk: sudo apk add netpbm-extras```

```zypper: sudo zypper install netpbm```

```brew: brew install netpbm```

```nix: nix profile install nixpkgs#netpbm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pnmquant](/man/pnmquant)(1), [pnmcolormap](/man/pnmcolormap)(1), [ppmtogif](/man/ppmtogif)(1), [netpbm](/man/netpbm)(1)
