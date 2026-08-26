# TAGLINE

将 Utah RLE 图像转换为 PNM 格式

# TLDR

**将 Utah RLE 转换为 PNM**

```rletopnm [input.rle] > [output.pnm]```

**详细输出**

```rletopnm -verbose [input.rle] > [output.pnm]```

# SYNOPSIS

**rletopnm** [_options_] [_file_]

# PARAMETERS

**-verbose**
> 打印图像信息。

**-headerdump**
> 转储 RLE 头部信息。

# DESCRIPTION

**rletopnm** 将 Utah RLE（Run Length Encoded，行程长度编码）图像转换为 PNM 格式。Utah RLE 是 Utah Raster Toolkit 的一部分。属于 Netpbm 工具集。

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

[pnmtorle](/man/pnmtorle)(1), [sgitopnm](/man/sgitopnm)(1)
