# TAGLINE

初始化磁盘以供 LVM 使用

# TLDR

将分区**初始化**为物理卷

```sudo pvcreate /dev/[sda1]```

一次**初始化多个**设备

```sudo pvcreate /dev/[sdb1] /dev/[sdc1]```

**强制**创建且不出现确认提示

```sudo pvcreate -ff /dev/[sda1]```

以指定的**元数据大小**初始化

```sudo pvcreate --metadatasize [512k] /dev/[sda1]```

# SYNOPSIS

**pvcreate** [_OPTIONS_] _PhysicalVolume_...

# DESCRIPTION

**pvcreate** 初始化磁盘或分区，使其可用作 LVM 中的物理卷。这会将 LVM 元数据写入设备，为其加入卷组做好准备。

# PARAMETERS

**-f, --force**
> 覆盖各种检查、确认和保护机制。使用两次（`-ff`）可强制覆盖已有的物理卷。

**-y, --yes**
> 自动对所有提示回答 yes。

**-Z, --zero** _y|n_
> 控制是否擦除设备的前 4 个扇区（2048 字节）。默认为 yes，除非指定了 `--restorefile` 或 `--uuid`。

**--metadatasize** _size_
> 为 PV 上每个元数据区域预留的大致空间量。

**--metadatacopies** _0|1|2_
> 该 PV 上元数据区域的副本数量。0 表示不存储副本，1 表示仅在前部存储，2 表示在前部和末尾都存储。

**--metadataignore** _y|n_
> 是否忽略该 PV 上的元数据区域。在创建大量 PV 时很有用，可以限制元数据副本的数量。

**--dataalignment** _size_
> 将数据区的起始位置对齐到该大小的倍数。

**--dataalignmentoffset** _size_
> 将数据区的起始位置额外偏移此数值。

**-u, --uuid** _uuid_
> 为物理卷指定 UUID。不带此选项时会生成随机 UUID。使用 vgcfgrestore 恢复元数据时需要此选项。

**--restorefile** _file_
> 使用备份文件中的元数据，以确保恢复卷组时 PV 的位置一致。

**--bootloaderareasize** _size_
> 在 LVM 元数据和第一个物理区块之间为引导加载程序预留空间。

**--labelsector** _number_
> 写入 LVM2 标签的扇区号（默认 1）。

**--setphysicalvolumesize** _size_
> 覆盖自动检测到的设备大小。

**-v, --verbose**
> 设置详细级别。最多可重复使用 4 次以增加详细程度。

# CAVEATS

设备上的所有现有数据都会被销毁。设备不应处于挂载或使用状态。物理卷必须先创建才能加入卷组。使用 `-ff` 会跳过对已有文件系统签名的检查。

# HISTORY

**pvcreate** 是 **LVM2**（Linux 逻辑卷管理器）的一部分。

# INSTALL

```apt: sudo apt install lvm2```

```dnf: sudo dnf install lvm2```

```pacman: sudo pacman -S lvm2```

```apk: sudo apk add lvm2```

```zypper: sudo zypper install lvm2```

```nix: nix profile install nixpkgs#lvm2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lvm](/man/lvm)(8), [vgcreate](/man/vgcreate)(8), [pvdisplay](/man/pvdisplay)(8), [pvremove](/man/pvremove)(8), [pvs](/man/pvs)(8), [pvscan](/man/pvscan)(8), [lvcreate](/man/lvcreate)(8)
