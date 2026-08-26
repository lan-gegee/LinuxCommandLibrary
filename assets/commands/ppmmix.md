# TAGLINE

将两幅 PPM 图像混合在一起

# TLDR

**混合两幅图像**

```ppmmix [factor] [image1.ppm] [image2.ppm] > [output.ppm]```

**50% 混合**

```ppmmix 0.5 [a.ppm] [b.ppm] > [blend.ppm]```

**取第一幅图像的 25%**

```ppmmix 0.25 [a.ppm] [b.ppm] > [output.ppm]```

# SYNOPSIS

**ppmmix** _fadefactor_ _ppmfile1_ _ppmfile2_

# PARAMETERS

_FADEFACTOR_
> 混合系数（0.0-1.0）。0.0 时完全取第一幅图像，1.0 时完全取第二幅图像。

_PPMFILE1_
> 第一幅输入的 PPM 图像。

_PPMFILE2_
> 第二幅输入的 PPM 图像。

# DESCRIPTION

**ppmmix** 使用指定的渐变系数将两幅 PPM 图像混合在一起。该系数控制每幅图像的贡献：0.0 时完全为第一幅图像，1.0 时完全为第二幅图像，介于两者之间的值则按比例混合。

该渐变系数作用于亮度而非光强度。这意味着在黑白两幅图像之间线性递增的渐变系数会产生线性递增的感知亮度，但实际光强度在高亮端增长得更快。若要基于光强度进行混合，请改用 **pamcomp**。

两幅输入图像必须具有相同的尺寸和相同的 maxval。属于 Netpbm 工具集。

# CAVEATS

两幅图像的尺寸和 maxval 必须相同。没有 ppmmix 特有的选项；它只识别 libnetpbm 的通用选项。

# HISTORY

ppmmix 作为 **Netpbm** 的一部分被创建，用于图像混合。

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

[ppmfade](/man/ppmfade)(1), [pamcomp](/man/pamcomp)(1), [ppm](/man/ppm)(5)
