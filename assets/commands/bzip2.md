# TAGLINE

块排序文件压缩器

# TLDR

**压缩**文件

```bzip2 [file.txt]```

**解压**文件

```bzip2 -d [file.txt.bz2]```

**保留**原始文件

```bzip2 -k [file.txt]```

**压缩**到 stdout

```bzip2 -c [file.txt] > [file.txt.bz2]```

设置**压缩**级别

```bzip2 -9 [file.txt]```

# SYNOPSIS

**bzip2** [_options_] [_file_...]

# DESCRIPTION

**bzip2** 使用 Burrows-Wheeler 块排序压缩算法压缩文件。它通常比 gzip 获得更好的压缩率，但速度较慢。默认情况下，它会用压缩后的 .bz2 文件替换原始文件。

该工具常用于压缩 tarball 和大文件。

# PARAMETERS

**-z**, **--compress**
> 强制压缩（默认行为）

**-d**, **--decompress**
> 解压文件

**-k**, **--keep**
> 保留原始文件

**-f**, **--force**
> 覆盖已有文件

**-c**, **--stdout**
> 写入标准输出

**-t**, **--test**
> 测试压缩文件的完整性

**-v**, **--verbose**
> 详细模式（重复使用可显示更多细节）

**-1** 到 **-9**
> 压缩级别（1=最快，9=最佳，默认：9）

**--fast**
> -1 的别名

**--best**
> -9 的别名

**-s**, **--small**
> 压缩/解压时使用更少内存（至多 2500 KB）

**-q**, **--quiet**
> 抑制非关键警告

**-L**, **--license**
> 显示许可和版本信息

# WORKFLOW

```bash
# Compress file (creates file.txt.bz2, removes original)
bzip2 file.txt

# Decompress
bzip2 -d file.txt.bz2

# Compress keeping original
bzip2 -k file.txt

# Compress to stdout
bzip2 -c file.txt > file.txt.bz2

# Test integrity
bzip2 -t file.txt.bz2

# Compress tar archive
tar -cjf archive.tar.bz2 directory/
```

# COMPRESSION

块大小影响内存占用和压缩效果：
- **-1** - 100 KB 块（快速，压缩率较低）
- **-9** - 900 KB 块（较慢，压缩率更高，默认值）

# CAVEATS

比 gzip 慢。默认删除原始文件（用 -k 保留）。单线程（并行压缩请使用 **pbzip2** 或 **lbzip2**）。内存占用与块大小成正比。.bz2 文件通常比 .xz 大但比 .gz 小。

# HISTORY

**bzip2** 由 Julian Seward 于 **1996 年**创建，作为早期 bzip 的替代品，采用改进的算法获得更好的压缩效果。

# INSTALL

```apt: sudo apt install bzip2```

```dnf: sudo dnf install bzip2```

```pacman: sudo pacman -S bzip2```

```apk: sudo apk add bzip2```

```zypper: sudo zypper install bzip2```

```brew: brew install bzip2```

```nix: nix profile install nixpkgs#bzip2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bunzip2](/man/bunzip2)(1), [gzip](/man/gzip)(1), [xz](/man/xz)(1), [tar](/man/tar)(1)
