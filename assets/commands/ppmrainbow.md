# TAGLINE

生成多色渐变图像

# TLDR

**生成彩虹渐变**

```ppmrainbow -width [100] -height [50] [color1] [color2] > [output.ppm]```

**创建从红到蓝的渐变**

```ppmrainbow -width 200 -height 100 red blue > [gradient.ppm]```

**多色渐变**

```ppmrainbow -width 300 -height 50 red yellow green blue > [rainbow.ppm]```

# SYNOPSIS

**ppmrainbow** [_options_] _colors_

# PARAMETERS

_COLORS_
> 颜色停靠点。

**-width** _N_
> 输出宽度。

**-height** _N_
> 输出高度。

**-norepeat**
> 不重复色谱。

# DESCRIPTION

**ppmrainbow** 创建一幅水平方向的颜色渐变图像，在指定的颜色停靠点之间平滑过渡。可以提供任意数量的命名颜色，工具会在整个图像宽度上均匀插值。

它适合用来创建渐变背景、测试用色条或装饰元素。**-norepeat** 选项可防止渐变绕回到第一种颜色。属于 Netpbm 工具集。

# CAVEATS

仅支持水平渐变。属于 Netpbm 套件。

# HISTORY

ppmrainbow 作为 **Netpbm** 的一部分被创建，用于渐变生成。

# INSTALL

```apt: sudo apt install netpbm```

```dnf: sudo dnf install netpbm```

```pacman: sudo pacman -S netpbm```

```apk: sudo apk add netpbm-extras```

```zypper: sudo zypper install netpbm```

```brew: brew install netpbm```

```nix: nix profile install nixpkgs#netpbm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ppm](/man/ppm)(5), [ppmmake](/man/ppmmake)(1)
