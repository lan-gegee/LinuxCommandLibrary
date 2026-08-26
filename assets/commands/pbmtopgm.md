# TAGLINE

通过对像素区域取平均值将 PBM 位图转换为 PGM 灰度图

# TLDR

**将位图转换为灰度图**

```pbmtopgm [width] [height] [input.pbm] > [output.pgm]```

# SYNOPSIS

**pbmtopgm** _width_ _height_ [_file_]

# PARAMETERS

_width_
> 取平均的宽度。

_height_
> 取平均的高度。

# DESCRIPTION

**pbmtopgm** 通过对像素区域取平均值将 PBM 位图转换为 PGM 灰度图。可为位图边缘抗锯齿。属于 Netpbm 工具集。

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

[pgmtopbm](/man/pgmtopbm)(1), [ppmtopgm](/man/ppmtopgm)(1)
