# TAGLINE

将 PPM 颜色映射到均匀分布的灰度级

# TLDR

按**亮度**排序并映射到灰度

```ppmdist -intensity [input.ppm] > [output.pgm]```

按**出现频率**排序并映射到灰度

```ppmdist -frequency [input.ppm] > [output.pgm]```

# SYNOPSIS

**ppmdist** [**-intensity** | **-frequency**] [_ppmfile_]

# PARAMETERS

**-intensity**
> 在映射到均匀分布的灰度级之前，先按灰度亮度对输入颜色排序。

**-frequency**
> 在映射到均匀分布的灰度级之前，先按颜色出现的次数对输入颜色排序。

# DESCRIPTION

**ppmdist** 读取一幅 PPM 图像并生成灰度级均匀分布的 PGM 输出。输入包含 n 种颜色时会产生 n 个灰度级，从而最大化输出的对比度。映射顺序由 **-intensity** 或 **-frequency** 选项控制。对颜色数量较少的图像最为有用。属于 Netpbm 工具集。

# CAVEATS

仅对颜色数量非常少的图像有帮助。未指定文件时从标准输入读取。

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

[ppmcolormask](/man/ppmcolormask)(1)
