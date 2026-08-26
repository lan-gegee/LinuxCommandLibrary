# TAGLINE

水平错切 PNM 图像

# TLDR

**水平错切图像**

```pnmshear [30] [input.pnm] > [output.pnm]```

**带背景色错切**

```pnmshear -background [white] [45] [input.pnm] > [output.pnm]```

# SYNOPSIS

**pnmshear** [_options_] _angle_ [_file_]

# PARAMETERS

_angle_
> 错切角度（度）。

**-background** _color_
> 新增区域的填充色。

**-noantialias**
> 禁用抗锯齿。

# DESCRIPTION

**pnmshear** 对 PNM 图像施加水平错切变换：每一行都按与其到中心线距离成比例的量进行平移。结果是得到一幅平行四边形形状的图像，错切角度以度为单位指定。

默认应用抗锯齿以获得平滑效果。**-background** 选项设置新露出区域的填充色，**-noantialias** 则禁用平滑处理。属于 Netpbm 工具集。

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

[pnmrotate](/man/pnmrotate)(1), [pnmflip](/man/pnmflip)(1)
