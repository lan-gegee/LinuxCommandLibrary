# TAGLINE

将 BMP 图像转换为 PPM 格式

# TLDR

**将 BMP 图像转换**为 PPM 格式

```bmptoppm [image.bmp] > [output.ppm]```

**从 stdin 转换**

```cat [image.bmp] | bmptoppm > [output.ppm]```

通过管道**将 BMP 转换为 JPEG**

```bmptoppm [image.bmp] | pnmtojpeg > [output.jpg]```

# SYNOPSIS

**bmptoppm** [_bmpfile_]

# DESCRIPTION

**bmptoppm** 读取 Microsoft Windows 或 OS/2 的 BMP 文件作为输入，并输出 PPM（Portable PixMap）彩色图像。它是 Netpbm 软件包的一部分。

该命令在 Netpbm 9.25（**2002 年 3 月**）中被 **bmptopnm** 取代，后者根据输入图像的特征自动确定合适的输出格式（PBM、PGM 或 PPM）。**bmptoppm** 仅出于向后兼容的目的而保留，本身不接受任何选项。

输入可以来自文件或标准输入；输出到标准输出。

# CAVEATS

对于灰度 BMP 图像，建议改用 **bmptopnm**，它会输出更合适的 PGM 格式。无论输入颜色深度如何，此命令总是输出 PPM。

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

[bmptopnm](/man/bmptopnm)(1), [ppmtobmp](/man/ppmtobmp)(1), [pnmtojpeg](/man/pnmtojpeg)(1), [netpbm](/man/netpbm)(1)

# RESOURCES

```[Homepage](https://netpbm.sourceforge.net/)```

```[Documentation](https://netpbm.sourceforge.net/doc/bmptoppm.html)```

<!-- verified: 2026-06-19 -->
