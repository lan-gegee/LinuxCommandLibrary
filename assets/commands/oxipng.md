# TAGLINE

使用 Rust 编写的多线程 PNG 优化工具

# TLDR

**优化 PNG 文件**

```oxipng [image.png]```

**以最大压缩率优化**

```oxipng -o max [image.png]```

**优化并写入另一个文件**

```oxipng --out [output.png] [input.png]```

**优化目录中的所有 PNG**

```oxipng [*.png]```

**移除所有元数据**

```oxipng --strip all [image.png]```

**使用多个线程**

```oxipng -t [4] [image.png]```

**尽可能降为 8 位调色板**

```oxipng --reduce [image.png]```

**试运行**（只显示可节省的空间而不写入）

```oxipng --pretend [image.png]```

# SYNOPSIS

**oxipng** [_-o level_] [_--strip mode_] [_-t threads_] [_--reduce_] [_options_] _files_

# PARAMETERS

**-o**, **--opt** _LEVEL_
> 优化级别（0-6、max）。

**-s**, **--strip** _MODE_
> 移除元数据：none、safe（非渲染元数据）、all（所有非关键数据）。单独的 -s 是 --strip safe 的简写。

**-a**, **--alpha**
> 额外的透明通道优化。

**-t**, **--threads** _NUM_
> 线程数量。

**--out** _DIR_
> 输出目录。

**--dir** _DIR_
> 递归处理目录。

**-r**, **--recursive**
> 递归处理目录。

**--reduce**
> 尝试降低位深。

**--interlace** _MODE_
> 隔行扫描：0（无）、1（Adam7）、keep。

**--pretend**
> 试运行，只显示可节省的空间而不写入。

**-b**, **--backup**
> 保留原文件的备份。

**-f** _NUM_, **--filters** _NUM_
> 要尝试的滤波策略（0=None、1=Sub、2=Up、3=Average、4=Paeth、5=MinSum、6=Entropy、7=Bigrams、8=BigEnt、9=Brute）。支持逗号分隔的列表或范围（例如 0-5）。

**-Z**, **--zopfli**
> 使用 Zopfli 以获得更好的压缩效果（慢得多）。

**--timeout** _seconds_
> 优化单个文件的最长时间。

**--check**
> 验证输出的完整性。

**-q**, **--quiet**
> 安静模式。

**-v**, **--verbose**
> 详细输出。

# DESCRIPTION

**oxipng** 是一款使用 Rust 编写的多线程 PNG 优化工具。它通过无损重压缩来减小 PNG 文件大小，且不影响图像质量。

优化级别（0-6）控制压缩与速度之间的权衡。默认为级别 2，可快速获得良好的压缩效果。级别 6 和 "max" 会尝试更多策略以实现最大压缩，但耗时更长。

该工具会尝试不同的 PNG 滤波策略和压缩参数来找到最小的输出结果。移除元数据可以进一步减小体积——"safe" 移除非必要的数据块，"all" 移除除关键图像数据以外的所有内容。

位深降低会在不损失质量的前提下自动将 16 位转为 8 位，或在可能时将 RGBA 转为调色板格式。对于合适的图像，这可以显著减小文件大小。

Zopfli 模式使用更彻底的压缩算法，压缩率提高约 5%，但处理时间大幅增加。这适用于会被反复分发的图像。

# CAVEATS

如果 PNG 已经是最佳压缩状态，则无法再减小文件大小。Zopfli 模式非常慢。最高优化级别会消耗大量 CPU 时间。部分 PNG 特性可能不被完全支持。大图需要大量内存。

# HISTORY

**oxipng** 由 **Josh Holmer** 于 **2016** 年前后创建，是 OptiPNG 的 Rust 重写版。其目标是提供一款代码现代、速度更快、支持多线程的 PNG 优化器。它在构建流水线和资源优化场景中广受欢迎，尤其是在 PNG 大小直接影响页面加载时间的 Web 开发领域。

# INSTALL

```dnf: sudo dnf install oxipng```

```pacman: sudo pacman -S oxipng```

```apk: sudo apk add oxipng```

```zypper: sudo zypper install oxipng```

```brew: brew install oxipng```

```nix: nix profile install nixpkgs#oxipng```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[optipng](/man/optipng)(1), [pngcrush](/man/pngcrush)(1), [pngquant](/man/pngquant)(1), [zopflipng](/man/zopflipng)(1)
