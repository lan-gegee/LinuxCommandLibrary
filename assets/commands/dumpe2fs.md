# TAGLINE

ext2/ext3/ext4 文件系统信息转储工具

# TLDR

显示**文件系统信息**

```sudo dumpe2fs /dev/sdXN```

仅显示**坏块**

```sudo dumpe2fs -b /dev/sdXN```

遇到无法识别的特性也**强制**显示

```sudo dumpe2fs -f /dev/sdXN```

仅显示**超级块**信息

```sudo dumpe2fs -h /dev/sdXN```

以**十六进制**显示块号

```sudo dumpe2fs -x /dev/sdXN```

# SYNOPSIS

**dumpe2fs** [_-bfghixV_] [_-o superblock=superblock_] [_-o blocksize=blocksize_] _device_

# DESCRIPTION

**dumpe2fs** 打印 ext2、ext3 和 ext4 文件系统的超级块和块组信息。它显示详细的文件系统元数据，包括特性、块数量和分配信息。

# PARAMETERS

**-b**
> 只打印被标记为坏块的块

**-f**
> 即使存在无法识别的特性标志也强制显示

**-g**
> 以冒号分隔格式显示块组描述符信息

**-h**
> 仅显示超级块信息，不含块组细节

**-i**
> 从镜像文件显示文件系统数据

**-o superblock=NUM**
> 使用位于块 NUM 处的备用超级块

**-o blocksize=SIZE**
> 搜索超级块时指定块大小

**-x**
> 以十六进制格式显示块号

**-V**
> 显示版本信息

# CAVEATS

dumpe2fs 只**读取**磁盘，因此在已挂载的文件系统上运行是安全的，但它打印的数字会略微过时：磁盘上的超级块落后于内核的内存副本，空闲块和 inode 计数可能不准确。如果数字必须精确，请先卸载。

输出很长，而你真正想要的通常是 **-h**：仅超级块就能给出块大小、inode 数量、特性标志、挂载次数和 UUID，省去好几页块组细节。

**-b** 列出的不是新扫描出的坏块。它打印的是文件系统坏块 inode 中已记录的块，而这些记录只有在有东西写入时才会存在，通常来自 `mke2fs -c` 或 `e2fsck -c`。因此结果为空表示"没有记录"，而不是"不存在"。

一个实用场景是从损坏的主超级块中恢复：`dumpe2fs` 会打印备用超级块的位置，这正是 `e2fsck -b` 随后需要的。

# HISTORY

**dumpe2fs** 属于 **e2fsprogs**——由 **Theodore Ts'o** 自 **1993 年**起维护至今的 ext2/3/4 工具套件。它是 `tune2fs` 的对应物：tune2fs 修改文件系统参数，dumpe2fs 展示这些参数，两者加起来几乎覆盖了在不挂载的情况下你对 ext 文件系统所能询问或设定的一切。该工具历经两次文件系统版本演进几乎没有变化，因为 ext3 和 ext4 都保留了 ext2 的磁盘布局，只是向超级块的特性标志中添加了新特性。

# INSTALL

```apt: sudo apt install e2fsprogs```

```dnf: sudo dnf install e2fsprogs```

```pacman: sudo pacman -S e2fsprogs```

```apk: sudo apk add e2fsprogs-extra```

```zypper: sudo zypper install e2fsprogs```

```brew: brew install e2fsprogs```

```nix: nix profile install nixpkgs#e2fsprogs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tune2fs](/man/tune2fs)(8), [e2fsck](/man/e2fsck)(8), [mke2fs](/man/mke2fs)(8), [debugfs](/man/debugfs)(8), [resize2fs](/man/resize2fs)(8), [blkid](/man/blkid)(8)

# RESOURCES

```[Source code](https://git.kernel.org/pub/scm/fs/ext2/e2fsprogs.git)```

```[Homepage](http://e2fsprogs.sourceforge.net)```

<!-- verified: 2026-07-14 -->
