# TAGLINE

对 PNM 图像执行像素算术运算

# TLDR

**相加两幅图像**

```pnmarith -add [image1.pnm] [image2.pnm] > [result.pnm]```

**图像相减**

```pnmarith -subtract [image1.pnm] [image2.pnm] > [result.pnm]```

**图像相乘**

```pnmarith -multiply [image1.pnm] [image2.pnm] > [result.pnm]```

**取最小值**

```pnmarith -minimum [image1.pnm] [image2.pnm] > [result.pnm]```

# SYNOPSIS

**pnmarith** _operation_ _pnmfile1_ _pnmfile2_

# PARAMETERS

**-add**
> 像素值相加。

**-subtract**
> 像素值相减。

**-multiply**
> 像素值相乘。

**-difference**
> 绝对差值。

**-minimum**
> 取像素最小值。

**-maximum**
> 取像素最大值。

**-mean**
> 取像素平均值。

# DESCRIPTION

**pnmarith** 对两幅 PNM 图像逐像素执行算术运算。两幅图像必须尺寸相同。适用于合成、遮罩和图像比较。

在现代 Netpbm 中已被 pamarith 取代。

# EXAMPLES

```bash
# Add two images (blend)
pnmarith -add image1.ppm image2.ppm > blended.ppm

# Create difference image
pnmarith -difference frame1.ppm frame2.ppm > diff.ppm

# Multiply (darken with mask)
pnmarith -multiply image.ppm mask.pgm > masked.ppm

# Find minimum
pnmarith -minimum img1.ppm img2.ppm > min.ppm
```

# CAVEATS

图像必须尺寸相同。结果会被截断到有效范围内。更多选项请使用 pamarith。

# HISTORY

pnmarith 是 **Jef Poskanzer** 编写的 **Netpbm** 的一部分，提供基础的图像算术运算功能。

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

[pamarith](/man/pamarith)(1), [pnmcat](/man/pnmcat)(1), [pnmcomp](/man/pnmcomp)(1), [netpbm](/man/netpbm)(1)
