# TAGLINE

随机水平移动图像的各行

# TLDR

**水平移动图像**

```ppmshift [shift] [input.ppm] > [output.ppm]```

**随机水平偏移**

```ppmshift 10 [input.ppm] > [output.ppm]```

# SYNOPSIS

**ppmshift** _shift_ [_file_]

# PARAMETERS

_SHIFT_
> 最大移动量。

_FILE_
> 输入的 PPM 文件。

**-seed** _N_
> 随机种子。

# DESCRIPTION

**ppmshift** 将 PPM 图像的每一行随机水平移动不超过指定最大值的距离。这会产生类似故障艺术（glitch）的扭曲效果，图像看起来像是出现了水平撕裂或错位。

随机种子选项支持结果复现。该效果类似于模拟视频信号干扰或数字故障艺术。属于 Netpbm 工具集。

# CAVEATS

每一行独立随机移动。属于 Netpbm 套件。

# HISTORY

ppmshift 作为 **Netpbm** 的一部分被创建，用于图像扭曲特效。

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

[ppm](/man/ppm)(5), [ppmspread](/man/ppmspread)(1)
