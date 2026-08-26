# TAGLINE

可脚本化的分区表操作工具

# TLDR

将分区布局**备份**到文件

```sudo sfdisk -d [/dev/sdX] > [path/to/file.dump]```

从备份**恢复**分区布局

```sudo sfdisk [/dev/sdX] < [path/to/file.dump]```

**设置**分区的类型

```sudo sfdisk --part-type [/dev/sdX] [partition_number] [swap]```

**删除**分区

```sudo sfdisk --delete [/dev/sdX] [partition_number]```

# SYNOPSIS

**sfdisk** [_options_] _device_

# PARAMETERS

**-d, --dump**
> 以 sfdisk 兼容格式转储分区表

**-l, --list**
> 列出设备上的分区

**--delete**
> 删除分区

**--part-type**
> 设置或更改分区类型

**-n, --no-act**
> 试运行；不写入更改

**-b, --backup**
> 在更改前备份分区表扇区

**-f, --force**
> 禁用所有一致性检查

**--verify**
> 检查分区表一致性

**-J, --json**
> 以 JSON 格式输出

# DESCRIPTION

**sfdisk** 是一个可脚本化的分区表操作工具。与 **fdisk** 等交互式工具不同，sfdisk 专为非交互式使用而设计，非常适合备份/恢复操作和自动化分区脚本。

其转储格式是人类可读的，可在恢复前进行编辑。这使其可用于在相同磁盘之间克隆分区布局。

# CAVEATS

需要 root 权限。修改分区表可能导致数据丢失；请务必先备份重要数据。分区布局必须与目标磁盘的几何结构兼容。属于 util-linux 软件包的一部分。

# INSTALL

```apt: sudo apt install fdisk```

```apk: sudo apk add sfdisk```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fdisk](/man/fdisk)(8), [parted](/man/parted)(8), [gdisk](/man/gdisk)(8), [partprobe](/man/partprobe)(8)
