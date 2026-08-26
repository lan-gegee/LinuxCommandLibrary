# TAGLINE

显示 ZFS 存储池事件日志

# TLDR

**显示存储池事件**

```zpool events```

**显示详细的事件信息**

```zpool events -v```

**显示特定存储池的事件**

```zpool events [poolname]```

**实时跟踪事件**

```zpool events -f```

**清空事件日志**

```zpool events -c```

**详细输出并实时跟踪**

```zpool events -vf```

# SYNOPSIS

**zpool events** [_options_] [_pool_]

# PARAMETERS

**-v**
> 详细输出，包含完整的事件负载。

**-f**
> 跟随模式；等待新事件。

**-c**
> 显示后清空事件日志。

**-H**
> 脚本模式；无表头，以制表符分隔。

# EVENT CLASSES

**ereport.fs.zfs.checksum**: 检测到校验和错误。

**ereport.fs.zfs.io**: vdev 上发生 I/O 错误。

**ereport.fs.zfs.delay**: I/O 完成缓慢。

**sysevent.fs.zfs.pool_import**: 存储池已导入。

**sysevent.fs.zfs.pool_export**: 存储池已导出。

**sysevent.fs.zfs.scrub_start**: 清理（scrub）已开始。

**sysevent.fs.zfs.resilver_finish**: 重建（resilver）已完成。

# DESCRIPTION

**zpool events** 显示 ZFS 自内核模块加载以来所维护的内部事件日志。事件包括错误、存储池状态变化、清理操作以及设备状态更新。

事件日志保存在内存中，其最大大小可以配置。这些事件对于诊断硬件问题、跟踪存储池操作以及理解 ZFS 行为都极为宝贵。

ZFS Event Daemon（zed）实时监视这些事件，并能触发脚本发送通知或对事件做出自动响应。

# CAVEATS

事件保存在内存中；重启或卸载内核模块后即丢失。日志大小受 zfs_event_len_max 参数限制。持久化的事件处理和告警请使用 zed。

# HISTORY

ZFS 事件系统提供了传统文件系统所不具备的对存储池操作和错误的可见性。它通过 zed 守护进程实现主动监控与自动响应，让 ZFS 的自愈能力更易用。

# INSTALL

```apt: sudo apt install zfs-fuse```

```apk: sudo apk add zfs```

```nix: nix profile install nixpkgs#zfs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[zpool-status](/man/zpool-status)(8), [zpool](/man/zpool)(8), [zed](/man/zed)(8), [zfs](/man/zfs)(8)
