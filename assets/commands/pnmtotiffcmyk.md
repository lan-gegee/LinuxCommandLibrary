# TAGLINE

将 PNM 转换为用于打印的 CMYK TIFF

# TLDR

**将 PNM 转换为 CMYK TIFF**

```pnmtotiffcmyk [input.pnm] > [output.tiff]```

**指定 UCR 百分比**

```pnmtotiffcmyk -ucr [20] [input.pnm] > [output.tiff]```

# SYNOPSIS

**pnmtotiffcmyk** [_options_] [_file_]

# PARAMETERS

**-ucr** _percent_
> 底色去除（Under Color Removal）百分比。

**-gcr** _percent_
> 灰色成分替代（Gray Component Replacement）。

# DESCRIPTION

**pnmtotiffcmyk** 将 PNM 图像转换为面向专业印刷生产的 CMYK（青、品红、黄、黑）TIFF 格式。它执行商业印刷流程所需的 RGB 到 CMYK 色彩空间转换。

**-ucr**（底色去除）和 **-gcr**（灰色成分替代）选项控制如何从 CMY 分量生成黑色通道，会影响墨水用量和打印质量。属于 Netpbm 工具集。

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

[pamtotiff](/man/pamtotiff)(1), [pnmtotiff](/man/pnmtotiff)(1)
