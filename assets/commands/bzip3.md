# TAGLINE

高性能文件压缩器，压缩比优于 bzip2

# TLDR

**压缩**文件

```bzip3 [file.txt]```

**解压**文件

```bzip3 -d [file.txt.bz3]```

**保留**原文件

```bzip3 -k [file.txt]```

**设置**块大小

```bzip3 -b [256] [file.txt]```

# SYNOPSIS

**bzip3** [_options_] [_file_...]

# DESCRIPTION

**bzip3** 是一款压缩工具，压缩比优于 bzip2、gzip 和 zstd，同时保持合理的速度。它使用比 bzip2 更现代的算法，性能有所提升。

该工具与 bzip2 向后不兼容，但对大多数数据类型能提供显著更好的压缩效果。

# PARAMETERS

**-d**, **--decompress**
> 解压文件

**-k**, **--keep**
> 保留原始文件

**-f**, **--force**
> 覆盖已存在的文件

**-c**, **--stdout**
> 写入标准输出

**-b**, **--block** _size_
> 块大小，单位为 MiB（1-511，默认 16）

**-j**, **--jobs** _n_
> 线程数

**-v**, **--verbose**
> 详细输出模式

# FEATURES

- 压缩比优于 bzip2
- 多线程压缩
- 可配置的块大小
- 解压速度快
- 内存占用低
- 现代算法

# WORKFLOW

```bash
# Compress file
bzip3 file.txt
# Creates: file.txt.bz3

# Decompress
bzip3 -d file.txt.bz3

# Compress keeping original
bzip3 -k file.txt

# Multi-threaded compression
bzip3 -j 4 largefile.bin

# Custom block size
bzip3 -b 128 file.txt
```

# COMPARISON

典型压缩比：
- **bzip3** - 最佳
- **xz/lzma** - 极佳但较慢
- **bzip2** - 良好
- **gzip** - 中等但快速
- **lz4** - 快速但压缩率较低

# CAVEATS

与 bzip2（.bz2 文件）不兼容。支持范围不如 gzip/bzip2 广泛。相对较新（可能存在 bug）。大多数系统默认不安装。部分功能需要较新版本。

# HISTORY

**bzip3** 由 Kamila Szewczyk 于 **2022** 年创建，作为 bzip2 的现代化后继者，采用改进的算法以获得更好的压缩效果。

# INSTALL

```apt: sudo apt install bzip3```

```dnf: sudo dnf install bzip3```

```pacman: sudo pacman -S bzip3```

```apk: sudo apk add bzip3```

```zypper: sudo zypper install bzip3```

```brew: brew install bzip3```

```nix: nix profile install nixpkgs#bzip3```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bzip2](/man/bzip2)(1), [xz](/man/xz)(1), [zstd](/man/zstd)(1)

# RESOURCES

```[Source code](https://github.com/kspalaiologos/bzip3)```

<!-- verified: 2026-06-22 -->
