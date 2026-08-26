# TAGLINE

检测 PNG 和 BMP 图像中的隐写内容

# TLDR

**分析图像**

```zsteg [image.png]```

**检查所有通道**

```zsteg -a [image.png]```

**提取特定数据**

```zsteg -E "[b1,rgb,lsb]" [image.png]```

**详细输出**

```zsteg -v [image.png]```

**检查 BMP 文件**

```zsteg [image.bmp]```

**限制输出**

```zsteg --limit [1000] [image.png]```

# SYNOPSIS

**zsteg** [_-a_] [_-v_] [_-E extract_] [_options_] _image_

# PARAMETERS

**-a**, **--all**
> 检查所有方法。

**-v**, **--verbose**
> 详细输出。

**-E** _SPEC_
> 提取数据。

**--limit** _N_
> 输出数量限制。

**-o** _FILE_
> 输出文件。

**--bits** _BITS_
> 要检查的位。

**--order** _ORDER_
> 位顺序。

# DESCRIPTION

**zsteg** 用于检测并提取隐藏在 PNG 和 BMP 图像文件中的隐写数据。它分析多个颜色通道（RGB、alpha 及各个单色通道）在不同位深下的情况，以识别文本、嵌入文件和二进制模式等隐藏内容。

该工具主要聚焦 LSB（最低有效位）隐写术，即把数据藏进像素颜色值的最低有效位。**-a** 标志会对所有常见方法和通道组合进行全面检查，**-E** 标志则从指定的通道与位配置中提取数据。

zsteg 广泛用于 CTF（Capture The Flag）竞赛中的隐写题，以及对可疑图像文件的取证分析。它使用 Ruby 编写。

# CAVEATS

仅支持 PNG 和 BMP。可能出现误报。需要 Ruby 环境。

# HISTORY

**zsteg** 为 CTF 竞赛和隐写分析而创建。它能快速检测图像中隐藏的数据。

# INSTALL

```nix: nix profile install nixpkgs#zsteg```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[steghide](/man/steghide)(1), [binwalk](/man/binwalk)(1), [exiftool](/man/exiftool)(1)
