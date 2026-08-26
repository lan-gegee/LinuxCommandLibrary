# TAGLINE

Gould 扫描仪文件转 PPM 转换器

# TLDR

**将 Gould 扫描仪文件转换为 PPM**

```gouldtoppm [file.gould] > [output.ppm]```

**从标准输入转换**

```cat [file.gould] | gouldtoppm > [output.ppm]```

# SYNOPSIS

**gouldtoppm** [_gouldfile_]

# DESCRIPTION

**gouldtoppm** 读取由 Gould 扫描仪生成的文件并将其转换为 PPM（Portable Pixmap）格式。它是 Netpbm 图像处理工具集的一部分。

该命令从文件参数或标准输入读取数据，并将 PPM 输出写入标准输出。

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

[ppmtogif](/man/ppmtogif)(1), [pnmtopng](/man/pnmtopng)(1), [netpbm](/man/netpbm)(1)

# RESOURCES

```[Homepage](https://netpbm.sourceforge.net/)```

```[Documentation](https://netpbm.sourceforge.net/doc/gouldtoppm.html)```

<!-- verified: 2026-07-17 -->
