# TAGLINE

将 MicroDesign Area 格式转换为 PBM

# TLDR

**将** MicroDesign area 转换为 PBM 并输出到 stdout

```mdatopbm [input.mda] > [output.pbm]```

**从 stdin 读取**并将 PBM 写到 stdout

```cat [input.mda] | mdatopbm > [output.pbm]```

**双倍高度**输出（针对非正方形的 PCW 像素）

```mdatopbm -d [input.mda] > [output.pbm]```

**反转**输出中的黑/白

```mdatopbm -i [input.mda] > [output.pbm]```

# SYNOPSIS

**mdatopbm** [**-d**] [**-i**] [_mdafile_]

# PARAMETERS

**-d**, **-double**
> 将图像高度加倍，以补偿 Amstrad PCW 屏幕的矩形像素宽高比。

**-i**, **-invert**
> 交换前景色与背景色，产生黑底白字的输出。

_mdafile_
> 输入的 MicroDesign Area (.mda) 文件。省略时从标准输入读取。

# DESCRIPTION

**mdatopbm** 将 MicroDesign Area 文件转换为 PBM。MicroDesign 是 Amstrad PCW 系列计算机上的桌面出版程序，其 .mda 文件以 PCW 的非正方形像素比例存储位图剪贴画。**-d** 选项将垂直分辨率加倍，使图像在正方形像素显示器上以正确比例显示。

输出写入标准输出。该工具是 **Netpbm** 工具集的一部分。

# CAVEATS

仅支持 MicroDesign Area (.mda) 变体；MicroDesign Plus 的文档可能需要先导出为 .mda。该格式为单色（1 bpp）。

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

[pbmtomda](/man/pbmtomda)(1), [pbmtolj](/man/pbmtolj)(1), [pbm](/man/pbm)(5)
