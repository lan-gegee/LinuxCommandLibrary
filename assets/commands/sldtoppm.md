# TAGLINE

将 AutoCAD 幻灯片文件转换为 PPM

# TLDR

**将 AutoCAD 幻灯片转换为 PPM**

```sldtoppm [input.sld] > [output.ppm]```

**指定输出尺寸**

```sldtoppm -xsize [640] -ysize [480] [input.sld] > [output.ppm]```

**从幻灯片库中提取一张幻灯片**

```sldtoppm -lib [slide_name] [library.slb] > [output.ppm]```

**调整为方形像素**

```sldtoppm -adjust [input.sld] > [output.ppm]```

**列出库中的幻灯片**

```sldtoppm -dir [library.slb]```

# SYNOPSIS

**sldtoppm** [_options_] [_file_]

# PARAMETERS

**-xsize** _n_, **-width** _n_
> 输出宽度（像素）。

**-ysize** _n_, **-height** _n_
> 输出高度（像素）。

**-adjust**
> 缩放宽度，使输出像素为正方形。

**-lib** _name_
> 从库中提取指定名称的幻灯片（名称会转换为大写）。

**-Lib** _name_
> 从库中提取指定名称的幻灯片（区分大小写）。

**-dir**
> 列出幻灯片库中的幻灯片。

**-scale** _s_
> 按系数 s（浮点数，> 0）缩放图像。

**-info**
> 将幻灯片头信息和矢量数据转储到 stderr。

**-verbose**
> 将幻灯片信息打印到 stderr。

# DESCRIPTION

**sldtoppm** 将 AutoCAD 幻灯片（.sld）文件和幻灯片库（.slb）文件转换为 PPM 格式。幻灯片曾用于 AutoCAD 的演示。它是 Netpbm 工具集的一部分。

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

[ppmtoacad](/man/ppmtoacad)(1), [netpbm](/man/netpbm)(1)
