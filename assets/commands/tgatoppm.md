# TAGLINE

将 TGA 图像转换为 PPM 格式

# TLDR

**将 TGA 转换为 PPM**

```tgatoppm [input.tga] > [output.ppm]```

**提取 alpha 通道**

```tgatoppm --alphaout=[alpha.pgm] [input.tga] > [output.ppm]```

# SYNOPSIS

**tgatoppm** [_options_] [_file_]

# PARAMETERS

**--alphaout** _file_
> 将 alpha 通道写入文件。

# DESCRIPTION

**tgatoppm** 将 TGA（Targa）图像转换为 PPM 格式。支持压缩和未压缩的 TGA 文件。是 Netpbm 工具包的一部分。

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

[ppmtotga](/man/ppmtotga)(1), [pngtopnm](/man/pngtopnm)(1)
