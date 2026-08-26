# TAGLINE

生成 HSV 色轮图像

# TLDR

**生成色轮**

```ppmwheel [diameter] > [output.ppm]```

**创建 200px 的色轮**

```ppmwheel 200 > [wheel.ppm]```

# SYNOPSIS

**ppmwheel** _diameter_

# PARAMETERS

_DIAMETER_
> 色轮直径（像素）。

# DESCRIPTION

**ppmwheel** 生成一幅指定直径（像素）的 HSV 色轮 PPM 图像。输出是一幅以色轮为中心的正方形图像：色相沿圆周变化，饱和度从中心到边缘递增，明度恒定为最大值。

属于 Netpbm 图像处理工具套件。

# CAVEATS

输出始终是正方形的 PPM 图像。如需转换为其他格式，可通过管道交给其他 Netpbm 工具或 ImageMagick。

# HISTORY

ppmwheel 作为 **Netpbm** 的一部分被创建，用于生成色轮。

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

[ppm](/man/ppm)(5), [ppmrainbow](/man/ppmrainbow)(1)
