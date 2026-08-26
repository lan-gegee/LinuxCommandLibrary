# TAGLINE

Epson ESC/P2 到 PBM 格式的转换器

# TLDR

**将 ESCP2 转换为 PBM**

```escp2topbm < [input.escp2] > [output.pbm]```

# SYNOPSIS

**escp2topbm** [_escp2file_]

# DESCRIPTION

**escp2topbm** 读取 Epson ESC/P2 打印机数据流，并将其中的图形作为 PBM（Portable Bitmap）图像写到标准输出。如果未指定文件，则从标准输入读取。它是 Netpbm 图像处理工具集的一部分。

ESC/P2 是 Epson 增强型打印机控制语言，广泛用于点阵打印机和喷墨打印机。escp2topbm 会提取此类数据流中嵌入的位图光栅数据，让你能够恢复或查看本应被打印出来的图像。它本质上是 pbmtoepson 的逆操作。

# PARAMETERS

escp2topbm 自身不定义任何选项；它接受所有 Netpbm 程序通用的选项，例如 **-plain** 和 **-quiet**（在 Netpbm 10.72 之前，通用的 **-plain** 选项不起作用）。

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

[pbmtoescp2](/man/pbmtoescp2)(1), [pbmtoepson](/man/pbmtoepson)(1), [pnmtopng](/man/pnmtopng)(1)

# RESOURCES

```[Source code](https://sourceforge.net/p/netpbm/code/HEAD/tree/)```

```[Homepage](https://netpbm.sourceforge.net/)```

```[Documentation](https://netpbm.sourceforge.net/doc/escp2topbm.html)```

<!-- verified: 2026-07-14 -->
