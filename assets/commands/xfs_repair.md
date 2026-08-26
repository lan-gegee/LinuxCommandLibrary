# TAGLINE

修复 XFS 文件系统

# TLDR

**修复**分区

```sudo xfs_repair [path/to/partition]```

# SYNOPSIS

**xfs_repair** [_OPTIONS_] _DEVICE_

# PARAMETERS

**-n**
> 不修改模式（仅检查）

**-L**
> 强制清零日志（有数据丢失风险）

**-v**
> 详细输出

**-d**
> 危险修复（允许修复已挂载的文件系统）

**-m** _MAXMEM_
> 最大内存用量

# DESCRIPTION

**xfs_repair** 用于修复 XFS 文件系统。它会检查并修复文件系统的元数据、目录结构和分配信息。

修复前必须先卸载文件系统。可能需要先执行日志重放。

# CAVEATS

需要卸载文件系统。使用 -L 可能导致数据丢失。修复前请备份重要数据。可能需要运行多次。

# INSTALL

```apt: sudo apt install xfsprogs```

```dnf: sudo dnf install xfsprogs```

```pacman: sudo pacman -S xfsprogs```

```apk: sudo apk add xfsprogs```

```zypper: sudo zypper install xfsprogs```

```nix: nix profile install nixpkgs#xfsprogs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xfs_admin](/man/xfs_admin)(8), [fsck](/man/fsck)(8), [mkfs.xfs](/man/mkfs.xfs)(8)
