# TAGLINE

分区表操作工具

# TLDR

**列出**分区

```sudo fdisk -l```

启动**交互式**分区操作程序

```sudo fdisk [/dev/sdX]```

# SYNOPSIS

**fdisk** [_-l_] [_-u_] [_-s partition_] [_device_]

# DESCRIPTION

**fdisk** 是一个对话驱动的程序，用于管理存储驱动器上的分区表和分区。它支持 MBR、GPT、SGI 和 Sun 分区表。

# PARAMETERS

**-l, --list**
> 列出所有设备或指定设备的分区表

**-u, --units**
> 以扇区（默认）或柱面为单位显示

**-s, --getsz partition**
> 打印分区大小（以 512 字节扇区计）

**-b, --sector-size size**
> 指定物理和逻辑扇区大小

**-c, --compatibility mode**
> 指定兼容模式（dos 或 nondos）

**-L, --color**
> 输出着色

**-t, --type type**
> 指定磁盘标签类型（dos、gpt、sgi、sun）

# INTERACTIVE COMMANDS

**m**: 显示帮助菜单
**p**: 打印分区表
**n**: 创建新分区
**d**: 删除分区
**t**: 更改分区类型
**l**: 列出已知的分区类型
**w**: 写入更改并退出
**q**: 不保存更改直接退出
**g**: 创建新的 GPT 分区表
**o**: 创建新的 DOS 分区表

# CAVEATS

**危险**：只有按下 'w' 时才会写入更改。写入前请仔细确认。现代 fdisk 原生支持 GPT。MBR 分区表（非 fdisk 本身）限制为 2TB；更大的磁盘请使用 GPT。

# HISTORY

util-linux 软件包的一部分。源自 **Minix** 和早期 Linux 的原始 fdisk。是最古老的 Linux 磁盘分区工具之一。

# INSTALL

```apt: sudo apt install fdisk```

```apk: sudo apk add util-linux-misc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[parted](/man/parted)(8), [cfdisk](/man/cfdisk)(8), [gdisk](/man/gdisk)(8), [sfdisk](/man/sfdisk)(8), [partprobe](/man/partprobe)(8)
