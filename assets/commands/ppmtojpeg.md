# TAGLINE

将 PPM 图像转换为 JPEG 格式

# TLDR

**将 PPM 转换为 JPEG**

```ppmtojpeg [input.ppm] > [output.jpg]```

**以指定质量转换**（默认：75）

```ppmtojpeg -quality [90] [input.ppm] > [output.jpg]```

**创建渐进式 JPEG**

```ppmtojpeg -progressive [input.ppm] > [output.jpg]```

**以优化的霍夫曼编码转换**

```ppmtojpeg -optimize [input.ppm] > [output.jpg]```

**转换为灰度输出**

```ppmtojpeg -grayscale [input.ppm] > [output.jpg]```

# SYNOPSIS

**ppmtojpeg** [_options_] [_file_]

# PARAMETERS

**-quality** _n_
> JPEG 质量因子（0-100，默认：75）。值越高质量越好，但文件也越大。

**-progressive**
> 创建渐进式 JPEG（分多遍加载）。

**-optimize**
> 优化霍夫曼编码表以获得更小的文件体积，代价是压缩速度更慢。

**-grayscale**
> 无论输入是否为彩色，都创建灰度 JPEG。

**-density** _DPI_
> 以每英寸点数设置像素密度。

**-smooth** _n_
> 平滑输入图像（1-100），以减少抖动伪影。

# DESCRIPTION

**ppmtojpeg** 将 PPM（Portable Pixel Map）图像转换为 JPEG/JFIF 格式。它是 **pnmtojpeg** 的别名，属于 Netpbm 工具集。该命令从文件或 stdin 读取数据，并将 JPEG 数据写到 stdout。

默认质量 75 在文件大小和视觉质量之间提供了良好的平衡。高于 95 的值对质量的提升微乎其微，却会显著增大文件体积。

# CAVEATS

输出写到 stdout，必须重定向到文件。JPEG 是有损格式；在 PPM 和 JPEG 之间来回转换会损失质量。**-optimize** 标志会增加编码时间，但通常可将文件大小减少 5-10%。

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

[pnmtojpeg](/man/pnmtojpeg)(1), [jpegtopnm](/man/jpegtopnm)(1), [cjpeg](/man/cjpeg)(1), [netpbm](/man/netpbm)(1)
