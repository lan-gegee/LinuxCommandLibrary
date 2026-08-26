# TAGLINE

调整虚拟机磁盘分区大小

# TLDR

**调整并扩展分区以填满可用空间**

```virt-resize --expand [/dev/sda2] [olddisk.qcow2] [newdisk.qcow2]```

**扩展分区和 LVM 逻辑卷**

```virt-resize --expand [/dev/sda2] --LV-expand [/dev/vg/lv_root] [old.qcow2] [new.qcow2]```

**收缩分区**

```virt-resize --shrink [/dev/sda1] [olddisk.qcow2] [newdisk.qcow2]```

**以详细输出调整大小**

```virt-resize -v --expand [/dev/sda2] [old.qcow2] [new.qcow2]```

**将指定分区调整为精确大小**

```virt-resize --resize [/dev/sda1=20G] [old.qcow2] [new.qcow2]```

# SYNOPSIS

**virt-resize** [_options_] _indisk_ _outdisk_

# PARAMETERS

**--expand** _partition_
> 扩展分区以填满可用空间。

**--shrink** _partition_
> 收缩分区以腾出空间。

**--resize** _part=size_
> 将分区调整为精确大小。

**--LV-expand** _logvol_
> 扩展 PV 内的 LVM 逻辑卷。

**--no-expand-content**
> 不扩展文件系统，只扩展分区。

**--ntfsresize-force**
> 强制调整 NTFS 大小（针对 Windows 客户机）。

**-v**, **--verbose**
> 详细输出。

**-d**, **--debug**
> 调试输出。

**--machine-readable**
> 便于脚本处理的输出格式。

# DESCRIPTION

**virt-resize** 复制虚拟机磁盘镜像，并在过程中调整分区和文件系统的大小。与仅改变容器大小的 qemu-img resize 不同，virt-resize 会修改分区表，并且可以调整文件系统大小。

该工具无法原地调整大小；它需要一个单独的输出磁盘。先用 qemu-img create 创建目标大小的新磁盘，然后运行 virt-resize 来复制并调整内容。

支持扩展的文件系统包括 ext2/3/4、XFS、Btrfs 和 NTFS。LVM 物理卷可以扩展，特定逻辑卷可通过 --LV-expand 增长。

# CAVEATS

无法原地调整大小；需要单独的输出磁盘。虚拟机必须处于关机状态。如果分区太满，收缩可能导致数据丢失。调整前请先备份。属于 libguestfs 的一部分。

# HISTORY

**virt-resize** 是 libguestfs 的一部分，libguestfs 是一个用于访问和修改虚拟机磁盘镜像的库及工具集。Libguestfs 由 Red Hat 开发，可在虚拟机不运行的情况下进行强大的离线磁盘操作。

# INSTALL

```apt: sudo apt install guestfs-tools```

```dnf: sudo dnf install guestfs-tools```

```pacman: sudo pacman -S guestfs-tools```

```zypper: sudo zypper install guestfs-tools```

```nix: nix profile install nixpkgs#guestfs-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qemu-img](/man/qemu-img)(1), [virt-sparsify](/man/virt-sparsify)(1), [virt-customize](/man/virt-customize)(1)
