# TAGLINE

将 BMP 图像转换为 PNM 格式

# TLDR

**将 BMP 图像转换**为 PNM 格式

```bmptopnm [image.bmp] > [output.pnm]```

**从 stdin 转换**到 stdout

```cat [image.bmp] | bmptopnm > [output.pnm]```

通过管道**将 BMP 转换为 PNG**

```bmptopnm [image.bmp] | pnmtopng > [output.png]```

# SYNOPSIS

**bmptopnm** [**-verbose**] [_bmpfile_]

# PARAMETERS

**-verbose**
> 输出关于输入文件的额外信息。

# DESCRIPTION

**bmptopnm** 读取 Microsoft Windows 或 OS/2 的 BMP 文件作为输入，并输出 PNM（Portable aNyMap）图像。输出格式（PBM、PGM 或 PPM）取决于输入内容：灰度图像生成 PGM，彩色图像生成 PPM，单色图像生成 PBM。

它是 Netpbm 图像处理实用工具包的一部分。输入可以来自文件或标准输入；输出到标准输出。

# CAVEATS

某些 BMP 变体可能不受完全支持。对于压缩的 BMP 文件，RLE 编码的图像会自动解压。非常老旧或非标准的 BMP 格式可能导致错误。

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

[bmptoppm](/man/bmptoppm)(1), [pnmtopng](/man/pnmtopng)(1), [netpbm](/man/netpbm)(1)
