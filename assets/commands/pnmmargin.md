# TAGLINE

为 PNM 图像添加纯色边框

# TLDR

**给图像四周添加边框**

```pnmmargin [10] [input.pnm] > [output.pnm]```

**添加彩色边框**

```pnmmargin -color [blue] [20] [input.pnm] > [output.pnm]```

# SYNOPSIS

**pnmmargin** [_options_] _size_ [_file_]

# PARAMETERS

_size_
> 边框宽度（像素）。

**-color** _color_
> 边框颜色。

**-white**
> 白色边框。

**-black**
> 黑色边框。

**-plain**
> 以 plain PNM 格式生成输出。

# DESCRIPTION

**pnmmargin** 在 PNM 图像的四条边上添加统一宽度的纯色边框。边框宽度以像素为单位指定，且四条边的宽度相同。

如果未指定颜色选项，程序会自行猜测。可以用 **-color** 指定自定义颜色，也可以用快捷方式 **-white** 和 **-black** 选择常见颜色。本命令是 **pnmpad** 的便捷封装。如果要为各侧设置不同的边距，请直接使用 pnmpad。要去除边框则使用 pamcut。属于 Netpbm 工具集。

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

[pnmpad](/man/pnmpad)(1), [pamcut](/man/pamcut)(1), [pnmcat](/man/pnmcat)(1), [pnmcrop](/man/pnmcrop)(1)
