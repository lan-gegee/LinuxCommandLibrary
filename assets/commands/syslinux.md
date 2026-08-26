# TAGLINE

FAT 文件系统引导加载程序安装器

# TLDR

**在 FAT 文件系统上安装 SYSLINUX**

```syslinux -i [/dev/sdb1]```

**安装到 USB 驱动器**并写入 MBR

```syslinux -i -m -a [/dev/sdb1]```

**安装到子目录**

```syslinux -i -d [/boot/syslinux] [/dev/sdb1]```

**更新已有安装**

```syslinux -U [/dev/sdb1]```

以 RAID 模式**安装**

```syslinux -i -r [/dev/sdb1]```

**强制安装**

```syslinux -f -i [/dev/sdb1]```

为有缺陷的 BIOS **安装安全/慢速版本**

```syslinux -s -i [/dev/sdb1]```

# SYNOPSIS

**syslinux** [_options_] _device_

# PARAMETERS

**-i**, **--install**
> 安装 SYSLINUX，覆盖之前的任何引导加载程序。

**-U**, **--update**
> 更新已有的 SYSLINUX 安装。

**-s**, **--stupid**
> 为有缺陷的 BIOS 安装安全、慢速的版本。

**-f**, **--force**
> 即使看起来不安全也强制安装。

**-r**, **--raid**
> RAID 模式：失败时引导下一个设备。

**-d**, **--directory** _subdir_
> 将控制文件安装到指定的子目录。

**-a**, **--active**
> 将分区标记为活动（可引导）分区。

**-m**, **--mbr**
> 安装主引导记录（MBR）代码。

**--offset** _bytes_
> 文件系统在磁盘映像中的字节偏移。

**-t**, **--type** _type_
> 显式指定文件系统类型。

**-z**, **--zipdrive**
> 假定使用 ZIP 驱动器的几何参数。

**-h**, **--help**
> 显示帮助信息。

**-v**, **--version**
> 显示版本信息。

# DESCRIPTION

**syslinux** 在 FAT 文件系统上安装 SYSLINUX 引导加载程序。SYSLINUX 是一个轻量级引导加载程序，设计用于从 MS-DOS FAT 文件系统引导 Linux，常用于 USB 驱动器和救援介质。

该引导加载程序由引导扇区和 **ldlinux.sys** 文件组成。配置通过 **syslinux.cfg** 完成，其中指定内核镜像和引导参数。

对于 ext2/3/4 和 btrfs 文件系统，请改用 **extlinux**。自 4.00 版起，EXTLINUX 与 SYSLINUX 共享同一代码库。

安装完成后，在安装目录中创建 syslinux.cfg 文件以配置引导项。

# CONFIGURATION

**syslinux.cfg**
> 引导配置文件，指定内核镜像、引导参数、菜单项和超时设置。位于 FAT 文件系统的根目录或安装子目录中。

# CAVEATS

只支持 FAT12、FAT16 和 FAT32 文件系统。安装时设备不能处于挂载状态，否则需使用 -f 标志。仅支持 BIOS 引导；UEFI 系统需要其他工具。某些 BIOS 可能需要 -s 选项才能兼容。

# HISTORY

**SYSLINUX** 由 H. Peter Anvin 自 1994 年开始开发。它逐步演化为一个引导加载程序家族，包括 ISOLINUX（用于光盘）、PXELINUX（用于网络引导）和 EXTLINUX（用于 Linux 文件系统）。该项目为可引导 USB 驱动器等特定场景提供了比 LILO 和 GRUB 更简单的选择。

# INSTALL

```apt: sudo apt install syslinux```

```dnf: sudo dnf install syslinux```

```pacman: sudo pacman -S syslinux```

```apk: sudo apk add syslinux```

```zypper: sudo zypper install syslinux```

```nix: nix profile install nixpkgs#syslinux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[grub-install](/man/grub-install)(1), [dd](/man/dd)(1), [mkfs.fat](/man/mkfs.fat)(8), [parted](/man/parted)(8)
