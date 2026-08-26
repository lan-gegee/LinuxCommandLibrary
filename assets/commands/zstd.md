# TAGLINE

快速的无损压缩算法

# TLDR

**压缩文件**

```zstd [file]```

**解压文件**

```zstd -d [file.zst]```

**压缩并保留原文件**

```zstd -k [file]```

**以最高压缩级别压缩**

```zstd -19 [file]```

**极限压缩**（最高压缩率）

```zstd --ultra -22 [file]```

**以最快速度压缩**

```zstd -1 [file]```

**压缩到 stdout**

```zstd -c [file] > [file.zst]```

**解压到 stdout**

```zstd -dc [file.zst]```

**多线程压缩**

```zstd -T0 [file]```

**测试归档完整性**

```zstd -t [file.zst]```

# SYNOPSIS

**zstd** [_options_] [_files_...]

# DESCRIPTION

**Zstandard**（zstd）是一种快速的无损压缩算法，能提供高压缩比。它的压缩比/速度权衡范围很广，既有极速模式，也有极致压缩模式。

在相近的压缩比下，zstd 通常比 zlib/gzip 更快，且明显快于 xz/lzma。更高的压缩级别可以逼近 xz 的压缩比，同时保持更快的解压速度。

zstd 支持面向小文件的字典压缩和并行压缩，可以在许多工作流中无缝替代 gzip。其格式由 RFC 8478 定义。

# PARAMETERS

**-d**, **--decompress**
> 解压文件。

**-k**, **--keep**
> 保留源文件。

**-c**, **--stdout**
> 写入 stdout。

**-1** to **-19**
> 压缩级别（默认 3）。

**--ultra**
> 启用极限压缩（级别 20-22）。

**-T** _n_, **--threads=** _n_
> 线程数（0=自动）。

**-t**, **--test**
> 测试压缩文件的完整性。

**-l**, **--list**
> 列出压缩文件信息。

**-f**, **--force**
> 强制覆盖/压缩。

**-r**
> 递归处理目录。

**--rm**
> 压缩后删除源文件。

**-D** _dict_
> 使用字典进行压缩。

**--train**
> 从样本创建字典。

**-q**, **--quiet**
> 抑制输出。

**-v**, **--verbose**
> 详细模式。

# CAVEATS

更高的压缩级别消耗更多内存。极限级别（20-22）所需的内存显著更多。字典压缩在解压时必须使用同一个字典。目前并非所有工具都支持 .zst 格式。

# HISTORY

**Zstandard** 由 **Yann Collet** 自 **2015 年**起在 **Facebook** 开发，建立在它早期的 LZ4 工作之上。该项目于 **2016 年**公开发布，并于 **2018 年**成为 RFC 8478。zstd 已被 Linux 内核采用用于压缩，tar、HTTP content-encoding 以及众多其他工具也提供了支持。

# INSTALL

```apt: sudo apt install zstd```

```dnf: sudo dnf install zstd```

```pacman: sudo pacman -S zstd```

```apk: sudo apk add zstd```

```zypper: sudo zypper install zstd```

```brew: brew install zstd```

```nix: nix profile install nixpkgs#zstd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gzip](/man/gzip)(1), [xz](/man/xz)(1), [lz4](/man/lz4)(1), [bzip2](/man/bzip2)(1)
