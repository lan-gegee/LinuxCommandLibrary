# TAGLINE

将 Windows 图标转换为 PPM 格式

# TLDR

**将 Windows 图标转换为 PPM**

```winicontoppm [input.ico] > [output.ppm]```

**提取特定图像**

```winicontoppm -image [0] [input.ico] > [output.ppm]```

# SYNOPSIS

**winicontoppm** [_options_] [_file_]

# PARAMETERS

**-image** _n_
> 提取指定索引的图像。

**-verbose**
> 打印图标信息。

# DESCRIPTION

**winicontoppm** 将 Windows ICO 文件转换为 PPM 格式。不保留透明度；需要 alpha 通道请使用 winicontopam。属于 Netpbm 工具集。

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

[ppmtowinicon](/man/ppmtowinicon)(1), [winicontopam](/man/winicontopam)(1)

