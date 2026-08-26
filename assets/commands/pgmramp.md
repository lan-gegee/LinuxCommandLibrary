# TAGLINE

生成灰度渐变图像

# TLDR

**创建水平渐变**

```pgmramp -lr [256] [256] > [gradient.pgm]```

**创建垂直渐变**

```pgmramp -tb [256] [256] > [gradient.pgm]```

**创建对角渐变**

```pgmramp -diagonal [256] [256] > [gradient.pgm]```

**创建圆形渐变**

```pgmramp -ellipse [256] [256] > [gradient.pgm]```

# SYNOPSIS

**pgmramp** _type_ _width_ _height_

# PARAMETERS

**-lr**
> 从左到右的渐变。

**-tb**
> 从上到下的渐变。

**-rectangle**
> 矩形渐变。

**-ellipse**
> 椭圆渐变。

**-diagonal**
> 对角渐变。

# DESCRIPTION

**pgmramp** 生成灰度渐变图像，可创建多种渐变图案，用于测试和背景。属于 Netpbm 工具集。

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

[ppmpat](/man/ppmpat)(1), [pgmnoise](/man/pgmnoise)(1)
