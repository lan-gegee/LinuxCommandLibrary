# TAGLINE

通过插值放大 PNM 图像

# TLDR

**插值放大图像**

```pnminterp [factor] [input.pnm] > [output.pnm]```

**放大到 2 倍**

```pnminterp 2 [input.pnm] > [output.pnm]```

**放大到 3 倍**

```pnminterp 3 [input.pnm] > [output.pnm]```

# SYNOPSIS

**pnminterp** _n_ [_file_]

# PARAMETERS

_N_
> 缩放倍数（整数倍）。

_FILE_
> 输入的 PNM 文件。

# DESCRIPTION

**pnminterp** 使用双线性插值将 PNM 图像按整数倍放大。与简单的像素复制（pnmenlarge 的做法）不同，插值通过计算相邻像素的加权平均来获得更平滑的结果。

缩放倍数必须是正整数，输出图像在每个维度上都是原来的 N 倍。该工具是 pamscale 插值模式的简化接口。属于 Netpbm 工具集；已被 **pamscale** 取代。

# CAVEATS

只支持整数缩放倍数。属于 Netpbm 套件。

# HISTORY

pnminterp 作为 **Netpbm** 的一部分创建，用于图像插值。

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

[pamscale](/man/pamscale)(1), [pnmscale](/man/pnmscale)(1), [pamenlarge](/man/pamenlarge)(1)
