# TAGLINE

将 PostScript 图像数据转换为 PGM

# TLDR

**将 PostScript 图像转换为 PGM**

```psidtopgm [width] [height] [bits] [input.ps] > [output.pgm]```

# SYNOPSIS

**psidtopgm** _width_ _height_ _bits_ [_file_]

# PARAMETERS

_width_
> 图像宽度。

_height_
> 图像高度。

_bits_
> 每个采样点的位数。

# DESCRIPTION

**psidtopgm** 从 PostScript 图像数据运算符的输出中提取灰度图像并转换为 PGM。Netpbm 工具集的一部分。

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

[pstopnm](/man/pstopnm)(1), [pgmtopbm](/man/pgmtopbm)(1)
