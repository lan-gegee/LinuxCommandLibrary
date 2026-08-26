# TAGLINE

在设备或镜像文件上创建 MS-DOS FAT 文件系统

# TLDR

在设备 X 的分区 Y 内创建 **FAT 文件系统**

```sudo mkfs.fat [/dev/sdXY]```

创建带**卷名**的 FAT 文件系统

```sudo mkfs.fat -n [volume_name] [/dev/sdXY]```

创建带指定**卷 ID** 的 FAT 文件系统

```sudo mkfs.fat -i [volume_id] [/dev/sdXY]```

指定 **FAT 类型**（12、16 或 32 位）

```sudo mkfs.fat -F [12|16|32] [/dev/sdXY]```

使用 **4 个文件分配表**而非默认的 2 个

```sudo mkfs.fat -f 4 [/dev/sdXY]```

创建文件系统前**检查设备**坏块

```sudo mkfs.fat -c [/dev/sdXY]```

# SYNOPSIS

**mkfs.fat** [**-a**] [**-A**] [**-c**] [**-C**] [**-f** _number-of-fats_] [**-F** _fat-size_] [**-i** _volume-id_] [**-l** _bad-block-file_] [**-n** _volume-name_] [**-r** _root-entries_] [**-R** _reserved-sectors_] [**-s** _sectors-per-cluster_] [**-S** _sector-size_] [**-v**] _device_ [_block-count_]

# PARAMETERS

**-F _fat-size_**
> 指定 FAT 类型：12、16 或 32 位；省略时根据大小自动选择

**-n _volume-name_**
> 设置卷标；最长 11 个字符

**-i _volume-id_**
> 设置 32 位十六进制卷 ID

**-f _number_**
> 文件分配表的数量；默认为 2

**-s _sectors_**
> 每簇扇区数；必须是 2 的幂

**-S _size_**
> 逻辑扇区大小（字节），可选 512、1024、2048、4096、8192、16384 或 32768

**-c**
> 创建文件系统前检查设备坏块

**-l _filename_**
> 从文件读取坏块列表

**-r _entries_**
> 根目录项数量；默认为 112-512，取决于 FAT 类型

**-R _sectors_**
> 保留扇区数量；FAT12/16 默认为 1，FAT32 默认为 32

**-a**
> 禁用数据结构的对齐

**-A**
> 切换 Atari 文件系统变体

**-C**
> 创建镜像文件而不是使用设备；需要提供 block-count

**-v**
> 详细输出模式

**-b _sector_**
> FAT32 备份引导扇区的位置

**-D _number_**
> BIOS 驱动器号；硬盘用 0x80 及以上，软盘用 0x00-0x7F

**-I**
> 忽略安全检查；格式化 superfloppy 格式的磁盘时必须使用

# DESCRIPTION

**mkfs.fat** 在设备或镜像文件上创建 MS-DOS FAT 文件系统。它支持 DOS、Windows 和大多数消费电子产品所使用的 FAT12、FAT16 和 FAT32 变体。

block-count 参数以 1024 字节块为单位指定文件系统大小。省略时，工具会填满设备的可用空间。除非用 -F 显式指定，FAT 类型会根据文件系统大小自动选择。

FAT 文件系统使用文件分配表来跟踪簇的分配情况。该表的多个副本（默认 2 份）提供冗余。凭借其通用兼容性，这种文件系统至今仍广泛用于 U 盘、SD 卡和 EFI 系统分区。

# CAVEATS

卷名限制为 11 个字符。该工具不会创建可引导的文件系统。默认拒绝格式化已分区的设备；对 superfloppy 格式的磁盘可使用 -I 覆盖此安全检查。FAT32 无法存储大于 4GB 的文件。

# HISTORY

FAT 文件系统由 **微软** 自 **1977 年**起为其独立的 Disk BASIC 开发。FAT12 随 1981 年的 MS-DOS 1.0 问世，FAT16 随 1984 年的 MS-DOS 3.0 问世，FAT32 则随 1996 年的 Windows 95 OSR2 问世。mkfs.fat 工具属于 Linux 上维护的 **dosfstools** 软件包。

# INSTALL

```apt: sudo apt install dosfstools```

```dnf: sudo dnf install dosfstools```

```pacman: sudo pacman -S dosfstools```

```apk: sudo apk add dosfstools```

```zypper: sudo zypper install dosfstools```

```brew: brew install dosfstools```

```nix: nix profile install nixpkgs#dosfstools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mkfs](/man/mkfs)(8), [fatlabel](/man/fatlabel)(8), [mkfs.ext4](/man/mkfs.ext4)(8)
