# TAGLINE

使用抖动图案减少颜色

# TLDR

**对图像做抖动处理**

```ppmdither [input.ppm] > [output.ppm]```

**指定每个通道的颜色数**

```ppmdither -red [4] -green [4] -blue [4] [input.ppm] > [output.ppm]```

**Floyd-Steinberg 抖动**

```ppmdither -fs [input.ppm] > [output.ppm]```

# SYNOPSIS

**ppmdither** [_options_] [_file_]

# PARAMETERS

_FILE_
> 输入的 PPM 文件。

**-red** _N_
> 红色通道的级数。

**-green** _N_
> 绿色通道的级数。

**-blue** _N_
> 蓝色通道的级数。

**-fs**
> Floyd-Steinberg 抖动。

# DESCRIPTION

**ppmdither** 使用抖动技术减少 PPM 图像中的颜色数量。抖动通过将可用的颜色排布成特定图案来模拟不可用的颜色，这些图案在远处看起来像是混合后的效果。红、绿、蓝三个颜色通道各自的级数可以独立指定。

默认使用有序抖动，而 **-fs** 选项选择 Floyd-Steinberg 误差扩散抖动，通常能产生更高质量的结果且图案感更不明显。与量化（ppmquant）不同，抖动并不挑选最优颜色，而是把误差分散到相邻像素上。属于 Netpbm 工具集。

# CAVEATS

与量化不同。属于 Netpbm 套件。

# HISTORY

ppmdither 作为 **Netpbm** 的一部分被创建，用于颜色抖动。

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

[ppmquant](/man/ppmquant)(1), [pnmremap](/man/pnmremap)(1), [ppm](/man/ppm)(5)
