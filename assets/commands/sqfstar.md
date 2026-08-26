# TAGLINE

从 tar 归档创建 squashfs 文件系统

# TLDR

从 **tar 归档**创建 squashfs

```sqfstar < [archive.tar] [filesystem.squashfs]```

以**指定压缩方式**创建

```zcat [archive.tar.gz] | sqfstar -comp [gzip|lzo|lz4|xz|zstd] [filesystem.squashfs]```

创建并**排除文件**

```xzcat [archive.tar.xz] | sqfstar [filesystem.squashfs] [file1] [file2]```

按**模式**排除

```zstdcat [archive.tar.zst] | sqfstar [filesystem.squashfs] "*.gz"```

按**正则表达式**排除

```lz4cat [archive.tar.lz4] | sqfstar [filesystem.squashfs] -regex "[pattern]"```

设置**块大小**

```cat [archive.tar] | sqfstar -b [131072] [filesystem.squashfs]```

# SYNOPSIS

**sqfstar** [_OPTIONS_] _FILESYSTEM_ [_exclude_files_...]

# PARAMETERS

**-comp** _compressor_
> 压缩算法：gzip、lzo、lz4、xz、zstd、lzma

**-b** _block_size_
> 以字节为单位的块大小（4K-1MB，默认：128K）

**-noI**
> 不压缩 inode 表

**-noD**
> 不压缩数据块

**-noF**
> 不压缩片段块（fragment）

**-no-duplicates**
> 不检测重复文件

**-all-root**
> 将所有文件设为 root 所有

**-force-uid** _uid_
> 设置所有文件的 UID

**-force-gid** _gid_
> 设置所有文件的 GID

**-regex**
> 将排除模式视为 POSIX 正则表达式

**-ignore-zeros**
> 允许拼接的 tar 归档

**-mkfs-time** _time_
> 设置文件系统创建时间

**-all-time** _time_
> 设置所有 inode 的时间戳

**-processors** _num_
> 使用的处理器数量

**-mem** _size_
> 设置内存限制

**-progress**
> 显示进度条

**-info**
> 在添加文件时打印文件名

# DESCRIPTION

**sqfstar** 直接从 stdin 读取的 tar 归档创建 squashfs 文件系统。Squashfs 是一种高压缩比的只读文件系统，支持多种压缩算法，块大小范围为 4K 到 1MB。

该工具适合将 tar 归档转换为 squashfs 而无需中间解压步骤。压缩的 tar 归档应先解压再通过管道传入（使用 zcat、xzcat 等）。可以按名称、通配符模式或正则表达式排除文件。

# CAVEATS

输入必须是 tar 格式；压缩的 tar 需要外部工具解压。Squashfs 创建后即为只读。大型归档在创建期间需要大量内存。块大小会影响压缩比和随机访问性能。

# HISTORY

**sqfstar** 是 **squashfs-tools** 的一部分，由 **Phillip Lougher** 创建。添加 sqfstar 工具是为了提供无需中间文件、直接将 tar 转换为 squashfs 的能力。Squashfs 广泛用于 Linux 发行版的 Live 系统、snap 软件包和容器镜像。

# INSTALL

```apt: sudo apt install squashfs-tools```

```dnf: sudo dnf install squashfs-tools```

```pacman: sudo pacman -S squashfs-tools```

```apk: sudo apk add squashfs-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mksquashfs](/man/mksquashfs)(1), [unsquashfs](/man/unsquashfs)(1), [sqfscat](/man/sqfscat)(1), [tar](/man/tar)(1)
