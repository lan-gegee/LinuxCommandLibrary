# TAGLINE

报告 LVM 卷组信息

# TLDR

**列出**卷组

```sudo vgs```

列出**所有**卷组

```sudo vgs -a```

**详细**输出

```sudo vgs -v```

显示**特定**字段

```sudo vgs -o vg_name,vg_size,vg_free```

**追加**字段

```sudo vgs -o +field_name```

**无标题行**

```sudo vgs --noheadings```

使用**分隔符**

```sudo vgs --separator =```

# SYNOPSIS

**vgs** [_OPTIONS_] [_VolumeGroupName_...]

# DESCRIPTION

**vgs** 以可配置的表格格式显示卷组信息，包括卷组名称、物理卷数量、逻辑卷数量、大小以及剩余空间。

# PARAMETERS

**-a, --all**
> 显示所有卷组，包括不完整的卷组

**-v, --verbose**
> 提高输出详细程度并显示更多细节

**-o, --options** _fields_
> 指定要显示的字段

**--noheadings**
> 不输出标题行

**--separator** _char_
> 使用指定字符作为字段分隔符

**--units** _units_
> 以指定单位显示大小

# CAVEATS

不完整的卷组（缺少物理卷）默认被隐藏；使用 -a 可显示它们。默认输出为人类可读格式；编写脚本时请使用格式化选项。

# HISTORY

**vgs** 是 **LVM2**（Linux 逻辑卷管理器）的一部分。

# INSTALL

```apt: sudo apt install lvm2```

```dnf: sudo dnf install lvm2```

```pacman: sudo pacman -S lvm2```

```apk: sudo apk add lvm2```

```zypper: sudo zypper install lvm2```

```nix: nix profile install nixpkgs#lvm2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lvm](/man/lvm)(8), [vgdisplay](/man/vgdisplay)(8), [pvs](/man/pvs)(8), [lvs](/man/lvs)(8)
