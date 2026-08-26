# TAGLINE

将 IFF ILBM 文件转换为 PPM 图像

# TLDR

**将 ILBM 文件转换为 PPM**

```ilbmtoppm [file.ilbm] > [output.ppm]```

**从 stdin 转换**

```cat [file.ilbm] | ilbmtoppm > [output.ppm]```

**只转换颜色映射，不转换图像本身**

```ilbmtoppm -cmaponly [file.ilbm] > [output.ppm]```

**带详细输出进行转换**

```ilbmtoppm -verbose [file.ilbm] > [output.ppm]```

**强制按 HAM 格式解析**

```ilbmtoppm -isham [file.ilbm] > [output.ppm]```

# SYNOPSIS

**ilbmtoppm** [_options_] [_ilbmfile_]

# PARAMETERS

**-verbose**
> 转换过程中显示关于 ILBM 文件的信息。

**-ignore** _chunkID_
> 处理时跳过指定的 4 字母 IFF 块（chunk）。

**-isham**
> 将输入视为 HAM（Hold-And-Modify）图片，即使 CAMG 块并未如此标示。

**-isnotham**
> 不将输入视为 HAM，即使 CAMG 块如此标示。

**-isehb**
> 将输入视为 Extra_Halfbrite（EHB），即使 CAMG 块中未标示。

**-isnotehb**
> 不将输入视为 EHB。

**-isdeep**
> 将输入视为深色（直接颜色）图像。

**-isnotdeep**
> 不将输入视为深色图像。

**-cmaponly**
> 只输出颜色映射的 PPM，而不是图像本身。

**-adjustcolors**
> 将颜色映射缩放到每通道 8 位。

**-transparent** _color_
> 设置透明色。

**-maskfile** _filename_
> 将透明掩码写入指定的 PBM 文件。

# DESCRIPTION

**ilbmtoppm** 将 IFF ILBM（Interleaved Bitmap，交错位图）文件转换为 PPM（Portable Pixmap）格式。ILBM 是 Amiga 计算机上的标准图像格式。

该程序支持 1-16 位平面的普通 ILBM、Amiga Extra_Halfbrite（EHB）、3-16 位平面的 Amiga HAM、多调色板图片（普通或 HAM）、仅颜色映射的图像，以及非官方的直接颜色格式。它是 **Netpbm** 图像处理工具集的一部分。

# CAVEATS

某些 ILBM 文件使用非标准或非官方扩展，可能无法被正确自动检测。当自动检测失败时，使用 **-isham**、**-isehb** 或 **-isdeep** 标志强制采用正确的解析方式。

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

[ppmtoilbm](/man/ppmtoilbm)(1), [netpbm](/man/netpbm)(1)

