# TAGLINE

将 PNM 图像转换为 Palm 图像格式

# TLDR

**将 PNM 转换为 Palm 图像**

```pnmtopalm [input.pnm] > [output.palm]```

**指定颜色深度**

```pnmtopalm -depth [8] [input.pnm] > [output.palm]```

**使用自定义调色板**

```pnmtopalm -colormap [input.pnm] > [output.palm]```

**把某种颜色标记为透明**

```pnmtopalm -transparent [rgb:ff/ff/ff] [input.pnm] > [output.palm]```

**应用扫描行压缩**

```pnmtopalm -scanline_compression [input.pnm] > [output.palm]```

# SYNOPSIS

**pnmtopalm** [_options_] [_pnmfile_]

# PARAMETERS

**-depth** _n_
> 输出的每像素位数：1、2、4、8 或 16。灰度输入最多只能用 4 位。

**-maxdepth** _n_
> 生成不超过 _n_ 位的最小位深输出。设为 16 会强制直接色输出。

**-colormap**
> 构建自定义调色板并嵌入输出中。效率低于默认的 Palm 调色板。

**-transparent** _colorspec_
> 将某一种颜色标记为完全透明（Palm OS 3.5+）。

**-density** _n_
> Palm Bitmap 密度。有效值为 72、108、144、216 或 288。

**-offset**
> 设置 `nextDepthOffset` 字段并填充到 4 字节边界，使多个图像版本可以串联在一起。

**-withdummy**
> 在图像之后插入一个占位图像头，让后续的高密度版本仍能被旧版解释器读取。需要配合 **-offset** 使用。

**-scanline_compression**
> 使用 Palm 扫描行压缩（Palm OS 2.0+）。

**-rle_compression**
> 使用 Palm RLE 压缩（Palm OS 3.5+）。

**-packbits_compression**
> 使用 Palm packbits 压缩（Palm OS 4.0+）。与 16 位直接色不兼容。

**-verbose**
> 打印输出文件的格式信息。

# DESCRIPTION

**pnmtopalm** 将 PNM 图像转换为 Palm Pilot 位图格式。它是 Netpbm 工具集的一部分。逆转换由 **palmtopnm** 完成。

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

[palmtopnm](/man/palmtopnm)(1), [pnmtopng](/man/pnmtopng)(1)
