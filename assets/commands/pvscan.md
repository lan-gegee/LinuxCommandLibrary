# TAGLINE

扫描并发现 LVM 物理卷

# TLDR

**列出**所有物理卷

```sudo pvscan```

显示使用某个物理卷的**卷组**

```sudo pvscan --cache --listvg [/dev/sdX]```

显示使用某个物理卷的**逻辑卷**

```sudo pvscan --cache --listlvs [/dev/sdX]```

以 **JSON** 格式输出

```sudo pvscan --reportformat json```

# SYNOPSIS

**pvscan** [**--cache**] [**--listvg**] [**--listlvs**] [**--reportformat** _format_] [_device_...]

# PARAMETERS

**--cache**
> 更新 LVM 元数据缓存

**--listvg**
> 列出指定设备所属的卷组

**--listlvs**
> 列出指定设备上的逻辑卷

**--reportformat _format_**
> 输出格式（basic、json）

**-v, --verbose**
> 详细输出

# DESCRIPTION

**pvscan** 扫描 LVM 物理卷并将其列出。它可以更新 LVM 元数据缓存，并报告特定设备上存在哪些卷组和逻辑卷。

该命令适合在添加新磁盘后发现物理卷，以及排查 LVM 配置问题。

# CAVEATS

需要 root 权限。结果取决于设备的可用性。硬件变更后可能需要更新缓存。配合 --cache 使用可实现 udev 集成。

# HISTORY

**pvscan** 是 **LVM2**（逻辑卷管理器）的一部分。它提供对动态 LVM 管理至关重要的物理卷发现功能。

# INSTALL

```apt: sudo apt install lvm2```

```dnf: sudo dnf install lvm2```

```pacman: sudo pacman -S lvm2```

```apk: sudo apk add lvm2```

```zypper: sudo zypper install lvm2```

```nix: nix profile install nixpkgs#lvm2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pvs](/man/pvs)(8), [pvdisplay](/man/pvdisplay)(8), [vgscan](/man/vgscan)(8), [lvscan](/man/lvscan)(8)
