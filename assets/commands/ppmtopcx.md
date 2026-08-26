# TAGLINE

将 PPM 图像转换为 PCX 格式

# TLDR

**将 PPM 转换为 PCX**

```ppmtopcx [input.ppm] > [output.pcx]```

**以 256 色转换**

```ppmtopcx -256 [input.ppm] > [output.pcx]```

**以 24 位真彩色转换**

```ppmtopcx -24bit [input.ppm] > [output.pcx]```

# SYNOPSIS

**ppmtopcx** [_options_] [_file_]

# PARAMETERS

**-256**
> 256 色调色板。

**-24bit**
> 24 位真彩色。

**-packed**
> 紧凑像素模式。

# DESCRIPTION

**ppmtopcx** 将 PPM 图像转换为 PCX 格式。PCX 是一种较旧的位图格式，曾在 DOS 应用程序中广泛使用。属于 Netpbm 工具集。

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

[pcxtoppm](/man/pcxtoppm)(1), [ppmtobmp](/man/ppmtobmp)(1)
