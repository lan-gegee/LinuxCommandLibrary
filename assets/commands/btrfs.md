# TAGLINE

管理 btrfs 写时复制文件系统

# TLDR

**创建**子卷

```sudo btrfs subvolume create path/to/subvolume```

**列出**子卷

```sudo btrfs subvolume list path/to/mount```

显示**空间使用**情况

```sudo btrfs filesystem df path/to/mount```

启用**配额**

```sudo btrfs quota enable path/to/subvolume```

显示**配额**

```sudo btrfs qgroup show path/to/subvolume```

# SYNOPSIS

**btrfs** _command_ [_OPTIONS_] [_path_]

# DESCRIPTION

**btrfs** 是 Btrfs（B-tree 文件系统）的主要管理工具。Btrfs 是一种现代的写时复制 Linux 文件系统，内置快照、子卷、透明压缩、在线扩缩容、多设备存储池、校验和以及 RAID0/1/10/5/6 支持。该命令分发给各子命令组（**subvolume**、**filesystem**、**device**、**balance**、**scrub**、**send**、**receive**、**quota**、**qgroup**、**inspect-internal** 等），它们与文件系统操作一一对应。

大多数子命令作用于已挂载的 Btrfs 路径。繁重的工作由内核完成；**btrfs** 可执行文件通过发出 IOCTL 来调用 balance、scrub、快照、碎片整理等操作。**send** / **receive** 组合可以将快照高效地增量复制到远程主机或备份卷。

# PARAMETERS

**subvolume** (su)
> 管理子卷和快照

**filesystem** (fi)
> 管理文件系统属性

**device** (dev)
> 管理文件系统中的设备

**balance** (bal)
> 在设备间平衡数据

**scrub** (sc)
> 校验数据完整性

**quota** (qu)
> 启用/禁用配额支持

**qgroup** (qg)
> 管理配额组

# CAVEATS

Btrfs 仍在积极开发中。RAID5/6 等部分功能在稳定性上可能存在隐患。建议定期运行 scrub 以校验数据完整性。快照在被修改前与其源共享空间。

# HISTORY

**btrfs** 是 **B-tree 文件系统**的管理工具，后者是一种具备先进存储能力的现代 Linux 文件系统。

# INSTALL

```apt: sudo apt install btrfs-progs```

```dnf: sudo dnf install btrfs-progs```

```pacman: sudo pacman -S btrfs-progs```

```apk: sudo apk add btrfs-progs```

```brew: brew install btrfs-progs```

```nix: nix profile install nixpkgs#btrfs-progs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[btrfs-subvolume](/man/btrfs-subvolume)(8), [btrfs-filesystem](/man/btrfs-filesystem)(8), [mkfs.btrfs](/man/mkfs.btrfs)(8)
