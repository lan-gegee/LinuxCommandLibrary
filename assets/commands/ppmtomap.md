# TAGLINE

从 PPM 图像中提取颜色映射表

# TLDR

**从图像中提取颜色映射表**

```ppmtomap [input.ppm] > [colormap.ppm]```

**按出现频率排序颜色**

```ppmtomap -sort [input.ppm] > [colormap.ppm]```

# SYNOPSIS

**ppmtomap** [_options_] [_file_]

# PARAMETERS

**-sort**
> 按出现频率排序颜色。

**-square**
> 使输出为正方形。

# DESCRIPTION

**ppmtomap** 从 PPM 图像中提取所有不同的颜色，生成一行式的颜色映射表图像。适用于分析或迁移调色板。属于 Netpbm 工具集。

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

[ppmhist](/man/ppmhist)(1), [pnmcolormap](/man/pnmcolormap)(1)
