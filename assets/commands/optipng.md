# TAGLINE

在不损失画质的前提下减小文件体积的 PNG 优化器

# TLDR

**优化 PNG 文件**

```optipng [image.png]```

**以最大压缩进行优化**

```optipng -o7 [image.png]```

**优化多个文件**

```optipng [*.png]```

**保留文件时间戳**

```optipng -preserve [image.png]```

**仅模拟**而不修改

```optipng -simulate [image.png]```

**剥离所有元数据**

```optipng -strip all [image.png]```

**转换为 PNG**

```optipng [image.bmp]```

# SYNOPSIS

**optipng** [_options_] _files_...

# DESCRIPTION

**optipng** 是一款 PNG 优化器，能在不损失画质的前提下减小文件体积。它会重新压缩图像数据并移除不必要的元数据。

该工具还可以将其他格式（BMP、GIF、TIFF）转换为优化后的 PNG。

# PARAMETERS

**-o** _level_
> 优化级别（0-7，默认 2）。

**-strip** _objects_
> 剥离元数据（all、exif、icc 等）。

**-preserve**
> 保留文件属性。

**-simulate**
> 试运行，不做修改。

**-out** _file_
> 输出到不同的文件。

**-dir** _directory_
> 输出目录。

**-backup**
> 保留原始文件的备份。

**-quiet**
> 静默模式。

**-verbose**
> 详细输出。

**-fix**
> 修复损坏的数据。

**-force**
> 强制写入新的输出文件。

**-snip**
> 从多图像或动画文件中裁出单幅图像。

**-nb**
> 不应用位深缩减。

**-nc**
> 不应用颜色类型缩减。

**-np**
> 不应用调色板缩减。

**-nx**
> 不应用任何无损图像缩减。

**-nz**
> 不重新编码 IDAT 数据流。

**-i** _type_
> 交错类型（0=非交错，1=Adam7）。

**-f** _filters_
> PNG 增量过滤器（0-5）。

**-zc** _levels_
> Zlib 压缩级别（1-9）。

**-zs** _strategies_
> Zlib 压缩策略（0-3）。

**-zm** _levels_
> Zlib 内存级别（1-9）。

**-zw** _size_
> Zlib 窗口大小（256、512、1k、2k、4k、8k、16k、32k）。

# CAVEATS

更高的优化级别会慢很多。仅无损——无法超越 PNG 的压缩极限。某些元数据可能有用途。默认会修改原始文件。

# HISTORY

**OptiPNG** 由 **Cosmin Truta** 创建，旨在提供最优的 PNG 压缩。它构建于 zlib 和 libpng 库之上，实现了多种优化策略来最小化文件体积。

# INSTALL

```apt: sudo apt install optipng```

```dnf: sudo dnf install optipng```

```pacman: sudo pacman -S optipng```

```apk: sudo apk add optipng```

```zypper: sudo zypper install optipng```

```brew: brew install optipng```

```nix: nix profile install nixpkgs#optipng```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pngcrush](/man/pngcrush)(1), [pngquant](/man/pngquant)(1), [jpegoptim](/man/jpegoptim)(1), [convert](/man/convert)(1)
