# TAGLINE

解压 XZ 压缩文件

# TLDR

**解压文件**

```unxz [file.xz]```

**保留原文件**

```unxz -k [file.xz]```

**输出到 stdout**

```unxz -c [file.xz]```

**强制覆盖**

```unxz -f [file.xz]```

**解压多个文件**

```unxz [file1.xz] [file2.xz]```

# SYNOPSIS

**unxz** [_-k_] [_-c_] [_-f_] [_options_] _files_

# PARAMETERS

**-k**
> 保留原始文件。

**-c**
> 写入到 stdout。

**-f**
> 强制覆盖。

**-v**
> 详细输出模式。

**-q**
> 安静模式。

# DESCRIPTION

**unxz** 用于解压采用 XZ 格式压缩的文件，该格式使用 LZMA2 算法以获得高压缩比。它在功能上等同于运行 **xz --decompress**，是 xz-utils 软件包中为方便使用而提供的独立命令。

默认情况下，unxz 会用解压后的结果替换 .xz 压缩文件并删除原始压缩包。**-k** 标志可保留原始压缩文件；**-c** 则把解压数据写入标准输出，便于通过管道传给其他命令。

凭借出色的压缩比，XZ 在 Linux 生态中被广泛用于分发源码 tar 包、内核源代码和软件包归档。它的解压速度很快，但压缩过程比 gzip、zstd 等替代方案更慢，也更耗内存。

# CAVEATS

处理非常大的文件时速度较慢。属于 xz-utils 的一部分。默认单线程运行。

# HISTORY

**unxz** 是 **XZ Utils** 的组成部分，由 **Lasse Collin** 创建，于 **2009 年**首次发布，作为 LZMA Utils 的后继者。XZ 格式已成为 Linux 内核源代码及众多源码 tar 包的标准压缩格式。

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

[xz](/man/xz)(1), [gzip](/man/gzip)(1), [bzip2](/man/bzip2)(1)
