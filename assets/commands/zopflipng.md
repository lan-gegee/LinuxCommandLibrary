# TAGLINE

使用 Zopfli 压缩优化 PNG 文件

# TLDR

**优化 PNG**

```zopflipng [input.png] [output.png]```

**原地优化**

```zopflipng -y [file.png] [file.png]```

**有损优化**

```zopflipng --lossy_transparent [input.png] [output.png]```

**最大压缩**

```zopflipng -m [input.png] [output.png]```

**保留元数据**

```zopflipng --keepchunks=iCCP,sRGB [input.png] [output.png]```

**快速模式**

```zopflipng -q [input.png] [output.png]```

**设置指定的迭代次数**

```zopflipng --iterations=[50] [input.png] [output.png]```

# SYNOPSIS

**zopflipng** [_-m_] [_-q_] [_--lossy_transparent_] [_options_] _input_ _output_

# PARAMETERS

**-m**
> 更高强度压缩：使用更多迭代（更慢但压缩效果更好）。

**-q**
> 快速模式，压缩不够彻底。

**-y**
> 允许覆盖输出文件。

**--iterations** _N_
> 压缩的迭代次数（默认：小文件 15 次，大文件 5 次）。

**--lossy_transparent**
> 对完全透明的像素做有损优化，以获得更小的文件。

**--keepchunks** _CHUNKS_
> 要保留的元数据块名称列表（以逗号分隔），例如 iCCP,sRGB。

**--keeptime**
> 保留输入文件原有的修改时间。

**--filters** _TYPES_
> 要尝试的过滤策略：0-4、m（最小和）、e（熵）、p（预定义）、b（暴力）。

**--prefix** _PREFIX_
> 为输出文件名添加前缀（可包含目录路径）。

# DESCRIPTION

**zopflipng** 使用 Zopfli 压缩算法优化 PNG 文件，其输出与 deflate 兼容，凡标准 PNG 可用的地方都可使用。相比标准 PNG 优化工具，它通常能让文件小 3-8%。

该工具默认剥离元数据块以实现最大限度的体积缩减，但可以用 **--keepchunks** 选项保留特定块。有损透明模式（**--lossy_transparent**）通过优化不可见的完全透明像素进一步减小文件体积，且不会产生任何可见的质量变化。

zopflipng 刻意采用慢速策略，以压缩时间换取更小的输出。它是为构建流水线中的最终阶段优化设计的，不适合交互式使用。**-m** 标志会启用更多迭代以获得更好的压缩，代价是更长的处理时间。

# CAVEATS

由于穷举式的压缩搜索，处理大图像时非常缓慢。CPU 占用高。最适合构建流水线中的最终阶段优化，而非交互式使用。默认剥离元数据块。

# HISTORY

**Zopfli** 由 **Google** 创建，用于实现最大程度的 deflate 压缩。zopflipng 将该算法应用到 PNG 图像上。

# INSTALL

```apt: sudo apt install zopfli```

```dnf: sudo dnf install zopfli```

```pacman: sudo pacman -S zopfli```

```apk: sudo apk add zopfli```

```zypper: sudo zypper install zopfli```

```brew: brew install zopfli```

```nix: nix profile install nixpkgs#zopfli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[optipng](/man/optipng)(1), [pngcrush](/man/pngcrush)(1), [pngquant](/man/pngquant)(1)
