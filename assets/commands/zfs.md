# TAGLINE

管理 ZFS 文件系统与快照

# TLDR

**列出所有数据集**

```zfs list```

**创建新文件系统**

```sudo zfs create [pool/dataset]```

**创建快照**

```sudo zfs snapshot [pool/dataset@snapshot_name]```

**列出快照**

```zfs list -t snapshot```

**回滚到快照**

```sudo zfs rollback [pool/dataset@snapshot_name]```

**设置属性**

```sudo zfs set [compression=lz4] [pool/dataset]```

**获取属性值**

```zfs get [compression] [pool/dataset]```

**销毁数据集**

```sudo zfs destroy [pool/dataset]```

# SYNOPSIS

**zfs** _command_ [_options_] [_arguments_]

# SUBCOMMANDS

**list** [**-t** _type_] [**-o** _properties_] [_dataset_]
> 列出数据集和属性

**create** [**-p**] _dataset_
> 创建文件系统或卷（-p 创建父级）

**destroy** [**-r**] _dataset_
> 销毁数据集（-r 递归）

**snapshot** _dataset@name_
> 创建快照

**rollback** _dataset@snapshot_
> 回滚到快照

**clone** _snapshot_ _dataset_
> 从快照创建克隆

**send** _snapshot_
> 生成用于复制的流

**receive** _dataset_
> 将流接收到数据集

**set** _property=value_ _dataset_
> 设置属性

**get** _property_ _dataset_
> 获取属性值

**mount** _dataset_
> 挂载文件系统

**unmount** _dataset_
> 卸载文件系统

# DESCRIPTION

**zfs** 管理 ZFS 文件系统、快照、克隆和卷。ZFS 是文件系统与卷管理器的结合体，具有写时复制、快照、校验和以及内置压缩等高级特性。

关键概念：
- **数据集**是池内的文件系统或卷
- **快照**是只读的时间点副本
- **克隆**是从快照创建的可写副本
- **属性**控制行为（压缩、配额、挂载点）

ZFS 使用分层数据集：**pool/parent/child** 从父级继承属性。可以在本地设置属性来覆盖继承。

常见属性包括 **compression**、**quota**、**reservation**、**recordsize**、**atime** 和 **mountpoint**。

# CAVEATS

大多数操作需要 root 权限。

**zfs destroy** 不可逆。快照可以防止误删，但必须提前创建。

ZFS 可能消耗大量内存用于缓存（ARC）。在内存受限的系统上请调整 **zfs_arc_max**。

快照开销很小但并非为零。数据变动频繁时的众多快照可能占用大量空间。

# INSTALL

```apt: sudo apt install zfs-fuse```

```apk: sudo apk add zfs```

```nix: nix profile install nixpkgs#zfs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[zpool](/man/zpool)(8), [zdb](/man/zdb)(8), [zfs-send](/man/zfs-send)(8), [zfs-receive](/man/zfs-receive)(8)
