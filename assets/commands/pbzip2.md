# TAGLINE

bzip2 压缩的并行实现

# TLDR

**压缩文件**

```pbzip2 [file]```

**解压文件**

```pbzip2 -d [file.bz2]```

**保留原文件**

```pbzip2 -k [file]```

**设置压缩级别**

```pbzip2 -[9] [file]```

**使用指定数量的处理器**

```pbzip2 -p[4] [file]```

**从 stdin 压缩**

```cat [file] | pbzip2 > [file.bz2]```

**解压到 stdout**

```pbzip2 -dc [file.bz2] > [file]```

**测试压缩文件**

```pbzip2 -t [file.bz2]```

# SYNOPSIS

**pbzip2** [_-d_] [_-k_] [_-p n_] [_-1..9_] [_options_] [_files_]

# PARAMETERS

**-d**
> 解压。

**-z**
> 压缩（默认）。

**-k**
> 保留原始文件。

**-p** _N_
> 使用的处理器数量。

**-1** 到 **-9**
> 压缩级别（9 = 最佳）。

**-c**
> 输出到 stdout。

**-f**
> 强制覆盖。

**-t**
> 测试完整性。

**-q**
> 静默模式。

**-v**
> 详细模式。

**-m** _N_
> 每线程内存限制（MB）。

**-r**
> 将整个文件读入 RAM。

# DESCRIPTION

**pbzip2** 是 bzip2 压缩的并行实现。它利用多个 CPU 核心压缩和解压文件，速度比单线程 bzip2 更快。

该工具生成的文件与标准 bzip2 兼容。输出可由 bzip2、bunzip2 或 pbzip2 自身解压。

并行度随可用处理器数量扩展。默认使用所有核心。-p 选项可限制处理器占用，适合后台压缩。

压缩级别与 bzip2 相同：数字越大，文件越小，但耗时更长。并行实现有助于弥补较慢的压缩速度。

内存用量随线程数扩展。每个线程都需要为其压缩缓冲区分配内存。设置限制可防止大型任务耗尽内存。

管道模式支持流式压缩。与 tar 结合可实现并行的压缩归档。

# CAVEATS

内存占用高于 bzip2。在多核系统上提速最明显。解压加速取决于文件的创建方式。

# HISTORY

**pbzip2** 由 **Jeff Gilchrist** 于 **2005 年**前后创建，旨在利用多核处理器进行 bzip2 压缩。随着多核 CPU 的普及，pbzip2 等并行压缩工具成为处理大规模数据的必备工具。

# INSTALL

```apt: sudo apt install pbzip2```

```dnf: sudo dnf install pbzip2```

```pacman: sudo pacman -S pbzip2```

```zypper: sudo zypper install pbzip2```

```brew: brew install pbzip2```

```nix: nix profile install nixpkgs#pbzip2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bzip2](/man/bzip2)(1), [pigz](/man/pigz)(1), [lbzip2](/man/lbzip2)(1), [xz](/man/xz)(1)
