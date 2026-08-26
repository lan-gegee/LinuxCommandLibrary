# TAGLINE

将 PPM 转换为 Windows 图标格式

# TLDR

**将 PPM 转换为 Windows 图标**

```ppmtowinicon [input.ppm] > [output.ico]```

**包含 AND 掩码**

```ppmtowinicon -andmask [mask.pbm] [input.ppm] > [output.ico]```

# SYNOPSIS

**ppmtowinicon** [_options_] [_file_]

# PARAMETERS

**-andmask** _file_
> 透明度掩码文件。

# DESCRIPTION

**ppmtowinicon** 将 PPM 图像转换为 Windows ICO 格式。通过 AND 掩码支持透明。属于 Netpbm 工具集。

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

[winicontoppm](/man/winicontoppm)(1), [pamtowinicon](/man/pamtowinicon)(1)
