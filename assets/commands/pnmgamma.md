# TAGLINE

对 PNM 图像应用 Gamma 校正

# TLDR

**应用 Gamma 校正**

```pnmgamma [gamma] [input.pnm] > [output.pnm]```

**调亮图像**

```pnmgamma 2.2 [input.pnm] > [output.pnm]```

**调暗图像**

```pnmgamma 0.5 [input.pnm] > [output.pnm]```

**逐通道设置 Gamma**

```pnmgamma [r_gamma] [g_gamma] [b_gamma] [input.pnm] > [output.pnm]```

# SYNOPSIS

**pnmgamma** [_options_] _gamma_ [_file_]

# PARAMETERS

_GAMMA_
> Gamma 校正值。

_FILE_
> 输入的 PNM 文件。

**-ungamma**
> 撤销 Gamma 校正。

**-cieramp**
> 使用 CIE 亮度斜坡。

# DESCRIPTION

**pnmgamma** 对 PNM 图像应用 Gamma 校正，通过把每个像素值做幂运算来调整亮度曲线。值大于 1 时会调亮图像，小于 1 时会调暗图像。

可以为红、绿、蓝三个通道分别指定 Gamma 值。**-ungamma** 选项用于反转之前应用的 Gamma 校正。属于 Netpbm 工具集；已被 **pamgamma** 取代。

# CAVEATS

值大于 1 调亮、小于 1 调暗。属于 Netpbm 套件。

# HISTORY

pnmgamma 作为 **Netpbm** 的一部分创建，用于执行 Gamma 校正操作。

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

[pamgamma](/man/pamgamma)(1), [pnmnorm](/man/pnmnorm)(1), [ppmchange](/man/ppmchange)(1)
