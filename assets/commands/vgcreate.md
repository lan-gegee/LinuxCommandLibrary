# TAGLINE

创建 LVM 卷组

# TLDR

用**单个**设备创建卷组

```sudo vgcreate volume_group /dev/sda1```

用**多个**设备创建

```sudo vgcreate volume_group /dev/sda1 /dev/sdb1```

# SYNOPSIS

**vgcreate** [_OPTIONS_] _VolumeGroupName_ _PhysicalVolume_...

# DESCRIPTION

**vgcreate** 通过组合一个或多个物理卷创建新的卷组。卷组是分配逻辑卷的存储池，提供灵活的存储管理。

# PARAMETERS

**-s, --physicalextentsize** _size_
> 卷组的物理区块（extent）大小

**-p, --maxphysicalvolumes** _count_
> 物理卷的最大数量

**-l, --maxlogicalvolumes** _count_
> 逻辑卷的最大数量

**-A, --autobackup** _y|n_
> 自动备份元数据

**--clustered** _y|n_
> 创建集群化的卷组

# CAVEATS

物理卷必须先用 pvcreate 初始化。卷组名称在系统内必须唯一。将设备添加到卷组后，即形成一个用于创建逻辑卷的统一存储池。

# HISTORY

**vgcreate** 是 **LVM2**（Linux 逻辑卷管理器）的一部分。

# INSTALL

```apt: sudo apt install lvm2```

```dnf: sudo dnf install lvm2```

```pacman: sudo pacman -S lvm2```

```apk: sudo apk add lvm2```

```zypper: sudo zypper install lvm2```

```nix: nix profile install nixpkgs#lvm2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lvm](/man/lvm)(8), [pvcreate](/man/pvcreate)(8), [lvcreate](/man/lvcreate)(8), [vgextend](/man/vgextend)(8)
