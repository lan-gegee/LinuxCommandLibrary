# TAGLINE

从设备上移除 LVM 标签

# TLDR

从物理卷上**移除** LVM 标签

```sudo pvremove [/dev/sdXY]```

以**详细输出**方式移除

```sudo pvremove -v [/dev/sdXY]```

**不经确认**直接移除

```sudo pvremove -y [/dev/sdXY]```

**强制**移除

```sudo pvremove -f [/dev/sdXY]```

以 **JSON** 格式输出

```sudo pvremove --reportformat json [/dev/sdXY]```

# SYNOPSIS

**pvremove** [**-v**] [**-y**] [**-f**] [**--reportformat** _format_] _PhysicalVolume_...

# PARAMETERS

**-v, --verbose**
> 操作过程中显示详细输出

**-y, --yes**
> 对所有提示回答 yes

**-f, --force**
> 即使出现警告也强制移除

**--reportformat _format_**
> 输出格式（basic、json）

# DESCRIPTION

**pvremove** 从物理卷上移除 LVM 标签，实质上是将其从 LVM 中取消初始化。移除后，该设备不再被识别为 LVM 物理卷。

移除时设备不能属于任何卷组。请先使用 vgreduce 将物理卷从其卷组中移除。

# CAVEATS

需要 root 权限。设备必须不在卷组中。物理卷上的数据不会被擦除，只有 LVM 元数据会被移除。误用强制选项可能导致数据丢失。

# HISTORY

**pvremove** 是 **LVM2**（逻辑卷管理器）的一部分。它是对 pvcreate 的补充，提供将物理卷退出 LVM 管理的途径。

# INSTALL

```apt: sudo apt install lvm2```

```dnf: sudo dnf install lvm2```

```pacman: sudo pacman -S lvm2```

```apk: sudo apk add lvm2```

```zypper: sudo zypper install lvm2```

```nix: nix profile install nixpkgs#lvm2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pvcreate](/man/pvcreate)(8), [vgreduce](/man/vgreduce)(8), [pvdisplay](/man/pvdisplay)(8)
