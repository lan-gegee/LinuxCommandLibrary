# TAGLINE

让内核忘掉一个分区

# TLDR

**让内核忘掉 /dev/sda 的分区 1**

```sudo delpart [/dev/sda] [1]```

**让内核忘掉一个 NVMe 分区**

```sudo delpart [/dev/nvme0n1] [3]```

**显示帮助**

```delpart --help```

# SYNOPSIS

**delpart** _device_ _partition_

# DESCRIPTION

**delpart** 让 Linux 内核忘掉指定块设备上（按编号指定的）分区。它是对 `BLKPG_DEL_PARTITION` ioctl 的薄封装，只更新内核内存中的视图——磁盘上的分区表不会被改动。

典型用法是在用 **fdisk** 或 **parted** 手动编辑过分区表之后、同一磁盘上的其他分区仍然繁忙时：**delpart** 只移除单个分区的内核节点，以便之后能用 **addpart** 重建，从而避免整表重读（那是 **partprobe** 或 `blockdev --rereadpt` 的做法）。

# PARAMETERS

_device_
> 包含该分区的块设备（例如 /dev/sda、/dev/nvme0n1）。

_partition_
> 要从内核视图中移除的分区编号。

**-h**, **--help**
> 显示帮助并退出。

**-V**, **--version**
> 显示版本信息并退出。

# CAVEATS

需要 root 权限。目标分区不能处于使用状态——先卸载其上的文件系统并停止所有 swap、LVM 或 RAID 组件，否则 ioctl 会以 **EBUSY** 失败。只有内核视图会被更新；重启后内核会重读磁盘上的分区表，因此除非表本身也被修改过，否则分区会重新出现。util-linux 软件包的一部分。

# HISTORY

**delpart** 随 **util-linux** 一起发布，该项目由 Karel Zak 维护并通过 Linux Kernel Archive 分发。它与 **addpart** 和 **resizepart** 互补，都是极简的 ioctl 封装，供在运行中的系统上修改分区的脚本使用。

# INSTALL

```apk: sudo apk add util-linux-misc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[addpart](/man/addpart)(8), [partx](/man/partx)(8), [partprobe](/man/partprobe)(8), [fdisk](/man/fdisk)(8), [parted](/man/parted)(8)
