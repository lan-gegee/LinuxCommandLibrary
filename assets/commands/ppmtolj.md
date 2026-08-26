# TAGLINE

将 PPM 转换为 HP LaserJet 格式

# TLDR

**将 PPM 转换为 HP LaserJet 格式**

```ppmtolj [input.ppm] > [output.lj]```

**指定分辨率**

```ppmtolj -resolution [300] [input.ppm] > [output.lj]```

# SYNOPSIS

**ppmtolj** [_options_] [_file_]

# PARAMETERS

**-resolution** _n_
> 打印分辨率（DPI）。

**-delta**
> 使用增量行压缩。

# DESCRIPTION

**ppmtolj** 将 PPM 彩色图像转换为 HP LaserJet PCL 格式以便直接打印。属于 Netpbm 工具集。

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

[pbmtolj](/man/pbmtolj)(1), [pnmtopclxl](/man/pnmtopclxl)(1)
