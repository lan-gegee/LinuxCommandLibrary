# TAGLINE

翻转和旋转 PNM 图像

# TLDR

**水平翻转**

```pnmflip -lr [input.pnm] > [output.pnm]```

**垂直翻转**

```pnmflip -tb [input.pnm] > [output.pnm]```

**顺时针旋转 90 度**

```pnmflip -cw [input.pnm] > [output.pnm]```

**逆时针旋转 90 度**

```pnmflip -ccw [input.pnm] > [output.pnm]```

**旋转 180 度**

```pnmflip -r180 [input.pnm] > [output.pnm]```

# SYNOPSIS

**pnmflip** [_options_] [_file_]

# PARAMETERS

**-lr**
> 左右翻转。

**-tb**
> 上下翻转。

**-cw**
> 顺时针旋转 90 度。

**-ccw**
> 逆时针旋转 90 度。

**-r180**
> 旋转 180 度。

**-transpose**
> 转置行与列。

# DESCRIPTION

**pnmflip** 用于翻转和旋转 PNM 图像。属于 Netpbm 图像处理工具集。支持所有基础的几何变换。

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

[pnmrotate](/man/pnmrotate)(1), [pamflip](/man/pamflip)(1)
