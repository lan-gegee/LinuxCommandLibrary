# TAGLINE

通过颜色量化实现有损 PNG 压缩

# TLDR

**在指定质量范围内压缩 PNG**

```pngquant --quality=[65-80] [image.png]```

**压缩到指定输出文件**

```pngquant [image.png] -o [output.png]```

**压缩并覆盖原文件**

```pngquant --ext=.png --force [image.png]```

**以指定颜色数压缩**

```pngquant [256] [image.png]```

**压缩多个文件**

```pngquant [*.png]```

**以最高质量压缩**

```pngquant --quality=[90-100] [image.png]```

**无法满足质量要求时跳过**

```pngquant --skip-if-larger [image.png]```

**输出到标准输出**（便于管道）

```pngquant - < [input.png] > [output.png]```

# SYNOPSIS

**pngquant** [_--quality min-max_] [_--speed N_] [_--output file_] [_--ext suffix_] [_colors_] _files_

# PARAMETERS

**--quality** _MIN_-_MAX_
> 质量范围（0-100）。若质量低于 MIN 则跳过。

**-o**, **--output** _FILE_
> 输出文件名。

**--ext** _SUFFIX_
> 设置输出文件名后缀（默认：视是否抖动而为 -or8.png 或 -fs8.png）。

**-f**, **--force**
> 覆盖已存在的文件。

**-s** _N_, **--speed** _N_
> 速度/质量权衡（1=最慢/最好，10=最快；默认 3）。

**--skip-if-larger**
> 若输出大于输入则不写入。

**--strip**
> 移除元数据。

**--posterize** _BITS_
> 降低颜色通道的精度。

**--nofs**
> 禁用 Floyd-Steinberg 抖动。

**--floyd**=_LEVEL_
> 设置抖动强度（0.0-1.0）。

**-v**, **--verbose**
> 详细输出。

**-**
> 从标准输入读取，写入标准输出。

_NUM_
> 最大颜色数（默认：256）。

# DESCRIPTION

**pngquant** 通过有损量化减少颜色数量来压缩 PNG 图像。它把 24/32 位 PNG 转换为 8 位调色板 PNG，在保持视觉质量的同时大幅减小文件体积。

该算法采用中位切分量化并配合抖动来掩盖减色产生的瑕疵。质量设置控制减色的激进程度——质量越高保留的细节越多，但生成的文件也越大。

质量范围（例如 65-80）设定可接受的最低质量。若达不到最低值，pngquant 会直接退出且不写入文件（退出码 99），以此避免生成画质不可接受的图像。

速度设置是用处理时间换取输出质量。较慢的速度能找到更好的调色板。对于自动化流水线，中等速度（3-4）是比较理想的平衡点。

该工具尤其擅长压缩图形、图标以及颜色数量有限的图像。受 256 色上限限制，照片可能出现更明显的画质损失。

# CAVEATS

有损压缩——会损失部分画质。256 色的上限对复杂图像是一种限制。照片可能得不到好的压缩效果。原始透明度会保留，但会被降为 8 位。默认剥离元数据。结果因图像内容不同而有明显差异。

# HISTORY

**pngquant** 由 **Greg Roelofs** 于 **1997 年**前后伴随最初的 PNG 规范工作创建。该项目后来由 **Kornel Lesinski** 接手，他于 **2011 年**前后基于 libimagequant 库重写了它。如今它已成为 Web 优化的关键工具，被构建工具和图片 CDN 用来节省带宽。

# INSTALL

```apt: sudo apt install pngquant```

```dnf: sudo dnf install pngquant```

```pacman: sudo pacman -S pngquant```

```apk: sudo apk add pngquant```

```zypper: sudo zypper install pngquant```

```brew: brew install pngquant```

```nix: nix profile install nixpkgs#pngquant```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[optipng](/man/optipng)(1), [oxipng](/man/oxipng)(1), [imagemagick](/man/imagemagick)(1), [jpegoptim](/man/jpegoptim)(1)
