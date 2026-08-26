# TAGLINE

使用多个处理器压缩文件

# TLDR

**使用多个处理器压缩文件**

```pigz [file]```

**解压文件**

```pigz -d [file.gz]```

**以指定压缩级别压缩**

```pigz -[9] [file]```

**压缩时保留原文件**

```pigz -k [file]```

**使用指定数量的线程压缩**

```pigz -p [4] [file]```

**压缩到 stdout**

```pigz -c [file] > [file.gz]```

**递归压缩目录中的文件**

```pigz -r [directory/]```

**测试压缩文件的完整性**

```pigz -t [file.gz]```

# SYNOPSIS

**pigz** [_-dkcp_] [_-# level_] [_-p threads_] [_files_]

# PARAMETERS

**-d**, **--decompress**
> 解压。

**-k**, **--keep**
> 保留原文件。

**-c**, **--stdout**
> 写入 stdout。

**-p** _NUM_, **--processes** _NUM_
> 压缩线程数。

**-#** (0-9, 11)
> 压缩级别（默认 6，11 = zopfli）。

**-f**, **--force**
> 即使文件已存在也强制压缩。

**-r**, **--recursive**
> 递归处理目录。

**-t**, **--test**
> 测试压缩文件的完整性。

**-l**, **--list**
> 列出压缩信息。

**-n**, **--no-name**
> 不存储原始名称/时间。

**-N**, **--name**
> 存储原始名称/时间。

**-b** _SIZE_, **--blocksize** _SIZE_
> 压缩的块大小。

**-z**, **--zlib**
> 压缩为 zlib 格式。

**-K**, **--zip**
> 压缩为单条目 zip。

**-q**, **--quiet**
> 静默模式。

**-v**, **--verbose**
> 详细输出模式。

# DESCRIPTION

**pigz** (Parallel Implementation of GZip) 使用多个处理器压缩文件。在多核系统上，它生成与 gzip 兼容的输出，速度显著快于标准 gzip。

压缩的并行化通过将输入划分为由不同线程处理的块来实现。结果被合并并保持 gzip 兼容性。解压的可并行度较低，但仍能从并行 CRC 校验中受益。

默认线程数与可用处理器数一致。在高核心数的系统上，超过 8-16 个线程后收益递减。块大小影响并行化的粒度。

压缩级别与 gzip 相同：1（最快）到 9（最佳）。级别 11 启用 zopfli 压缩，可获得最大压缩比但速度慢得多，适合压缩一次、多次读取的文件。

该工具在大多数场景下是 gzip 的直接替代品。输出格式完全相同，因此文件可用标准 gunzip 解压。

# CAVEATS

解压并非完全并行——受 gzip 格式设计的限制。内存占用随线程数增加。很小的文件可能无法受益于并行化。zopfli 模式（级别 11）极其缓慢。压缩输出可能与 gzip 不同（内容相同，字节不同）。

# HISTORY

**pigz** 由 **Mark Adler**（gzip 和 zlib 的共同作者）于 **2007 年**前后编写，以满足并行压缩的需求。名称是对 "pig"（gzip 的并行实现）和猪叫声的双关。它已成为现代多核系统上快速压缩大文件的必备工具。

# INSTALL

```apt: sudo apt install pigz```

```dnf: sudo dnf install pigz```

```pacman: sudo pacman -S pigz```

```apk: sudo apk add pigz```

```zypper: sudo zypper install pigz```

```brew: brew install pigz```

```nix: nix profile install nixpkgs#pigz```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gzip](/man/gzip)(1), [zstd](/man/zstd)(1), [lz4](/man/lz4)(1), [pbzip2](/man/pbzip2)(1)
