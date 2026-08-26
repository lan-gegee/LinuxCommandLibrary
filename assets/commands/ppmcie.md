# TAGLINE

生成 CIE 色度图图像

# TLDR

**生成 CIE 色度图**

```ppmcie > [output.ppm]```

**指定尺寸**

```ppmcie -size [512] > [output.ppm]```

**使用指定的标准照明体生成**

```ppmcie -illuminant [D65] > [output.ppm]```

# SYNOPSIS

**ppmcie** [_options_]

# PARAMETERS

**-size** _N_
> 输出尺寸（像素）。

**-illuminant** _NAME_
> 白点标准照明体。

**-spectral** _N_
> 光谱类型。

# DESCRIPTION

**ppmcie** 以 PPM 图像的形式生成 CIE 色度图，将可见颜色的完整色域绘制在标准的 CIE 1931 xy 色彩空间上。该图是色彩科学中的标准参考图，用于可视化色域以及比较显示或打印设备的能力。

选项可控制输出尺寸、照明体白点，以及是否包含光谱波长标签。生成的图像可用于色彩科学教学、显示校准文档，或作为色域比较的参考叠加图。属于 Netpbm 工具集。

# CAVEATS

色彩科学工具。属于 Netpbm 套件。

# HISTORY

ppmcie 作为 **Netpbm** 的一部分被创建，用于色彩科学可视化。

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

[ppm](/man/ppm)(5), [ppmgamma](/man/ppmgamma)(1)
