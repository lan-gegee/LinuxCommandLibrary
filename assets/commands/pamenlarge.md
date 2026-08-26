# TAGLINE

通过复制像素将 Netpbm 图像放大 N 倍

# TLDR

**将图像放大 2 倍**

```pamenlarge 2 [input.pam] > [output.pam]```

**将图像放大 4 倍**

```pamenlarge 4 [input.pam] > [output.pam]```

**使用命名选项放大**

```pamenlarge -scale=[3] [input.pam] > [output.pam]```

**以不同的 x/y 因子放大**

```pamenlarge -xscale=[3] -yscale=[2] [input.pam] > [output.pam]```

**仅水平方向放大**

```pamenlarge -xscale=[4] [input.pam] > [output.pam]```

# SYNOPSIS

**pamenlarge** [**-scale=**_N_] [**-xscale=**_N_] [**-yscale=**_N_] [_pamfile_]

**pamenlarge** _N_ [_pamfile_]

# PARAMETERS

**-scale=**_N_
> 水平和垂直方向都应用的缩放因子。不能与 -xscale 或 -yscale 组合使用。

**-xscale=**_N_
> 水平缩放因子。若未给出 -yscale，垂直缩放默认为 1。

**-yscale=**_N_
> 垂直缩放因子。若未给出 -xscale，水平缩放默认为 1。

_N_
> 位置参数形式的缩放因子（旧语法）。等价于 -scale=N。

# DESCRIPTION

**pamenlarge** 读取 Netpbm 图像，将其像素复制 N 次，生成放大的 Netpbm 图像。每个像素变成一个 N x N 的相同像素块。

这会产生块状/像素化的外观，适用于像素画或简单缩放。需要平滑缩放时应改用 **pamscale**。当缩放因子为 3 或更大时，之后再运行 **pnmsmooth** 可以减轻像素化程度。

对于 PBM 图像，针对最大到 10 的缩放因子存在优化算法。用较小因子运行多轮可能比单次大因子更快。

# EXAMPLE

```bash
# Double the size
pamenlarge 2 small.ppm > large.ppm

# Triple horizontal, double vertical
pamenlarge -xscale=3 -yscale=2 input.ppm > output.ppm
```

# COMPARISON

```
pamenlarge - Fast, integer factors, blocky
pamscale   - Smooth scaling, any factor
```

# CAVEATS

只支持整数倍。不做插值。大倍数会迅速产生很大的文件。-scale、-xscale 和 -yscale 选项是在 Netpbm 10.86（2019 年 3 月）中加入的；更早的版本只支持位置参数语法。

# HISTORY

**pamenlarge** 于 **10.25 版本**（2004 年 10 月）加入 Netpbm，取代了旧的 **pnmenlarge**。

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

[pamscale](/man/pamscale)(1), [pnmenlarge](/man/pnmenlarge)(1), [pamstretch](/man/pamstretch)(1)
