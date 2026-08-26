# TAGLINE

通过反转所有像素值生成 PAM 或 PNM 图像的负片

# TLDR

**反转图像颜色**

```paminvert [input.pam] > [output.pam]```

**从管道输入进行反转**

```cat [image.ppm] | paminvert > [inverted.ppm]```

# SYNOPSIS

**paminvert** [_pamfile_]

# DESCRIPTION

**paminvert** 通过反转所有像素值来生成 PAM 或 PNM 图像的负片。每个采样值都被替换为 maxval 减去该采样值的差。

对于灰度图，黑色变白色，白色变黑色。对于彩色图，每个通道独立反转。

# EXAMPLE

```bash
# Create negative
paminvert photo.ppm > negative.ppm

# Invert and convert to PNG
paminvert photo.ppm | pnmtopng > negative.png
```

# FORMULA

```
output = maxval - input

For 8-bit (maxval=255):
Black (0)   -> White (255)
White (255) -> Black (0)
Gray (128)  -> Gray (127)
```

# CAVEATS

这是简单反转，不是感知上的负片效果。如果存在 Alpha 通道，同样会被反转。

# HISTORY

paminvert 是 **Netpbm** 的组成部分，作为一种基础操作提供简单的图像反转功能。

# SEE ALSO

[pnminvert](/man/pnminvert)(1), [pamarith](/man/pamarith)(1), [netpbm](/man/netpbm)(1)
