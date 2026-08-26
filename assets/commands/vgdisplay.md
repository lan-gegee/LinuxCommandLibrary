# TAGLINE

显示 LVM 卷组信息

# TLDR

**显示**所有卷组的信息

```sudo vgdisplay```

**显示**特定卷组的信息

```sudo vgdisplay [vg1]```

# SYNOPSIS

**vgdisplay** [_options_] [_volume_group_...]

# PARAMETERS

**-c, --colon**
> 以冒号分隔的格式输出

**-s, --short**
> 简短的列表格式

**-v, --verbose**
> 详细输出，包含额外信息

**-A, --activevolumegroups**
> 只显示活动卷组

**--units _units_**
> 以指定单位显示大小（b、s、k、m、g、t、p、e）

**-C, --columns**
> 按列输出（类似 vgs）

# DESCRIPTION

**vgdisplay** 显示 LVM 卷组的详细信息，包括大小、区块（extent）信息以及其中包含的物理卷和逻辑卷。

输出包括总大小、物理区块大小、物理卷和逻辑卷的数量以及分配状态。用它来了解 LVM 配置的结构和容量。

# CAVEATS

需要 root 权限。脚本处理建议改用支持格式选项的 **vgs**。属于 LVM2 软件包。

# INSTALL

```apt: sudo apt install lvm2```

```dnf: sudo dnf install lvm2```

```pacman: sudo pacman -S lvm2```

```apk: sudo apk add lvm2```

```zypper: sudo zypper install lvm2```

```nix: nix profile install nixpkgs#lvm2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lvm](/man/lvm)(8), [vgs](/man/vgs)(8), [vgchange](/man/vgchange)(8), [lvdisplay](/man/lvdisplay)(8), [pvdisplay](/man/pvdisplay)(8)
