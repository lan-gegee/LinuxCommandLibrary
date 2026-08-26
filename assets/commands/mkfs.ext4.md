# TAGLINE

在设备上创建 ext4 文件系统

# TLDR

创建 **ext4** 文件系统

```sudo mkfs.ext4 /dev/sdXY```

创建带**卷标**的文件系统

```sudo mkfs.ext4 -L [label] /dev/sdXY```

创建时**减少保留块**（1% 而非 5%）

```sudo mkfs.ext4 -m [1] /dev/sdXY```

以指定的**块大小**创建

```sudo mkfs.ext4 -b [4096] /dev/sdXY```

指定**所有者**和 UUID 创建

```sudo mkfs.ext4 -E root_owner=[uid]:[gid] -U [uuid] /dev/sdXY```

**安静**模式创建（适合脚本使用）

```sudo mkfs.ext4 -q /dev/sdXY```

# SYNOPSIS

**mkfs.ext4** [_options_] _device_ [_blocks-count_]

# DESCRIPTION

**mkfs.ext4** 在设备上创建 ext4 文件系统。ext4 是 Linux 的默认文件系统，提供日志功能、大文件支持和出色的性能。它等价于 **mke2fs -t ext4**。

# PARAMETERS

**-L** _LABEL_
> 设置卷标（最长 16 个字符）。

**-b** _BLOCKSIZE_
> 以字节为单位设置块大小（1024、2048 或 4096）。

**-m** _PERCENT_
> 为超级用户保留块的百分比（默认：5%）。

**-i** _BYTES_PER_INODE_
> 设置每 inode 的字节比率。

**-N** _INODES_
> 设置 inode 数量。

**-U** _UUID_
> 设置文件系统 UUID。

**-E** _OPTIONS_
> 扩展选项（逗号分隔），例如 root_owner=uid:gid、discard、stride=N、stripe-width=N。

**-O** _FEATURES_
> 设置文件系统特性（逗号分隔），例如 ^has_journal、extent、dir_index。

**-T** _USAGE_TYPE_
> 指定用途类型（如 largefile、largefile4、news、small）以设置默认参数。

**-c**
> 创建文件系统前检查设备上的坏块。

**-cc**
> 执行较慢的破坏性读写坏块测试。

**-n**
> 试运行；显示将要执行的操作但不实际创建文件系统。

**-F**
> 即使设备不是块特殊设备或看起来正在使用中也强制创建。

**-q**
> 安静模式执行。

# CAVEATS

设备上的所有数据都将丢失。本工具是 e2fsprogs 软件包的一部分。非根文件系统的默认保留块（5%）可用 **-m** 减少。使用两次 **-F** 可强制在已挂载的设备上创建。等价于 **mke2fs -t ext4**。

# INSTALL

```apt: sudo apt install e2fsprogs```

```dnf: sudo dnf install e2fsprogs```

```pacman: sudo pacman -S e2fsprogs```

```apk: sudo apk add e2fsprogs```

```zypper: sudo zypper install e2fsprogs```

```brew: brew install e2fsprogs```

```nix: nix profile install nixpkgs#e2fsprogs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mkfs](/man/mkfs)(8), [tune2fs](/man/tune2fs)(8), [e2fsck](/man/e2fsck)(8), [mke2fs](/man/mke2fs)(8)
