# TAGLINE

增大 LVM 中逻辑卷的容量

# TLDR

扩展到**绝对**大小

```sudo lvextend -L 120G logical_volume```

按**相对**大小扩展

```sudo lvextend -L +40G -r logical_volume```

使用**全部空闲**空间

```sudo lvextend -l +100%FREE logical_volume```

扩展并**调整文件系统大小**

```sudo lvextend -l +100%FREE -r logical_volume```

# SYNOPSIS

**lvextend** [_OPTIONS_] _LogicalVolume_

# DESCRIPTION

**lvextend** 增大 LVM 中逻辑卷的大小。它可以按绝对大小、相对大小或可用空间的百分比进行扩展。底层文件系统可以自动调整大小。

# PARAMETERS

**-L, --size** _size_
> 指定新的绝对大小或相对增量（+size）

**-l, --extents** _extents_
> 以 extent 数量或百分比指定大小（%VG、%FREE、%PVS）

**-r, --resizefs**
> 自动调整底层文件系统的大小

**-n, --nofsck**
> 调整大小前跳过文件系统检查

**--use-policies**
> 使用精简池自动扩展策略

# CAVEATS

确保卷组中有足够的空闲空间。-r 的文件系统扩容仅适用于 ext2/3/4 和 XFS。其他文件系统需要在扩展后手动调整大小。XFS 只能增大，不能缩小。

# HISTORY

**lvextend** 是 **LVM2**（Linux 逻辑卷管理器）的一部分，提供动态存储管理。

# INSTALL

```apt: sudo apt install lvm2```

```dnf: sudo dnf install lvm2```

```pacman: sudo pacman -S lvm2```

```apk: sudo apk add lvm2```

```zypper: sudo zypper install lvm2```

```nix: nix profile install nixpkgs#lvm2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lvm](/man/lvm)(8), [lvresize](/man/lvresize)(8), [lvreduce](/man/lvreduce)(8), [lvcreate](/man/lvcreate)(8)
