# TAGLINE

修改 LVM 物理卷属性

# TLDR

**允许**在物理卷上分配

```sudo pvchange -x y /dev/sdXN```

**禁止**在物理卷上分配

```sudo pvchange -x n /dev/sdXN```

**忽略**元数据区域

```sudo pvchange --metadataignore y /dev/sdXN```

**停止忽略**元数据区域

```sudo pvchange --metadataignore n /dev/sdXN```

为物理卷**添加标签**

```sudo pvchange --addtag mytag /dev/sdXN```

生成**新的 UUID**

```sudo pvchange --uuid /dev/sdXN```

更改**所有**可见的物理卷

```sudo pvchange -a -x y```

# SYNOPSIS

**pvchange** [_options_] _PhysicalVolume_...

# DESCRIPTION

**pvchange** 更改 LVM 中物理卷的属性。它可以控制物理卷的分配、元数据处理、标签和 UUID 生成。

# PARAMETERS

**-x, --allocatable {y|n}**
> 允许或禁止在该卷上分配物理区块（extent）

**--metadataignore {y|n}**
> 忽略或使用该物理卷上的元数据区域

**--addtag TAG**
> 为物理卷添加标签

**--deltag TAG**
> 从物理卷移除标签

**--uuid**
> 为物理卷生成新的 UUID

**-a, --all**
> 更改所有可见的物理卷

**-f, --force**
> 强制执行操作

**-v, --verbose**
> 详细模式

# CAVEATS

请谨慎使用 --uuid，因为如果卷组处于活动状态或备份引用了旧 UUID，可能会引发问题。禁用 PV 上的分配会阻止新的区块被放置在其上。

# HISTORY

**pvchange** 是 **LVM2**（逻辑卷管理器）的一部分，为 Linux 系统提供灵活的磁盘管理和存储虚拟化。

# INSTALL

```apt: sudo apt install lvm2```

```dnf: sudo dnf install lvm2```

```pacman: sudo pacman -S lvm2```

```apk: sudo apk add lvm2```

```zypper: sudo zypper install lvm2```

```nix: nix profile install nixpkgs#lvm2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pvs](/man/pvs)(8), [pvdisplay](/man/pvdisplay)(8), [pvcreate](/man/pvcreate)(8), [vgchange](/man/vgchange)(8)
