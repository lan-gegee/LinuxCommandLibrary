# TAGLINE

在块设备上创建 Flash-Friendly File System

# TLDR

在设备 X 的分区 Y 内创建 **F2FS 文件系统**

```sudo mkfs.f2fs [/dev/sdXY]```

创建带**卷标**的 F2FS 文件系统

```sudo mkfs.f2fs -l [volume_label] [/dev/sdXY]```

创建启用**加密支持**的 F2FS 文件系统

```sudo mkfs.f2fs -O encrypt [/dev/sdXY]```

创建启用**压缩**的 F2FS 文件系统

```sudo mkfs.f2fs -O compress [/dev/sdXY]```

通过覆盖已有文件系统来**强制**创建

```sudo mkfs.f2fs -f [/dev/sdXY]```

# SYNOPSIS

**mkfs.f2fs** [**-l** _label_] [**-a** _0|1_] [**-o** _overprovision-ratio_] [**-s** _#-of-segments-per-section_] [**-z** _#-of-sections-per-zone_] [**-e** _cold-file-extensions_] [**-E** _hot-file-extensions_] [**-w** _sector-size_] [**-R** _root-uid:root-gid_] [**-f**] [**-q**] [**-O** _feature_] [**-c** _device_] _device_ [_size_]

# PARAMETERS

**-l _label_**
> 设置文件系统的卷标

**-a _0|1_**
> 是否使用基于堆的块分配方式（1 使用，0 不使用）；默认为 1

**-o _ratio_**
> 以百分比设置超配比率；默认为 5%

**-s _segments_**
> 每个 section 的 segment 数量；默认为 1

**-z _sections_**
> 每个 zone 的 section 数量；默认为 1

**-e _extensions_**
> 冷文件的扩展名（如多媒体文件）

**-E _extensions_**
> 热文件的扩展名（如数据库文件）

**-w _size_**
> 扇区大小（字节）

**-R _uid:gid_**
> 设置根目录所有者的 UID 和 GID

**-f**
> 设备上已有文件系统时强制覆盖

**-q**
> 安静模式；抑制输出消息

**-O _feature_**
> 启用文件系统特性：encrypt、compress、quota、verity、casefold

**-c _device_**
> 为多设备卷添加额外设备（最多 7 个设备）

**-t _0|1_**
> 设置 discard 策略；1 启用 discard 支持

**-d _level_**
> 设置详细输出的调试级别

**-T _timestamp_**
> 将 inode 时间戳设置为指定值

**-S**
> 启用稀疏模式以创建镜像文件

# DESCRIPTION

**mkfs.f2fs** 在块设备上创建 Flash-Friendly File System（F2FS）。F2FS 是专为 SSD、eMMC、SD 卡等闪存存储设计的现代文件系统。

该文件系统采用针对 NAND 闪存特性优化的日志结构（log-structured）设计原则，与闪存介质上的传统文件系统相比能提供更好的性能并延长设备寿命。它支持内联数据、内联目录、基于 extent 的映射和原子写入等特性。

创建文件系统时，该工具会将设备划分为 segment、section 和 zone，以便高效地进行垃圾回收和磨损均衡。超配比率正是为此预留的空间。退出状态码：成功为 0，失败为 1。

# CAVEATS

F2FS 对设备最小容量有要求，可能无法用于非常小的分区。超配比率直接影响可用空间与性能及设备寿命之间的权衡。同时启用多个特性会增加元数据开销。多设备卷要求挂载时所有设备均可用。

# HISTORY

F2FS 由 **三星电子** 开发，于 **2012 年**随 **Linux 内核 3.8** 引入。它从零开始针对闪存存储设备的独特特性而设计，注重性能优化和磨损均衡以延长设备寿命。

# INSTALL

```apt: sudo apt install f2fs-tools```

```dnf: sudo dnf install f2fs-tools```

```pacman: sudo pacman -S f2fs-tools```

```apk: sudo apk add f2fs-tools```

```zypper: sudo zypper install f2fs-tools```

```nix: nix profile install nixpkgs#f2fs-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mkfs](/man/mkfs)(8), [mkfs.ext4](/man/mkfs.ext4)(8), [mkfs.btrfs](/man/mkfs.btrfs)(8)
