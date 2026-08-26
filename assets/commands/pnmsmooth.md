# TAGLINE

平滑和模糊 PNM 图像

# TLDR

**平滑/模糊图像**

```pnmsmooth [input.pnm] > [output.pnm]```

**以自定义尺寸平滑**

```pnmsmooth -size [5] [input.pnm] > [output.pnm]```

**多次处理**

```pnmsmooth [input.pnm] | pnmsmooth > [output.pnm]```

# SYNOPSIS

**pnmsmooth** [_options_] [_pnmfile_]

# PARAMETERS

**-size** _n_
> 卷积尺寸（默认 3）。

**-dump** _file_
> 转储卷积矩阵。

# DESCRIPTION

**pnmsmooth** 使用卷积对 PNM 图像应用平滑（模糊）滤波器。它通过对相邻像素取平均来降低噪声并弱化锐利的边缘。

本命令是 pnmconvol 配合平滑核使用的封装。

# EXAMPLES

```bash
# Basic smoothing
pnmsmooth noisy.ppm > smooth.ppm

# Stronger smoothing with larger kernel
pnmsmooth -size 5 image.ppm > blurred.ppm

# Multiple smoothing passes
pnmsmooth image.ppm | pnmsmooth | pnmsmooth > very_smooth.ppm

# Reduce noise then enhance
pnmsmooth noisy.pgm | pgmenhance > cleaned.pgm
```

# CONVOLUTION

默认的 3x3 平均核：
```
1 1 1
1 1 1
1 1 1
```

更大的尺寸会产生更强的模糊效果。

# CAVEATS

会降低图像清晰度。要使用自定义卷积核请用 pnmconvol。属于 Netpbm。

# HISTORY

pnmsmooth 是 **Jef Poskanzer** 所作 **Netpbm** 的一部分，通过卷积提供简单的图像平滑功能。

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

[pnmconvol](/man/pnmconvol)(1), [pgmenhance](/man/pgmenhance)(1), [netpbm](/man/netpbm)(1)
