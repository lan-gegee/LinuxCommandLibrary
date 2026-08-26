# TAGLINE

将 PPM 转换为 HP PaintJet XL 格式

# TLDR

**将 PPM 转换为 HP PaintJet XL 格式**

```ppmtopjxl [input.ppm] > [output.pjxl]```

**指定渲染模式**

```ppmtopjxl -render [best] [input.ppm] > [output.pjxl]```

# SYNOPSIS

**ppmtopjxl** [_options_] [_file_]

# PARAMETERS

**-render** _mode_
> 渲染模式（draft、normal、best）。

**-dpi** _n_
> 打印分辨率。

# DESCRIPTION

**ppmtopjxl** 将 PPM 图像转换为 HP PaintJet XL/XL300 PCL 格式以便直接打印。属于 Netpbm 工具集。

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

[ppmtopj](/man/ppmtopj)(1), [ppmtolj](/man/ppmtolj)(1)
