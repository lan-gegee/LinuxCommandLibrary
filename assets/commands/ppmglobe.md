# TAGLINE

制作可打印的纸质地球仪条带

# TLDR

**创建地球仪条带**

```ppmglobe [strips] [input.ppm] [output]```

**创建 12 条带的地球仪**

```ppmglobe 12 [map.ppm] globe```

# SYNOPSIS

**ppmglobe** _strips_ _input_ _output_

# PARAMETERS

_STRIPS_
> 地球仪条带的数量。

_INPUT_
> 输入的地图图像。

_OUTPUT_
> 输出文件名的基础名。

# DESCRIPTION

**ppmglobe** 将等距圆柱投影（equirectangular）的地图图像转换为一组锥形条带，这些条带可以打印、裁剪并组装成纸质地球仪。条带数量决定地球仪被划分成多少片，条带越多，球面越平滑。

输入图像应采用等距圆柱投影（plate carrée），即经度线性映射到 x 轴、纬度线性映射到 y 轴。每条输出条带都保存为单独的带编号 PPM 文件。属于 Netpbm 工具集。

# CAVEATS

假定输入为等距圆柱投影。属于 Netpbm 套件。

# HISTORY

ppmglobe 作为 **Netpbm** 的一部分被创建，用于生成纸质地球仪。

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

[ppm](/man/ppm)(5)
