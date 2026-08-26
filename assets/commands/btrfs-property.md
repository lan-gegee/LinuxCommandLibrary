# TAGLINE

获取和设置 btrfs 文件系统对象的属性

# TLDR

**列出** btrfs 对象的可用属性

```sudo btrfs property list [path/to/btrfs_object]```

**获取** btrfs 对象的所有属性

```sudo btrfs property get [path/to/btrfs_object]```

获取文件系统的 **label** 属性

```sudo btrfs property get [path/to/btrfs_filesystem] label```

获取**特定对象类型**的属性

```sudo btrfs property get -t [subvol|filesystem|inode|device] [path/to/btrfs_filesystem]```

为文件或目录**设置压缩**

```sudo btrfs property set [path/to/btrfs_inode] compression [zstd|zlib|lzo|none]```

# SYNOPSIS

**btrfs property** _subcommand_ [_options_] _path_ [_property_ [_value_]]

# DESCRIPTION

**btrfs property** 管理 btrfs 文件系统对象的属性，对象包括文件、目录、子卷、文件系统和设备。属性控制压缩、只读状态和标签等行为。

不同的对象类型支持不同的属性。list 命令可以显示每个对象可用的属性。

# SUBCOMMANDS

**list**
> 列出可用的属性及其说明

**get**
> 获取属性值

**set**
> 设置属性值

# PARAMETERS

**-t** _type_
> 对象类型：subvol、filesystem、inode 或 device

# PROPERTIES

**compression**
> 文件的压缩算法：zstd、zlib、lzo、none

**label**
> 文件系统标签（filesystem 属性）

**ro**
> 只读状态（subvolume 属性）

# CAVEATS

对目录设置压缩只影响新文件；已有文件需要显式重新压缩。并非所有属性都可写。某些操作需要 root 权限。

# INSTALL

```apt: sudo apt install btrfs-progs```

```dnf: sudo dnf install btrfs-progs```

```pacman: sudo pacman -S btrfs-progs```

```apk: sudo apk add btrfs-progs```

```brew: brew install btrfs-progs```

```nix: nix profile install nixpkgs#btrfs-progs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[btrfs](/man/btrfs)(8), [btrfs-subvolume](/man/btrfs-subvolume)(8), [chattr](/man/chattr)(1)

# RESOURCES

```[Source code](https://github.com/kdave/btrfs-progs)```

```[Documentation](https://btrfs.readthedocs.io/)```

<!-- verified: 2026-06-22 -->
