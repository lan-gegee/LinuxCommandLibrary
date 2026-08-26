# TAGLINE

通过 FUSE 使用 GRUB 的驱动程序挂载文件系统

# TLDR

将块设备或文件系统镜像**挂载**到挂载点

```grub-mount [/dev/sdXY] [/mnt]```

从磁盘镜像挂载**特定分区**

```grub-mount -r [2] [disk.img] [/mnt]```

以密码提示方式挂载**加密**设备

```grub-mount -C [/dev/sdXY] [/mnt]```

从文件加载 **ZFS 加密密钥**

```grub-mount -K [path/to/zfs.key] [/dev/sdX] [/mnt]```

启用**详细输出**

```grub-mount -v [image] [/mnt]```

# SYNOPSIS

**grub-mount** [_options_] _device_ _mountpoint_

# PARAMETERS

**-r**, **--root** _PARTITION_
> 指定要从磁盘镜像挂载的分区号

**-C**, **--crypto**
> 启用加密设备支持，会提示输入密码

**-K**, **--zfs-key** _FILE_
> 从指定文件加载 ZFS 加密密钥

**-d**, **--debug** _STRING_
> 显示匹配类别的调试输出

**-v**, **--verbose**
> 启用详细输出

**--version**
> 显示版本信息

# DESCRIPTION

**grub-mount** 通过 FUSE 使用 GRUB 内置的文件系统驱动程序以只读方式挂载文件系统或磁盘镜像。这适用于访问 GRUB 支持但宿主操作系统可能不支持的文件系统，或检查启动镜像。

该工具支持多种文件系统，包括 ext2/3/4、XFS、Btrfs、ZFS、FAT、NTFS 和 ISO9660。配合适当的选项还可以处理加密卷。

# CAVEATS

所有挂载均为只读。要求宿主系统支持 FUSE。某些高级文件系统特性可能不被完全支持。加密卷需要相应的密钥或密码。

# HISTORY

grub-mount 是 GRUB 2 的一部分，基于 GRUB 的文件系统驱动程序提供 FUSE 挂载接口。它让管理员无需内核支持所有文件系统类型即可访问和验证启动环境。

# INSTALL

```apt: sudo apt install grub-common```

```apk: sudo apk add grub-mount```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[grub-probe](/man/grub-probe)(8), [grub-install](/man/grub-install)(8), [grub-mkconfig](/man/grub-mkconfig)(8), [mount](/man/mount)(8), [fusermount](/man/fusermount)(1)
