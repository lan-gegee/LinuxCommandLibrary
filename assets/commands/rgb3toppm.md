# TAGLINE

将 RGB 分量文件合成为 PPM 图像

# TLDR

**将 RGB 分量合成 PPM**

```rgb3toppm [red.pgm] [green.pgm] [blue.pgm] > [output.ppm]```

# SYNOPSIS

**rgb3toppm** _redfile_ _greenfile_ _bluefile_

# PARAMETERS

_redfile_
> 红色通道的 PGM 文件。

_greenfile_
> 绿色通道的 PGM 文件。

_bluefile_
> 蓝色通道的 PGM 文件。

# DESCRIPTION

**rgb3toppm** 将三个独立的 PGM 灰度文件（红、绿、蓝通道）合并为单个 PPM 彩色图像。三个输入文件的尺寸必须相同。输出写入标准输出。属于 Netpbm 工具集。

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

[ppmtorgb3](/man/ppmtorgb3)(1), [pamstack](/man/pamstack)(1), [pgmtoppm](/man/pgmtoppm)(1), [ppmtopgm](/man/ppmtopgm)(1), [yuvsplittoppm](/man/yuvsplittoppm)(1)
