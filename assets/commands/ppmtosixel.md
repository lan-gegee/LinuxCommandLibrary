# TAGLINE

将 PPM 转换为 DEC Sixel 终端格式

# TLDR

**将 PPM 转换为 Sixel**

```ppmtosixel [input.ppm]```

**以原始输出转换**

```ppmtosixel -raw [input.ppm]```

# SYNOPSIS

**ppmtosixel** [_options_] [_file_]

# PARAMETERS

**-raw**
> 原始 sixel 输出。

**-margin**
> 添加边距。

# DESCRIPTION

**ppmtosixel** 将 PPM 图像转换为 DEC Sixel 格式。Sixel 让兼容的终端能够内联显示图形。属于 Netpbm 工具集。

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

[ppmtoascii](/man/ppmtoascii)(1), [ppmtoterm](/man/ppmtoterm)(1)
