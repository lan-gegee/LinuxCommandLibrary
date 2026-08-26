# TAGLINE

从受损的 btrfs 文件系统中抢救文件

# TLDR

从 btrfs 设备**恢复**所有文件

```sudo btrfs restore [path/to/btrfs_device] [path/to/target_directory]```

**列出文件**（试运行）而不实际写入

```sudo btrfs restore -D [path/to/btrfs_device] [path/to/target_directory]```

恢复匹配**正则表达式模式**的文件

```sudo btrfs restore --path-regex [regex] -c [path/to/btrfs_device] [path/to/target_directory]```

使用指定的**根树**恢复

```sudo btrfs restore -t [bytenr] [path/to/btrfs_device] [path/to/target_directory]```

恢复时包含**元数据、扩展属性和符号链接**

```sudo btrfs restore -m -x -S -o [path/to/btrfs_device] [path/to/target_directory]```

# SYNOPSIS

**btrfs restore** [_options_] _device_ _target_

# DESCRIPTION

**btrfs restore** 尝试从无法正常挂载的受损 btrfs 文件系统中抢救文件。它直接从设备读取文件系统结构，并将可恢复的文件复制到目标目录。

这是一个在其他方法失败后使用的数据恢复工具。它不会修复文件系统，而是将数据提取到健康的位置。

# PARAMETERS

**-D, --dry-run**
> 仅列出文件而不提取

**--path-regex** _regex_
> 只恢复匹配该模式的文件

**-c**
> 正则表达式匹配不区分大小写

**-t** _bytenr_
> 使用指定的根树（参见 btrfs-find-root）

**-m, --metadata**
> 恢复元数据（权限、时间戳）

**-x, --xattr**
> 恢复扩展属性

**-S, --symlinks**
> 恢复符号链接

**-o, --overwrite**
> 覆盖目标目录中已存在的文件

**-v**
> 详细输出

# CAVEATS

不会修复文件系统，只提取数据。严重损坏的文件系统可能无法恢复全部文件。正则表达式必须匹配完整路径，包括父目录。目标目录应位于不同的文件系统上。

# INSTALL

```apt: sudo apt install btrfs-progs```

```dnf: sudo dnf install btrfs-progs```

```pacman: sudo pacman -S btrfs-progs```

```apk: sudo apk add btrfs-progs```

```brew: brew install btrfs-progs```

```nix: nix profile install nixpkgs#btrfs-progs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[btrfs](/man/btrfs)(8), [btrfs-rescue](/man/btrfs-rescue)(8), [btrfs-check](/man/btrfs-check)(8)

# RESOURCES

```[Source code](https://github.com/kdave/btrfs-progs)```

```[Documentation](https://btrfs.readthedocs.io/)```

<!-- verified: 2026-06-22 -->
