# TAGLINE

将 PGM 灰度图像转换为 PPM 彩色图像

# TLDR

**将灰度转换为彩色**

```pgmtoppm [color] [input.pgm] > [output.ppm]```

**用特定颜色着色**

```pgmtoppm [red] [input.pgm] > [output.ppm]```

**将黑白映射到颜色范围**

```pgmtoppm [black]-[blue] [input.pgm] > [output.ppm]```

**使用颜色映射文件**

```pgmtoppm -map [colormap.ppm] [input.pgm] > [output.ppm]```

# SYNOPSIS

**pgmtoppm** _colorspec_ [_pgmfile_]

**pgmtoppm** **-map** _mapfile_ [_pgmfile_]

# PARAMETERS

**colorspec**
> 颜色名或黑白范围（如 "red"、"black-blue"）。

**-map** _file_
> 颜色映射文件。

# DESCRIPTION

**pgmtoppm** 将 PGM 灰度图像转换为 PPM 彩色图像。它把灰度值映射为颜色，可以是单一颜色、一个颜色范围，也可以通过颜色映射表完成。
# Grayscale to red tint
pgmtoppm red image.pgm > red.ppm

# Map to blue gradient
pgmtoppm black-blue image.pgm > blue.ppm

# Heat map style
pgmtoppm blue-red image.pgm > heat.ppm

# Using hex colors
pgmtoppm "#000000-#ff5500" image.pgm > orange.ppm

# From color map
pgmtoppm -map palette.ppm image.pgm > colored.ppm
```

# COLOR FORMATS

```
Color names: red, blue, green, yellow...
Hex: #rrggbb
RGB: rgb:rr/gg/bb
Range: color1-color2
```

# CAVEATS

输入必须是 PGM。反向转换请使用 ppmtopgm。属于 Netpbm 工具集。

# HISTORY

pgmtoppm 是由 **Jef Poskanzer** 开发的 **Netpbm** 的一部分，提供灰度到彩色的转换。

# SEE ALSO

[ppmtopgm](/man/ppmtopgm)(1), [pgmramp](/man/pgmramp)(1), [ppmchange](/man/ppmchange)(1), [netpbm](/man/netpbm)(1)

# INSTALL

```apt: sudo apt install netpbm```

```dnf: sudo dnf install netpbm```

```pacman: sudo pacman -S netpbm```

```apk: sudo apk add netpbm```

```zypper: sudo zypper install netpbm```

```brew: brew install netpbm```

```nix: nix profile install nixpkgs#netpbm```

<!-- packages: 2026-07-22 -->
