# TAGLINE

在设备（通常是硬盘分区）上创建 Minix 文件系统

# TLDR

在设备 X 的分区 Y 内创建 **Minix 文件系统**

```sudo mkfs.minix [/dev/sdXY]```

创建 Minix 文件系统并**检查坏块**

```sudo mkfs.minix -c [/dev/sdXY]```

创建 **Minix 版本 2** 文件系统

```sudo mkfs.minix -2 [/dev/sdXY]```

创建 **Minix 版本 3** 文件系统

```sudo mkfs.minix -3 [/dev/sdXY]```

指定**文件名最大长度**

```sudo mkfs.minix -n [30] [/dev/sdXY]```

以指定的 **inode 数量**创建

```sudo mkfs.minix -i [number] [/dev/sdXY]```

# SYNOPSIS

**mkfs.minix** [**-c**] [**-n** _namelength_] [**-i** _inodes_] [**-l** _badblocks_] [**-1**|**-2**|**-3**] _device_ [_size-in-blocks_]

# PARAMETERS

**-c, --check**
> 创建文件系统前检查设备坏块

**-n, --namelength _length_**
> 文件名最大长度；版本 1-2 为 14 或 30，版本 3 为 60；默认为 30

**-i, --inodes _number_**
> 为文件系统创建的 inode 数量

**-l, --badblocks _filename_**
> 从文件读取坏块列表（每行一个块号）

**-1**
> 创建 Minix 版本 1 文件系统；这是最初的默认值，在许多发行版中仍是默认。

**-2**, **-v**
> 创建 Minix 版本 2 文件系统（支持更大的文件）。

**-3**
> 创建 Minix 版本 3 文件系统（文件名最长可达 60 个字符）。

**--lock[=_mode_]**
> 使用独占的 BSD 锁；mode 可为 yes、no 或 nonblock

**-h, --help**
> 显示帮助信息

**-V, --version**
> 显示版本信息

# DESCRIPTION

**mkfs.minix** 在设备（通常是硬盘分区）上创建 Minix 文件系统。Minix 是一种简单的教学型文件系统，最初为 Minix 操作系统设计。

可选的 size-in-blocks 参数指定文件系统大小；省略时自动确定大小。块数必须大于 10 且小于 65536。版本 1 是默认且兼容性最好的；版本 2 增加了对更大文件的支持；版本 3 将文件名长度扩展到 60 个字符。

# CAVEATS

Minix 文件系统有明显局限：版本 1 的文件系统最大为 64MB、文件名受限且没有日志功能。它主要用于教学、启动软盘或需要极低开销的嵌入式系统。不建议在现代存储上用于生产环境。

# HISTORY

Minix 文件系统由 **Andrew S. Tanenbaum** 于 **1987 年**为其 **Minix 操作系统** 创建。它作为教学工具直接影响了 Linux 内核的开发。Linus Torvalds 最初就是在 Minix 上开发 Linux 的，早期 Linux 的文件系统也以 Minix 为基础。mkfs.minix 工具属于 **util-linux**。

# INSTALL

```apt: sudo apt install util-linux-extra```

```apk: sudo apk add util-linux-misc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mkfs](/man/mkfs)(8), [fsck](/man/fsck)(8)
