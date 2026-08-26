# TAGLINE

极快的无损压缩算法

# TLDR

**压缩文件**

```lz4 [file]```

**解压文件**

```lz4 -d [file.lz4]```

**以高压缩级别压缩**

```lz4 -9 [file]```

**压缩并保留原文件**

```lz4 -k [file]```

**压缩到 stdout**

```lz4 -c [file] > [file.lz4]```

**测试压缩文件**

```lz4 -t [file.lz4]```

**以最快速度压缩**

```lz4 -1 [file]```

**解压到 stdout**

```lz4 -dc [file.lz4]```

# SYNOPSIS

**lz4** [_-d_] [_-k_] [_-# level_] [_-c_] [_options_] [_input_] [_output_]

# PARAMETERS

**-d**, **--decompress**
> 解压。

**-z**, **--compress**
> 压缩（默认）。

**-k**, **--keep**
> 保留源文件。

**-c**, **--stdout**
> 写入 stdout。

**-#** (1-12)
> 压缩级别（1 最快，12 压缩率最高）。

**-f**, **--force**
> 不提示直接覆盖。

**-t**, **--test**
> 测试压缩文件的完整性。

**-l**, **--list**
> 列出 .lz4 文件的信息。

**-m**
> 多文件模式。

**-r**
> 递归模式。

**-B#**
> 块大小（4-7，默认 7 即 4MB）。

**--content-size**
> 在头部存储原始大小。

**-v**, **--verbose**
> 详细输出模式。

**-q**, **--quiet**
> 抑制警告。

**--rm**
> 操作完成后删除源文件。

# DESCRIPTION

**LZ4** 是一种极快的无损压缩算法。它优先考虑速度而非压缩比，因此非常适合实时压缩场景。

其压缩速度每核可超过 500 MB/s，解压速度更快，可超过 1 GB/s。这使 LZ4 适用于速度比文件大小更重要的场景。

更高的压缩级别（最高 12 级）用速度换取更好的压缩比。级别 1 最快，默认为 1。HC（高压缩）模式能以较慢的速度提供更好的压缩比。

块大小同时影响速度和压缩比。较大的块能改善压缩效果但占用更多内存。默认的 4MB 块大小在性能与内存占用之间取得平衡。

LZ4 广泛应用于数据库（MySQL、PostgreSQL）、文件系统（ZFS、Btrfs）和实时应用中。其帧格式包含用于完整性校验的校验和。

# CAVEATS

压缩比低于 gzip/zstd。在对体积要求苛刻的场景不适用。较大的块会占用更多内存。并非所有系统都默认安装了 lz4。帧格式与原始 LZ4 块格式不同。

# HISTORY

**LZ4** 由 **Yann Collet** 自 **2011 年**前后开始开发。它的设计目标是成为当时最快的压缩算法，同时保持合理的压缩比。算法与实现采用 BSD 许可证授权，因而在各类项目中得到广泛采用。

# INSTALL

```apt: sudo apt install lz4```

```dnf: sudo dnf install lz4```

```pacman: sudo pacman -S lz4```

```apk: sudo apk add lz4```

```zypper: sudo zypper install lz4```

```brew: brew install lz4```

```nix: nix profile install nixpkgs#lz4```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[zstd](/man/zstd)(1), [gzip](/man/gzip)(1), [pigz](/man/pigz)(1), [lzop](/man/lzop)(1)
