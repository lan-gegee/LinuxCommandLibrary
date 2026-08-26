# TAGLINE

LZMA2 压缩工具

# TLDR

**压缩文件**

```xz [file]```

**解压文件**

```xz -d [file.xz]```

**以最大压缩率压缩**

```xz -9 [file]```

**压缩时保留原文件**

```xz -k [file]```

**压缩到 stdout**（用于管道）

```xz -c [file] > [file.xz]```

**解压到 stdout**

```xz -dc [file.xz]```

**列出压缩文件信息**

```xz -l [file.xz]```

**测试压缩文件的完整性**

```xz -t [file.xz]```

# SYNOPSIS

**xz** [_options_] [_file_...]

# PARAMETERS

**-d**, **--decompress**
> 解压文件

**-z**, **--compress**
> 压缩文件（默认）

**-k**, **--keep**
> 保留原文件

**-c**, **--stdout**
> 写入 stdout，保留原文件

**-f**, **--force**
> 强制压缩/解压

**-t**, **--test**
> 测试压缩文件的完整性

**-l**, **--list**
> 列出压缩文件的相关信息

**-0** 到 **-9**
> 压缩级别（0=最快，9=压缩率最高）

**-e**, **--extreme**
> 更高压缩率（更慢）

**-T** _N_, **--threads**=_N_
> 使用 N 个线程（0 = 自动检测核心数）

**-v**, **--verbose**
> 详细输出

**-q**, **--quiet**
> 抑制警告

# DESCRIPTION

**xz** 是一款使用 LZMA2 算法的通用压缩工具。它提供很高的压缩率，通常优于 gzip 和 bzip2，但压缩速度较慢。

默认情况下，xz 会压缩文件并用 .xz 版本替换原文件。使用 **-k** 保留原文件，或使用 **-c** 写入 stdout 以便用于管道。

多线程支持（**-T**）可以显著加快多核系统上的压缩速度。解压是单线程的，但速度较快。

压缩级别同时影响压缩率和内存占用。级别 9 在压缩和解压时所需的内存都远高于较低级别。

# CAVEATS

高压缩级别（7-9）会占用大量内存。级别 9 可能需要超过 600MB 内存进行压缩、65MB 进行解压。

分发归档时需考虑目标系统上 xz 的内存需求。较低的压缩级别适用性更广。

xz 格式与 gzip 和 bzip2 不兼容。处理这些格式请使用相应的工具（**gzip**、**bzip2**）。

# HISTORY

**xz** 由 **Lasse Collin** 和 **Igor Pavlov**（LZMA SDK）开发。xz 格式和 liblzma 于 **2009 年**发布，作为 7-Zip 所用 LZMA 格式的后继者。xz 现已被广泛用于压缩 Linux 内核 tar 包和软件包归档。

# INSTALL

```apt: sudo apt install xz-utils```

```dnf: sudo dnf install xz```

```pacman: sudo pacman -S xz```

```apk: sudo apk add xz```

```zypper: sudo zypper install xz```

```brew: brew install xz```

```nix: nix profile install nixpkgs#xz```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gzip](/man/gzip)(1), [bzip2](/man/bzip2)(1), [zstd](/man/zstd)(1), [tar](/man/tar)(1), [xzcat](/man/xzcat)(1)
