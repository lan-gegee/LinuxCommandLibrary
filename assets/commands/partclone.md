# TAGLINE

创建和还原分区镜像，并跳过空块

# TLDR

**克隆**分区到镜像文件

```sudo partclone.ext4 -c -s /dev/sdXY -o [path/to/backup.img]```

从镜像**还原**分区

```sudo partclone.ext4 -r -s [path/to/backup.img] -o /dev/sdXY```

克隆 **btrfs** 分区

```sudo partclone.btrfs -c -s /dev/sdXY -o [path/to/backup.img]```

**设备到设备**克隆

```sudo partclone.ext4 -b -s /dev/sdX1 -o /dev/sdY1```

以**救援模式**克隆（遇到读取错误后继续）

```sudo partclone.ext4 -c -R -s /dev/sdXY -o [path/to/backup.img]```

使用 **ncurses** 界面克隆

```sudo partclone.ext4 -c -N -s /dev/sdXY -o [path/to/backup.img]```

# SYNOPSIS

**partclone.**_fstype_ [**-c**|**-r**|**-b**] [**-s** _source_] [**-o** _output_] [_options_]

# COMMANDS

**partclone.ext4**
> 克隆 ext4 文件系统

**partclone.btrfs**
> 克隆 btrfs 文件系统

**partclone.ntfs**
> 克隆 NTFS 文件系统

**partclone.fat32**
> 克隆 FAT32 文件系统

**partclone.xfs**
> 克隆 XFS 文件系统

**partclone.dd**
> 原始块复制（任意文件系统）

# PARAMETERS

**-c**, **--clone**
> 将分区克隆到镜像文件。

**-r**, **--restore**
> 从镜像文件还原分区。

**-b**, **--dev-to-dev**
> 设备到设备克隆。

**-s** _source_, **--source** _source_
> 源设备或镜像文件。

**-o** _output_, **--output** _output_
> 输出设备或镜像文件。

**-L** _file_, **--logfile** _file_
> 将日志写入文件。

**-C**, **--no-check**
> 跳过克隆前的文件系统检查。

**-R**, **--rescue**
> 遇到磁盘读取错误后继续。

**-N**, **--ncurses**
> 使用 Ncurses 文本用户界面。

**-O** _file_, **--overwrite** _file_
> 输出文件，若已存在则覆盖。

**-n**, **--note** _MSG_
> 在镜像中添加备注（最多 128 个词）。

# DESCRIPTION

**partclone** 在创建和还原分区镜像时跳过空块，因此与原始磁盘映像相比，备份文件更小、速度更快。每种文件系统类型都有各自的二进制程序，能够理解对应文件系统的结构。

该工具只从源文件系统读取已使用的块，因此备份体积会显著小于分区大小。这对未存满的分区尤其有利。

# CAVEATS

克隆期间应卸载源分区。针对特定文件系统的二进制程序必须与分区类型匹配。还原出的分区可能需要运行 fsck。镜像文件不能直接挂载。

# HISTORY

**partclone** 的开发目标是作为 **dd** 之外的高效分区备份替代方案。凭借对文件系统元数据的理解，它无需外部工具就能获得压缩效果，因此在系统备份和部署场景中颇受欢迎。

# INSTALL

```dnf: sudo dnf install partclone```

```pacman: sudo pacman -S partclone```

```zypper: sudo zypper install partclone```

```nix: nix profile install nixpkgs#partclone```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dd](/man/dd)(1), [clonezilla](/man/clonezilla)(1), [fsarchiver](/man/fsarchiver)(1)
