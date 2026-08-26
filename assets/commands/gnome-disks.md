# TAGLINE

图形化磁盘管理工具

# TLDR

**启动 GNOME Disks**

```gnome-disks```

**打开指定的块设备**

```gnome-disks --block-device [/dev/sda]```

**恢复磁盘镜像**

```gnome-disks --restore-disk-image [image.img]```

# SYNOPSIS

**gnome-disks** [_options_]

# PARAMETERS

**--block-device** _DEVICE_
> 打开指定的块设备（如 /dev/sda）。

**--restore-disk-image** _FILE_
> 恢复磁盘镜像。

**--format-device**
> 为指定的块设备打开格式化对话框（与 --block-device 配合使用）。

**--xid** _XID_
> 对话框的父窗口 XID。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gnome-disks** 是 GNOME 桌面的图形化磁盘管理工具。它通过易用的 GTK 界面管理磁盘、分区、文件系统和 RAID 阵列。

该工具可执行格式化、挂载、镜像制作和性能基准测试。它与 udisks2 集成以执行特权操作，并支持加密卷。

# CAVEATS

GTK 应用程序需要图形环境。某些操作需要 root 权限。属于 GNOME 实用工具的一部分。

# HISTORY

GNOME Disks 作为 **GNOME** 项目的一部分开发，用一个现代化的集成工具取代了旧的磁盘管理工具。

# INSTALL

```apt: sudo apt install gnome-disk-utility```

```dnf: sudo dnf install gnome-disk-utility```

```pacman: sudo pacman -S gnome-disk-utility```

```apk: sudo apk add gnome-disk-utility```

```zypper: sudo zypper install gnome-disk-utility```

```nix: nix profile install nixpkgs#gnome-disk-utility```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[udisksctl](/man/udisksctl)(1), [fdisk](/man/fdisk)(1), [parted](/man/parted)(1), [lsblk](/man/lsblk)(1)
