# TAGLINE

将 PNM 转换为 SGI 图像格式

# TLDR

**将 PNM 转换为 SGI 图像**

```pnmtosgi [input.pnm] > [output.rgb]```

**使用 RLE 压缩**

```pnmtosgi -rle [input.pnm] > [output.rgb]```

# SYNOPSIS

**pnmtosgi** [_options_] [_file_]

# PARAMETERS

**-verbatim**
> 不压缩（默认）。

**-rle**
> 使用 RLE 压缩。

**-imagename** _name_
> 设置存储在 SGI 文件内的图像名称字段。

**-mtime** _seconds_
> 设置存储在文件内的修改时间。

# DESCRIPTION

**pnmtosgi** 将 PNM 图像转换为 SGI（Silicon Graphics）图像格式。属于 Netpbm 工具集。

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

[sgitopnm](/man/sgitopnm)(1), [pnmtorle](/man/pnmtorle)(1)
