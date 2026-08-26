# TAGLINE

托管的基于存储池的 Linux 存储

# TLDR

**创建**存储池

```sudo stratis pool create [pool_name] [/dev/sdX] [/dev/sdY]```

**在池中创建**文件系统

```sudo stratis filesystem create [pool_name] [volume_name]```

**列出**所有文件系统

```sudo stratis filesystem list```

**向现有池添加**设备

```sudo stratis pool add-data [pool_name] [/dev/sdZ]```

**创建**快照

```sudo stratis filesystem snapshot [pool_name] [source_fs] [snapshot_name]```

**销毁**文件系统

```sudo stratis filesystem destroy [pool_name] [volume_name]```

**列出**池

```sudo stratis pool list```

# SYNOPSIS

**stratis** _command_ [_subcommand_] [_arguments_]

# COMMANDS

**pool create** _name_ _devices_...
> 用块设备创建存储池

**pool list**
> 列出现有的池

**pool add-data** _pool_ _device_
> 向池中添加设备

**pool destroy** _pool_
> 移除一个池（要求其中没有文件系统）

**pool rename** _old_ _new_
> 重命名一个池

**pool init-cache** _pool_ _devices_
> 初始化 SSD 缓存层

**filesystem create** _pool_ _name_
> 从池中创建精简文件系统

**filesystem list**
> 列出文件系统

**filesystem snapshot** _pool_ _source_ _name_
> 创建文件系统快照

**filesystem destroy** _pool_ _name_
> 移除文件系统

**filesystem rename** _pool_ _old_ _new_
> 重命名文件系统

**blockdev list**
> 列出池中的块设备

**daemon version**
> 显示 stratisd 版本

# DESCRIPTION

**stratis** 是一个本地存储管理工具，基于 Linux devicemapper 和 XFS 提供类似 ZFS/Btrfs 的特性。它通过抽象块设备池简化了存储管理，这些池可动态分配给精简配置的 XFS 文件系统。

使用 stratis 命令前必须先运行 stratisd 守护进程。文件系统出现在 **/dev/stratis/pool_name/filesystem_name**，并支持快照、精简配置和池扩展等特性。

# MOUNTING

手动挂载：

```
mount /dev/stratis/pool_name/fs_name /mnt/target
```

添加到 /etc/fstab：

```
/dev/stratis/pool/fs /mnt xfs defaults,x-systemd.requires=stratisd.service 0 0
```

# CAVEATS

需要 stratisd 服务处于运行状态。仅使用 XFS；不支持其他文件系统。池设备应当专用；包含现有数据的分区将被覆盖。快照在被修改之前与源共享空间。

# HISTORY

**Stratis** 由 **Red Hat** 从 **2017 年**前后开始开发，旨在为 Linux 提供易于使用的存储管理。它的设计目标是提供现代存储特性，同时避免 LVM 的复杂性以及 Btrfs/ZFS 对内核集成的依赖。Stratis 自 Fedora 28 和 RHEL 8 起可用。

# SEE ALSO

[lvm](/man/lvm)(8), [btrfs](/man/btrfs)(8), [xfs](/man/xfs)(5), [systemctl](/man/systemctl)(1)
