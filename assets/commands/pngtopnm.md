# TAGLINE

将 PNG 图像转换为 PNM 格式

# TLDR

**将 PNG 转换为 PNM**

```pngtopnm [input.png] > [output.pnm]```

**将 Alpha 通道提取到单独的文件**

```pngtopnm -alpha [input.png] > [alpha.pgm]```

# SYNOPSIS

**pngtopnm** [_options_] [_file_]

# PARAMETERS

**-alpha**
> 将 Alpha 通道提取为 PGM。

**-mix**
> 与背景色混合。

**-background** _color_
> 用于混合的背景色。

**-verbose**
> 详细输出。

# DESCRIPTION

**pngtopnm** 将 PNG 图像转换为 PNM（PBM/PGM/PPM）格式。它是 Netpbm 图像转换工具集的一部分。输出类型取决于 PNG 的颜色深度。

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

[pnmtopng](/man/pnmtopng)(1), [pngtopam](/man/pngtopam)(1)
