# TAGLINE

从硬盘、存储卡和其他存储介质中恢复被删除的文件

# TLDR

对**设备**运行 PhotoRec

```sudo photorec /dev/sdb```

对**磁盘镜像**运行 PhotoRec

```sudo photorec [path/to/image.dd]```

带**日志文件**和自定义恢复目录运行

```sudo photorec /log /d [path/to/recovery] /dev/sdb```

# SYNOPSIS

**photorec** [**/log**] [**/debug**] [**/d** _directory_] _device_|_image_

# PARAMETERS

**/log**
> 创建 photorec.log 文件

**/debug**
> 在日志中附加调试信息

**/d _directory_**
> 恢复文件的目标目录

# DESCRIPTION

**photorec** 通过扫描文件特征（文件雕刻）从硬盘、存储卡和其他存储介质中恢复被删除的文件。它不理会文件系统，即使介质严重损坏或已被重新格式化也能工作。

该工具可识别 480 多种文件格式，包括图像、视频、文档和归档。它以文本交互模式运行，引导用户完成分区选择和恢复选项设置。

# CAVEATS

恢复出的文件要写到与被恢复磁盘不同的驱动器上。原始文件名不会保留。扫描大容量驱动器可能耗时很久。在已挂载的文件系统上运行可能造成进一步的数据丢失。

# HISTORY

**photorec** 由 **Christophe Grenier** 创建，是 **TestDisk** 的配套工具。它最初专注于照片恢复（名字由此而来），后来扩展为可恢复多种文件类型。它是 TestDisk 软件包的一部分，被广泛用于数据恢复。

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

[testdisk](/man/testdisk)(8), [foremost](/man/foremost)(1), [scalpel](/man/scalpel)(1)
