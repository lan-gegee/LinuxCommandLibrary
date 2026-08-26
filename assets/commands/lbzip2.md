# TAGLINE

并行的 bzip2 压缩与解压工具

# TLDR

**压缩文件**

```lbzip2 [file]```

**解压文件**

```lbzip2 -d [file.bz2]```

**指定线程数**

```lbzip2 -n [4] [file]```

**保留原始文件**

```lbzip2 -k [file]```

**压缩到标准输出**

```lbzip2 -c [file] > [file.bz2]```

**测试归档完整性**

```lbzip2 -t [file.bz2]```

# SYNOPSIS

**lbzip2** [_options_] [_files_...]

# PARAMETERS

**-d**, **--decompress**
> 解压。

**-z**, **--compress**
> 压缩（默认）。

**-k**, **--keep**
> 保留输入文件。

**-c**, **--stdout**
> 输出到标准输出。

**-t**, **--test**
> 测试完整性。

**-n** _threads_
> 线程数。

**-1** 到 **-9**
> 压缩级别。

**-f**, **--force**
> 强制覆盖。

**-v**, **--verbose**
> 详细输出。

# DESCRIPTION

**lbzip2** 是一个并行的 bzip2 压缩与解压工具。它利用多个 CPU 核心来压缩和解压文件，比标准 bzip2 更快。

lbzip2 生成的输出与 bzip2/bunzip2 兼容。它会自动使用可用的 CPU 核心，因此在多核系统上速度快得多。

# COMPARISON

```
bzip2   - Single-threaded
pbzip2  - Parallel, different archive format
lbzip2  - Parallel, fully compatible format
```

# CAVEATS

内存占用高于 bzip2。线程数会影响内存用量。与 bzip2 文件兼容。默认使用所有核心。

# HISTORY

lbzip2 由 **Mikolaj Izdebski** 编写，是 bzip2 的即插即用型并行替代品，与原始格式完全兼容。

# INSTALL

```apt: sudo apt install lbzip2```

```dnf: sudo dnf install lbzip2```

```pacman: sudo pacman -S lbzip2```

```zypper: sudo zypper install lbzip2```

```nix: nix profile install nixpkgs#lbzip2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bzip2](/man/bzip2)(1), [pbzip2](/man/pbzip2)(1), [pigz](/man/pigz)(1), [xz](/man/xz)(1)
