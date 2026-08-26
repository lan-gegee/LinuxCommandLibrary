# TAGLINE

管理 ZFS 存储池

# TLDR

**列出所有存储池**

```zpool list```

**显示存储池状态**

```zpool status [pool]```

**创建镜像存储池**

```sudo zpool create [pool] mirror [/dev/sda] [/dev/sdb]```

**创建 RAID-Z 存储池**

```sudo zpool create [pool] raidz [/dev/sda] [/dev/sdb] [/dev/sdc]```

**向存储池添加设备**

```sudo zpool add [pool] [/dev/sdc]```

**启动一次清理（scrub）**

```sudo zpool scrub [pool]```

**导入存储池**

```sudo zpool import [pool]```

**导出存储池**

```sudo zpool export [pool]```

# SYNOPSIS

**zpool** _command_ [_options_] [_arguments_]

# SUBCOMMANDS

**create** _pool_ _vdev_...
> 创建新的存储池

**destroy** _pool_
> 销毁存储池及其全部数据

**add** _pool_ _vdev_...
> 向存储池添加设备

**remove** _pool_ _device_
> 从存储池移除设备

**list** [_pool_]
> 列出存储池及其属性

**status** [_pool_]
> 显示详细状态

**iostat** [_pool_] [_interval_]
> 显示 I/O 统计信息

**scrub** _pool_
> 校验数据完整性

**import** [_pool_]
> 导入存储池

**export** _pool_
> 导出存储池以便迁移

**upgrade** _pool_
> 升级存储池版本

**history** _pool_
> 显示存储池的命令历史

**attach** _pool_ _device_ _new_device_
> 为设备附加镜像

**detach** _pool_ _device_
> 分离镜像设备

**replace** _pool_ _old_ _new_
> 更换存储池中的磁盘

**online/offline** _pool_ _device_
> 使设备上线/离线

# DESCRIPTION

**zpool** 用于管理 ZFS 存储池。存储池由虚拟设备（vdev）组成，vdev 可以是单块磁盘、镜像或 RAID-Z 配置。存储池为 ZFS 数据集提供底层存储。

Vdev 类型：
- **mirror** - 数据镜像到 2 块及以上磁盘
- **raidz**、**raidz2**、**raidz3** - 带 1/2/3 个奇偶校验盘的 RAID-Z
- **spare** - 热备磁盘
- **cache** - L2ARC 读缓存（SSD）
- **log** - ZIL 写日志（SSD）

清理（scrub）会校验所有数据的校验和，并利用冗余副本修复错误。定期清理对数据完整性至关重要。

# CAVEATS

大多数操作需要 root 权限。

销毁存储池不可逆。**zpool destroy** 会删除所有数据。

RAID-Z 无法通过向现有 vdev 追加磁盘来扩容（自 OpenZFS 2.2 起，部分平台已支持扩容）。

定期清理至关重要。ZFS 能检测到单盘存储池的错误，但无法修复。

# INSTALL

```apt: sudo apt install zfs-fuse```

```apk: sudo apk add zfs```

```nix: nix profile install nixpkgs#zfs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[zfs](/man/zfs)(8), [zdb](/man/zdb)(8), [zpool-status](/man/zpool-status)(8)
