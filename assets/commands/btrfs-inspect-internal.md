# TAGLINE

调试和检查 btrfs 文件系统内部结构

# TLDR

打印**超级块**信息

```sudo btrfs inspect-internal dump-super [path/to/partition]```

打印**所有超级块副本**

```sudo btrfs inspect-internal dump-super -a [path/to/partition]```

打印文件系统**元数据**信息

```sudo btrfs inspect-internal dump-tree [path/to/partition]```

按 **inode** 号打印文件列表

```sudo btrfs inspect-internal inode-resolve [inode_number] [path/to/btrfs_mount]```

在**逻辑地址**处打印文件列表

```sudo btrfs inspect-internal logical-resolve [logical_address] [path/to/btrfs_mount]```

打印文件系统的**树统计**信息

```sudo btrfs inspect-internal tree-stats [path/to/partition]```

计算收缩时的**最小设备容量**

```sudo btrfs inspect-internal min-dev-size [path/to/btrfs_mount]```

# SYNOPSIS

**btrfs inspect-internal** _subcommand_ [_options_] _device_|_path_

# DESCRIPTION

**btrfs inspect-internal** 提供对 btrfs 文件系统内部结构的底层访问。它主要用于调试、取证和高级故障排查。

该命令可以转储超级块数据、元数据树，并将 inode 解析为文件路径，或将逻辑地址解析为物理位置。

# SUBCOMMANDS

**dump-super**
> 打印超级块信息

**dump-tree**
> 打印元数据树结构

**inode-resolve**
> 根据 inode 号查找文件路径

**logical-resolve**
> 在逻辑地址处查找文件

**tree-stats**
> 打印树统计信息

**min-dev-size**
> 计算收缩时的最小设备容量

# PARAMETERS

**-a, --all**
> 转储所有超级块副本

**-f**
> 即使有警告也强制输出

# CAVEATS

输出内容偏技术性，面向开发者或高级用户。部分命令要求文件系统处于卸载状态，另一些则要求已挂载。错误使用不会损坏数据，但解读输出需要了解 btrfs 内部结构。

# SEE ALSO

[btrfs](/man/btrfs)(8), [btrfs-check](/man/btrfs-check)(8), [btrfs-rescue](/man/btrfs-rescue)(8), [btrfs-restore](/man/btrfs-restore)(8)
