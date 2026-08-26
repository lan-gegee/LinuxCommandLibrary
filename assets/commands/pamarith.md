# TAGLINE

对两幅 PAM/PNM 图像执行算术运算

# TLDR

**将两幅图像相加**

```pamarith -add [image1.pam] [image2.pam] > [result.pam]```

**图像相减**

```pamarith -subtract [image1.pam] [image2.pam] > [result.pam]```

**图像相乘**

```pamarith -multiply [image1.pam] [image2.pam] > [result.pam]```

**求差异**

```pamarith -difference [image1.pam] [image2.pam] > [result.pam]```

**取两图的最小值**

```pamarith -minimum [image1.pam] [image2.pam] > [result.pam]```

# SYNOPSIS

**pamarith** _-function_ _pamfile1_ _pamfile2_

# PARAMETERS

**-add**
> 像素值相加。

**-subtract**
> 像素值相减。

**-multiply**
> 像素值相乘。

**-divide**
> 像素值相除。

**-difference**
> 绝对差值。

**-minimum**
> 每个像素取最小值。

**-maximum**
> 每个像素取最大值。

**-mean**
> 像素平均值。

**-and**, **-or**, **-xor**
> 按位运算。

# DESCRIPTION

**pamarith** 对两幅 PAM/PNM 图像执行算术运算。两幅图像必须具有相同尺寸。常用于合成、遮罩和图像比较。

# EXAMPLE

```bash
# Find difference between images
pamarith -difference old.ppm new.ppm > diff.ppm

# Blend two images
pamarith -mean image1.ppm image2.ppm > blended.ppm
```

# CAVEATS

图像尺寸必须相同。优先使用 PAM 格式。输出可能需要缩放才能正常显示。

# HISTORY

pamarith 是 **Netpbm** 的一部分，Netpbm 是一个可追溯至 20 世纪 80 年代后期的图像处理工具集。

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

[pnmarith](/man/pnmarith)(1), [pamcomp](/man/pamcomp)(1), [netpbm](/man/netpbm)(1)
