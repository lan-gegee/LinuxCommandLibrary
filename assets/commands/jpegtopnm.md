# TAGLINE

将 JFIF/JPEG 图像转换为 Netpbm PNM 格式

# TLDR

**将 JPEG 转换为 PNM**

```jpegtopnm [image.jpg] > [image.pnm]```

**转换时提取 EXIF**

```jpegtopnm -exif=[exif.dat] [image.jpg] > [image.pnm]```

**修复损坏的 JPEG**

```jpegtopnm -repair [corrupted.jpg] > [output.pnm]```

**显示 JPEG 中的注释**

```jpegtopnm -comments [image.jpg] > /dev/null```

# SYNOPSIS

**jpegtopnm** [_options_] [_filename_]

# PARAMETERS

**-repair**
> 尝试从损坏的 JPEG 中抢救数据。

**-exif** _file_
> 将 EXIF 数据提取到文件。

**-comments**
> 打印 JPEG 文件中的注释。

**-dct** _method_
> DCT 方法：int、fast 或 float。

**-multiple**
> 从流中读取多张图像。

# DESCRIPTION

**jpegtopnm** 将 JFIF/JPEG 图像转换为 Netpbm PNM 格式。彩色图像输出 PPM，灰度图像输出 PGM。它属于 Netpbm 工具集，使用 Independent JPEG Group 的解码库。

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

[pnmtojpeg](/man/pnmtojpeg)(1), [djpeg](/man/djpeg)(1), [pamscale](/man/pamscale)(1)
