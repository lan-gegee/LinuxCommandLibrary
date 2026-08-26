# TAGLINE

在设备或分区上创建 ext2、ext3 或 ext4 文件系统

# TLDR

在分区上创建 **ext2 文件系统**

```sudo mke2fs -t ext2 [/dev/sdXY]```

在分区上创建 **ext3 文件系统**

```sudo mke2fs -t ext3 [/dev/sdXY]```

在分区上创建 **ext4 文件系统**

```sudo mke2fs -t ext4 [/dev/sdXY]```

创建带**卷标**的 ext4

```sudo mke2fs -t ext4 -L [my_label] [/dev/sdXY]```

**试运行**预览参数而不写入

```sudo mke2fs -n -t ext4 [/dev/sdXY]```

创建**无 root 保留块**的 ext4

```sudo mke2fs -t ext4 -m 0 [/dev/sdXY]```

# SYNOPSIS

**mke2fs** [_options_] _device_

# PARAMETERS

**-t _type_**
> 文件系统类型：ext2、ext3 或 ext4

**-L _label_**
> 设置卷标

**-U _uuid_**
> 设置文件系统 UUID

**-b _size_**
> 块大小，单位字节（1024、2048 或 4096）

**-i _bytes-per-inode_**
> 每 inode 字节数比率（影响创建的 inode 数量）

**-N _number_**
> 精确创建指定数量的 inode

**-m _percentage_**
> 为 root 保留的块百分比（默认 5%）

**-O _features_**
> 启用/禁用文件系统特性

**-c**
> 创建文件系统前检查设备坏块（用 **-cc** 进行读写测试）。

**-j**
> 创建带 ext3 日志的文件系统。

**-E** _extended-options_
> 设置扩展选项（逗号分隔），例如 `discard`、`lazy_itable_init`、`stride`、`stripe_width`。

**-T** _usage-type_
> 用途类型（default、small、big、huge、news、largefile、largefile4），用于调整默认值。

**-n**
> 试运行：显示将要执行的操作但不实际创建文件系统（用于定位备份超级块）。

**-F**
> 即使目标看起来不像分区或正在使用也强制创建。指定两次可覆盖所有安全检查。

**-q**
> 安静模式（抑制信息输出，脚本中很有用）。

**-v**
> 详细输出。

# DESCRIPTION

**mke2fs** 在设备或分区上创建 ext2、ext3 或 ext4 文件系统。它初始化超级块、块组、inode 表及其他文件系统结构。

ext4 是 Linux 当前的标准文件系统，提供日志、extents 以及相对 ext2/ext3 改进的性能。**-t** 选项选择文件系统类型并自动启用相应特性。

它常以 **mkfs.ext2**、**mkfs.ext3** 或 **mkfs.ext4** 的形式调用——这些是指向 mke2fs 并预设文件系统类型的符号链接。默认值从 **/etc/mke2fs.conf** 读取。

# CAVEATS

会**销毁目标设备上的所有数据**。运行前务必确认正确的设备路径。非 root 分区可用 **-m 0** 减少保留块百分比（默认 5%），之后也可用 **tune2fs** 调整。在已挂载的分区上创建文件系统会损坏数据。

# HISTORY

**mke2fs** 由 **Remy Card** 编写，是面向 Linux **1.0（1993 年）**引入的 ext2 文件系统的 **e2fsprogs** 套件的一部分。后来扩展为支持 ext3（日志，**2001 年**）和 ext4（extents、大容量卷，**2008 年**）。目前由 **Theodore Ts'o** 主导维护。

# INSTALL

```apt: sudo apt install e2fsprogs```

```dnf: sudo dnf install e2fsprogs```

```pacman: sudo pacman -S e2fsprogs```

```apk: sudo apk add e2fsprogs```

```zypper: sudo zypper install e2fsprogs```

```brew: brew install e2fsprogs```

```nix: nix profile install nixpkgs#e2fsprogs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mkfs](/man/mkfs)(8), [mkfs.ext4](/man/mkfs.ext4)(8), [tune2fs](/man/tune2fs)(8), [e2fsck](/man/e2fsck)(8), [dumpe2fs](/man/dumpe2fs)(8)
