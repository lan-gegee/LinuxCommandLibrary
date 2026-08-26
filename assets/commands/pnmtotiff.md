# TAGLINE

将 PNM 图像转换为 TIFF 格式

# TLDR

**将 PNM 转换为 TIFF**

```pnmtotiff [input.pnm] > [output.tiff]```

**使用 LZW 压缩转换**

```pnmtotiff -lzw [input.pnm] > [output.tiff]```

**使用 JPEG 压缩转换**

```pnmtotiff -jpeg [input.pnm] > [output.tiff]```

**创建多页 TIFF**

```pnmtotiff -append [input.pnm] >> [output.tiff]```

# SYNOPSIS

**pnmtotiff** [_options_] [_file_]

# PARAMETERS

**-none**
> 不压缩。

**-lzw**
> LZW 压缩。

**-jpeg**
> JPEG 压缩。

**-packbits**
> PackBits 压缩。

**-g3**
> Group 3 传真压缩。

**-append**
> 追加到现有 TIFF 文件。

**-resolution** _dpi_
> 设置分辨率。

# DESCRIPTION

**pnmtotiff** 将 PNM 图像转换为 TIFF（Tagged Image File Format），这种格式广泛用于高质量图像存储和打印工作流。它支持多种压缩方法，包括 LZW、JPEG、PackBits 和 Group 3 传真编码。

**-append** 选项可以把图像追加到现有文件，从而构建多页 TIFF。**-resolution** 选项嵌入 DPI 元数据以确定打印尺寸。属于 Netpbm 工具集；已被 **pamtotiff** 取代。

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

[tifftopnm](/man/tifftopnm)(1), [pnmtojpeg](/man/pnmtojpeg)(1)
