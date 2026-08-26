# TAGLINE

替换 PPM 图像中的特定颜色

# TLDR

**替换特定颜色**

```ppmchange [oldcolor] [newcolor] [input.ppm] > [output.ppm]```

**把红色换成蓝色**

```ppmchange red blue [input.ppm] > [output.ppm]```

**一次替换多种颜色**

```ppmchange [old1] [new1] [old2] [new2] [input.ppm] > [output.ppm]```

# SYNOPSIS

**ppmchange** [_options_] _oldcolor_ _newcolor_ [_file_]

# PARAMETERS

_OLDCOLOR_
> 要替换的颜色。

_NEWCOLOR_
> 替换后的颜色。

_FILE_
> 输入的 PPM 文件。

**-closeness** _N_
> 颜色匹配的容差。

# DESCRIPTION

**ppmchange** 将 PPM 图像中的特定颜色替换为新颜色。在命令行上提供多组旧颜色和新颜色的配对，即可在一次调用中完成多种颜色替换。

默认只替换完全匹配的颜色。**-closeness** 选项可通过指定容差值实现模糊匹配，适用于处理因压缩或抗锯齿而存在轻微色彩偏差的图像。属于 Netpbm 工具集。

# CAVEATS

默认进行精确颜色匹配。属于 Netpbm 套件。

# HISTORY

ppmchange 作为 **Netpbm** 的一部分被创建，用于颜色替换。

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

[ppmcolormask](/man/ppmcolormask)(1), [pnmremap](/man/pnmremap)(1), [ppm](/man/ppm)(5)
