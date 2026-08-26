# TAGLINE

按亮度系数调暗 PPM 图像

# TLDR

**调暗图像**

```ppmdim [factor] [input.ppm] > [output.ppm]```

**调暗至 50%**

```ppmdim 0.5 [input.ppm] > [output.ppm]```

**调暗至 25%**

```ppmdim 0.25 [input.ppm] > [output.ppm]```

# SYNOPSIS

**ppmdim** _factor_ [_file_]

# PARAMETERS

_FACTOR_
> 调暗系数（0.0-1.0）。

_FILE_
> 输入的 PPM 文件。

# DESCRIPTION

**ppmdim** 通过将每个像素值乘以指定系数来降低 PPM 图像的亮度。系数为 1.0 时图像不变，为 0.0 时产生全黑图像。未指定文件时从标准输入读取。

它是 **ppmflash**（向白色方向提亮）的互补工具。这两个工具在帧序列上以不同系数应用时，可用于制作渐隐到黑或渐隐到白的动画效果。属于 Netpbm 工具集。

该程序已在很大程度上被更通用的 **pamfunc**（配合 -multiplier 选项）取代。ppmdim 为向后兼容而保留，由于使用整数运算可能更快。

# CAVEATS

系数 1.0 表示不变，0.0 表示全黑。仅适用于 PPM 格式图像。属于 Netpbm 套件。

# HISTORY

ppmdim 作为 **Netpbm** 的一部分被创建，用于图像调暗。

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

[ppmflash](/man/ppmflash)(1), [pamfunc](/man/pamfunc)(1), [ppmbrighten](/man/ppmbrighten)(1), [ppm](/man/ppm)(5)
