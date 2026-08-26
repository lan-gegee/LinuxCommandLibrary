# TAGLINE

显示 PGM 图像的灰度直方图

# TLDR

**显示灰度直方图**

```pgmhist [input.pgm]```

**显示中值**

```pgmhist -median [input.pgm]```

# SYNOPSIS

**pgmhist** [_options_] [_file_]

# PARAMETERS

**-median**
> 显示灰度中值。

**-quartile**
> 显示四分位数。

# DESCRIPTION

**pgmhist** 显示 PGM 图像的灰度直方图，展示灰度值的分布情况。属于用于图像分析的 Netpbm 工具集。

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

[ppmhist](/man/ppmhist)(1), [pgmnorm](/man/pgmnorm)(1)
