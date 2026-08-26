# TAGLINE

将 PPM 图像转换为 GIF 格式

# TLDR

**将 PPM 转换为 GIF**

```ppmtogif [input.ppm] > [output.gif]```

**带透明色**

```ppmtogif -transparent [color] [input.ppm] > [output.gif]```

**交错式 GIF**

```ppmtogif -interlace [input.ppm] > [output.gif]```

**使用来自 PGM 文件的 alpha 透明**

```ppmtogif -alpha [mask.pgm] [input.ppm] > [output.gif]```

# SYNOPSIS

**ppmtogif** [_options_] [_ppmfile_]

# PARAMETERS

**-transparent** [**=**]_color_
> 将指定颜色设为透明。若带 **=** 前缀，则只进行精确匹配；否则选择图像中最接近的颜色。

**-alpha** _pgmfile_
> 使用 PGM 文件作为 alpha（透明度）掩码。白色为不透明，黑色为透明。不能与 **-transparent** 同时使用。

**-interlace**
> 生成交错式（interlaced）GIF 文件。

**-sort**
> 生成颜色映射表按可预测顺序排序的 GIF 文件。

**-map** _mapfile_
> 使用指定 PPM 文件中的颜色作为颜色映射表，而不是输入图像中的颜色。

**-comment** _text_
> 在 GIF 输出中包含一条注释。

**-nolzw**
> 不使用 LZW 压缩。输出更大但不受专利限制。

# DESCRIPTION

**ppmtogif** 将 PPM 图像转换为 GIF 格式。GIF 最多只支持 256 种颜色，必要时请先用 ppmquant 处理。

该程序在 Netpbm 10.37（2006 年 12 月）中被 **pamtogif** 取代。不建议再使用 ppmtogif，请改用 pamtogif。

属于 Netpbm 工具集。

# EXAMPLES

```bash
# Basic conversion
ppmtogif image.ppm > image.gif

# With transparency (exact color match)
ppmtogif -transparent =white logo.ppm > logo.gif

# With alpha mask from a PGM file
ppmtogif -alpha mask.pgm image.ppm > transparent.gif

# Quantize first for photos with many colors
ppmquant 256 photo.ppm | ppmtogif > photo.gif

# Interlaced for web
ppmtogif -interlace image.ppm > interlaced.gif

# From JPEG
jpegtopnm photo.jpg | ppmquant 256 | ppmtogif > photo.gif
```

# CAVEATS

GIF 最多支持 256 种颜色。转换前请使用 ppmquant 减少颜色数。**-transparent** 与 **-alpha** 选项不能同时使用。此命令已弃用，请改用 pamtogif。

# HISTORY

ppmtogif 是 **Jef Poskanzer** 编写的 **Netpbm** 的组成部分，LZW 压缩代码由多位贡献者提供。

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

[pamtogif](/man/pamtogif)(1), [giftopnm](/man/giftopnm)(1), [ppmquant](/man/ppmquant)(1), [netpbm](/man/netpbm)(1)
