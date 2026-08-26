# TAGLINE

以读写支持挂载 NTFS 文件系统

# TLDR

**挂载 NTFS 分区**

```ntfs-3g [/dev/sda1] [/mnt/windows]```

**只读挂载**

```ntfs-3g -o ro [/dev/sda1] [/mnt/windows]```

**指定权限挂载**

```ntfs-3g -o uid=[1000],gid=[1000] [/dev/sda1] [/mnt]```

**指定 umask 挂载**

```ntfs-3g -o umask=[022] [/dev/sda1] [/mnt]```

**强制挂载脏卷**

```ntfs-3g -o force [/dev/sda1] [/mnt]```

# SYNOPSIS

**ntfs-3g** [_options_] _device_ _mount_point_

# PARAMETERS

_DEVICE_
> NTFS 分区设备。

_MOUNT_POINT_
> 挂载位置。

**-o** _OPTIONS_
> 挂载选项。

**ro**
> 只读挂载。

**force**
> 强制挂载。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ntfs-3g** 以读写支持挂载 NTFS 文件系统，是基于 FUSE 的驱动。

该工具让 Linux 能够访问 NTFS，具备完整的读写能力。

# CAVEATS

基于 FUSE。Windows 使用前可能需要先卸载。需要相应权限。

# HISTORY

ntfs-3g 的创建目的是通过 FUSE 在 Linux 上提供**完整的 NTFS 读写**支持。

# INSTALL

```apt: sudo apt install ntfs-3g```

```dnf: sudo dnf install ntfs-3g```

```pacman: sudo pacman -S ntfs-3g```

```apk: sudo apk add ntfs-3g```

```zypper: sudo zypper install ntfs-3g```

```brew: brew install ntfs-3g```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mount](/man/mount)(1), [ntfsfix](/man/ntfsfix)(1), [fusermount](/man/fusermount)(1)
