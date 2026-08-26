# TAGLINE

在设备（通常是硬盘分区）上构建 Linux 文件系统

# TLDR

构建 **ext2** 文件系统（默认）

```sudo mkfs /dev/sdXY```

构建**指定类型**的文件系统

```sudo mkfs -t ext4 /dev/sdXY```

构建文件系统并**检查坏块**

```sudo mkfs -c -t ext4 /dev/sdXY```

构建 **XFS** 文件系统

```sudo mkfs -t xfs /dev/sdXY```

显示**详细**输出

```sudo mkfs -V -t ext4 /dev/sdXY```

# SYNOPSIS

**mkfs** [_options_] [_-t type_] [_fs-options_] _device_ [_size_]

# DESCRIPTION

**mkfs** 在设备（通常是硬盘分区）上构建 Linux 文件系统。它是一个前端封装，会调用 mkfs.ext4、mkfs.xfs 等针对特定文件系统的工具。设备可以是块设备或普通文件。

# PARAMETERS

**-t, --type TYPE**
> 指定文件系统类型（ext2、ext3、ext4、xfs、btrfs 等）；默认为 ext2

**-c**
> 构建前检查设备上的坏块

**-V, --verbose**
> 输出详细信息，包括所执行的命令

**-h, --help**
> 显示帮助文本

**-V, --version**
> 显示版本信息

# COMMON FILESYSTEM TYPES

**ext2**: 传统的 Linux 文件系统
**ext3**: 带日志功能的 ext2
**ext4**: 现代 Linux 文件系统（推荐）
**xfs**: 高性能文件系统
**btrfs**: 写时复制文件系统
**vfat**: 兼容用途的 FAT32
**ntfs**: Windows 的 NTFS 文件系统

# CAVEATS

此命令已弃用，建议改用针对特定文件系统的 mkfs 工具（mkfs.ext4、mkfs.xfs 等）。目标设备上的所有数据都将被销毁。运行前务必仔细核对设备路径。

# HISTORY

**mkfs** 属于 **util-linux**。它作为一个封装，根据指定的类型委托给相应的 mkfs.* 工具执行。

# INSTALL

```apt: sudo apt install util-linux```

```dnf: sudo dnf install util-linux```

```pacman: sudo pacman -S util-linux```

```apk: sudo apk add util-linux-misc```

```zypper: sudo zypper install util-linux```

```brew: brew install util-linux```

```nix: nix profile install nixpkgs#util-linux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mkfs.ext4](/man/mkfs.ext4)(8), [mkfs.xfs](/man/mkfs.xfs)(8), [mkfs.btrfs](/man/mkfs.btrfs)(8), [fsck](/man/fsck)(8), [mount](/man/mount)(8)
