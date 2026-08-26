# TAGLINE

调整 PPM 图像的亮度和饱和度

# TLDR

**提高亮度**

```ppmbrighten -v [50] [input.ppm] > [output.ppm]```

**降低饱和度**

```ppmbrighten -s [-30] [input.ppm] > [output.ppm]```

**同时调整两者**

```ppmbrighten -v [20] -s [10] [input.ppm] > [output.ppm]```

**先做归一化再调整**

```ppmbrighten -n -v [30] [input.ppm] > [output.ppm]```

# SYNOPSIS

**ppmbrighten** [_options_] [_ppmfile_]

# PARAMETERS

**-v** _value_
> 亮度（value）变化量（-100 到 100）。

**-s** _saturation_
> 饱和度变化量（-100 到 100）。

**-n**
> 先对明度范围做归一化。

# DESCRIPTION

**ppmbrighten** 用于调整 PPM 图像的亮度和饱和度。它在 HSV 色彩空间中工作，改变明度（V）和饱和度（S）分量。

属于 Netpbm 工具集。

# EXAMPLES

```bash
# Brighten image
ppmbrighten -v 30 photo.ppm > bright.ppm

# Desaturate (toward grayscale)
ppmbrighten -s -50 photo.ppm > muted.ppm

# Increase vibrancy
ppmbrighten -s 40 photo.ppm > vivid.ppm

# Normalize and brighten
ppmbrighten -n -v 20 dark.ppm > fixed.ppm

# Chain operations
jpegtopnm photo.jpg | ppmbrighten -v 20 | pnmtojpeg > bright.jpg
```

# CAVEATS

超出 -100 到 100 的值会被截断。仅适用于 PPM 格式。如需更多选项，可考虑使用 pamaltsat。

# HISTORY

ppmbrighten 是 **Jef Poskanzer** 及众多贡献者开发的 **Netpbm** 的组成部分，用于基础色彩调整。

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

[ppmcolormask](/man/ppmcolormask)(1), [ppmgamma](/man/ppmgamma)(1), [netpbm](/man/netpbm)(1)
