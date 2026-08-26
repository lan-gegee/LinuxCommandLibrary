# TAGLINE

安全擦除磁盘空闲空间

# TLDR

**安全擦除**空闲空间（38 次覆写）

```sfill /path/to/mounted_disk```

**降低安全性的擦除**，2 次覆写

```sfill -l -v /path/to/mounted_disk```

**最快的擦除**，仅 1 次随机覆写

```sfill -ll -v /path/to/mounted_disk```

只擦除**空闲空间**（不处理 inode）

```sfill -I /path/to/mounted_disk```

只擦除**空闲 inode**

```sfill -i /path/to/mounted_disk```

# SYNOPSIS

**sfill** [_options_] _directory_

# DESCRIPTION

**sfill** 安全覆写指定目录所在分区的空闲空间和 inode。它通过多次覆写防止先前删除的文件被恢复。

# PARAMETERS

**-l**
> 降低安全性。只写入两次：一次用 0xff，最后一次用随机值。

**-ll**
> 进一步降低安全性。只写入一次随机数据。

**-v**
> 详细模式；显示进度

**-I**
> 只覆写空闲磁盘空间，不处理 inode

**-i**
> 只覆写空闲 inode，不处理磁盘空间

**-f**
> 快速但不安全的模式。不使用 /dev/urandom，不同步。

**-z**
> 最后一次用零而不是随机数据进行覆写

# CAVEATS

此操作非常耗时，尤其是默认的 38 次覆写。由于磨损均衡机制，SSD 可能无法被有效擦除。目标必须是已挂载的文件系统，不能是原始设备。

# HISTORY

**sfill** 是 **secure-delete** 软件包的一部分，该软件包提供安全擦除数据以防止取证恢复的工具。

# INSTALL

```apt: sudo apt install secure-delete```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[srm](/man/srm)(1), [shred](/man/shred)(1), [wipe](/man/wipe)(1)
