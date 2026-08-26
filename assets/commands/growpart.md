# TAGLINE

扩展分区以填满可用空间

# TLDR

**扩展**第 n 个分区，填满直到磁盘末尾的空闲空间

```growpart /dev/sdX [n]```

显示将要进行的修改（**dry run**）

```growpart -N /path/to/disk.img [n]```

# SYNOPSIS

**growpart** [_options_] _disk_ _partition-number_

# PARAMETERS

**-N**, **--dry-run**
> 显示将要执行的操作而不实际修改

**-u**, **--update** _TYPE_
> 更新类型：auto、growfs、off

**-v**, **--verbose**
> 启用详细输出

**-h**, **--help**
> 显示帮助消息

# DESCRIPTION

**growpart** 将一个分区扩展到磁盘上紧随其后的可用空闲空间。它常用于扩大虚拟磁盘或云盘卷之后，使新增的空间可供该分区使用。

该工具既适用于物理磁盘（如 /dev/sda），也适用于磁盘映像文件。它会自动处理 MBR 和 GPT 两种分区方案的分区表更新。

扩展分区之后，通常还需要用 **resize2fs**（ext4）、**xfs_growfs**（XFS）或 **btrfs filesystem resize**（Btrfs）等工具调整其中文件系统的大小。

# CAVEATS

只能将分区扩展到紧随其后的空闲空间。如果分区后面还有其他分区，则必须先移动那些分区才能扩展。调整根分区大小时需要卸载或使用 live 系统。

# HISTORY

growpart 属于 cloud-utils 软件包，由 Canonical 为 Ubuntu 开发，在云环境中被广泛使用。它的出现是为了简化虚拟磁盘扩容后扩展分区的常见任务。

# INSTALL

```dnf: sudo dnf install cloud-utils-growpart```

```apk: sudo apk add cloud-utils-growpart```

```zypper: sudo zypper install growpart```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fdisk](/man/fdisk)(8), [parted](/man/parted)(8), [resize2fs](/man/resize2fs)(8)
