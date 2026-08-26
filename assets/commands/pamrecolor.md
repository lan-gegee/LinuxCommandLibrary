# TAGLINE

在保持亮度不变的前提下更改图像的颜色

# TLDR

**为灰度图着色**

```pamrecolor -colorfile [color.ppm] [gray.ppm] > [output.ppm]```

**应用单一目标色**

```pamrecolor -targetcolor "rgb:ff/00/00" [gray.ppm] > [red.ppm]```

**保持亮度不变**

```pamrecolor -colorfile [palette.ppm] -rmult [1.0] [input.ppm] > [output.ppm]```

# SYNOPSIS

**pamrecolor** [_options_] [_pamfile_]

# PARAMETERS

**-colorfile** _file_
> 提供颜色的源图像。

**-targetcolor** _color_
> 单一目标颜色。

**-rmult**, **-gmult**, **-bmult** _factor_
> 各通道的乘数。

# DESCRIPTION

**pamrecolor** 在保持亮度不变的前提下更改图像的颜色。它可以为灰度图上色，也可以利用另一幅图像中的颜色重新映射当前图像的颜色。

# EXAMPLE

```bash
# Colorize old photo with sepia
pamrecolor -targetcolor "rgb:94/6d/50" old_photo.ppm > sepia.ppm

# Apply palette from reference
pamrecolor -colorfile reference.ppm target.ppm > recolored.ppm
```

# CAVEATS

效果取决于亮度的保持程度。对灰度图或低饱和度图像效果最佳。

# HISTORY

pamrecolor 是 **Netpbm** 的组成部分，为图像处理提供色彩操作工具。

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

[ppmchange](/man/ppmchange)(1), [pamgamma](/man/pamgamma)(1), [ppmtopgm](/man/ppmtopgm)(1)
