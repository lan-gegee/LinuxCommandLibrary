# TAGLINE

对 PNM 图像做直方图均衡化

# TLDR

**直方图均衡化**

```pnmhisteq [input.pnm] > [output.pnm]```

**详细输出**

```pnmhisteq -verbose [input.pnm] > [output.pnm]```

**对灰度图做均衡化**

```ppmtopgm [input.ppm] | pnmhisteq > [output.pgm]```

# SYNOPSIS

**pnmhisteq** [_options_] [_pnmfile_]

# PARAMETERS

**-gray**
> 基于灰度值进行均衡化。

**-verbose**
> 打印信息。

# DESCRIPTION

**pnmhisteq** 对 PNM 图像执行直方图均衡化。这一过程会铺开出现最频繁的强度值，从而改善亮度层级聚集在一起的图像的对比度。

属于 Netpbm 图像增强工具集。

# EXAMPLES

```bash
# Basic histogram equalization
pnmhisteq photo.pgm > enhanced.pgm

# Color image via grayscale
jpegtopnm photo.jpg | pnmhisteq > enhanced.ppm

# Chain with conversion
pnmhisteq dark.pgm | pnmtopng > enhanced.png
```

# ALGORITHM

直方图均衡化将输入强度映射为输出强度，使输出直方图近似均匀分布。这样可以最大化图像对比度。

# CAVEATS

可能放大均匀区域的噪声。效果取决于图像内容。对灰度图像的效果好于彩色图像。

# HISTORY

pnmhisteq 是 **Jef Poskanzer** 及各位贡献者所作 **Netpbm** 的一部分，实现了经典的直方图均衡化。

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

[pgmhist](/man/pgmhist)(1), [pnmnorm](/man/pnmnorm)(1), [pgmenhance](/man/pgmenhance)(1), [netpbm](/man/netpbm)(1)
