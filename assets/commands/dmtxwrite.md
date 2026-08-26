# TAGLINE

Data Matrix 条码编码器

# TLDR

**将文本编码为 Data Matrix 条码**

```echo "[text]" | dmtxwrite -o [output.png]```

**从文件内容创建条码**

```dmtxwrite -o [output.png] < [data.txt]```

**设置模块（单元格）大小（像素）**

```echo "[text]" | dmtxwrite -d [5] -o [output.png]```

**设置边距大小（像素）**

```echo "[text]" | dmtxwrite -m [10] -o [output.png]```

**创建 SVG 输出**

```echo "[text]" | dmtxwrite -o [output.svg]```

**使用指定的符号尺寸**

```echo "[text]" | dmtxwrite -s s -o [output.png]```

**打印码字列表而非条码图像**

```echo "[text]" | dmtxwrite -c```

**设置图像打印分辨率（DPI）**

```echo "[text]" | dmtxwrite -R [300] -o [output.png]```

# SYNOPSIS

**dmtxwrite** [_options_] [**-o** _output_]

# PARAMETERS

**-o**, **--output** _file_
> 输出文件名。默认为标准输出。

**-d**, **--module** _pixels_
> 模块（单元格）大小（像素）。

**-m**, **--margin** _pixels_
> 边距大小（像素）。

**-s**, **--symbol-size** _size_
> 符号尺寸：s（自动正方形）、r（自动矩形）或 RxC（如 24x24）。

**-e**, **--encoding** _scheme_
> 编码方案：b（最优）、a（ASCII）[默认]、c（40）、t（文本）、x（12）、e（EDIFACT）、8（Base 256）。

**-R**, **--resolution** _dpi_
> 图像打印分辨率（DPI）。

**-f**, **--format** _format_
> 输出格式：png [默认]、tif、gif、pdf、svg。

**-c**, **--codewords**
> 打印码字列表而不生成条码图像。

**-M**, **--mosaic**
> 创建非标准的 Data Mosaic 条码。

**-v**, **--verbose**
> 详细输出。

**-V**, **--version**
> 打印版本信息。

# DESCRIPTION

**dmtxwrite** 从输入的文本或二进制数据生成 Data Matrix 条码图像。Data Matrix 条码是二维的正方形或矩形图案，编码数据时自带纠错功能。

该工具从标准输入读取数据并生成各种格式的图像。符号尺寸会根据数据长度自动选择，也可以手动指定。纠错信息按照 Data Matrix 标准自动加入。

Data Matrix 条码广泛用于小件物品标识（电子元件、医疗器械）、物流等需要在狭小空间内存储高密度数据的场景。

# SYMBOL SIZES

**s**: 自动选择正方形尺寸
**r**: 自动选择矩形尺寸
**10x10** 至 **144x144**: 特定的正方形尺寸
**8x18** 至 **16x48**: 特定的矩形尺寸

# CAVEATS

数据容量取决于符号尺寸和编码方式；更大的符号可容纳更多数据。二进制数据的编码可能需要特定的编码方案。模块尺寸过小时可能难以可靠扫描。部分扫描仪难以识别矩形 Data Matrix 码。

# HISTORY

dmtxwrite 属于 **libdmtx**，由 **Mike Laughton** 于 **2006 年**创建。该库为 Data Matrix 条码的生成和读取提供开源工具。Data Matrix 是 ISO/IEC 16022 标准，最初为工业标识应用而开发。

# INSTALL

```apt: sudo apt install dmtx-utils```

```dnf: sudo dnf install dmtx-utils```

```brew: brew install dmtx-utils```

```nix: nix profile install nixpkgs#dmtx-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dmtxread](/man/dmtxread)(1), [qrencode](/man/qrencode)(1), [zint](/man/zint)(1)
