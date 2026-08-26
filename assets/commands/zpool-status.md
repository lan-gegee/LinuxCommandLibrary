# TAGLINE

显示 ZFS 存储池健康状态

# TLDR

**显示所有存储池的状态**

```zpool status```

**显示特定存储池的状态**

```zpool status [poolname]```

**只显示有错误的存储池**

```zpool status -x```

**显示详细的错误信息**

```zpool status -v```

**显示去重统计信息**

```zpool status -D```

**以 JSON 格式输出**

```zpool status -j```

# SYNOPSIS

**zpool status** [_options_] [_pool_...]

# PARAMETERS

**-v**
> 详细模式；显示数据错误列表。

**-x**
> 只显示有错误或不可用的存储池。

**-D**
> 显示去重统计信息。

**-g**
> 显示 vdev GUID。

**-L**
> 显示实际的设备路径。

**-P**
> 显示完整的设备路径。

**-T** _d_|_u_
> 时间戳格式：d（日期）或 u（Unix）。

**-j**
> 以 JSON 格式输出。

# POOL STATES

**ONLINE**: 完全正常运行。

**DEGRADED**: 一个或多个设备故障，但存储池仍可运行。

**FAULTED**: 存储池完全无法访问。

**OFFLINE**: 设备被显式置于离线状态。

**UNAVAIL**: 设备无法打开。

**REMOVED**: 设备已被物理移除。

# DESCRIPTION

**zpool status** 显示 ZFS 存储池的详细健康信息。它会展示设备层级结构、每个 vdev 的状态、错误计数以及正在进行的清理（scrub）或重建（resilver）操作。

READ、WRITE 和 CKSUM 列显示每个设备的错误计数。非零值表示可能存在需要关注的硬件问题。定期执行 scrub 有助于及早发现静默损坏。

当 scrub 或 resilver 正在进行时，会显示进度百分比和预计完成时间。-x 选项提供了一种快速检查是否有存储池需要关注的途径。

# CAVEATS

错误计数会一直保留直到被清除。CKSUM 错误可能意味着控制器或线缆有问题，而不仅仅是硬盘故障。降级（degraded）的存储池应及时修复，避免数据丢失。

# HISTORY

**zpool status** 是监控 ZFS 存储池健康状态的主要工具。ZFS 由 Sun Microsystems 开发，引入了数据完整性校验特性，使其状态报告比传统存储系统信息更丰富。

# INSTALL

```apt: sudo apt install zfs-fuse```

```apk: sudo apk add zfs```

```nix: nix profile install nixpkgs#zfs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[zpool](/man/zpool)(8), [zpool-events](/man/zpool-events)(8), [zfs](/man/zfs)(8)
