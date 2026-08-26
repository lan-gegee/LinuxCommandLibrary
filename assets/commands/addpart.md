# TAGLINE

告知内核存在新分区

# TLDR

告知内核某个**分区**的存在

```addpart [device] [partition] [start] [length]```

# SYNOPSIS

**addpart** _device_ _partition_ _start_ _length_

# DESCRIPTION

**addpart** 是对“添加分区” ioctl 的简单封装，用于通知 Linux 内核某个确实存在于磁盘上但未被自动识别的分区。当磁盘使用期间分区表被修改，或内核在启动时的分区扫描漏掉了某个条目时，这个命令很有用。

该命令只更新内核内存中的分区表；它不会创建或修改磁盘上的实际分区表。

# PARAMETERS

**device**
> 包含该分区的块设备（如 /dev/sda）

**partition**
> 要添加的分区号

**start**
> 分区的起始位置，以 512 字节扇区为单位

**length**
> 分区的长度，以 512 字节扇区为单位

# CAVEATS

此命令只向内核通报分区信息；不会创建或修改磁盘上的实际分区表。请使用 **fdisk** 或 **parted** 等工具来修改分区表。

# HISTORY

属于 **util-linux** 软件包，该包为 Linux 提供基础系统实用工具。

# INSTALL

```apk: sudo apk add util-linux-misc```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[delpart](/man/delpart)(8), [partx](/man/partx)(8), [fdisk](/man/fdisk)(8), [parted](/man/parted)(8)

# RESOURCES

```[Source code](https://github.com/util-linux/util-linux)```

```[Documentation](https://man7.org/linux/man-pages/man8/addpart.8.html)```

<!-- verified: 2026-06-11 -->
