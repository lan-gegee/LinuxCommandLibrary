# TAGLINE

在其所属卷组内重命名逻辑卷

# TLDR

使用**完整路径**重命名

```sudo lvrename /dev/vg_name/old_lv /dev/vg_name/new_lv```

使用 **VG 名和 LV 名**重命名

```sudo lvrename [vg_name] [old_lv] [new_lv]```

以**自动确认**方式重命名

```sudo lvrename --yes /dev/vg_name/old_lv /dev/vg_name/new_lv```

# SYNOPSIS

**lvrename** [_options_] _vg_/_old_lv_ _new_lv_

# DESCRIPTION

**lvrename** 在其所属卷组内重命名逻辑卷。重命名操作期间卷可以保持激活状态。

# PARAMETERS

**-y, --yes**
> 对所有提示回答 yes

**-A, --autobackup y|n**
> 更改后自动备份元数据（默认 y）。

**--noudevsync**
> 禁用 udev 同步

**-t, --test**
> 测试模式（不应用更改）

**-v, --verbose**
> 详细输出

# CAVEATS

请更新 /etc/fstab 以及所有引用旧 LV 名称的脚本。活动文件系统在重命名后可能需要重新挂载。

# INSTALL

```apt: sudo apt install lvm2```

```dnf: sudo dnf install lvm2```

```pacman: sudo pacman -S lvm2```

```apk: sudo apk add lvm2```

```zypper: sudo zypper install lvm2```

```nix: nix profile install nixpkgs#lvm2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lvcreate](/man/lvcreate)(8), [lvremove](/man/lvremove)(8), [lvm](/man/lvm)(8)
