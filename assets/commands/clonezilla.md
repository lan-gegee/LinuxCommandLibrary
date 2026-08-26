# TAGLINE

磁盘克隆与镜像方案

# TLDR

**启动 Clonezilla 并进入交互模式**

```clonezilla```

**将磁盘保存为镜像**

```ocs-sr -q2 -c -j2 -z1p -i 2000 -fsck-y -senc -p reboot savedisk [image_name] [sda]```

**将镜像恢复到磁盘**

```ocs-sr -g auto -e1 auto -e2 -r -j2 -c -p reboot restoredisk [image_name] [sda]```

**磁盘对磁盘克隆**

```ocs-onthefly -g auto -e1 auto -e2 -r -j2 -sfsck -k -p reboot -f [sda] -d [sdb]```

**将分区保存为镜像**

```ocs-sr -q2 -c -j2 -z1p -i 2000 -fsck-y -senc -p reboot saveparts [image_name] [sda1]```

**列出可用镜像**

```ocs-sr -l```

# SYNOPSIS

**ocs-sr** [_options_] _action_ _image_name_ _device_

# PARAMETERS

**savedisk** _name_ _disk_
> 将整个磁盘保存为镜像。

**restoredisk** _name_ _disk_
> 将镜像恢复到磁盘。

**saveparts** _name_ _parts_
> 将分区保存为镜像。

**restoreparts** _name_ _parts_
> 从镜像恢复分区。

**-q2**
> 使用 partclone 进行镜像。

**-c**
> 操作前确认。

**-j2**
> 克隆 MBR 与分区之间的隐藏数据。

**-z1p**
> 使用并行 gzip 压缩。

**-i** _size_
> 将镜像拆分为指定 MB 大小的文件。

**-fsck-y**
> 自动运行 fsck。

**-senc**
> 加密镜像。

**-g auto**
> 自动重装 grub。

**-p** _action_
> 完成后的动作：reboot、poweroff 或 choose。

# DESCRIPTION

**Clonezilla** 是一款类似 Norton Ghost 的磁盘克隆与镜像方案。它可以为整块磁盘或分区创建备份镜像，并将其还原到相同或不同的硬件上。

Clonezilla 从 USB 或 CD 启动到一个带有专门镜像工具的 Linux 环境。它通过只复制已使用的块来高效地对文件系统（ext4、NTFS、HFS+ 等）成像。原始模式则支持任何文件系统。

有两种模式可用：用于单机镜像的 **Clonezilla Live**，以及通过 PXE 启动进行网络大规模部署的 **Clonezilla SE（Server Edition）**。

# SUPPORTED FILESYSTEMS

**Linux**: ext2/3/4, XFS, Btrfs, JFS, ReiserFS
**Windows**: NTFS, FAT12/16/32, exFAT
**macOS**: HFS+, APFS (limited)
**Others**: UFS, VMFS, minix

# CAVEATS

差分镜像要求目标磁盘/分区不小于源盘。加密分区可能需要原始模式（镜像更大）。UEFI 和 Secure Boot 可能需要额外配置。网络部署需要 DHCP 和 TFTP 基础设施。

# HISTORY

Clonezilla 由台湾**国家高速网络与计算中心**的 **Steven Shiau** 和 DRBL（Diskless Remote Boot in Linux）项目创建，于 **2004 年**首次发布。它构建在 Partclone、Partimage 等开源工具之上，成为流行的商业磁盘镜像方案的免费替代品。Live 版和 Server 版至今仍在积极开发中。

# INSTALL

```pacman: sudo pacman -S clonezilla```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dd](/man/dd)(1), [partclone](/man/partclone)(8), [rsync](/man/rsync)(1), [ddrescue](/man/ddrescue)(1)
