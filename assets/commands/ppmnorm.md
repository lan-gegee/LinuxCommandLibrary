# TAGLINE

归一化 PPM 图像的对比度范围

# TLDR

**归一化图像对比度**

```ppmnorm [input.ppm] > [output.ppm]```

**指定百分位范围**

```ppmnorm -bpercent [2] -wpercent [1] [input.ppm] > [output.ppm]```

# SYNOPSIS

**ppmnorm** [_options_] [_file_]

# PARAMETERS

_FILE_
> 输入的 PPM 文件。

**-bpercent** _N_
> 黑色百分比。

**-wpercent** _N_
> 白色百分比。

**-bvalue** _N_
> 黑色截断值。

**-wvalue** _N_
> 白色截断值。

# DESCRIPTION

**ppmnorm** 通过将颜色直方图拉伸到完整的可用范围来归一化 PPM 图像的对比度。偏暗的图像会被提亮，发灰的图像会获得对比度，是一个快速自动增强的工具。

黑色和白色百分位参数控制在拉伸之前对直方图两端裁剪的激进程度，防止离群像素限制增强效果。它是 **pnmnorm** 在彩色模式下的别名。属于 Netpbm 工具集。

# CAVEATS

是 pnmnorm 彩色模式的别名。属于 Netpbm 套件。

# HISTORY

ppmnorm 作为 **Netpbm** 的一部分被创建，用于彩色图像归一化。

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

[pnmnorm](/man/pnmnorm)(1), [ppmgamma](/man/ppmgamma)(1), [ppm](/man/ppm)(5)
