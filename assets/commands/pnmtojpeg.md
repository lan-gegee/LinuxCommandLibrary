# TAGLINE

将 PNM 图像转换为 JPEG 格式

# TLDR

**将 PNM 转换为 JPEG**

```pnmtojpeg [input.pnm] > [output.jpg]```

**以指定质量转换**

```pnmtojpeg -quality [85] [input.pnm] > [output.jpg]```

**创建渐进式 JPEG**

```pnmtojpeg -progressive [input.pnm] > [output.jpg]```

**优化霍夫曼表**

```pnmtojpeg -optimize [input.pnm] > [output.jpg]```

# SYNOPSIS

**pnmtojpeg** [_options_] [_file_]

# PARAMETERS

**-quality** _n_
> 质量（0-100，默认 75）。

**-progressive**
> 创建渐进式 JPEG。

**-optimize**
> 优化霍夫曼表。

**-grayscale**
> 强制输出灰度图像。

**-baseline**
> 强制输出基线（baseline）JPEG。

# DESCRIPTION

**pnmtojpeg** 将 PNM（PBM、PGM、PPM）图像转换为 JPEG/JFIF 格式。**-quality** 选项控制压缩率与画质之间的权衡，值越高生成的文件越大，但图像质量更好。

**-progressive** 选项创建渐进式 JPEG，加载时会逐步呈现更多细节。**-optimize** 标志通过计算最优的霍夫曼编码表来减小文件体积。**-grayscale** 选项强制输出单通道图像，即使输入是彩色图。属于 Netpbm 工具集。

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

[jpegtopnm](/man/jpegtopnm)(1), [pnmtopng](/man/pnmtopng)(1)
