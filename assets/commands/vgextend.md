# TAGLINE

向卷组添加物理卷

# TLDR

**添加**单个设备

```sudo vgextend vg1 /dev/sda1```

添加**多个**设备

```sudo vgextend vg1 /dev/sda1 /dev/sdb1```

# SYNOPSIS

**vgextend** [_OPTIONS_] _VolumeGroupName_ _PhysicalVolume_...

# DESCRIPTION

**vgextend** 将一个或多个物理卷添加到现有卷组。这会增加可用于在该组内创建或扩展逻辑卷的总空间。

# PARAMETERS

**-f, --force**
> 强制扩展，无需确认

**-y, --yes**
> 对所有提示回答 yes

**-A, --autobackup** _y|n_
> 更改后自动备份元数据

**--restoremissing**
> 恢复曾被移除的物理卷

# CAVEATS

物理卷必须先用 pvcreate 初始化。一个物理卷同一时间只能属于一个卷组。添加设备不会自动重新分布已有数据。

# HISTORY

**vgextend** 是 **LVM2**（Linux 逻辑卷管理器）的一部分。

# INSTALL

```apt: sudo apt install lvm2```

```dnf: sudo dnf install lvm2```

```pacman: sudo pacman -S lvm2```

```apk: sudo apk add lvm2```

```zypper: sudo zypper install lvm2```

```nix: nix profile install nixpkgs#lvm2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lvm](/man/lvm)(8), [vgcreate](/man/vgcreate)(8), [vgreduce](/man/vgreduce)(8), [pvcreate](/man/pvcreate)(8)
