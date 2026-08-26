# TAGLINE

将原始灰度数据转换为 PGM 格式

# TLDR

**将原始灰度数据转换为 PGM**

```rawtopgm [width] [height] [input.raw] > [output.pgm]```

**转换时跳过头部字节**

```rawtopgm -headerskip [512] [width] [height] [input.raw] > [output.pgm]```

# SYNOPSIS

**rawtopgm** [_options_] _width_ _height_ [_file_]

# PARAMETERS

_width_
> 图像宽度（像素）。

_height_
> 图像高度（像素）。

**-headerskip** _BYTES_
> 在读取像素数据前跳过输入开头的 _BYTES_ 个字节（用于带专有头部的文件）。

**-rowskip** _BYTES_
> 跳过每条扫描线末尾的 _BYTES_ 个字节（例如行步长填充）。

**-bpp** _N_
> 每像素字节数：_1_（默认，8 位）或 _2_（16 位大端采样）。

**-littleendian**
> 当使用 **-bpp 2** 时，将 16 位采样按小端解释。

**-maxval** _N_
> 覆盖写入输出 PGM 的最大灰度值（默认 _255_；使用 **-bpp 2** 时为 _65535_）。

**-topbottom**
> 将第 0 行视为图像顶部（默认行为；配合 **-bottomtop** 可翻转）。

**-bottomtop**
> 将第 0 行视为图像底部。

# DESCRIPTION

**rawtopgm** 将原始灰度字节数据转换为便携式灰度图（PGM）格式，它按照指定的图像尺寸来解释像素值流。由于原始数据不包含元数据，必须以参数形式提供宽度和高度，工具才能知道如何把这些字节排列成正确的图像网格。

**-headerskip** 选项允许跳过位于实际像素数据之前的文件头部，**-bpp** 则用于处理高动态范围图像的 16 位采样。该命令属于 Netpbm 图像处理工具集。

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

[rawtoppm](/man/rawtoppm)(1), [pgmtopbm](/man/pgmtopbm)(1)
