# TAGLINE

生成分形地形和云彩图像

# TLDR

**生成分形地形**

```ppmforge > [terrain.ppm]```

**生成云彩**

```ppmforge -clouds > [clouds.ppm]```

**生成夜景**

```ppmforge -night > [night.ppm]```

**指定尺寸**

```ppmforge -width [512] -height [512] > [output.ppm]```

# SYNOPSIS

**ppmforge** [_options_]

# PARAMETERS

**-clouds**
> 生成云彩图像。

**-night**
> 生成夜景。

**-width** _N_
> 输出宽度。

**-height** _N_
> 输出高度。

**-seed** _N_
> 随机种子。

**-mesh** _N_
> 网格大小。

# DESCRIPTION

**ppmforge** 使用程序化算法生成分形图像，可产生逼真的地形、云彩和行星表面图像。地形模式创建带水域的按海拔着色的地貌，云彩模式则生成大气纹理图案。

随机种子参数支持可复现的生成，网格大小控制分形细节的层级。夜景模式可创建星空图像。输出尺寸的宽度和高度可以独立配置。属于 Netpbm 工具集。

# CAVEATS

程序化生成。属于 Netpbm 套件。

# HISTORY

ppmforge 作为 **Netpbm** 的一部分被创建，用于分形图像生成。

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

[ppm](/man/ppm)(5), [ppmplasma](/man/ppmplasma)(1)
