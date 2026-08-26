# TAGLINE

将颜色调整到 NTSC 广播安全范围

# TLDR

**转换为 NTSC 安全颜色**

```ppmntsc [input.ppm] > [output.ppm]```

**使用 PAL 限制**而不是 NTSC

```ppmntsc --pal [input.ppm] > [output.ppm]```

**显示非法像素的数量**

```ppmntsc --verbose [input.ppm] > [output.ppm]```

**只输出被修正的像素**（合规像素变为黑色）

```ppmntsc --correctedonly [input.ppm] > [output.ppm]```

# SYNOPSIS

**ppmntsc** [**--pal**] [**--legalonly**] [**--illegalonly**] [**--correctedonly**] [**--verbose**] [**--debug**] [_infile_]

# PARAMETERS

_infile_
> 输入的 PPM 文件。省略时从标准输入读取。

**--pal**
> 使用 PAL 广播颜色限制，代替默认的 NTSC。

**--verbose**
> 显示发现的非法像素数量。

**--debug**
> 显示详细输出，列出每个非法颜色及其修正后的版本。

**--legalonly**
> 只输出合规像素；不合规像素替换为黑色。

**--illegalonly**
> 只输出未经修正的不合规像素；合规像素替换为黑色。

**--correctedonly**
> 只输出不合规像素修正后的版本；合规像素替换为黑色。

# DESCRIPTION

**ppmntsc** 将 PPM 图像中的颜色调整到 NTSC 电视广播的合法范围内。它会检测每个像素，对超出合法范围的像素降低饱和度，同时保持合规像素不变。超过 NTSC 信号限值的颜色会被截断到最接近的合法值，从而避免广播显示上的光晕和色彩溢出等瑕疵。

**--pal** 选项可切换为使用 PAL 广播限制。**--verbose** 模式报告有多少像素非法，有助于评估源图像是否明显超出色域。过滤选项（**--legalonly**、**--illegalonly**、**--correctedonly**）可用于分离特定像素以进行分析。属于 Netpbm 工具集。

# CAVEATS

面向视频制作。属于 Netpbm 套件。该程序可处理包含多幅图像的 PPM 流。

# HISTORY

ppmntsc 由 Wes Barris 在明尼苏达超级计算中心创建，作为 **Netpbm** 工具集的一部分，用于 NTSC 颜色合规性处理。

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

[ppm](/man/ppm)(5), [ppmdim](/man/ppmdim)(1), [pambrighten](/man/pambrighten)(1), [pamdepth](/man/pamdepth)(1)
