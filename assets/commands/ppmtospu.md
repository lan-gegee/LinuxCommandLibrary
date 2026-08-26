# TAGLINE

将 PPM 转换为 Atari Spectrum 512 格式

# TLDR

**将 PPM 转换为 Atari Spectrum 512**

```ppmtospu [input.ppm] > [output.spu]```

# SYNOPSIS

**ppmtospu** [_options_] [_file_]

# PARAMETERS

**-d**
> 双倍分辨率。

# DESCRIPTION

**ppmtospu** 将 PPM 图像转换为 Atari Spectrum 512 格式，该格式可在 Atari ST 上显示 512 种颜色。属于 Netpbm 工具集。

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

[sputoppm](/man/sputoppm)(1), [ppmtoneo](/man/ppmtoneo)(1)
