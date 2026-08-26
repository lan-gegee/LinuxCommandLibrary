# TAGLINE

将 Solitaire 图像记录器文件转换为 PNM 格式

# TLDR

将 Solitaire 图像转换为 PNM

```sirtopnm [input.sir] > [output.pnm]```

转换并通过管道交给 PNG 编码器

```sirtopnm [input.sir] | pnmtopng > [output.png]```

# SYNOPSIS

**sirtopnm** [_sirfile_]

# DESCRIPTION

**sirtopnm** 读取 Solitaire Image Recorder 文件（`.sir`）作为输入，并在标准输出上生成 PNM（Portable Any Map）图像。Solitaire Image Recorder 是一种高分辨率胶片记录仪，用于将数字图像制作成幻灯片和透明胶片。

未指定输入文件时，**sirtopnm** 从标准输入读取。输出格式（PBM、PGM 或 PPM）取决于输入图像的内容。

该工具是 **Netpbm** 工具集的一部分，这是一组用于在各种图像格式之间相互转换的图像处理实用程序。

# PARAMETERS

_sirfile_
> 要转换的 Solitaire Image Recorder 文件路径。省略时从标准输入读取。

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

[pnmtosir](/man/pnmtosir)(1), [sgitopnm](/man/sgitopnm)(1), [anytopnm](/man/anytopnm)(1), [pnmtopng](/man/pnmtopng)(1), [pnmtojpeg](/man/pnmtojpeg)(1)
