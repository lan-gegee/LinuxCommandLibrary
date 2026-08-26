# TAGLINE

将 Sun 图标文件转换为 PBM 格式

# TLDR

**将图标转换为 PBM**

```icontopbm [file.icon] > [output.pbm]```

**从 stdin 转换**

```cat [file.icon] | icontopbm > [output.pbm]```

**转换并通过 Netpbm 工具管道输出**为 PNG

```icontopbm [file.icon] | pnmtopng > [output.png]```

# SYNOPSIS

**icontopbm** [_iconfile_]

# PARAMETERS

_iconfile_
> Sun 图标格式的输入文件。若未指定，则从标准输入读取。

# DESCRIPTION

**icontopbm** 将 Sun 图标文件转换为 PBM（Portable Bitmap，可移植位图）格式。Sun 图标文件是 Sun Microsystems 工作站历史上用于桌面图标的一种简单位图格式。输出以 PBM 格式写入标准输出，可通过管道传给其他 Netpbm 工具做进一步转换。

属于 Netpbm 图像处理工具集的一部分。

# CAVEATS

只能读取 Sun 图标格式的文件。该格式基本已过时，但处理遗留文件归档时可能仍需转换。

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

[pbmtoicon](/man/pbmtoicon)(1), [xbmtopbm](/man/xbmtopbm)(1), [netpbm](/man/netpbm)(1)

