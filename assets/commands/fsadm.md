# TAGLINE

LVM 文件系统管理工具

# TLDR

**检查**文件系统错误

```fsadm check /dev/vg_name/lv_name```

**试运行**调整到指定大小

```fsadm -n resize /dev/vg_name/lv_name 10G```

将文件系统**扩容**至占满设备

```fsadm resize /dev/vg_name/lv_name```

同时调整文件系统**与逻辑卷**的大小

```fsadm -l resize /dev/vg_name/lv_name 100G```

**离线**调整 ext2/3/4 文件系统大小

```fsadm -e resize /dev/vg_name/lv_name 20G```

# SYNOPSIS

**fsadm** [_options_] **check** _device_

**fsadm** [_options_] **resize** _device_ [_newsize_]

# DESCRIPTION

**fsadm** 用于检查或调整 LVM 逻辑卷上文件系统的大小。它是一个辅助脚本，封装了 resize2fs、xfs_growfs 和 fsck 等针对特定文件系统的工具。

# PARAMETERS

**check**
> 检查文件系统错误。

**resize**
> 调整文件系统大小（扩大或缩小）。

**-n, --dry-run**
> 只打印将要执行的操作而不实际更改。

**-l, --lvresize**
> 同时调整底层逻辑卷的大小。

**-e, --ext-offline**
> 卸载 ext2/3/4 文件系统并离线调整大小。

**-f, --force**
> 无需确认强制执行操作。

**-v, --verbose**
> 详细模式。

**-y, --yes**
> 对所有提示自动回答 yes。

# CAVEATS

resize 时若未指定大小，文件系统将被扩容至占满整个设备。缩小文件系统需要谨慎规划，且可能需要卸载。并非所有文件系统都支持缩小（例如 XFS）。

# HISTORY

**fsadm** 是 **LVM2** 的一部分，为逻辑卷上的文件系统操作提供统一接口，无论底层文件系统类型是什么。

# INSTALL

```apt: sudo apt install lvm2```

```dnf: sudo dnf install lvm2```

```pacman: sudo pacman -S lvm2```

```apk: sudo apk add lvm2-extra```

```zypper: sudo zypper install lvm2```

```nix: nix profile install nixpkgs#lvm2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lvresize](/man/lvresize)(8), [resize2fs](/man/resize2fs)(8), [fsck](/man/fsck)(8)
