# TAGLINE

创建 MS-DOS FAT 文件系统

# TLDR

**创建 FAT 文件系统**

```mkdosfs [/dev/sdb1]```

**创建 FAT32**

```mkdosfs -F [32] [/dev/sdb1]```

**创建 FAT16**

```mkdosfs -F [16] [/dev/sdb1]```

**设置卷标**

```mkdosfs -n "[LABEL]" [/dev/sdb1]```

**详细输出**

```mkdosfs -v [/dev/sdb1]```

**在镜像文件中创建 FAT 文件系统**

```mkdosfs -C [disk.img] [size_in_blocks]```

**检查坏块**

```mkdosfs -c [/dev/sdb1]```

# SYNOPSIS

**mkdosfs** [_options_] _device_

# PARAMETERS

_DEVICE_
> 块设备或镜像文件。

**-F** _SIZE_
> FAT 大小（12、16 或 32）。

**-n** _LABEL_
> 卷标。

**-c**
> 创建文件系统前检查坏块。

**-C**
> 创建以 DEVICE 命名的文件并将文件系统写入其中（用于镜像文件）。

**-I**
> 允许格式化没有分区表的整个磁盘设备（超级软盘格式）。

**-s** _SECTORS_
> 每个簇的磁盘扇区数（必须是 2 的幂）。

**-S** _SIZE_
> 每逻辑扇区的字节数（512、1024、2048 等）。

**-v**
> 详细输出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mkdosfs** 创建 MS-DOS FAT 文件系统。它将设备格式化为 FAT12、FAT16 或 FAT32。

该工具也称为 mkfs.fat。用于 U 盘和兼容性场景。

# CAVEATS

会破坏现有数据。请选择正确的 FAT 类型。需要 root 权限。

# HISTORY

mkdosfs 属于 **dosfstools**，为 Linux 提供 FAT 文件系统创建功能。

# INSTALL

```apt: sudo apt install dosfstools```

```dnf: sudo dnf install dosfstools```

```pacman: sudo pacman -S dosfstools```

```apk: sudo apk add dosfstools```

```zypper: sudo zypper install dosfstools```

```brew: brew install dosfstools```

```nix: nix profile install nixpkgs#dosfstools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mkfs.fat](/man/mkfs.fat)(8), [mkfs](/man/mkfs)(8), [dosfslabel](/man/dosfslabel)(8), [fatlabel](/man/fatlabel)(8)
