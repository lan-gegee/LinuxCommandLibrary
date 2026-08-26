# TAGLINE

创建指定尺寸的纯色 PGM 灰度图像

# TLDR

**创建纯灰色图像**

```pgmmake [0.5] [100] [100] > [gray.pgm]```

**创建白色图像**

```pgmmake 1.0 [200] [150] > [white.pgm]```

**创建黑色图像**

```pgmmake 0.0 [640] [480] > [black.pgm]```

**指定最大值**

```pgmmake -maxval [65535] [0.5] [100] [100] > [gray16.pgm]```

# SYNOPSIS

**pgmmake** [_options_] _grayval_ _width_ _height_

# PARAMETERS

**grayval**
> 灰度值（0.0 = 黑色，1.0 = 白色）。

**width**
> 图像宽度（像素）。

**height**
> 图像高度（像素）。

**-maxval** _n_
> 最大灰度值（默认 255）。

# DESCRIPTION

**pgmmake** 创建指定尺寸的纯色 PGM 灰度图像。灰度值是一个比例值，0.0 表示黑色，1.0 表示白色。

# 50% gray 100x100 image
pgmmake 0.5 100 100 > gray.pgm

# Black background
pgmmake 0 1920 1080 > black.pgm

# 16-bit white image
pgmmake -maxval 65535 1.0 100 100 > white16.pgm

# Create and convert to PNG
pgmmake 0.75 200 200 | pnmtopng > gray.png
```

# CAVEATS

只能创建灰度图。彩色请使用 ppmmake。属于 Netpbm 工具集。

# HISTORY

pgmmake 是 **Netpbm** 图像处理工具集的一部分，该工具集最初由 **Jef Poskanzer** 创建。

# SEE ALSO

[ppmmake](/man/ppmmake)(1), [pbmmake](/man/pbmmake)(1), [pnmtopng](/man/pnmtopng)(1), [netpbm](/man/netpbm)(1)

# INSTALL

```apt: sudo apt install netpbm```

```dnf: sudo dnf install netpbm```

```pacman: sudo pacman -S netpbm```

```apk: sudo apk add netpbm```

```zypper: sudo zypper install netpbm```

```brew: brew install netpbm```

```nix: nix profile install nixpkgs#netpbm```

<!-- packages: 2026-07-22 -->
