# TAGLINE

从卷组中移除逻辑卷

# TLDR

移除**指定的**卷

```sudo lvremove volume_group/logical_volume```

移除组内的**所有**卷

```sudo lvremove volume_group```

# SYNOPSIS

**lvremove** [_OPTIONS_] _LogicalVolume_...

# DESCRIPTION

**lvremove** 从卷组中移除逻辑卷。逻辑卷在移除前必须处于关闭状态（已卸载）。此操作会永久销毁逻辑卷上的所有数据。

# PARAMETERS

**-f, --force**
> 强制移除而不确认

**-y, --yes**
> 对所有提示回答 yes

**--noudevsync**
> 跳过 udev 同步

# CAVEATS

逻辑卷上的所有数据将永久丢失。移除前确保已有备份。必须先卸载卷且不在使用中。移除卷不会移除其所在的卷组。

# HISTORY

**lvremove** 是 **LVM2**（Linux 逻辑卷管理器）的一部分。

# INSTALL

```apt: sudo apt install lvm2```

```dnf: sudo dnf install lvm2```

```pacman: sudo pacman -S lvm2```

```apk: sudo apk add lvm2```

```zypper: sudo zypper install lvm2```

```nix: nix profile install nixpkgs#lvm2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lvm](/man/lvm)(8), [lvcreate](/man/lvcreate)(8), [vgremove](/man/vgremove)(8)
