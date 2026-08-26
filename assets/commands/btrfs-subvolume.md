# TAGLINE

管理 btrfs 子卷和快照

# TLDR

**创建**子卷

```sudo btrfs subvolume create path/to/new_subvolume```

**列出**子卷

```sudo btrfs subvolume list path/to/filesystem```

**删除**子卷

```sudo btrfs subvolume delete path/to/subvolume```

创建**只读**快照

```sudo btrfs subvolume snapshot -r path/to/source path/to/target```

创建**可读写**快照

```sudo btrfs subvolume snapshot path/to/source path/to/target```

**显示**子卷详情

```sudo btrfs subvolume show path/to/subvolume```

# SYNOPSIS

**btrfs subvolume** _command_ [_OPTIONS_] [_path_]

# DESCRIPTION

**btrfs subvolume** 管理 btrfs 子卷和快照。子卷是可单独挂载的文件系统树，可以拥有独立的快照和配额策略。快照是某一时刻的副本，初始时与其源共享全部数据。

# PARAMETERS

**create**
> 创建一个新的空子卷

**list**
> 列出文件系统中的所有子卷

**delete**
> 删除子卷或快照

**snapshot**
> 为现有子卷创建快照

**show**
> 显示子卷的详细信息

**-r, --readonly**
> 创建只读快照

**get-default**
> 获取默认子卷

**set-default**
> 设置默认子卷

# CAVEATS

删除子卷不会立即释放空间；异步清理在后台进行。快照不是递归的 - 嵌套的子卷必须单独做快照。

# HISTORY

**btrfs subvolume** 是 **btrfs-progs** 软件包的一部分，用于管理 Linux 上的 btrfs 文件系统。

# INSTALL

```apt: sudo apt install btrfs-progs```

```dnf: sudo dnf install btrfs-progs```

```pacman: sudo pacman -S btrfs-progs```

```apk: sudo apk add btrfs-progs```

```brew: brew install btrfs-progs```

```nix: nix profile install nixpkgs#btrfs-progs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[btrfs](/man/btrfs)(8), [btrfs-filesystem](/man/btrfs-filesystem)(8)

# RESOURCES

```[Source code](https://github.com/kdave/btrfs-progs)```

```[Documentation](https://btrfs.readthedocs.io/)```

<!-- verified: 2026-06-22 -->
