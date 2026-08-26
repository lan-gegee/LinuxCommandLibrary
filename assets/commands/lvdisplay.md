# TAGLINE

显示 LVM 逻辑卷的详细信息，包括大小

# TLDR

显示**所有**逻辑卷

```sudo lvdisplay```

以**短格式**显示

```sudo lvdisplay --columns```

显示**指定 VG** 中的卷

```sudo lvdisplay [vg_name]```

显示**指定的 LV**

```sudo lvdisplay [vg_name]/[lv_name]```

# SYNOPSIS

**lvdisplay** [_options_] [_vg_/_lv_...]

# DESCRIPTION

**lvdisplay** 显示 LVM 逻辑卷的详细信息，包括大小、段、状态和属性。如需紧凑列表，请改用 lvs。

# PARAMETERS

**-C**, **--columns**
> 以简短的列式格式显示（类似 lvs）

**-v**, **--verbose**
> 详细输出

**-a**, **--all**
> 显示内部逻辑卷

**--maps**
> 显示段映射信息

**--colon**
> 冒号分隔输出（已弃用）

# OUTPUT FIELDS

**LV Path**: 设备路径
**LV Name**: 逻辑卷名称
**VG Name**: 卷组名称
**LV Size**: 卷大小
**LV Status**: available/unavailable

# INSTALL

```apt: sudo apt install lvm2```

```dnf: sudo dnf install lvm2```

```pacman: sudo pacman -S lvm2```

```apk: sudo apk add lvm2```

```zypper: sudo zypper install lvm2```

```nix: nix profile install nixpkgs#lvm2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lvs](/man/lvs)(1), [lvm](/man/lvm)(1), [vgdisplay](/man/vgdisplay)(1), [pvdisplay](/man/pvdisplay)(1)
