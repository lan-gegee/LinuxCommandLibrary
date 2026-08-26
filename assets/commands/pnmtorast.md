# TAGLINE

将 PNM 转换为 Sun rasterfile 格式

# TLDR

**将 PNM 转换为 Sun 光栅图像**

```pnmtorast [input.pnm] > [output.ras]```

**指定编码方式**

```pnmtorast -rle [input.pnm] > [output.ras]```

# SYNOPSIS

**pnmtorast** [_options_] [_file_]

# PARAMETERS

**-rle**
> 使用 RLE 压缩。

**-standard**
> 使用标准格式。

# DESCRIPTION

**pnmtorast** 将 PNM 图像转换为 Sun Rasterfile 格式。属于 Netpbm 工具集。

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

[rasttopnm](/man/rasttopnm)(1), [pnmtoxwd](/man/pnmtoxwd)(1)
