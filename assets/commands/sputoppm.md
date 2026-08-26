# TAGLINE

将 Atari Spectrum 512 图像转换为 PPM

# TLDR

**将 Atari Spectrum 512 转换为 PPM**

```sputoppm [input.spu] > [output.ppm]```

# SYNOPSIS

**sputoppm** [_file_]

# DESCRIPTION

**sputoppm** 将 Atari Spectrum 512 未压缩格式（SPU）的图像转换为 PPM（Portable Pixmap）格式。Spectrum 512 格式曾用于 Atari ST 计算机，通过在每个扫描行上循环切换调色板来显示最多 512 种同时可见的颜色。该工具是 Netpbm 图像处理工具集的一部分，后者提供了众多图像格式之间的转换器。

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

[ppmtospu](/man/ppmtospu)(1), [spctoppm](/man/spctoppm)(1)
