# TAGLINE

显示 PNM 图像文件的信息

# TLDR

**显示图像信息**

```pnmfile [image.pnm]```

**显示多个文件的信息**

```pnmfile [file1.pnm] [file2.pnm]```

**机器可读输出**

```pnmfile -machine [image.pnm]```

# SYNOPSIS

**pnmfile** [_options_] [_files_]

# PARAMETERS

_FILES_
> 输入的 PNM 文件。

**-machine**
> 机器可读的输出格式，以空格分隔打印类型、宽度、高度、深度和 maxval。

# DESCRIPTION

**pnmfile** 显示 PNM 图像文件的相关信息，包括格式类型（PBM、PGM 或 PPM）、尺寸（宽和高）、最大采样值，以及文件使用 ASCII（plain）编码还是二进制（raw）编码。

**-machine** 标志以适合脚本处理的易解析格式输出。属于 Netpbm 工具集；已被 **pamfile** 取代，后者还能处理 PAM 格式文件。

# CAVEATS

只能读取 PNM 格式文件（PBM、PGM、PPM）。要处理 PAM 文件请改用 **pamfile**。

# HISTORY

**pnmfile** 作为 **Netpbm** 工具集的一部分创建，用于检查图像信息。如今在很大程度上已被 **pamfile** 取代。

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

[pamfile](/man/pamfile)(1), [file](/man/file)(1), [identify](/man/identify)(1), [pnmtopng](/man/pnmtopng)(1), [pnmtojpeg](/man/pnmtojpeg)(1)
