# TAGLINE

使用 HSV 颜色模型调整 Netpbm 图像的亮度和饱和度

# TLDR

**将图像亮度提高 50%**

```pambrighten -value 50 [input.pam] > [output.pam]```

**将饱和度降低 30%**

```pambrighten -saturation -30 [input.pam] > [output.pam]```

**同时调整亮度和饱和度**

```pambrighten -value [20] -saturation [10] [input.pam] > [output.pam]```

**从 stdin 读取**

```cat [input.pam] | pambrighten -value [50] > [output.pam]```

# SYNOPSIS

**pambrighten** [**-value** _n_] [**-saturation** _n_] [_file_]

# PARAMETERS

**-value** _n_
> 按百分比改变 Value（亮度）。可为负数。默认为 0。

**-saturation** _n_
> 按百分比改变 Saturation（饱和度）。可为负数。默认为 0。

# DESCRIPTION

**pambrighten** 按指定百分比增大或减小 Netpbm 图像每个像素的 Saturation 和 Value（来自 HSV 色彩空间）。正值增加，负值减少。未指定文件时从 stdin 读取。

选项名接受最短的唯一缩写形式。可以使用双连字符代替单连字符。属于 Netpbm 工具集。

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

[pamfunc](/man/pamfunc)(1), [ppmbrighten](/man/ppmbrighten)(1)
