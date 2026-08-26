# TAGLINE

报告物理卷信息

# TLDR

**列出**物理卷

```sudo pvs```

列出**全部**设备，包括非物理卷

```sudo pvs -a```

**详细输出**

```sudo pvs -v```

显示**特定**字段

```sudo pvs -o pv_name,vg_name,pv_size```

**追加**字段

```sudo pvs -o +field_name```

**不显示表头**

```sudo pvs --noheadings```

使用**分隔符**

```sudo pvs --separator =```

# SYNOPSIS

**pvs** [_OPTIONS_] [_PhysicalVolume_...]

# DESCRIPTION

**pvs** 以可配置的表格形式显示物理卷信息。它显示每个物理卷的设备名、卷组、大小和可用空间。

# PARAMETERS

**-a**, **--all**
> 显示不是物理卷的设备

**-v**, **--verbose**
> 提高详细程度并显示额外信息

**-o**, **--options** _fields_
> 指定要显示的字段

**--noheadings**
> 不在输出中显示表头行

**--separator** _char_
> 使用指定字符作为字段分隔符

**--units** _units_
> 以指定单位显示大小

# CAVEATS

不属于任何卷组的物理卷会显示空的 VG 字段。使用 -a 可以查看可能成为物理卷的设备。

# HISTORY

**pvs** 是 **LVM2**（Linux 逻辑卷管理器）的一部分。

# INSTALL

```apt: sudo apt install lvm2```

```dnf: sudo dnf install lvm2```

```pacman: sudo pacman -S lvm2```

```apk: sudo apk add lvm2```

```zypper: sudo zypper install lvm2```

```nix: nix profile install nixpkgs#lvm2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lvm](/man/lvm)(1), [pvdisplay](/man/pvdisplay)(1), [lvs](/man/lvs)(1), [vgs](/man/vgs)(1)
