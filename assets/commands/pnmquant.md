# TAGLINE

减少 PNM 图像中的颜色数量

# TLDR

**减少颜色数**

```pnmquant [256] [input.pnm] > [output.pnm]```

**使用盒中心选色**

```pnmquant -center [16] [input.pnm] > [output.pnm]```

**应用 Floyd-Steinberg 抖动**

```pnmquant -floyd [256] [input.pnm] > [output.pnm]```

**量化到预定义的颜色表**

```pnmquant -mapfile [mapfile.pnm] [256] [input.pnm] > [output.pnm]```

# SYNOPSIS

**pnmquant** [_options_] _ncolors_ [_file_]

# PARAMETERS

_ncolors_
> 目标颜色数。

**-floyd**, **-fs**
> 启用 Floyd-Steinberg 抖动以改善视觉质量。

**-nofloyd**, **-nofs**
> 禁用抖动（默认）。

**-center**
> 选取每个颜色盒的中心作为代表色。

**-meancolor**
> 选取每个盒中所有颜色的平均值（默认）。

**-meanpixel**
> 选取按每个盒中像素数加权的平均值。

**-spreadbrightness**
> 按亮度范围而非颜色数量来铺开盒子。

**-spreadluminosity**
> 按光度范围来铺开盒子。

**-mapfile** _file_
> 量化到文件中预定义的颜色表。

# DESCRIPTION

**pnmquant** 使用中位切分颜色量化算法，把 PNM 图像的颜色数量减少到指定数目。这有助于为调色板受限的格式准备图像，或减小文件体积。

**-floyd** 选项启用 Floyd-Steinberg 抖动，通过把量化误差扩散到相邻像素来模拟出更多的颜色。**-mapfile** 选项允许量化到来自另一幅图像的预定调色板。属于 Netpbm 工具集；本命令是一个封装脚本，内部调用 **pnmcolormap** 和 **pnmremap**。

# INSTALL

```apt: sudo apt install netpbm```

```dnf: sudo dnf install netpbm```

```pacman: sudo pacman -S netpbm```

```apk: sudo apk add netpbm-extras```

```zypper: sudo zypper install netpbm```

```brew: brew install netpbm```

```nix: nix profile install nixpkgs#netpbm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ppmquant](/man/ppmquant)(1), [pnmcolormap](/man/pnmcolormap)(1), [pnmremap](/man/pnmremap)(1), [pnmdepth](/man/pnmdepth)(1)
