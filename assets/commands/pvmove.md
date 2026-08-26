# TAGLINE

在物理卷之间迁移 LVM 数据

# TLDR

**在物理卷之间移动数据**

```pvmove [/dev/sda1] [/dev/sdb1]```

**移动物理卷上的所有数据**

```pvmove [/dev/sda1]```

**显示进度**

```pvmove -v [/dev/sda1]```

**中止移动**

```pvmove --abort```

# SYNOPSIS

**pvmove** [_options_] _source_ [_dest_]

# PARAMETERS

_SOURCE_
> 源物理卷。

_DEST_
> 目标物理卷。

**-v**
> 详细输出。

**--abort**
> 中止进行中的移动。

**-b**
> 后台模式。

**-n** _LV_
> 只移动该逻辑卷。

# DESCRIPTION

**pvmove** 在 LVM 物理卷之间迁移数据，同时逻辑卷保持在线且可访问。这实现了在线存储迁移，让管理员可以更换磁盘、重新均衡存储，或在将某个物理卷移出卷组之前先清空它。

以源和目标物理卷调用时，pvmove 会把所有物理区块（physical extent）从源迁移到目标。如果未指定目标，LVM 会自动将数据分布到同一卷组内可用的物理卷上。**-n** 选项将移动限制为特定的逻辑卷。操作可以用 **-b** 在后台运行，必要时用 **--abort** 中止。

# CAVEATS

需要 LVM。大卷时可能较慢。可中断。

# HISTORY

pvmove 是 **LVM2** 的组成部分，用于物理卷数据迁移。

# INSTALL

```apt: sudo apt install lvm2```

```dnf: sudo dnf install lvm2```

```pacman: sudo pacman -S lvm2```

```apk: sudo apk add lvm2```

```zypper: sudo zypper install lvm2```

```nix: nix profile install nixpkgs#lvm2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lvm](/man/lvm)(8), [pvcreate](/man/pvcreate)(8), [vgreduce](/man/vgreduce)(8)
