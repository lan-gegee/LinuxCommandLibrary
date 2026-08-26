# TAGLINE

把天文 FITS 图像转换为 PNM

# TLDR

**将 FITS 转换为 PNM**

```fitstopnm [input.fits] > [output.pnm]```

**转换文件中的指定图像**

```fitstopnm -image [2] [input.fits] > [output.pnm]```

# SYNOPSIS

**fitstopnm** [_options_] [_file_]

# PARAMETERS

**-image** _num_
> 从多图像文件中选择指定的图像。

**-noraw**
> 以纯文本格式输出。

# DESCRIPTION

**fitstopnm** 将 FITS（Flexible Image Transport System）文件转换为 PNM 格式。FITS 是天文学界用于科学数据交换的标准图像格式。

该工具从 FITS 文件读取多维图像数据，并将其转换为 portable anymap 格式，使天文图像可以被标准图像处理工具使用。它是 Netpbm 工具集的一部分。

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

[pnmtofits](/man/pnmtofits)(1), [pamtofits](/man/pamtofits)(1)

# RESOURCES

```[Homepage](https://netpbm.sourceforge.net/)```

<!-- verified: 2026-07-15 -->
