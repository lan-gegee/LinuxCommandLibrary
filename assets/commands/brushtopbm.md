# TAGLINE

将 deskjet 笔刷文件转换为 PBM 图像

# TLDR

将 **deskjet 笔刷文件**转换为 PBM

```brushtopbm [brushfile] > [output.pbm]```

从标准输入**转换**

```cat [brushfile] | brushtopbm > [output.pbm]```

通过管道将笔刷**转换为 PNG**

```brushtopbm [brushfile] | pnmtopng > [output.png]```

# SYNOPSIS

**brushtopbm** [_brushfile_]

# DESCRIPTION

**brushtopbm** 读取一个 deskjet 笔刷文件并输出 PBM（Portable BitMap）图像。它是 Netpbm 图像处理工具集的一部分。

笔刷文件曾被某些 HP DeskJet 打印机实用程序用于自定义笔刷图案。该转换器可将这些图案提取为标准位图图像。

未指定文件时，程序从标准输入读取。输出写入标准输出。

# CAVEATS

该工具处理的是一种特定的遗留格式。现代系统已很少使用笔刷文件格式。输出为单色 PBM；如需彩色输出，请用其他 Netpbm 工具转换。

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

[pbmtogo](/man/pbmtogo)(1), [pnmtopng](/man/pnmtopng)(1), [netpbm](/man/netpbm)(1)

# RESOURCES

```[Homepage](https://netpbm.sourceforge.net/)```

<!-- verified: 2026-06-22 -->
