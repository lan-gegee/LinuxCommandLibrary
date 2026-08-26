# TAGLINE

在一个或多个设备上创建 Btrfs

# TLDR

在分区上创建 **Btrfs 文件系统**

```sudo mkfs.btrfs /dev/sdXY```

创建**单设备**文件系统

```sudo mkfs.btrfs -m single -d single /dev/sdX```

在多设备上创建 **RAID1** 文件系统

```sudo mkfs.btrfs -m raid1 -d raid1 /dev/sdX /dev/sdY```

设置文件系统**卷标**

```sudo mkfs.btrfs -L "mylabel" /dev/sdX```

**强制**创建（覆盖已有内容）

```sudo mkfs.btrfs -f /dev/sdX```

以指定的**节点大小**创建

```sudo mkfs.btrfs -n 32k /dev/sdX```

# SYNOPSIS

**mkfs.btrfs** [_options_] _device_ [_device_...]

# DESCRIPTION

**mkfs.btrfs** 在一个或多个设备上创建 Btrfs（B-tree 文件系统）。Btrfs 支持多设备配置、写时复制、快照、子卷以及多种 RAID 级别。

# PARAMETERS

**-L, --label NAME**
> 设置文件系统卷标（最长 256 个字符）

**-f, --force**
> 强制覆盖已有的文件系统

**-m, --metadata PROFILE**
> 元数据配置（single、dup、raid0、raid1、raid10、raid5、raid6）

**-d, --data PROFILE**
> 数据配置（single、dup、raid0、raid1、raid10、raid5、raid6）

**-n, --nodesize SIZE**
> 设置节点/叶子大小（默认 16KB）

**-s, --sectorsize SIZE**
> 设置扇区大小

**-O, --features LIST**
> 启用或禁用特性

**-r, --rootdir DIR**
> 将目录内容复制到文件系统根目录

**-U, --uuid UUID**
> 指定文件系统 UUID

**--mixed**
> 将数据和元数据混在同一块组中（适用于小设备）

# CAVEATS

创建文件系统会销毁现有数据。指定多个设备时，元数据默认使用 raid1 配置，数据默认使用 single 配置。RAID5/6 支持仍被视为实验性功能。

# HISTORY

**mkfs.btrfs** 是 **btrfs-progs**（Btrfs 文件系统工具集）的一部分。Btrfs 是为 Linux 开发的一款现代写时复制文件系统。

# INSTALL

```apt: sudo apt install btrfs-progs```

```dnf: sudo dnf install btrfs-progs```

```pacman: sudo pacman -S btrfs-progs```

```apk: sudo apk add btrfs-progs```

```brew: brew install btrfs-progs```

```nix: nix profile install nixpkgs#btrfs-progs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[btrfs](/man/btrfs)(8), [btrfs-filesystem](/man/btrfs-filesystem)(8), [mkfs](/man/mkfs)(8)
