# TAGLINE

将 XPM 像素图转换为 PPM 格式

# TLDR

将 **XPM** 图像转换为 **PPM**

```xpmtoppm [input.xpm] > [output.ppm]```

从**标准输入**读取

```cat [input.xpm] | xpmtoppm > [output.ppm]```

将 **alpha（透明度）通道**提取到单独的 PBM 文件

```xpmtoppm --alphaout=[alpha.pbm] [input.xpm] > [output.ppm]```

# SYNOPSIS

**xpmtoppm** [_options_] [_file_]

# PARAMETERS

**--alphaout=**_file_
> 将透明度掩码写入指定的 PBM 文件。如果输入不包含透明度信息，则文件内容全为白色（不透明）值。指定 `-` 可将 alpha 输出写到标准输出而不是图像本身。

# DESCRIPTION

**xpmtoppm** 读取 X11 像素图（XPM 版本 1 或 3）作为输入，生成 PPM 图像作为输出。它能处理透明度和颜色映射图像。属于 Netpbm 工具集。

# CAVEATS

仅支持有限的一部分 XPM 版本 3 特性；许多合法的 XPM 图像可能被拒绝。输入行长度超过 8K 字符会导致错误。

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

[ppmtoxpm](/man/ppmtoxpm)(1), [xbmtopbm](/man/xbmtopbm)(1), [netpbm](/man/netpbm)(1)
