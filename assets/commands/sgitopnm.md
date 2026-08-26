# TAGLINE

将 SGI 图像转换为 PNM 格式

# TLDR

**将 SGI 图像转换为 PNM**

```sgitopnm [input.rgb] > [output.pnm]```

**提取特定通道**（0=红，1=绿，2=蓝）

```sgitopnm -channel [0] [input.rgb] > [output.pgm]```

**转换并显示详细输出**，展示图像信息

```sgitopnm -verbose [input.rgb] > [output.pnm]```

# SYNOPSIS

**sgitopnm** [_options_] [_file_]

# PARAMETERS

**-channel** _n_
> 提取特定通道（0=红，1=绿，2=蓝）。

**-verbose**
> 打印图像信息。

# DESCRIPTION

**sgitopnm** 将 Silicon Graphics 图像格式（SGI RGB）转换为 PNM（Portable aNyMap）。SGI 图像通常使用 .rgb、.rgba 或 .bw 扩展名。单通道图像输出 PGM；多通道图像输出 PPM。属于 Netpbm 工具集的一部分。

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

[pnmtosgi](/man/pnmtosgi)(1), [rletopnm](/man/rletopnm)(1)
