# TAGLINE

保存 ext 文件系统元数据镜像

# TLDR

将元数据写入**文件**

```e2image [/dev/sdXN] [path/to/image_file]```

将元数据打印到**标准输出**

```e2image [/dev/sdXN] -```

**恢复**元数据到设备

```e2image -I [/dev/sdXN] [path/to/image_file]```

创建**原始稀疏**镜像

```e2image -r [/dev/sdXN] [path/to/image_file]```

创建 **QCOW2** 镜像

```e2image -Q [/dev/sdXN] [path/to/image_file]```

创建目录项已**打乱**的原始镜像（用于提交 bug 报告）

```e2image -r -s [/dev/sdXN] - | bzip2 > [hda1.e2i.bz2]```

# SYNOPSIS

**e2image** [_options_] _device_ _image-file_

# DESCRIPTION

**e2image** 将关键的 ext2/ext3/ext4 文件系统元数据保存到文件。这对于备份文件系统结构以备灾难恢复，或调试文件系统损坏问题很有用。

镜像文件只包含元数据（超级块、块组、inode 表等），不含文件内容，因此比完整备份小得多。这让文件系统专家无需访问实际数据或复制整个文件系统就能诊断问题。

# PARAMETERS

**-I**
> 将元数据从镜像恢复到设备

**-r**
> 创建原始稀疏镜像（元数据位于正确的偏移处）

**-Q**
> 创建 QCOW2 格式镜像

**-a**
> 包含所有数据（而不仅是元数据）

**-f**
> 即使文件系统已挂载也强制操作（结果可能不可靠）

**-s**
> 打乱目录项并将未使用的目录块部分清零

**-o** _src_offset_
> 文件系统在源设备上的起始字节偏移

**-O** _dest_offset_
> 写入前在目标文件中定位到的偏移

**-b** _blocksize_
> 设置文件系统块大小（字节）（通常自动检测）

**-p**
> 写入前比较块；跳过相同的块（对闪存存储有用）

# CAVEATS

默认不备份文件内容。属于 e2fsprogs。适用于调试和恢复场景。QCOW2 格式与 QEMU 兼容。-f 标志允许对已挂载的文件系统成像，但结果很可能不可靠。

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

[dumpe2fs](/man/dumpe2fs)(8), [e2fsck](/man/e2fsck)(8), [debugfs](/man/debugfs)(8), [tune2fs](/man/tune2fs)(8)
