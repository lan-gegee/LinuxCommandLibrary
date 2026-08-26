# TAGLINE

从卷组中移除物理卷

# TLDR

**从卷组中移除物理卷**

```sudo vgreduce [vg_name] [/dev/sdb]```

**移除所有空的物理卷**

```sudo vgreduce -a [vg_name]```

**移除缺失的物理卷**

```sudo vgreduce --removemissing [vg_name]```

**强制移除含部分逻辑卷的缺失物理卷**

```sudo vgreduce --removemissing --force [vg_name]```

**测试移除而不实际更改**

```sudo vgreduce -t [vg_name] [/dev/sdb]```

# SYNOPSIS

**vgreduce** [_options_] _volume_group_ [_physical_volume_...]

# PARAMETERS

**-a**, **--all**
> 移除所有空的物理卷。

**--removemissing**
> 移除缺失（故障）的物理卷。

**--mirrorsonly**
> 只从镜像逻辑卷中移除缺失的物理卷。

**-f**, **--force**
> 强制移除，必要时删除不完整的逻辑卷。

**-t**, **--test**
> 测试模式；不做实际更改。

**-v**, **--verbose**
> 详细输出。

**-y**, **--yes**
> 对提示自动回答 yes。

# DESCRIPTION

**vgreduce** 从卷组中移除物理卷，缩小其容量。被移除的物理卷随后可用于其他卷组，或从系统中彻底清除。

移除之前，请用 pvdisplay 确认该物理卷上没有数据。如果存在数据，先用 pvmove 将其迁移到其他物理卷。vgreduce 之后，使用 pvremove 清除磁盘上的 LVM 元数据。

--removemissing 选项用于处理已不存在故障磁盘。配合 --force 使用时，会删除数据位于缺失磁盘上的所有逻辑卷。

# CAVEATS

未经 pvmove 无法移除含有活动数据的物理卷。强制移除会销毁受影响逻辑卷上的数据。建议在执行强制操作前先使用测试模式。被移除的物理卷需用 pvremove 清理后才能复用。

# HISTORY

**vgreduce** 是 LVM2（逻辑卷管理器）的一部分，LVM2 由 Linux 2.4 中的原始 LVM 演进而来。LVM2 提供灵活的磁盘管理，支持存储的动态调整大小。vgreduce 命令可以从卷组中无损地移除存储设备。

# INSTALL

```apt: sudo apt install lvm2```

```dnf: sudo dnf install lvm2```

```pacman: sudo pacman -S lvm2```

```apk: sudo apk add lvm2```

```zypper: sudo zypper install lvm2```

```nix: nix profile install nixpkgs#lvm2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vgextend](/man/vgextend)(8), [vgdisplay](/man/vgdisplay)(8), [pvmove](/man/pvmove)(8), [pvremove](/man/pvremove)(8), [lvm](/man/lvm)(8)
