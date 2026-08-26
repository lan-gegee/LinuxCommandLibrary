# TAGLINE

使用高质量重采样调整 PAM/PNM 图像的尺寸

# TLDR

**缩放到指定尺寸**

```pamscale -width [800] -height [600] [input.pam] > [output.pam]```

**按倍数缩放**

```pamscale [0.5] [input.pam] > [half.pam]```

**保持宽高比缩放**

```pamscale -xyfit [800] [600] [input.pam] > [output.pam]```

**只缩放宽度**

```pamscale -xsize [800] [input.pam] > [output.pam]```

**高质量缩放**

```pamscale -filter=lanczos [0.5] [input.pam] > [output.pam]```

# SYNOPSIS

**pamscale** [_options_] [_scale_] [_pamfile_]

# PARAMETERS

**scale**
> 缩放倍数（0.5 表示一半）。

**-width**, **-xsize** _n_
> 输出宽度。

**-height**, **-ysize** _n_
> 输出高度。

**-xyfit** _w_ _h_
> 在指定框内适配，并保持宽高比。

**-filter** _name_
> 重采样滤波器。

**-linear**
> 线性插值。

# DESCRIPTION

**pamscale** 使用高质量重采样来调整 PAM/PNM 图像的尺寸。它可以按倍数缩放、缩放到指定尺寸，或者在保持宽高比的前提下适配到给定边框内。

# FILTERS

```
point    - Nearest neighbor
box      - Box filter
triangle - Linear/bilinear
lanczos  - High quality (default)
```

# CAVEATS

放大可能产生模糊。过小的缩放比例可能丢失细节。处理大图像需要较多内存。

# HISTORY

pamscale 是 **Netpbm** 的组成部分，通过多种重采样算法提供高质量的图像缩放。

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

[pamenlarge](/man/pamenlarge)(1), [pamstretch](/man/pamstretch)(1), [pnmscale](/man/pnmscale)(1)
