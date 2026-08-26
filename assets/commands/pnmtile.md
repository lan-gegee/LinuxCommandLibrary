# TAGLINE

用 PNM 图像创建平铺图案

# TLDR

**由图像创建平铺图案**

```pnmtile [640] [480] [input.pnm] > [output.pnm]```

# SYNOPSIS

**pnmtile** _width_ _height_ [_file_]

# PARAMETERS

_width_
> 输出宽度（像素）。

_height_
> 输出高度（像素）。

# DESCRIPTION

**pnmtile** 通过平铺（重复）输入图像来填满指定的尺寸，从而生成一幅新图像。适合用来制作背景。属于 Netpbm 工具集。

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

[pnmcat](/man/pnmcat)(1), [pnmmontage](/man/pnmmontage)(1)
