# TAGLINE

感知式 JPEG 编码器，在小体积下优化视觉质量

# TLDR

**重新编码 JPEG**

```guetzli [input.jpg] [output.jpg]```

**将 PNG 编码为 JPEG**

```guetzli [input.png] [output.jpg]```

**设置质量级别（84-100）**

```guetzli --quality [90] [input.jpg] [output.jpg]```

**最大压缩（支持的最低质量）**

```guetzli --quality [84] [input.jpg] [output.jpg]```

**显示进度跟踪**

```guetzli --verbose [input.png] [output.jpg]```

# SYNOPSIS

**guetzli** [**--quality** _Q_] [**--verbose**] _input_ _output.jpg_

# PARAMETERS

_input_
> 源图像。支持 PNG 和 JPEG 输入。

_output.jpg_
> 目标 JPEG 文件。

**--quality** _Q_
> 视觉质量，以 libjpeg 等价单位表示。范围 84-100，默认 95。不支持低于 84 的值。

**--verbose**
> 打印编码尝试的跟踪记录。

# DESCRIPTION

**Guetzli** 是一款面向人类视觉系统的 JPEG 编码器。它使用心理视觉模型 Butteraugli 搜索 JPEG 量化空间，生成基线兼容的 JPEG 文件，在相同感知质量下通常比 libjpeg 的等效输出小 20-30%。

输出文件与所有标准 JPEG 解码器兼容。代价是编码开销：guetzli 需要大量计算和内存。

# CAVEATS

非常慢：编码一百万像素可能需要一分钟以上。内存占用约为每百万像素 300 MB。只接受 84-100 的质量值。对未降质的源（PNG 或高质量 JPEG）效果最佳；重新编码高度压缩的 JPEG 收益有限。

# HISTORY

**Guetzli** 由 **Google Research** 开发，于 **2017 年 3 月**连同 Butteraugli 感知距离度量一起开源发布。

# INSTALL

```apt: sudo apt install guetzli```

```pacman: sudo pacman -S guetzli```

```apk: sudo apk add guetzli```

```brew: brew install guetzli```

```nix: nix profile install nixpkgs#guetzli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cjpeg](/man/cjpeg)(1), [jpegoptim](/man/jpegoptim)(1)
