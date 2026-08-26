# TAGLINE

Data Matrix 条码解码器

# TLDR

**从图片读取 Data Matrix 条码**

```dmtxread [image.png]```

**从多张图片读取**

```dmtxread [image1.png] [image2.png]```

**以详细模式输出**

```dmtxread -v [image.png]```

**设置扫描超时**（毫秒）

```dmtxread -m [5000] [image.png]```

**解码 N 个条码后停止**

```dmtxread -N [1] [image.png]```

**输出以换行分隔**（适用于多个条码）

```dmtxread -n [image.png]```

**从摄像头读取**（配合其他工具）

```fswebcam -r 640x480 - | dmtxread```

# SYNOPSIS

**dmtxread** [_options_] _image_...

# PARAMETERS

**-v**, **--verbose**
> 详细输出，显示扫描进度。

**-n**, **--newline**
> 每个解码消息后打印换行符。

**-m**, **--milliseconds** _ms_
> 最大扫描时间（毫秒）。

**-N**, **--stop-after** _n_
> 解码 n 个条码后停止。

**-c**, **--codewords**
> 打印码字而非解码后的消息。

**-e**, **--min-edge** _pixels_
> 考虑的最小边长。

**-E**, **--max-edge** _pixels_
> 考虑的最大边长。

# DESCRIPTION

**dmtxread** 从图像文件中解码 Data Matrix 条码。Data Matrix 是一种二维条码格式，常用于小件物品标识、电子产品和工业领域，适合在极小空间内存储高密度数据。

该工具支持多种图像格式（PNG、JPEG、TIFF 等）并搜索 Data Matrix 图案。单张图片中可检测到多个条码。解码后的文本输出到 stdout。

dmtxread 属于 **libdmtx** 库，该库提供 Data Matrix 编码和解码功能，并处理 Data Matrix 格式内置的纠错机制。

# CAVEATS

图像质量对检测成功率影响很大。过小、模糊或受损的条码可能无法解码。处理高分辨率图像可能较慢；使用区域限定可获得更好性能。仅支持 Data Matrix 格式，不支持 QR 码。

# HISTORY

**libdmtx** 及其工具由 **Mike Laughton** 创建，于 **2006 年**首次发布。该库提供开源的 Data Matrix 条码支持，填补了当时大多数实现均为专有软件的空白。Data Matrix 本身由 **RVSI Acuity CiMatrix** 于 **1987 年**发明，现已成为 ISO 标准。

# INSTALL

```apt: sudo apt install dmtx-utils```

```dnf: sudo dnf install dmtx-utils```

```brew: brew install dmtx-utils```

```nix: nix profile install nixpkgs#dmtx-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dmtxwrite](/man/dmtxwrite)(1), [zbarimg](/man/zbarimg)(1), [qrencode](/man/qrencode)(1)
