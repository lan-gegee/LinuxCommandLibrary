# TAGLINE

生成装饰性图案图像

# TLDR

**创建棋盘格图案**

```ppmpat -gingham2 [100] [100] > [pattern.ppm]```

**创建格子呢图案**

```ppmpat -tartan [200] [200] > [tartan.ppm]```

**创建菱形花纹图案**

```ppmpat -argyle1 [150] [150] > [argyle.ppm]```

# SYNOPSIS

**ppmpat** _pattern_ _width_ _height_

# PARAMETERS

**-gingham2**
> 方格纹棋盘格。

**-gingham3**
> 三色方格纹。

**-tartan**
> 格子呢。

**-argyle1**
> 菱形花纹。

**-argyle2**
> 带线条的菱形花纹。

**-poles**
> 理发店旋转柱条纹。

**-squig**
> 波浪曲线。

**-camo**
> 迷彩图案。

# DESCRIPTION

**ppmpat** 生成各种图案图像。可创建测试图案、格纹和装饰性背景。属于 Netpbm 工具集。

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

[pgmramp](/man/pgmramp)(1), [ppmforge](/man/ppmforge)(1)
