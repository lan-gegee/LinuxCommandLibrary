# TAGLINE

通过删除元数据和可选地降低画质来优化 JPEG 文件

# TLDR

**无损优化 JPEG**

```jpegoptim [image.jpg]```

**以目标画质优化**

```jpegoptim -m [85] [image.jpg]```

**优化到目标大小**（千字节或百分比）

```jpegoptim --size=[500k] [image.jpg]```

**剥离全部元数据**

```jpegoptim --strip-all [image.jpg]```

**优化目录中的所有 JPEG**

```jpegoptim [*.jpg]```

**将优化后的副本写入**另一目录，保留原文件

```jpegoptim -d [output_dir] [image.jpg]```

**模拟运行**（只打印结果而不写入）

```jpegoptim -n [image.jpg]```

# SYNOPSIS

**jpegoptim** [_options_] _files_...

# DESCRIPTION

**jpegoptim** 通过删除元数据和可选地降低画质来优化 JPEG 文件。它可以通过无损优化或有损降质来生成更小的文件。

该工具适用于 Web 图片、照片库等场景，可在保持可接受视觉质量的同时减少存储占用。

# PARAMETERS

**-m** _quality_, **--max**=_quality_
> 设置最高画质因子（0-100）。会禁用默认的无损模式。

**-S** _size_, **--size**=_size_
> 尽量优化到给定大小，可用千字节（如 500k）或百分比（1%-99%）表示。会禁用无损模式。

**-d** _dir_, **--dest**=_dir_
> 将优化后的文件写入备用目标目录，而不是覆盖原文件。

**-f**, **--force**
> 即使结果比原文件更大也强制优化。

**-T** _threshold_, **--threshold**=_threshold_
> 当体积收益低于给定的百分比阈值时保留旧文件。

**-n**, **--noaction**
> 模拟运行：只打印结果，不修改任何文件。

**-o**, **--overwrite**
> 覆盖目标目录中已存在的同名文件（仅在配合 -d 时有意义）。

**-p**, **--preserve**
> 保留文件的修改时间和访问时间。

**-r**, **--retry**
> 递归地反复优化，直到文件大小不再缩小为止。

**-w** _max_, **--workers**=_max_
> 设置并行线程的最大数量（默认 1）。

**-t**, **--totals**
> 处理完所有文件后打印总计信息。

**--strip-all**
> 从输出中剥离所有标记（元数据）。

**--strip-com**
> 剥离注释标记。

**--strip-exif**
> 剥离 Exif 数据。

**--strip-icc**
> 剥离 ICC 色彩配置文件标记。

**--strip-xmp**
> 剥离 XMP 标记。

**--all-progressive**
> 强制所有输出文件使用渐进式编码（基线式请用 --all-normal）。

**--stdin**, **--stdout**
> 从标准输入读取 / 将结果写入标准输出。

**-q**, **--quiet**
> 静默模式。

# CAVEATS

有损优化不可逆。剥离 ICC 配置可能影响颜色显示。部分元数据对整理归类有用。渐进式编码可能与原文件不同。

# HISTORY

**jpegoptim** 由 **Timo Kokkonen** 开发，是一款命令行 JPEG 优化工具。针对常见优化任务，它提供了比 jpegtran 更简单的选择，主打易用的批量处理体验。

# INSTALL

```apt: sudo apt install jpegoptim```

```dnf: sudo dnf install jpegoptim```

```pacman: sudo pacman -S jpegoptim```

```apk: sudo apk add jpegoptim```

```zypper: sudo zypper install jpegoptim```

```brew: brew install jpegoptim```

```nix: nix profile install nixpkgs#jpegoptim```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jpegtran](/man/jpegtran)(1), [optipng](/man/optipng)(1), [convert](/man/convert)(1), [exiftool](/man/exiftool)(1)
