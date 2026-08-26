# TAGLINE

为 PNM 图像添加填充

# TLDR

**为图像添加填充**

```pnmpad -left [10] -right [10] [input.pnm] > [output.pnm]```

**添加均匀填充**

```pnmpad -width [100] -height [100] [input.pnm] > [output.pnm]```

**以指定颜色填充**

```pnmpad -color [white] -left [5] [input.pnm] > [output.pnm]```

# SYNOPSIS

**pnmpad** [_options_] [_file_]

# PARAMETERS

_FILE_
> 输入的 PNM 文件。

**-left** _N_
> 在左侧添加的像素数。

**-right** _N_
> 在右侧添加的像素数。

**-top** _N_
> 在顶部添加的像素数。

**-bottom** _N_
> 在底部添加的像素数。

**-width** _N_
> 目标宽度（居中放置）。

**-height** _N_
> 目标高度（居中放置）。

**-color** _COLOR_
> 填充颜色（默认：黑色）。

**-white**
> 用白色填充（快捷方式）。

**-halign** _RATIO_
> 水平对齐比例（0.0=左，0.5=中，1.0=右）。

**-valign** _RATIO_
> 垂直对齐比例（0.0=下，0.5=中，1.0=上）。

**-mwidth** _N_
> 将宽度填充到 N 像素的倍数。

**-mheight** _N_
> 将高度填充到 N 像素的倍数。

**-extend-edge**
> 通过复制相邻边缘像素来填充。

**-detect-background**
> 检测并使用图像背景色进行填充。

**-reportonly**
> 只打印填充方案的说明而不生成输出。

# DESCRIPTION

**pnmpad** 在 PNM 图像四周添加填充（空白区域），在不缩放原始内容的前提下扩大画布尺寸。可以使用 **-left**、**-right**、**-top** 和 **-bottom** 为每一侧独立指定填充量。

也可以改用 **-width** 和 **-height** 指定期望的输出尺寸，并用 **-halign** 与 **-valign** 控制图像在填充后画布中的对齐方式（默认居中）。**-color** 选项设置填充颜色（默认为黑色）。**-mwidth** 和 **-mheight** 选项将尺寸填充到给定像素数的整数倍。本命令与 pnmcrop 互为逆操作。属于 Netpbm 工具集。

# CAVEATS

与 pnmcrop 相反。属于 Netpbm 套件。**-extend-edge** 和 **-detect-background** 选项要求 Netpbm 11.05 或更高版本。

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

[pnmcrop](/man/pnmcrop)(1), [pamcomp](/man/pamcomp)(1), [pnmcat](/man/pnmcat)(1)
