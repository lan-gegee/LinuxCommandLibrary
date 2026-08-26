# TAGLINE

虚拟磁盘镜像格式转换

# TLDR

将 **raw 挂载为 DMG**

```xmount --in raw [path/to/image.dd] --out dmg [mountpoint]```

带缓存将 **EWF 挂载为 VHD**

```xmount --cache [path/to/cache.ovl] --in ewf [path/to/image.E??] --out vhd [mountpoint]```

在偏移处挂载**分区**

```xmount --offset 2048 --in raw [path/to/image.dd] --out raw [mountpoint]```

# SYNOPSIS

**xmount** [_OPTIONS_] --in _FORMAT_ _IMAGE_ --out _FORMAT_ _MOUNTPOINT_

# PARAMETERS

**--in** _FORMAT_ _IMAGE_
> 输入格式和镜像文件（raw、ewf、aff 等）

**--out** _FORMAT_
> 输出格式（raw、dmg、vhd、vdi、vmdk）

**--cache** _FILE_
> 用于记录修改的写入缓存文件

**--offset** _SECTORS_
> 分区的扇区偏移量

**--sizelimit** _BYTES_
> 限制虚拟镜像的大小

# DESCRIPTION

**xmount** 使用 FUSE 创建虚拟磁盘镜像，并在格式之间实时转换。它对取证分析很有用，允许以只读方式访问不同格式的磁盘镜像。

写入缓存支持使你能够进行修改而不改动原始镜像。

# CAVEATS

需要 FUSE 支持。某些格式转换可能不支持全部特性。主要用于取证和虚拟化用途。

# INSTALL

```apt: sudo apt install xmount```

```dnf: sudo dnf install xmount```

```brew: brew install xmount```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mount](/man/mount)(8), [losetup](/man/losetup)(8), [qemu-img](/man/qemu-img)(1)
