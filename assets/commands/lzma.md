# TAGLINE

使用 Lempel-Ziv-Markov 链算法压缩文件

# TLDR

**压缩文件**

```lzma [file]```

**解压文件**

```lzma -d [file.lzma]```

**保留原始文件**

```lzma -k [file]```

**压缩到 stdout**

```lzma -c [file] > [file.lzma]```

**设置压缩级别**

```lzma -9 [file]```

**列出**压缩文件的信息

```lzma -l [file.lzma]```

**测试归档完整性**

```lzma -t [file.lzma]```

# SYNOPSIS

**lzma** [_options_] [_files_...]

# PARAMETERS

**-d**, **--decompress**
> 解压。

**-z**, **--compress**
> 压缩（默认）。

**-k**, **--keep**
> 保留原始文件。

**-c**, **--stdout**
> 写入 stdout。

**-1** 至 **-9**
> 压缩级别。

**-e**, **--extreme**
> 最大压缩率。

**-t**, **--test**
> 测试完整性。

**-f**, **--force**
> 强制覆盖。

**-v**, **--verbose**
> 详细输出模式；显示压缩比等细节。

**-q**, **--quiet**
> 抑制警告；指定两次可同时抑制错误信息。

**-l**, **--list**
> 列出压缩文件的信息。

**-T**, **--threads** _NUM_
> 设置工作线程数（0 表示根据 CPU 核心数自动检测）。

# DESCRIPTION

**lzma** 使用 Lempel-Ziv-Markov 链算法（LZMA）压缩文件。它提供很高的压缩比，但压缩速度较慢。

lzma 命令通常是指向 xz 的符号链接，xz 在支持较新的 .xz 格式的同时也兼容旧式 .lzma 格式。

# COMPARISON

```
Tool     Compression  Speed
gzip     Medium       Fast
bzip2    Good         Medium
lzma/xz  Best         Slow
```

# CAVEATS

压缩速度慢于 gzip。极高压缩级别下内存占用较大。属于旧式格式；新文件建议改用 xz。

# HISTORY

LZMA 由 **Igor Pavlov** 于 **1998 年**为其 7-Zip 归档工具开发。该算法后来被标准化，并催生了作为现代容器的 xz 格式。

# INSTALL

```dnf: sudo dnf install xz```

```pacman: sudo pacman -S xz```

```apk: sudo apk add xz```

```zypper: sudo zypper install xz```

```brew: brew install xz```

```nix: nix profile install nixpkgs#xz```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xz](/man/xz)(1), [unlzma](/man/unlzma)(1), [gzip](/man/gzip)(1), [bzip2](/man/bzip2)(1), [zstd](/man/zstd)(1), [7z](/man/7z)(1)
