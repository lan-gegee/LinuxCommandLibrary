# TAGLINE

将 HP PaintJet 格式转换为 PPM

# TLDR

**将 HP PaintJet 文件转换为 PPM**

```pjtoppm [input.pj] > [output.ppm]```

**从 stdin 读取 PaintJet 数据**

```cat [input.pj] | pjtoppm > [output.ppm]```

**管道传给另一个 Netpbm 工具**（例如经 pnmtopng 转为 PNG）

```pjtoppm [input.pj] | pnmtopng > [output.png]```

# SYNOPSIS

**pjtoppm** [_paintjetfile_]

# DESCRIPTION

**pjtoppm** 读取 HP PaintJet 打印机文件，并将 PPM（Portable Pixmap）图像写入标准输出。若未给出文件名，则从 stdin 读取输入。

它是一个快速实现，仅处理解码大多数光栅图像所需的 PaintJet 转义序列子集，并不是完整的 PCL 解释器。生成的 PPM 可以由 Netpbm 工具链的其余部分（例如 **pnmtopng** 或 **pnmtojpeg**）转换为其他格式。

# CAVEATS

仅支持有限的 PaintJet 命令子集，因此复杂的 PCL 文档可能无法正确转换。除可选的输入文件外没有任何命令行选项。**ppmtopj** 执行相反方向的转换。

# HISTORY

**pjtoppm** 由 Christos Zoulas 于 1991 年编写，此后一直随 **Netpbm** 软件包发布。其实现参考了 HP PaintJet XL 彩色图形打印机用户指南。

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

[ppmtopj](/man/ppmtopj)(1), [pcxtoppm](/man/pcxtoppm)(1), [pnmtops](/man/pnmtops)(1)
