# TAGLINE

将 PNM 转换为 Utah RLE 格式

# TLDR

**将 PNM 转换为 Utah RLE 格式**

```pnmtorle [input.pnm] > [output.rle]```

**添加 Alpha 通道**

```pnmtorle -alpha [mask.pgm] [input.pnm] > [output.rle]```

# SYNOPSIS

**pnmtorle** [_options_] [_file_]

# PARAMETERS

**-alpha** _file_
> Alpha 遮罩文件。

**-verbose**
> 打印进度信息。

# DESCRIPTION

**pnmtorle** 将 PNM 图像转换为 Utah Raster Toolkit 所使用的 Utah RLE（行程长度编码）格式。属于 Netpbm 工具集。

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

[rletopnm](/man/rletopnm)(1), [pnmtosgi](/man/pnmtosgi)(1)
