# TAGLINE

将 Atari Spectrum 图像转换为 PPM

# TLDR

**将 Atari SPC 转换为 PPM**

```spctoppm [input.spc] > [output.ppm]```

# SYNOPSIS

**spctoppm** [_file_]

# DESCRIPTION

**spctoppm** 将 Atari 压缩 Spectrum 格式（SPC）的图像转换为 PPM（Portable Pixmap）格式。Spectrum 格式曾用于 Atari ST 计算机上存储彩色图像。此工具是 Netpbm 图像处理工具包的一部分，该工具包提供多种图像格式之间的转换器。

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

[sputoppm](/man/sputoppm)(1), [neotoppm](/man/neotoppm)(1)
