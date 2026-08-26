# TAGLINE

在一个或多个设备上创建 bcachefs 文件系统

# TLDR

在分区上创建 **bcachefs 文件系统**

```sudo mkfs.bcachefs [/dev/sdXY]```

创建带**卷标**的 bcachefs 文件系统

```sudo mkfs.bcachefs -L [volume_label] [/dev/sdXY]```

创建启用 **zstd 压缩**的 bcachefs 文件系统

```sudo mkfs.bcachefs --compression=zstd [/dev/sdXY]```

创建带**加密**的 bcachefs 文件系统（会提示输入密码）

```sudo mkfs.bcachefs --encrypted [/dev/sdXY]```

创建具有 2 个副本的**多设备** bcachefs 文件系统

```sudo mkfs.bcachefs --replicas=2 [/dev/sdX] [/dev/sdY]```

即使设备**已包含文件系统**也强制创建

```sudo mkfs.bcachefs -f [/dev/sdXY]```

# SYNOPSIS

**mkfs.bcachefs** [_options_] _devices_...

# PARAMETERS

**-L, --fs_label=_label_**
> 设置文件系统卷标

**-U, --uuid=_uuid_**
> 使用指定的 UUID 创建文件系统

**-f, --force**
> 强制创建文件系统，即使设备上已存在文件系统

**-q, --quiet**
> 只输出错误信息

**-v, --verbose**
> 详细输出文件系统初始化过程

**--replicas=_n_**
> 同时设置数据副本数和元数据副本数（一次性设置两者的简写）

**--data_replicas=_n_**
> 数据副本数量

**--metadata_replicas=_n_**
> 元数据副本数量

**--metadata_checksum=_type_**
> 元数据校验和算法（none、crc32c、crc64、xxhash）；默认：crc32c

**--data_checksum=_type_**
> 数据校验和算法（none、crc32c、crc64、xxhash）；默认：crc32c

**--compression=_type_**
> 前台压缩算法（none、lz4、gzip、zstd）；默认：none

**--background_compression=_type_**
> 应用于已有数据的后台压缩算法（none、lz4、gzip、zstd）

**--encrypted**
> 启用整个文件系统的加密（chacha20/poly1305）；将提示输入密码

**--no_passphrase**
> 与 --encrypted 一起使用时，不加密主加密密钥

**--nocow**
> 启用非写时复制模式：写入时尽可能就地完成。隐式禁用校验和、压缩与加密。快照和 reflink 仍使用写时复制。

**--errors=_action_**
> 文件系统出错时采取的操作：continue、ro 或 panic

**--metadata_target=_target_**
> 元数据写入优先使用的设备或标签（用于多设备分层配置）

**--foreground_target=_target_**
> 前台（同步）写入优先使用的设备或标签

**--background_target=_target_**
> 后台迁移数据的目标设备或标签

**--promote_target=_target_**
> 读取时数据提升到的目标设备或标签（SSD 缓存层）

**--discard**
> 在设备上启用 discard/TRIM 支持

**--fs_size=_size_**
> 将文件系统限制在后续设备上的 _size_ 字节内

**--bucket=_size_**
> 设备的桶大小；必须大于 btree 节点大小

**--durability=_n_**
> 将写入该设备的数据视为已复制 _n_ 次

**--btree_node_size=_size_**
> Btree 节点大小；默认：256k

**--block_size=_size_**
> 文件系统块大小（字节），例如 4k

**--acl**
> 启用 POSIX ACL 支持

**--usrquota**
> 启用用户配额

**--grpquota**
> 启用组配额

**--prjquota**
> 启用项目配额

# DESCRIPTION

**mkfs.bcachefs** 在一个或多个设备上创建 bcachefs 文件系统，等价于 **bcachefs format**。Bcachefs 是 Linux 上一款现代的写时复制文件系统，特性包括校验和、压缩、加密、快照、reflink 以及支持存储分层的多设备。

该文件系统可以跨越多个设备并配置可调的复制份数，无需单独的卷管理器即可提供类 RAID 冗余。不同的存储层（例如高速 NVMe SSD 和低速 HDD）可以通过 target 选项（--foreground_target、--promote_target、--background_target）组合在同一个文件系统中。

所有持久的文件系统级选项都可以在格式化时设置，其中许多之后还能用 **bcachefs set-fs-option** 更改。

# CAVEATS

会**销毁目标设备上的所有数据**。如果设备上已有文件系统，可用 **-f** 覆盖安全检查。加密要求在创建时设置密码；密码丢失后数据将无法恢复。**--nocow** 标志会禁用校验和与压缩，且无法按文件选择性撤销。**--erasure_code** 选项虽然存在，但尚不适合实际使用。

# HISTORY

Bcachefs 由 Kent Overstreet 开发，源自 bcache 块缓存层。经过多年的树外开发，它在 Linux 内核 6.7 版（2023 年 12 月发布）中被合入主线。

# INSTALL

```dnf: sudo dnf install bcachefs-tools```

```pacman: sudo pacman -S bcachefs-tools```

```apk: sudo apk add bcachefs-tools```

```nix: nix profile install nixpkgs#bcachefs-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bcachefs](/man/bcachefs)(8), [bcachefs-device](/man/bcachefs-device)(8), [mkfs](/man/mkfs)(8), [mount](/man/mount)(8), [blkid](/man/blkid)(8), [cryptsetup](/man/cryptsetup)(8)
