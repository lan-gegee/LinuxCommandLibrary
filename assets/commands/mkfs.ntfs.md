# TAGLINE

在设备或文件上创建 NTFS 文件系统

# TLDR

在设备 X 的分区 Y 内创建 **NTFS 文件系统**

```sudo mkfs.ntfs [/dev/sdXY]```

创建带**卷标**的 NTFS 文件系统

```sudo mkfs.ntfs -L [volume_label] [/dev/sdXY]```

创建带**随机 UUID** 的 NTFS 文件系统

```sudo mkfs.ntfs -U [/dev/sdXY]```

执行**快速格式化**（跳过清零和坏扇区检查）

```sudo mkfs.ntfs -f [/dev/sdXY]```

启用文件系统的**压缩**

```sudo mkfs.ntfs -C [/dev/sdXY]```

创建带指定**簇大小**的 NTFS 文件系统

```sudo mkfs.ntfs -c [4096] [/dev/sdXY]```

**模拟**格式化而不写入设备

```sudo mkfs.ntfs -n [/dev/sdXY]```

# SYNOPSIS

**mkfs.ntfs** [**-f**|**-Q**] [**-c** _cluster-size_] [**-L** _label_] [**-C**] [**-U**] [**-n**] [**-q**|**-v**] _device_ [_number-of-sectors_]

# PARAMETERS

**-f, -Q, --fast, --quick**
> 执行快速格式化；跳过卷清零和坏扇区检查

**-L, --label _string_**
> 设置文件系统的卷标

**-C, --enable-compression**
> 启用文件系统级压缩

**-U, --with-uuid**
> 生成随机卷 UUID

**-c, --cluster-size _bytes_**
> 设置簇大小，范围为 256 到 2,097,152 字节；默认为 4096

**-s, --sector-size _bytes_**
> 设置扇区大小：256、512、1024、2048 或 4096 字节

**-p, --partition-start _sector_**
> 指定分区起始扇区

**-H, --heads _num_**
> 磁头数；要使 Windows 可引导则必须设置

**-S, --sectors-per-track _num_**
> 每磁道扇区数；要使 Windows 可引导则必须设置

**-z, --mft-zone-multiplier _num_**
> MFT 区大小倍数（1-4）；影响碎片行为

**-I, --no-indexing**
> 禁用卷上的内容索引

**-n, --no-action**
> 模拟格式化而不实际写入更改

**-q, --quiet**
> 抑制非错误输出

**-v, --verbose**
> 启用详细输出

# DESCRIPTION

**mkfs.ntfs**（也称 **mkntfs**）在设备或文件上创建 NTFS 文件系统。NTFS 是 Windows NT 及后续版本使用的主要文件系统，支持文件权限、压缩、加密和大容量卷等特性。

省略扇区数时，该工具会自动确定文件系统大小。它会创建 NTFS 所需的主文件表（MFT）、系统文件和目录结构。该工具属于 **ntfs-3g** 软件包。

# CAVEATS

由于各 Windows 版本与 mkntfs 之间的 Unicode 版本差异，Windows chkdsk 可能报告大写文件名警告。对于可引导的 Windows 分区，必须正确设置 -H 和 -S 选项。Linux 上的 NTFS 写入支持需要 ntfs-3g 驱动。

# HISTORY

NTFS 由 **微软** 开发，随 **1993 年的 Windows NT 3.1** 引入。它取代 FAT 成为 Windows 的主要文件系统。Linux 的 ntfs-3g 驱动和 mkfs.ntfs 工具由 **NTFS-3G** 项目开发，为 Linux 系统提供对 NTFS 卷可靠的读写访问。

# INSTALL

```apt: sudo apt install ntfs-3g```

```dnf: sudo dnf install ntfs-3g```

```pacman: sudo pacman -S ntfs-3g```

```apk: sudo apk add ntfs-3g-progs```

```zypper: sudo zypper install ntfs-3g```

```brew: brew install ntfs-3g```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mkfs](/man/mkfs)(8), [mkfs.ext4](/man/mkfs.ext4)(8), [mkfs.vfat](/man/mkfs.vfat)(8), [ntfs-3g](/man/ntfs-3g)(8), [ntfsfix](/man/ntfsfix)(8), [fdisk](/man/fdisk)(8), [mount](/man/mount)(8), [badblocks](/man/badblocks)(8)
