# TAGLINE

校验 btrfs 文件系统上的数据完整性

# TLDR

**开始** scrub

```sudo btrfs scrub start path/to/mount```

显示**状态**

```sudo btrfs scrub status path/to/mount```

**取消** scrub

```sudo btrfs scrub cancel path/to/mount```

**继续** scrub

```sudo btrfs scrub resume path/to/mount```

在**前台**启动

```sudo btrfs scrub start -B path/to/mount```

以**静默**模式启动

```sudo btrfs scrub start -q path/to/mount```

# SYNOPSIS

**btrfs scrub** _command_ [_OPTIONS_] _path_

# DESCRIPTION

**btrfs scrub** 通过读取所有数据和元数据块并检查其校验和，来校验 btrfs 文件系统的数据完整性。建议每月运行一次 scrub，以检测并在可能的情况下修复损坏的数据。

# PARAMETERS

**start**
> 开始一次 scrub 操作

**status**
> 显示正在运行或上次完成的 scrub 的状态

**cancel**
> 取消正在运行的 scrub

**resume**
> 继续已取消的 scrub

**-B**
> 不在后台运行（前台模式）

**-q, --quiet**
> 抑制错误和统计输出

**-r**
> 只读模式 - 不尝试修复

**-d**
> 为文件系统中的每个设备分别打印统计信息

**-R**
> 原始打印模式 - 打印不带单位的统计数值

# CAVEATS

scrub 的 I/O 开销可能很大，会影响系统性能。在 RAID 配置下，scrub 可以利用冗余副本修复错误。单磁盘配置只能检测错误而无法修复。

# HISTORY

**btrfs scrub** 是 **btrfs-progs** 软件包的一部分，为 btrfs 文件系统提供数据完整性校验。

# SEE ALSO

[btrfs](/man/btrfs)(8), [btrfs-balance](/man/btrfs-balance)(8), [btrfs-check](/man/btrfs-check)(8)
