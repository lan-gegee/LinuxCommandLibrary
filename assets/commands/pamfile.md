# TAGLINE

显示图像文件信息

# TLDR

**显示图像信息**

```pamfile [image.pam]```

**机器可读输出**

```pamfile -machine [image.pam]```

**只显示图像尺寸**

```pamfile -size [image.pam]```

**统计多图像文件中的图像数量**

```pamfile -count [image.pam]```

**描述多图像文件中的所有图像**

```pamfile -allimages [image.pam]```

**显示多个文件**

```pamfile [image1.pam] [image2.pam]```

# SYNOPSIS

**pamfile** [**-allimages**] [**-comments**] [**-count**] [**-machine**] [**-size**] [_file_...]

# PARAMETERS

_FILE_
> 一个或多个 PAM/PNM 图像文件。未指定时从 stdin 读取。

**-allimages**
> 描述每个输入文件中的每一幅图像，而不只是第一幅。

**-comments**
> 包含 PAM 图像头部中的注释。

**-count**
> 只显示每个输入文件中有多少幅图像的计数。

**-machine**
> 机器可解析的输出。以空格分隔的字段报告格式、子格式、宽度、高度、深度、maxval 和元组类型，每幅图像一行。

**-size**
> 只输出图像的宽度和高度，以空格分隔。

# DESCRIPTION

**pamfile** 读取一个或多个 Netpbm 图像文件，输出关于图像类型、尺寸、深度、maxval 和格式的简短描述。支持 PAM、PBM、PGM 和 PPM 格式。属于 Netpbm 套件。

**-count**、**-machine** 和 **-size** 中最多只能指定一个。

# CAVEATS

**-comments** 选项仅对 PAM 图像有效；对于 PBM、PGM 或 PPM 图像，即使存在注释也不会报告。不使用 **-allimages** 时，每个文件只描述第一幅图像。

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

[pnmfile](/man/pnmfile)(1), [file](/man/file)(1), [netpbm](/man/netpbm)(1)
