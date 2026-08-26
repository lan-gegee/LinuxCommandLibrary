# TAGLINE

创建 squashfs 文件系统以及向其追加内容

# TLDR

从文件和目录创建 **squashfs 文件系统**

```mksquashfs [path/to/source1] [path/to/source2] [filesystem.squashfs]```

使用指定的**压缩算法**创建 squashfs

```mksquashfs [path/to/source] [filesystem.squashfs] -comp [gzip|lzo|lz4|xz|zstd]```

**排除**特定文件或目录

```mksquashfs [path/to/source] [filesystem.squashfs] -e [file_or_dir1] [file_or_dir2]```

排除匹配**通配符模式**的文件

```mksquashfs [path/to/source] [filesystem.squashfs] -wildcards -e "[*.gz]"```

排除匹配**正则表达式模式**的文件

```mksquashfs [path/to/source] [filesystem.squashfs] -regex -e "[pattern]"```

设置自定义**块大小**（默认 128 KB，最大 1 MB）

```mksquashfs [path/to/source] [filesystem.squashfs] -b [256K]```

创建**全新的**文件系统而不追加

```mksquashfs [path/to/source] [filesystem.squashfs] -noappend```

# SYNOPSIS

**mksquashfs** _source1_ [_source2_...] _filesystem_ [**-comp** _method_] [**-b** _blocksize_] [**-e** _excludes_] [_options_]

# PARAMETERS

**-comp _method_**
> 压缩算法：gzip（默认）、lzo、lz4、xz、zstd、lzma

**-b _size_**
> 数据块大小；默认 128 KB，最大 1 MB。支持 K/M 后缀

**-e _items_**
> 排除指定的文件和目录

**-wildcards**
> 为排除规则启用 glob 模式匹配

**-regex**
> 为排除规则使用 POSIX 正则表达式

**-all-root**
> 使所有文件归 root 所有

**-force-uid _user_**
> 覆盖文件的属主用户

**-force-gid _group_**
> 覆盖文件的属主组

**-processors _num_**
> 压缩线程数

**-mem _size_**
> 设置缓存内存大小

**-noI**
> 禁用 inode 压缩

**-noD**
> 禁用数据压缩

**-noF**
> 禁用片段（fragment）压缩

**-noX**
> 禁用扩展属性压缩

**-no-compression**
> 禁用所有压缩

**-noappend**
> 不追加到已有文件系统；而是新建一个

**-info**
> 打印写入文件系统的文件

**-no-recovery**
> 不生成恢复文件

**-recover _file_**
> 使用恢复文件恢复文件系统

**-xattrs**
> 存储扩展属性（默认）

**-no-xattrs**
> 不存储扩展属性

**-tar**
> 从标准输入读取未压缩的 tar 归档

**-quiet**
> 抑制详细输出

**-progress**
> 显示进度条

# DESCRIPTION

**mksquashfs** 创建 squashfs 文件系统以及向其追加内容。Squashfs 是一种高压缩比的只读文件系统，常用于 Live CD、嵌入式系统和应用打包（AppImage、snap）。

该工具使用可配置的算法压缩文件、inode 和目录。它支持去重、扩展属性和稀疏文件的高效存储。块压缩使得可以随机访问压缩数据。

# CAVEATS

Squashfs 文件系统是只读的，且需要 squashfs 内核模块。向已有归档追加可能增加碎片。极高的压缩级别会显著增加创建时间。最大文件大小取决于块大小配置。

# HISTORY

**Squashfs** 由 **Phillip Lougher** 创建，首次发布于 **2002 年**。它在 **2.6.29 版（2009 年）**合入 Linux 内核主线。这种文件系统在 Linux 发行版中广泛用于 Live 介质、容器镜像和只读根文件系统。

# INSTALL

```apt: sudo apt install squashfs-tools```

```dnf: sudo dnf install squashfs-tools```

```pacman: sudo pacman -S squashfs-tools```

```apk: sudo apk add squashfs-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[unsquashfs](/man/unsquashfs)(1), [sqfscat](/man/sqfscat)(1), [mount](/man/mount)(8)
