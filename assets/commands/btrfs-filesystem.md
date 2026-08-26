# TAGLINE

管理 btrfs 文件系统的属性和操作

# TLDR

显示空间**使用**统计

```btrfs filesystem usage path/to/mount```

显示**设备**使用情况

```sudo btrfs filesystem show path/to/mount```

对文件进行**碎片整理**

```sudo btrfs filesystem defragment -v path/to/file```

递归地对目录进行**碎片整理**

```sudo btrfs filesystem defragment -v -r path/to/dir```

**同步**到磁盘

```sudo btrfs filesystem sync path/to/mount```

显示目录的**磁盘占用**

```sudo btrfs filesystem du -s path/to/dir```

创建**交换文件**

```sudo btrfs filesystem mkswapfile --size 8g path/to/swapfile```

# SYNOPSIS

**btrfs filesystem** _command_ [_OPTIONS_] [_path_]

# DESCRIPTION

**btrfs filesystem** 管理 btrfs 文件系统的属性和操作，包括使用统计、碎片整理、同步以及设备信息的显示。

# PARAMETERS

**usage**
> 显示详细的文件系统空间使用情况

**show**
> 显示文件系统信息和设备使用情况

**df**
> 以类似 df 命令的方式显示磁盘空间使用情况

**defragment**
> 对文件或目录进行碎片整理

**sync**
> 强制将未写入的数据同步到磁盘

**du**
> 计算文件和目录的磁盘占用

**mkswapfile**
> 创建为 btrfs 正确格式化的交换文件

**-v, --verbose**
> 启用详细输出

**-r**
> 对 defragment 和 du 进行递归操作

**-s, --summarize**
> du 命令仅显示汇总结果

# CAVEATS

碎片整理可能破坏 reflink 并削弱去重的效果。在去重活动进行时运行碎片整理可能引发问题。由于 btrfs 的空间核算方式不同，其 df 命令的输出可能与标准 df 不同。

# HISTORY

**btrfs filesystem** 是 **btrfs-progs** 软件包的一部分，用于管理 Linux 上的 btrfs 文件系统。

# INSTALL

```apt: sudo apt install btrfs-progs```

```dnf: sudo dnf install btrfs-progs```

```pacman: sudo pacman -S btrfs-progs```

```apk: sudo apk add btrfs-progs```

```brew: brew install btrfs-progs```

```nix: nix profile install nixpkgs#btrfs-progs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[btrfs](/man/btrfs)(8), [btrfs-device](/man/btrfs-device)(8), [df](/man/df)(1)

# RESOURCES

```[Source code](https://github.com/kdave/btrfs-progs)```

```[Documentation](https://btrfs.readthedocs.io/)```

<!-- verified: 2026-06-22 -->
