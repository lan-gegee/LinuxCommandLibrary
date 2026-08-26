# TAGLINE

支持 MBR 和 GPT 分区表的分区管理程序

# TLDR

启动**交互模式**并选中指定的磁盘

```sudo parted /dev/sdX```

在交互模式下显示**分区信息**

```print```

在交互模式下**选择**一块磁盘

```select /dev/sdX```

创建带文件系统的 **16 GB 分区**（GPT 分区表）

```mkpart partition_name ext4 0% 16G```

创建带文件系统的分区（**MBR** 分区表）

```mkpart primary ext4 0% 16G```

在交互模式下**调整**分区大小

```resizepart /dev/sdX1 end_position```

在交互模式下**移除**分区

```rm /dev/sdX1```

显示**帮助**

```?```

# SYNOPSIS

**parted** [_options_] [_device_]

# PARAMETERS

**print**
> 显示分区表信息

**select** _device_
> 选择要操作的磁盘

**mkpart** _name_ _fs-type_ _start_ _end_
> 创建新分区

**resizepart** _partition_ _end_
> 调整分区大小

**rm** _partition_
> 移除分区

**?**
> 显示交互式命令的帮助

# DESCRIPTION

**parted** 是一款支持 MBR 和 GPT 分区表的分区管理程序。在交互模式下，它提供一个用于查看和修改磁盘分区的命令行界面。

交互模式允许实时管理分区，并对更改立即给出反馈。它支持多种文件系统类型，包括 ext2、ext3、ext4、btrfs、fat16、fat32、ntfs 和 xfs。

# CAVEATS

分区变更可能导致数据丢失。修改分区前务必备份重要数据。某些操作要求先卸载分区。

# HISTORY

属于 **GNU Parted**，作为一款自由的分区编辑器而开发，支持多种分区表类型和文件系统。

# SEE ALSO

[parted](/man/parted)(8), [partprobe](/man/partprobe)(8), [fdisk](/man/fdisk)(8), [gdisk](/man/gdisk)(8)
