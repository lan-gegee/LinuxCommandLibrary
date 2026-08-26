# TAGLINE

将 PPM 图像转换为 TGA 格式

# TLDR

**将 PPM 转换为 TGA**

```ppmtotga [input.ppm] > [output.tga]```

**以压缩方式转换**

```ppmtotga -rle [input.ppm] > [output.tga]```

# SYNOPSIS

**ppmtotga** [_options_] [_file_]

# PARAMETERS

**-rle**
> 行程长度编码压缩。

**-norle**
> 不压缩。

# DESCRIPTION

**ppmtotga** 将 PPM 图像转换为 TGA（Targa）格式。TGA 常用于游戏开发和 3D 图形领域。属于 Netpbm 工具集。

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

[tgatoppm](/man/tgatoppm)(1), [ppmtobmp](/man/ppmtobmp)(1)
