# TAGLINE

在设备或文件上设置 Linux 交换区

# TLDR

设置**交换区**

```sudo mkswap /dev/sdXY```

创建交换区前检查**坏块**

```sudo mkswap -c /dev/sdXY```

为交换分区设置**卷标**

```sudo mkswap -L swap_label /dev/sdXY```

设置指定的 **UUID**

```sudo mkswap -U random /dev/sdXY```

创建指定大小的**交换文件**

```sudo mkswap -s 4G -F /path/to/swapfile```

# SYNOPSIS

**mkswap** [_options_] _device_ [_size_]

# DESCRIPTION

**mkswap** 在设备或文件上设置 Linux 交换区。设备可以是磁盘分区或普通文件。创建后使用 swapon 启用交换区。

# PARAMETERS

**-c, --check**
> 创建交换区前检查设备坏块

**-f, --force**
> 即使检测到设备上有文件系统也强制创建

**-L, --label LABEL**
> 为交换区指定卷标（配合 swapon -L 使用）

**-p, --pagesize SIZE**
> 以字节为单位指定页大小

**-U, --uuid UUID**
> 指定 UUID（clear、random、time 或具体的 UUID 值）

**-v, --swapversion VERSION**
> 指定交换区版本（仅支持版本 1）

**-e, --endianness ENDIAN**
> 指定字节序（native 或 little）

**-o, --offset OFFSET**
> 设备上交换头的偏移量

**-s, --size SIZE**
> 交换文件的大小（与 -F 配合使用）

**-F, --file**
> 创建交换文件而不是设置已有的文件

**--verbose**
> 输出详细消息

# CAVEATS

运行 mkswap 时设备或文件不能正在使用中。btrfs 上的交换文件需要特殊处理。mkswap 之后务必运行 swapon 来激活交换区。

# HISTORY

**mkswap** 属于 **util-linux**。交换空间在物理内存耗尽时提供虚拟内存。

# INSTALL

```apt: sudo apt install util-linux```

```dnf: sudo dnf install util-linux```

```pacman: sudo pacman -S util-linux```

```apk: sudo apk add util-linux-misc```

```zypper: sudo zypper install util-linux```

```brew: brew install util-linux```

```nix: nix profile install nixpkgs#util-linux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[swapon](/man/swapon)(8), [swapoff](/man/swapoff)(8), [fdisk](/man/fdisk)(8)
