# TAGLINE

基于 curses 的磁盘分区编辑器

# TLDR

为**指定设备**启动分区管理器

```sudo cfdisk [/dev/sdX]```

创建**新分区表**并进行管理

```sudo cfdisk -z [/dev/sdX]```

# SYNOPSIS

**cfdisk** [_options_] _device_

# DESCRIPTION

**cfdisk** 是 util-linux 软件包中基于 curses 的磁盘分区表编辑器。它提供友好的文本界面来创建、删除、调整大小和更改磁盘分区类型，比命令驱动的 fdisk 更容易上手。

该工具同时支持 MBR (DOS) 和 GPT 分区表，并以交互式菜单形式显示分区布局。使用方向键选择分区和操作，所有改动先保存在内存中，直到显式执行 "Write" 命令才写入磁盘。

`-z` 标志从清零的分区表开始，适用于初始化新磁盘或在 MBR 和 GPT 方案之间切换。

# PARAMETERS

**-z, --zero**
> 从空分区表开始（适用于新磁盘）

**-L, --color**
> 输出带颜色

**-h, --help**
> 显示帮助

# INTERACTIVE COMMANDS

用方向键导航，按 Enter 选择：

**New**
> 创建新分区

**Delete**
> 删除选中的分区

**Type**
> 更改分区类型

**Write**
> 将改动写入磁盘

**Quit**
> 不写入直接退出

**Sort**
> 按起始扇区排序分区

# CAVEATS

只有显式选择 "Write" 才会写入改动。错误地修改分区可能导致数据丢失。修改前请先卸载相关分区。需要 root 权限。

# INSTALL

```apt: sudo apt install fdisk```

```apk: sudo apk add cfdisk```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fdisk](/man/fdisk)(8), [parted](/man/parted)(8), [gdisk](/man/gdisk)(8)

# RESOURCES

```[Source code](https://github.com/util-linux/util-linux)```

```[Documentation](https://man7.org/linux/man-pages/man8/cfdisk.8.html)```

<!-- verified: 2026-06-22 -->
