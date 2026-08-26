# TAGLINE

计算两幅图像之间的峰值信噪比

# TLDR

**比较两幅 PNM 图像并显示 PSNR**

```pnmpsnr [original.pnm] [compressed.pnm]```

**比较 JPEG 转换结果与原图**（使用 Netpbm 进行转换）

```pnmpsnr [original.ppm] [converted.ppm]```

**比较来自管道的图像**（第二幅图像取自标准输入）

```pnmpsnr [reference.pnm] < [comparison.pnm]```

# SYNOPSIS

**pnmpsnr** [_file1_] [_file2_]

# PARAMETERS

_file1_
> 第一幅输入图像（参考图/原图）。

_file2_
> 第二幅输入图像（比较图/失真图）。省略时从标准输入读取。

# DESCRIPTION

**pnmpsnr** 计算两幅 PNM 图像之间的峰值信噪比（PSNR）。PSNR 是衡量图像质量的标准指标，常用于评估压缩或处理后的图像相对于原图的保真度。

PSNR 值（以分贝为单位）越高，说明两幅图像越相似。可接受质量的典型值在 30-50 dB 之间；完全相同的图像则产生无穷大的 PSNR。对彩色图像，该工具会分别报告每个通道（红、绿、蓝）的 PSNR，并给出整体亮度值。

两幅图像必须具有相同的尺寸和位深。属于 Netpbm 工具集。

# CAVEATS

两幅图像必须尺寸相同。仅支持 PNM/PAM 格式；其他格式请先用 Netpbm 工具转换。PSNR 并非总能可靠反映感知质量。

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

[pnmarith](/man/pnmarith)(1), [pamarith](/man/pamarith)(1), [pamfile](/man/pamfile)(1), [pnmcat](/man/pnmcat)(1)
