# TAGLINE

备份 LVM 卷组元数据

# TLDR

备份**所有**卷组

```sudo vgcfgbackup```

备份**指定**卷组

```sudo vgcfgbackup [vg_name]```

备份到**文件**

```sudo vgcfgbackup -f [path/to/backup] [vg_name]```

用模板备份**多个**卷组

```sudo vgcfgbackup -f [/tmp/vg-backup-%s] [vg1] [vg2]```

**详细**输出

```sudo vgcfgbackup -v [vg_name]```

# SYNOPSIS

**vgcfgbackup** [_OPTIONS_] [_VG_NAME_...]

# PARAMETERS

**-f, --file** _FILE_
> 将备份写入指定的文件

**-v, --verbose**
> 提高输出详细程度（可重复使用）

# DESCRIPTION

**vgcfgbackup** 将 LVM 卷组的配置元数据备份到文件。它备份的是卷组结构，而非逻辑卷中包含的实际用户数据。

默认情况下，备份写入 /etc/lvm/backup/。文件名中的 %s 占位符会被替换为卷组名称。

# CAVEATS

只备份元数据，不备份数据。需要 root 权限。备份文件应安全地存放在被备份系统之外。

# INSTALL

```apt: sudo apt install lvm2```

```dnf: sudo dnf install lvm2```

```pacman: sudo pacman -S lvm2```

```apk: sudo apk add lvm2```

```zypper: sudo zypper install lvm2```

```nix: nix profile install nixpkgs#lvm2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vgcfgrestore](/man/vgcfgrestore)(8), [vgdisplay](/man/vgdisplay)(8), [lvm](/man/lvm)(8)
