# TAGLINE

释放 RAM 磁盘占用的内存

# TLDR

**释放一个 RAM 磁盘**

```freeramdisk [/dev/ram0]```

# SYNOPSIS

**freeramdisk** _device_

# DESCRIPTION

**freeramdisk** 释放分配给 RAM 磁盘设备的内存，将其归还给系统的可用内存池。RAM 磁盘是以系统内存作为存储的块设备，I/O 极快，但会占用物理内存。

在运行 freeramdisk 之前，必须先用 umount 卸载该 RAM 磁盘。释放后，这些内存即可供其他进程使用。这适合在临时 RAM 磁盘不再需要时进行清理。

RAM 磁盘通常在 ramdisk 内核模块加载时定义大小限制。freeramdisk 工具属于 util-linux 软件包，配合旧式 ramdisk 驱动工作；不过在现代系统中更常用的是 tmpfs 和 ramfs。

# INSTALL

```apt: sudo apt install loadlin```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mount](/man/mount)(8), [umount](/man/umount)(8)

# RESOURCES

```[Source code](https://github.com/util-linux/util-linux)```

<!-- verified: 2026-07-15 -->
