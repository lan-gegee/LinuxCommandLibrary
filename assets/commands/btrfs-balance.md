# TAGLINE

在 btrfs 设备间重新分布数据

# TLDR

**查看 balance 状态**

```sudo btrfs balance status [/mnt/data]```

**开始完整的 balance 操作**

```sudo btrfs balance start [/mnt/data]```

**平衡利用率低的数据块组**（在后台进行）

```sudo btrfs balance start --bg -dusage=[15] [/mnt/data]```

**平衡元数据并限制块组数量**

```sudo btrfs balance start -musage=[20],limit=[10] [/mnt/data]```

**转换 RAID 配置档**

```sudo btrfs balance start -dconvert=[raid6] -mconvert=[raid1c3] [/mnt/data]```

**取消正在运行的 balance 操作**

```sudo btrfs balance cancel [/mnt/data]```

# SYNOPSIS

**btrfs balance** _command_ [_OPTIONS_] _path_

# DESCRIPTION

**btrfs balance** 在 btrfs 文件系统的各设备之间重新分布数据和元数据。它作用于块组（chunk），移动其中的内容，以实现更均匀的分布或在 RAID 配置档之间转换。

常见用例包括：添加或移除设备后重新平衡、从一种 RAID 级别转换为另一种，以及通过合并部分使用的块组来回收空间。过滤器可以针对特定的块组类型（数据、元数据、系统）和使用率阈值，避免不必要的工作。

# PARAMETERS

**start**
> 开始一次 balance 操作

**status**
> 显示正在运行或已暂停的 balance 的状态

**cancel**
> 取消正在运行的 balance

**pause**
> 暂停正在运行的 balance

**resume**
> 恢复已暂停的 balance

**-d** _filters_
> 将过滤器应用于数据块组

**-m** _filters_
> 将过滤器应用于元数据块组

**-s** _filters_
> 将过滤器应用于系统块组

**--bg, --background**
> 在后台运行

**usage=** _percent_
> 仅平衡使用率低于该百分比的块组

**limit=** _count_
> 最多处理这么多个块组

**convert=** _profile_
> 转换为指定的 RAID 配置档

**soft**
> 跳过已经符合目标配置档的块组

**devid=** _id_
> 仅平衡给定设备上的块组

**drange=** _start..end_
> 仅平衡与该字节范围重叠的块组

**-f**
> 强制降低元数据冗余级别（例如 raid1 转为 single）

# CAVEATS

完整的 balance 会重写所有数据，速度非常慢。应使用过滤器只处理必要的块组。balance 需要空闲空间来迁移数据。在繁忙的系统上转换 RAID 配置档可能耗时很久。

# HISTORY

**btrfs balance** 是 **btrfs-progs** 软件包的一部分，用于管理 Linux 上的 btrfs 文件系统。

# INSTALL

```apt: sudo apt install btrfs-progs```

```dnf: sudo dnf install btrfs-progs```

```pacman: sudo pacman -S btrfs-progs```

```apk: sudo apk add btrfs-progs```

```brew: brew install btrfs-progs```

```nix: nix profile install nixpkgs#btrfs-progs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[btrfs](/man/btrfs)(8), [btrfs-device](/man/btrfs-device)(8), [btrfs-filesystem](/man/btrfs-filesystem)(8), [btrfs-scrub](/man/btrfs-scrub)(8), [mkfs.btrfs](/man/mkfs.btrfs)(8)
