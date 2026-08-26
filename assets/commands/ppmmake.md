# TAGLINE

创建纯色 PPM 图像

# TLDR

**创建纯色图像**

```ppmmake [color] [width] [height] > [output.ppm]```

**创建红色图像**

```ppmmake red 100 100 > [red.ppm]```

**使用 RGB 值创建**

```ppmmake "rgb:ff/00/00" 200 200 > [output.ppm]```

# SYNOPSIS

**ppmmake** [**-maxval** _val_] _color_ _width_ _height_

# PARAMETERS

_COLOR_
> 颜色规格：名称（red、blue）、十六进制（#rrggbb）或 RGB 三元组（rgb:rr/gg/bb）。

_WIDTH_
> 图像宽度（像素）。

_HEIGHT_
> 图像高度（像素）。

**-maxval** _val_
> 输出图像中颜色分量的最大值（默认 255）。

# DESCRIPTION

**ppmmake** 创建指定尺寸、以单一纯色填充的 PPM 图像。颜色可以通过名称（red、blue、white）、十六进制记法（#rrggbb）或 RGB 三元组格式（rgb:rr/gg/bb）指定。

它适合用来创建背景图像、测试图案，或用于与其他 Netpbm 工具合成时的空白画布。配套工具 **pgmmake** 和 **pbmmake** 分别用于创建灰度和位图图像。属于 Netpbm 工具集。

# CAVEATS

输出为写到 stdout 的原始 PPM 格式；请重定向到文件或通过管道交给其他 Netpbm 工具。属于 Netpbm 套件。

# HISTORY

ppmmake 作为 **Netpbm** 的一部分被创建，用于生成纯色图像。

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

[ppm](/man/ppm)(5), [pgmmake](/man/pgmmake)(1), [pbmmake](/man/pbmmake)(1), [pnmtopng](/man/pnmtopng)(1)
