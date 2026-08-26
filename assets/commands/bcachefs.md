# TAGLINE

新一代写时复制文件系统工具

# TLDR

用 bcachefs **格式化**分区

```sudo bcachefs format [path/to/partition]```

**挂载** bcachefs 文件系统

```sudo bcachefs mount [path/to/partition] [path/to/mountpoint]```

创建带 **SSD 缓存的 RAID** 与 HDD 存储

```sudo bcachefs format -l ssd.ssd1 [path/to/ssd] -l hdd.hdd1 [path/to/hdd] --replicas 1 --foreground_target ssd --promote_target ssd --background_target hdd```

挂载**多设备文件系统**

```sudo bcachefs mount [path/to/partition1]:[path/to/partition2] [path/to/mountpoint]```

显示**磁盘用量**

```bcachefs fs usage -h [path/to/mountpoint]```

格式化后设置**副本数**

```sudo bcachefs set-fs-option --metadata_replicas [2] --data_replicas [2] [path/to/partition]```

强制对所有文件**重新复制**

```sudo bcachefs data rereplicate [path/to/mountpoint]```

为目录创建**快照**

```bcachefs subvolume snapshot [path/to/directory] [path/to/snapshot]```

# SYNOPSIS

**bcachefs** _command_ [_options_] [_arguments_]

# DESCRIPTION

**bcachefs** 是 Linux 的新一代写时复制文件系统，它结合了 btrfs 和 ZFS 的特性以及 bcache 的性能特点。它提供校验和、压缩、加密、快照和多设备支持。

该文件系统支持分层存储，可在快速（SSD）与慢速（HDD）设备之间自动迁移数据，适合混合存储配置。

# SUBCOMMANDS

**format**
> 创建新的 bcachefs 文件系统。

**mount**
> 挂载 bcachefs 文件系统。

**fsck**
> 检查并修复文件系统。

**fs usage**
> 显示文件系统的磁盘用量。

**device**
> 管理文件系统中的设备（添加、移除、迁出、设置状态）。

**subvolume**
> 管理子卷和快照。

**data rereplicate**
> 重写数据，使所有数据块满足其复制要求。

**set-fs-option**
> 在已挂载或离线的文件系统上修改选项。

**show-super**
> 打印文件系统超级块的内容。

**unlock**
> 挂载前解锁加密的文件系统。

# CAVEATS

bcachefs 已于内核 **6.7**（2024 年 1 月发布）合入 Linux 主线。较旧的内核需要自行编译外部模块。该文件系统仍在积极开发中，请务必备份重要数据。**bcachefs** 用户态工具必须与你的内核所期望的磁盘格式相匹配。

# HISTORY

bcachefs 由 Kent Overstreet 开发，他也是 bcache 的作者。开发始于 **2015** 年前后，作为 bcache 向完整文件系统的演进，并于 **2024** 年初随内核 **6.7** 合入 Linux 主线。

# INSTALL

```dnf: sudo dnf install bcachefs-tools```

```pacman: sudo pacman -S bcachefs-tools```

```apk: sudo apk add bcachefs-tools```

```nix: nix profile install nixpkgs#bcachefs-tools```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[bcachefs-device](/man/bcachefs-device)(8), [mkfs](/man/mkfs)(8), [fsck](/man/fsck)(8), [mount](/man/mount)(8), [btrfs](/man/btrfs)(8)

# RESOURCES

```[Homepage](https://bcachefs.org)```

```[Source code](https://evilpiepirate.org/git/bcachefs-tools.git)```

```[Documentation](https://bcachefs-docs.readthedocs.io/en/latest/)```

<!-- verified: 2026-06-19 -->
