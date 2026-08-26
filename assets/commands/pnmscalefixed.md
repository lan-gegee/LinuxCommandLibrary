# TAGLINE

使用定点运算缩放图像

# TLDR

**用定点数缩放图像**

```pnmscalefixed [2.0] [input.pnm] > [output.pnm]```

**缩放到指定尺寸**

```pnmscalefixed -width [800] -height [600] [input.pnm] > [output.pnm]```

# SYNOPSIS

**pnmscalefixed** [_options_] _scale_ [_file_]

# PARAMETERS

_scale_
> 缩放倍数。

**-width** _n_
> 目标宽度。

**-height** _n_
> 目标高度。

# DESCRIPTION

**pnmscalefixed** 使用定点整数运算而非浮点运算来缩放 PNM 图像。这使它在缺少硬件浮点支持的系统上比 pamscale 更快，代价是精度略有降低。

该工具接受一个缩放倍数，或通过 **-width** 和 **-height** 指定目标尺寸。在大多数现代系统上，为了更好的质量更推荐 pamscale。属于 Netpbm 工具集。

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

[pamscale](/man/pamscale)(1), [pnmenlarge](/man/pnmenlarge)(1)
