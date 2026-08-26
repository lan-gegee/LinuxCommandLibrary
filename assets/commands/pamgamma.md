# TAGLINE

对图像应用伽马校正

# TLDR

**应用伽马校正**

```pamgamma [2.2] [input.pam] > [output.pam]```

**应用逆伽马**

```pamgamma [0.45] [input.pam] > [output.pam]```

**将 sRGB 转换为线性**

```pamgamma -ungamma [input.pam] > [linear.pam]```

**将线性转换为 sRGB**

```pamgamma -gamma [linear.pam] > [srgb.pam]```

# SYNOPSIS

**pamgamma** [_options_] [_gamma_] [_pamfile_]

# PARAMETERS

**gamma**
> 伽马值（大于 0）。

**-ungamma**
> 去除伽马（转为线性）。

**-gamma**
> 应用伽马（转为 sRGB）。

**-bt709**
> 使用 BT.709 传递函数。

**-srgb**
> 使用 sRGB 传递函数。

# DESCRIPTION

**pamgamma** 对图像应用伽马校正。伽马校正调整亮度曲线：值 > 1 会加深中间调，值 < 1 则会提亮中间调。

标准显示伽马约为 2.2，其逆值约为 0.45。

# COMMON VALUES

```
2.2   - Standard gamma
0.45  - Inverse gamma (1/2.2)
1.0   - No change
```

# EXAMPLE

```bash
# Brighten dark image
pamgamma 0.7 dark.ppm > brighter.ppm

# Standard gamma encode
pamgamma 2.2 linear.ppm > encoded.ppm
```

# CAVEATS

输入应与预期的伽马相匹配。极端情况下可能出现截断。

# HISTORY

pamgamma 是 **Netpbm** 的组成部分，在色彩空间转换过程中提供伽马校正功能。

# SEE ALSO

[pnmgamma](/man/pnmgamma)(1), [pamrecolor](/man/pamrecolor)(1), [netpbm](/man/netpbm)(1)
