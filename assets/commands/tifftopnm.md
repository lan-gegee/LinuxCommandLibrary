# TAGLINE

将 TIFF 图像转换为 PNM 格式

# TLDR

**将 TIFF 转换为 PNM**

```tifftopnm [input.tiff] > [output.pnm]```

**转换指定页**

```tifftopnm -page [2] [input.tiff] > [output.pnm]```

**列出 TIFF 中的页面**

```tifftopnm -headerdump [input.tiff]```

# SYNOPSIS

**tifftopnm** [_options_] [_file_]

# PARAMETERS

**-page** _n_
> 提取指定页。

**-headerdump**
> 转储 TIFF 头信息。

**-alphaout** _file_
> 将 alpha 通道写入文件。

**-respectfillorder**
> 遵循 fill order 标签。

# DESCRIPTION

**tifftopnm** 将 TIFF 图像转换为 PNM 格式。是 Netpbm 工具包的一部分。支持多页 TIFF 文件和 alpha 通道提取。

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

[pnmtotiff](/man/pnmtotiff)(1), [pngtopnm](/man/pngtopnm)(1)
