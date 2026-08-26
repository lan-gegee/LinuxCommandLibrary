# TAGLINE

优化 PNG 文件以减小体积

# TLDR

**优化 PNG**

```pngcrush [input.png] [output.png]```

**原地优化**

```pngcrush -ow [image.png]```

**移除元数据**

```pngcrush -rem alla [input.png] [output.png]```

**最佳压缩**

```pngcrush -brute [input.png] [output.png]```

**减少颜色数**

```pngcrush -reduce [input.png] [output.png]```

**批量优化**目录中的所有 PNG

```pngcrush -d [output_dir/] [input_dir/]*.png```

**设置指定压缩级别**（0-9）

```pngcrush -l [9] [input.png] [output.png]```

# SYNOPSIS

**pngcrush** [_options_] _input_ [_output_]

# PARAMETERS

_INPUT_
> 输入的 PNG 文件。

_OUTPUT_
> 输出的 PNG 文件。

**-ow**
> 原地覆盖输入文件。

**-d** _DIRECTORY_
> 将输出文件写入指定目录。

**-rem** _CHUNK_
> 移除指定的辅助数据块。使用 **alla** 移除所有文本数据块，或使用 **allb** 移除所有非关键数据块。

**-brute**
> 尝试全部 148 种滤波/压缩组合，以获得最大程度的缩减。

**-reduce**
> 在不损失数据的前提下尽可能降低颜色深度和位深。

**-l** _LEVEL_
> 设置 zlib 压缩级别（0 = 不压缩，9 = 最高）。

**-n**
> 不生成输出文件；只测试压缩而不写入（适合做基准测试）。

**-fix**
> 修复原本会导致失败的问题，例如错误的 CRC。

# DESCRIPTION

**pngcrush** 通过尝试多种压缩策略并选取最小结果来优化 PNG 文件。这种优化完全无损——图像数据被原样保留，只是借助更好的压缩参数来减小文件体积。

**-brute** 选项会尝试所有滤波与压缩组合以获得最大程度的缩减，代价是更长的处理时间。**-rem** 选项会剥离文本注释、时间戳和色彩配置文件等元数据块，从而进一步缩小体积。

# CAVEATS

所有优化均无损；图像数据被完整保留。由于要逐一测试全部 148 种压缩策略，**-brute** 选项在处理大图时可能非常慢。**-ow** 标志会先创建临时文件再替换原文件，因此需要足够的磁盘空间。不支持动画 PNG（APNG）。

# HISTORY

**pngcrush** 由 Glenn Randers-Pehrson 创建，是最古老、应用最广泛的 PNG 优化工具之一，于 1998 年首次发布。

# INSTALL

```apt: sudo apt install pngcrush```

```dnf: sudo dnf install pngcrush```

```pacman: sudo pacman -S pngcrush```

```apk: sudo apk add pngcrush```

```zypper: sudo zypper install pngcrush```

```brew: brew install pngcrush```

```nix: nix profile install nixpkgs#pngcrush```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[optipng](/man/optipng)(1), [pngcheck](/man/pngcheck)(1), [pngquant](/man/pngquant)(1), [zopflipng](/man/zopflipng)(1), [convert](/man/convert)(1)
