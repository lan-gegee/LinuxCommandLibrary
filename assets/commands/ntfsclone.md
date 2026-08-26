# TAGLINE

高效地克隆、镜像、恢复或抢救 NTFS 卷

# TLDR

**将 NTFS 分区克隆到镜像文件**

```ntfsclone --output [clone.img] [/dev/sda1]```

**保存为节省空间的特殊镜像格式**

```ntfsclone --save-image --output [clone.img] [/dev/sda1]```

**从特殊镜像恢复到分区**

```ntfsclone --restore-image --output [/dev/sda1] [clone.img]```

**仅克隆元数据（用于调试）**

```ntfsclone --metadata --output [meta.img] [/dev/sda1]```

**克隆到 stdout 并用 gzip 压缩**

```ntfsclone --save-image -o - [/dev/sda1] | gzip -c > [clone.img.gz]```

**抢救故障磁盘（读错误时继续）**

```ntfsclone --rescue --output [rescue.img] [/dev/sda1]```

# SYNOPSIS

**ntfsclone** [_options_] _source_

# PARAMETERS

**-o**, **--output** _FILE_
> 输出文件或设备。使用 **-** 表示标准输出。

**-O**, **--overwrite** _FILE_
> 覆盖已存在的文件或设备（写入分区时必须使用）。

**-s**, **--save-image**
> 保存为特殊的 ntfsclone 镜像格式（只复制已使用的簇）。

**-r**, **--restore-image**
> 从特殊的 ntfsclone 镜像恢复。

**-m**, **--metadata**
> 仅克隆 NTFS 元数据（用于调试；结果仍可挂载）。

**--rescue**
> 遇到磁盘读取错误时继续，用零填充坏扇区。

**--ignore-fs-check**
> 忽略文件系统一致性检查的结果。

**-f**, **--force**
> 即使卷被标记为脏也强制克隆。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ntfsclone** 将 NTFS 文件系统高效地克隆到稀疏文件、特殊镜像、设备或标准输出。它在簇级别工作且只复制已使用的数据，因此比 **dd** 这类扇区级工具快得多，也更节省空间。

特殊镜像格式（**--save-image**）用控制码编码未使用的空间而不是实际存储它们，从而产生显著更小的备份文件。这类镜像只能用 **ntfsclone --restore-image** 恢复，无法直接挂载。

**--rescue** 模式专为濒临损坏的磁盘设计，以对硬件压力最小的方式读取数据，并用零填充不可读的扇区。

# CAVEATS

属于 ntfs-3g 软件包的一部分。特殊镜像文件不可挂载，只能用 ntfsclone 恢复。克隆到分区时，目标分区必须不小于源分区。克隆期间应卸载该卷。

# HISTORY

**ntfsclone** 作为 **ntfs-3g**（前身为 ntfsprogs）的一部分开发，用于在 Linux 系统上高效备份和恢复 NTFS。

# INSTALL

```apt: sudo apt install ntfs-3g```

```dnf: sudo dnf install ntfs-3g```

```pacman: sudo pacman -S ntfs-3g```

```apk: sudo apk add ntfs-3g-progs```

```zypper: sudo zypper install ntfs-3g```

```brew: brew install ntfs-3g```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ntfsresize](/man/ntfsresize)(1), [ntfs-3g](/man/ntfs-3g)(1), [ntfsfix](/man/ntfsfix)(1), [dd](/man/dd)(1), [partclone](/man/partclone)(1)
