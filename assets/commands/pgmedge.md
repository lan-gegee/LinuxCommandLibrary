# TAGLINE

使用 Sobel 边缘检测算法检测 PGM 灰度图像中的边缘

# TLDR

**检测图像边缘**

```pgmedge [input.pgm] > [output.pgm]```

**处理其他格式**

```jpegtopnm [image.jpg] | ppmtopgm | pgmedge > [edges.pgm]```

**与格式转换串联使用**

```pgmedge [input.pgm] | pnmtopng > [edges.png]```

# SYNOPSIS

**pgmedge** [_pgmfile_]

# PARAMETERS

**pgmfile**
> 输入的 PGM 文件。未指定时使用 stdin。

# DESCRIPTION

**pgmedge** 使用 Sobel 边缘检测算法检测 PGM 灰度图像中的边缘。输出是一幅 PGM 图像，其中明亮的像素表示强边缘。

该算法使用 Sobel 核计算图像的水平梯度和垂直梯度并将其组合，为每个像素生成一个与局部梯度幅值成正比的强度值。

# CAVEATS

输入必须是灰度 PGM。请先用 **ppmtopgm** 转换彩色图像。**pgmedge** 是旧版工具——**pamedge** 提供更多选项，包括阈值化和方向输出。

# HISTORY

pgmedge 是由 **Jef Poskanzer** 及众多贡献者开发的 **Netpbm** 的一部分，实现了经典的图像处理算法。

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

[pamedge](/man/pamedge)(1), [pgmenhance](/man/pgmenhance)(1), [ppmtopgm](/man/ppmtopgm)(1), [netpbm](/man/netpbm)(1)
