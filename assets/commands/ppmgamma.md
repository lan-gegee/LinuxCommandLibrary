# TAGLINE

对 PPM 图像应用伽马校正

# TLDR

**应用伽马校正**

```ppmgamma [2.2] [input.ppm] > [output.ppm]```

**提亮图像**

```ppmgamma [0.5] [input.ppm] > [output.ppm]```

**调暗图像**

```ppmgamma [2.0] [input.ppm] > [output.ppm]```

**分通道伽马值**

```ppmgamma [1.0] [1.2] [1.0] [input.ppm] > [output.ppm]```

# SYNOPSIS

**ppmgamma** _gamma_ [_ppmfile_]

**ppmgamma** _rgamma_ _ggamma_ _bgamma_ [_ppmfile_]

# PARAMETERS

**gamma**
> 应用于所有通道的伽马值。

**rgamma**, **ggamma**, **bgamma**
> 各通道各自的伽马值。

# DESCRIPTION

**ppmgamma** 对 PPM 图像应用伽马校正。伽马 < 1 时提亮图像，伽马 > 1 时调暗图像。每个像素值都会被求 1/gamma 次幂。

属于 Netpbm 工具集。

# EXAMPLES

```bash
# Standard gamma correction
ppmgamma 2.2 image.ppm > corrected.ppm

# Lighten dark image
ppmgamma 0.5 dark.ppm > lighter.ppm

# Darken bright image
ppmgamma 2.0 bright.ppm > darker.ppm

# Adjust blue channel only
ppmgamma 1.0 1.0 1.3 image.ppm > blue_adjusted.ppm

# Reverse gamma
ppmgamma 0.45 linear.ppm > srgb.ppm
```

# GAMMA VALUES

```
< 1.0  - Lighten midtones
= 1.0  - No change
> 1.0  - Darken midtones
2.2    - Typical monitor gamma
```

# CAVEATS

如需更多功能请使用 pamgamma。值为 0 和最大值的像素保持不变。属于 Netpbm。

# HISTORY

ppmgamma 是 **Jef Poskanzer** 编写的 **Netpbm** 的组成部分，用于实现图像的伽马校正。

# SEE ALSO

[pamgamma](/man/pamgamma)(1), [ppmbrighten](/man/ppmbrighten)(1), [pnmgamma](/man/pnmgamma)(1), [netpbm](/man/netpbm)(1)
