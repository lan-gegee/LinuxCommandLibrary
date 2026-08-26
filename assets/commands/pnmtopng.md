# TAGLINE

将 PNM 图像转换为 PNG 格式

# TLDR

**将 PNM 转换为 PNG**

```pnmtopng [input.pnm] > [output.png]```

**以指定压缩级别转换**

```pnmtopng -compression [9] [input.pnm] > [output.png]```

**添加 Alpha 通道**

```pnmtopng -alpha [alpha.pgm] [input.ppm] > [output.png]```

**创建交错式 PNG**

```pnmtopng -interlace [input.pnm] > [output.png]```

# SYNOPSIS

**pnmtopng** [_options_] [_file_]

# PARAMETERS

**-alpha** _file_
> Alpha 通道文件。

**-compression** _n_
> 压缩级别（0-9）。

**-interlace**
> 创建交错式（interlaced）PNG。

**-transparent** _color_
> 透明色。

**-gamma** _value_
> Gamma 值。

# DESCRIPTION

**pnmtopng** 以无损压缩方式将 PNM（PBM、PGM、PPM）图像转换为 PNG 格式。它会根据输入图像自动选择最优的 PNG 颜色类型。

**-alpha** 选项附加一个单独的 PGM 文件作为 Alpha 透明通道。**-compression** 级别（0-9）控制 deflate 压缩的投入程度，**-interlace** 则创建 Adam7 交错式 PNG 以便渐进显示。**-transparent** 选项将某个特定颜色指定为完全透明。属于 Netpbm 工具集；已被 **pamtopng** 取代。

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

[pngtopnm](/man/pngtopnm)(1), [pamtopng](/man/pamtopng)(1)
