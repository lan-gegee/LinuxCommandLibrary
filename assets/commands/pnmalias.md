# TAGLINE

对 PNM 图像的边缘进行抗锯齿处理

# TLDR

**对图像边缘抗锯齿**

```pnmalias [input.pnm] > [output.pnm]```

**指定背景色**

```pnmalias -bgcolor [white] [input.pnm] > [output.pnm]```

# SYNOPSIS

**pnmalias** [_options_] [_file_]

# PARAMETERS

**-bgcolor** _color_
> 抗锯齿使用的背景色。

**-fgcolor** _color_
> 前景色。

# DESCRIPTION

**pnmalias** 通过平滑前景色与背景色之间的过渡，对 PNM 图像的边缘进行抗锯齿处理。属于 Netpbm 工具集。

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

[pnmsmooth](/man/pnmsmooth)(1), [ppmquant](/man/ppmquant)(1)
