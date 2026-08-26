# TAGLINE

水平或垂直拼接 PNM 图像

# TLDR

**水平拼接**

```pnmcat -lr [image1.pnm] [image2.pnm] > [result.pnm]```

**垂直拼接**

```pnmcat -tb [image1.pnm] [image2.pnm] > [result.pnm]```

**使用背景色**

```pnmcat -lr -white [image1.pnm] [image2.pnm] > [result.pnm]```

**居中对齐**

```pnmcat -tb -jcenter [image1.pnm] [image2.pnm] > [result.pnm]```

# SYNOPSIS

**pnmcat** [_options_] _pnmfiles_...

# PARAMETERS

**-lr**
> 从左到右（水平）。

**-tb**
> 从上到下（垂直）。

**-jleft**, **-jcenter**, **-jright**
> 水平对齐方式。

**-jtop**, **-jcenter**, **-jbottom**
> 垂直对齐方式。

**-white**
> 白色背景。

**-black**
> 黑色背景。

# DESCRIPTION

**pnmcat** 将多幅 PNM 图像水平或垂直地拼接在一起。它相当于 cat 命令在图像领域的对应物。

借助对齐和背景选项，它可以处理尺寸各异的图像。

# EXAMPLES

```bash
# Side by side
pnmcat -lr left.ppm right.ppm > combined.ppm

# Stack vertically
pnmcat -tb top.ppm bottom.ppm > stacked.ppm

# Multiple images
pnmcat -lr img1.ppm img2.ppm img3.ppm > row.ppm

# Centered with white background
pnmcat -tb -jcenter -white small.ppm large.ppm > out.ppm
```

# CAVEATS

所有图像必须是同一类型（PBM、PGM 或 PPM）。可以处理不同的位深。属于 Netpbm。

# HISTORY

pnmcat 是 **Jef Poskanzer** 所作 **Netpbm** 的一部分，自早期的 Pbmplus 起便提供图像拼接功能。

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

[pamstack](/man/pamstack)(1), [pnmtile](/man/pnmtile)(1), [pnmpaste](/man/pnmpaste)(1), [netpbm](/man/netpbm)(1)
