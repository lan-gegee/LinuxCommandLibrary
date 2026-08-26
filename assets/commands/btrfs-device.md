# TAGLINE

管理 btrfs 文件系统中的设备

# TLDR

**添加**设备

```sudo btrfs device add /dev/sdb /dev/sdc path/to/filesystem```

**移除**设备

```sudo btrfs device remove /dev/sdb path/to/filesystem```

显示错误**统计**信息

```sudo btrfs device stats path/to/filesystem```

**扫描**所有磁盘

```sudo btrfs device scan --all-devices```

显示每个设备的**使用**情况

```sudo btrfs device usage path/to/filesystem```

# SYNOPSIS

**btrfs device** _command_ [_OPTIONS_] [_device_|_path_]

# DESCRIPTION

**btrfs device** 管理 btrfs 文件系统中的设备。它可以添加或移除设备、显示统计信息，以及扫描 btrfs 文件系统。这使得动态调整容量和更改 RAID 配置成为可能。

# PARAMETERS

**add**
> 向文件系统添加一个或多个设备

**remove**
> 从文件系统中移除设备

**delete**
> remove 的别名

**stats**
> 显示设备错误统计信息

**scan**
> 扫描设备上的 btrfs 文件系统

**usage**
> 显示详细的每设备分配统计

**ready**
> 检查设备是否就绪

**-d, --all-devices**
> 扫描所有设备以查找 btrfs 文件系统

# CAVEATS

移除设备时，其余设备上必须有足够空间容纳被迁移的数据。添加或移除设备时文件系统必须已挂载。添加设备不会自动平衡数据。

# HISTORY

**btrfs device** 是 **btrfs-progs** 软件包的一部分，用于管理 Linux 上的 btrfs 文件系统。

# INSTALL

```apt: sudo apt install btrfs-progs```

```dnf: sudo dnf install btrfs-progs```

```pacman: sudo pacman -S btrfs-progs```

```apk: sudo apk add btrfs-progs```

```brew: brew install btrfs-progs```

```nix: nix profile install nixpkgs#btrfs-progs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[btrfs](/man/btrfs)(8), [btrfs-balance](/man/btrfs-balance)(8), [btrfs-filesystem](/man/btrfs-filesystem)(8)

# RESOURCES

```[Source code](https://github.com/kdave/btrfs-progs)```

```[Documentation](https://btrfs.readthedocs.io/)```

<!-- verified: 2026-06-22 -->
