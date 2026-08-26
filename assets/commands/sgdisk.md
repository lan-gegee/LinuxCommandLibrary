# TAGLINE

可脚本化的 GPT 分区表管理工具

# TLDR

**显示分区表**

```sgdisk -p [/dev/sda]```

**创建新的 GPT**

```sgdisk -o [/dev/sda]```

**创建分区**

```sgdisk -n [1:0:+500M] [/dev/sda]```

**设置分区类型**

```sgdisk -t [1:8300] [/dev/sda]```

**删除分区**

```sgdisk -d [1] [/dev/sda]```

**更改分区名称**

```sgdisk -c [1:boot] [/dev/sda]```

**备份分区表**

```sgdisk -b [backup.gpt] [/dev/sda]```

**恢复分区表**

```sgdisk -l [backup.gpt] [/dev/sda]```

# SYNOPSIS

**sgdisk** [_-n part:start:end_] [_-t part:type_] [_options_] _device_

# PARAMETERS

**-p**, **--print**
> 打印分区表。

**-o**, **--clear**
> 创建新的 GPT。

**-n**, **--new** _PART:START:END_
> 创建分区。

**-d**, **--delete** _PART_
> 删除分区。

**-t**, **--typecode** _PART:TYPE_
> 设置类型代码。

**-c**, **--change-name** _PART:NAME_
> 设置名称。

**-b**, **--backup** _FILE_
> 备份分区表。

**-l**, **--load-backup** _FILE_
> 恢复分区表。

**-L**, **--list-types**
> 列出已知的分区类型代码。

**-i**, **--info** _PART_
> 显示某个分区的详细信息。

**-v**, **--verify**
> 校验磁盘的 GPT 数据结构。

**-Z**, **--zap-all**
> 销毁 GPT 和 MBR 两种数据结构。

**-g**, **--mbrtogpt**
> 将 MBR 转换为 GPT。

# DESCRIPTION

**sgdisk** 是交互式 **gdisk** 分区工具的命令行、可脚本化对应版本，专门用于操作 GUID 分区表（GPT）磁盘布局。它通过标志和参数执行所有操作，而不是交互式菜单，因此非常适合在脚本、自动化预配置和磁盘镜像工作流中使用。

创建分区采用灵活的表示法：大小可以用 **+** 前缀指定相对尺寸，用 **0** 表示填满剩余空间。诸如 **8300**（Linux 文件系统）、**EF00**（EFI 系统分区）和 **8200**（Linux swap）之类的类型代码标识每个分区的用途。可以在单条命令中串联多个操作，以原子方式构建完整的分区布局。

该工具还支持备份和恢复整个分区表、将 MBR 磁盘转换为 GPT，以及校验分区表的完整性。命令成功完成后，所有更改会在一次操作中写入。

# CAVEATS

破坏性操作会立即生效且无法撤销。指定错误的设备会销毁数据。只适用于 GPT 分区表（MBR 请使用 fdisk）。更改前请使用 `-b` 备份分区表。

# HISTORY

**sgdisk** 属于 **Rod Smith** 开发的 **GPT fdisk** 套件，最初发布于约 **2010 年**。它作为交互式 **gdisk** 工具的可脚本化对应版本而创建，填补了在脚本和部署工作流中自动化管理 GPT 分区的需求。

# INSTALL

```apt: sudo apt install gdisk```

```dnf: sudo dnf install gdisk```

```apk: sudo apk add sgdisk```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gdisk](/man/gdisk)(1), [fdisk](/man/fdisk)(1), [parted](/man/parted)(1)
