# TAGLINE

恢复 LVM 卷组元数据

# TLDR

从**最近一次**备份恢复

```sudo vgcfgrestore [vg_name]```

从**文件**恢复

```sudo vgcfgrestore -f [path/to/file] [vg_name]```

**列出**所有备份

```sudo vgcfgrestore -l [vg_name]```

列出**特定**备份文件的内容

```sudo vgcfgrestore -l -f [path/to/file] [vg_name]```

# SYNOPSIS

**vgcfgrestore** [_OPTIONS_] _VG_NAME_

# PARAMETERS

**-f**, **--file** _FILE_
> 从指定文件读取元数据备份。

**-l**, **--list**
> 列出与该卷组相关的元数据备份和归档文件。

**--force**
> 即使存在 thin pool 逻辑卷也强制恢复元数据。使用时务必极其谨慎。

**-M**, **--metadatatype** lvm2
> 指定要使用的磁盘上元数据类型。

**-t**, **--test**
> 以测试模式运行。命令不会更新元数据。

**-d**, **--debug**
> 设置调试级别。重复使用 1 到 6 次以增加详细信息。

# DESCRIPTION

**vgcfgrestore** 从 vgcfgbackup 生成的文本备份文件中恢复 LVM 卷组配置。它恢复的是卷组结构，而非实际用户数据。

该命令适用于从元数据损坏中恢复，或在更换磁盘后重建卷组配置。

# CAVEATS

只恢复元数据，不恢复数据。需要 root 权限。物理卷必须存在，恢复才能成功。如果元数据与磁盘内容不一致，可能丢失数据。

# INSTALL

```apt: sudo apt install lvm2```

```dnf: sudo dnf install lvm2```

```pacman: sudo pacman -S lvm2```

```apk: sudo apk add lvm2```

```zypper: sudo zypper install lvm2```

```nix: nix profile install nixpkgs#lvm2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vgcfgbackup](/man/vgcfgbackup)(8), [vgdisplay](/man/vgdisplay)(8), [lvm](/man/lvm)(8)
