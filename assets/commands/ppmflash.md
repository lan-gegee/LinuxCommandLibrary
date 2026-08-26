# TAGLINE

将 PPM 图像向白色方向提亮

# TLDR

**按系数提亮图像**

```ppmflash [0.5] [input.ppm] > [output.ppm]```

# SYNOPSIS

**ppmflash** _factor_ [_file_]

# PARAMETERS

_factor_
> 提亮系数（0-1，1 表示白色）。

# DESCRIPTION

**ppmflash** 按指定系数将 PPM 图像向白色方向提亮。可用于制作闪光/渐隐效果。属于 Netpbm 工具集。

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

[ppmbrighten](/man/ppmbrighten)(1), [ppmdim](/man/ppmdim)(1)
