# TAGLINE

在现有卷组中创建逻辑卷

# TLDR

创建 **10 GB** 的卷

```sudo lvcreate -L 10G vg1```

创建**命名**卷

```sudo lvcreate -L 1500M -n mylv vg1```

使用卷组的 **60%**

```sudo lvcreate -l 60%VG -n mylv vg1```

使用**全部空闲**空间

```sudo lvcreate -l 100%FREE -n mylv vg1```

# SYNOPSIS

**lvcreate** [_OPTIONS_] _VolumeGroup_

# DESCRIPTION

**lvcreate** 在现有卷组中创建逻辑卷。逻辑卷是可跨多个物理卷的虚拟块设备，支持快照、条带化和镜像等特性。

# PARAMETERS

**-L, --size** _size_
> 指定大小（例如 10G、1500M）

**-l, --extents** _extents_
> 以 extent 数量或百分比指定大小（%VG、%FREE、%PVS）

**-n, --name** _name_
> 逻辑卷的名称

**-s, --snapshot**
> 创建快照卷

**-T, --thin**
> 创建精简池或精简卷

**--thinpool** _pool_
> 为精简卷指定精简池

**-m, --mirrors** _count_
> 创建镜像卷

**-i, --stripes** _count_
> 条带化卷的条带数量

# CAVEATS

卷组必须有足够的空闲空间。逻辑卷名称在卷组内必须唯一。创建之后，必须先在 LV 上建立文件系统才能挂载。

# HISTORY

**lvcreate** 是 **LVM2**（Linux 逻辑卷管理器）的一部分。

# INSTALL

```apt: sudo apt install lvm2```

```dnf: sudo dnf install lvm2```

```pacman: sudo pacman -S lvm2```

```apk: sudo apk add lvm2```

```zypper: sudo zypper install lvm2```

```nix: nix profile install nixpkgs#lvm2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lvm](/man/lvm)(8), [lvextend](/man/lvextend)(8), [lvremove](/man/lvremove)(8), [vgcreate](/man/vgcreate)(8)
