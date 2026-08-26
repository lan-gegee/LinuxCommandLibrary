# TAGLINE

随机移动像素以产生噪点效果

# TLDR

**随机散布像素**

```ppmspread [amount] [input.ppm] > [output.ppm]```

**轻度散布效果**

```ppmspread 5 [input.ppm] > [output.ppm]```

**重度散布效果**

```ppmspread 20 [input.ppm] > [output.ppm]```

# SYNOPSIS

**ppmspread** _amount_ [_file_]

# PARAMETERS

_AMOUNT_
> 散布半径（像素）。

_FILE_
> 输入的 PPM 文件。

# DESCRIPTION

**ppmspread** 将 PPM 图像中的每个像素随机移动到指定半径内的新位置，产生分散的、类似噪点的模糊效果。散布量越大，结果越弥散；散布量较小则会增添细微的纹理。

与对像素取平均的高斯模糊不同，散布保留各个像素的颜色但随机化其位置，呈现出独特的磨砂玻璃或点彩画风格。属于 Netpbm 工具集。

# CAVEATS

仅接受 PPM 格式的输入。请先用 **pnmtoppm** 从其他格式转换。amount 参数指定任意方向上的最大位移；每个像素的实际位移在该范围内随机。

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

[ppmshift](/man/ppmshift)(1), [pnmnoise](/man/pnmnoise)(1), [netpbm](/man/netpbm)(1)
