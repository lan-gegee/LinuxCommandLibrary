# TAGLINE

恢复丢失的分区和引导扇区

# TLDR

交互式**启动 testdisk**

```sudo testdisk```

**分析指定磁盘**

```sudo testdisk [/dev/sdX]```

**分析磁盘镜像**文件

```testdisk [path/to/image.dd]```

恢复期间**创建日志文件**

```sudo testdisk /log [/dev/sdX]```

**列出设备上的分区**

```sudo testdisk /list [/dev/sdX]```

**将原始扇区转储**到日志

```sudo testdisk /dump [/dev/sdX]```

**显示版本**并退出

```testdisk /version```

# SYNOPSIS

**testdisk** [_/log_] [_/debug_] [_/list_] [_/dump_] [_/version_] [_device|image_]

# PARAMETERS

**/log**
> 将所有操作和分析结果追加到当前目录的 **testdisk.log** 中。

**/debug**
> 启用调试模式并输出更多详细信息。

**/list**
> 显示指定设备或镜像的分区信息后退出。

**/dump**
> 将原始扇区内容转储到日志中，供事后检查。

**/version**
> 打印 TestDisk 版本后退出。

**device**
> 要分析的磁盘设备（例如 **/dev/sda**、**/dev/nvme0n1**）。

**image**
> 要分析的磁盘镜像文件，用于代替物理设备。

# DESCRIPTION

**TestDisk** 是一款强大的开源数据恢复工具，旨在恢复丢失的分区和修复引导扇区。它可以还原分区表、恢复被删除的分区、重建 FAT 和 NTFS 的引导扇区，并修复损坏的文件系统。

TestDisk 支持多种文件系统，包括 FAT12/FAT16/FAT32、NTFS、exFAT、ext2/ext3/ext4、HFS/HFS+、JFS、ReiserFS、XFS 等。它兼容多种分区表类型，包括 DOS/MBR、GPT、Mac 和 BSD disklabel。

该工具运行于基于 ncurses 的交互式菜单中，引导用户完成恢复过程。TestDisk 还通过其 Advanced（高级）菜单提供文件恢复功能，可以从受支持的文件系统中恢复被删除的文件。

# CAVEATS

操作物理磁盘设备需要 root 权限。恢复文件时务必保存到另一个磁盘或分区，以免覆盖尚可恢复的数据。TestDisk 主要是一个分区恢复工具；若要从受损分区做文件级恢复，可考虑它的姊妹工具 **photorec**。

# HISTORY

TestDisk 由 **Christophe Grenier** 创建，最初是一个 DOS 分区修复工具，这解释了它 **/flag** 风格的命令行语法。该项目后来并入 **CGSecurity** 并以 GPL 开源。它与 **PhotoRec** 一同发布，后者是一款无视文件系统的文件雕刻（file carving）工具。

# INSTALL

```apt: sudo apt install testdisk```

```dnf: sudo dnf install testdisk```

```pacman: sudo pacman -S testdisk```

```apk: sudo apk add testdisk```

```zypper: sudo zypper install testdisk```

```brew: brew install testdisk```

```nix: nix profile install nixpkgs#testdisk```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[photorec](/man/photorec)(1), [fdisk](/man/fdisk)(8), [gdisk](/man/gdisk)(8), [fsck](/man/fsck)(8), [ddrescue](/man/ddrescue)(1)
