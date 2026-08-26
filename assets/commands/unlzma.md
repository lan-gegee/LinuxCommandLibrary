# TAGLINE

解压 LZMA 压缩文件

# TLDR

**解压文件**

```unlzma [file.lzma]```

**保留原文件**

```unlzma -k [file.lzma]```

**输出到 stdout**

```unlzma -c [file.lzma]```

**强制覆盖**

```unlzma -f [file.lzma]```

**详细输出**

```unlzma -v [file.lzma]```

# SYNOPSIS

**unlzma** [_-k_] [_-c_] [_-f_] [_options_] _files_

# PARAMETERS

**-k**
> 保留原文件。

**-c**
> 写入 stdout。

**-f**
> 强制覆盖。

**-v**
> 详细模式。

**-q**
> 安静模式。指定两次可抑制错误信息。

**-T**, **--threads** _N_
> 使用至多 N 个线程进行解压（xz 5.2+）。

# DESCRIPTION

**unlzma** 解压使用 LZMA（Lempel-Ziv-Markov 链算法）压缩格式压缩的文件。它在功能上等同于运行 **xz --format=lzma --decompress**，作为 xz-utils 软件包中的便捷命令提供。

默认情况下，unlzma 用解压后的输出替换压缩的 .lzma 文件，并删除原文件。**-k** 标志保留原始压缩文件，**-c** 将解压数据写入标准输出以便通过管道传给其他命令。

LZMA 格式是一种遗留压缩格式，已在很大程度上被 XZ 格式取代，后者使用改进的 LZMA2 算法并提供更好的多线程支持。unlzma 对于解压旧归档以及与仍使用 .lzma 格式的系统保持兼容仍然有用。

# CAVEATS

.lzma 是一种没有完整性校验的遗留格式。新文件请使用 xz。属于 xz-utils 的一部分。其命令行语法是 LZMA Utils 4.32.x 的超集，以保持向后兼容。

# HISTORY

**unlzma** 是 **xz-utils** 的一部分，为遗留的 LZMA 格式提供解压功能。

# INSTALL

```dnf: sudo dnf install xz```

```pacman: sudo pacman -S xz```

```apk: sudo apk add xz```

```zypper: sudo zypper install xz```

```brew: brew install xz```

```nix: nix profile install nixpkgs#xz```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xz](/man/xz)(1), [lzma](/man/lzma)(1), [unxz](/man/unxz)(1)
