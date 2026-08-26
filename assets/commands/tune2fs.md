# TAGLINE

调整 ext2/ext3/ext4 文件系统参数

# TLDR

设置检查前的最大**挂载次数**

```sudo tune2fs -c 2 /dev/sdXN```

设置文件系统**标签**

```sudo tune2fs -L 'MY_LABEL' /dev/sdXN```

启用 **discard** 和扩展属性

```sudo tune2fs -o discard,user_xattr /dev/sdXN```

启用**日志功能**

```sudo tune2fs -o has_journal /dev/sdXN```

分配新的**随机 UUID**

```sudo tune2fs -U random /dev/sdXN```

设置**保留块**百分比

```sudo tune2fs -m 1 /dev/sdXN```

# SYNOPSIS

**tune2fs** [_options_] _device_

# DESCRIPTION

**tune2fs** 调整 ext2、ext3 或 ext4 文件系统上的可调参数。许多参数可以在文件系统挂载状态下修改，但有些则要求文件系统处于卸载状态。

# PARAMETERS

**-c MAX-MOUNT-COUNTS**
> 设置 fsck 前的最大挂载次数

**-C MOUNT-COUNT**
> 设置当前挂载计数

**-e ERROR-BEHAVIOR**
> 设置错误处理行为（continue、remount-ro、panic）

**-E EXTENDED-OPTIONS**
> 设置扩展选项

**-f**
> 强制对存在错误的文件系统执行操作

**-i INTERVAL**
> 文件系统检查的间隔时间（d/w/m 表示天/周/月）

**-j**
> 为 ext2 文件系统添加 ext3 日志

**-J JOURNAL-OPTIONS**
> 设置日志选项

**-l**
> 列出文件系统超级块内容

**-L LABEL**
> 设置文件系统标签

**-m RESERVED-BLOCKS-PERCENTAGE**
> 设置保留块的百分比

**-o OPTIONS**
> 设置/清除默认挂载选项

**-O FEATURES**
> 设置/清除文件系统特性

**-r RESERVED-BLOCKS-COUNT**
> 设置保留块的数量

**-T TIME**
> 设置上次文件系统检查的时间

**-u USER**
> 设置可以使用保留块的用户

**-U UUID**
> 设置文件系统的 UUID

# CAVEATS

某些更改需要先卸载文件系统。错误地更改某些特性可能导致文件系统无法挂载。进行任何更改前请务必备份重要数据。

# HISTORY

**tune2fs** 属于 **e2fsprogs**，即 ext2/3/4 文件系统工具软件包。

# INSTALL

```apt: sudo apt install e2fsprogs```

```dnf: sudo dnf install e2fsprogs```

```pacman: sudo pacman -S e2fsprogs```

```apk: sudo apk add e2fsprogs-extra```

```zypper: sudo zypper install e2fsprogs```

```brew: brew install e2fsprogs```

```nix: nix profile install nixpkgs#e2fsprogs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[e2fsck](/man/e2fsck)(8), [dumpe2fs](/man/dumpe2fs)(8), [mke2fs](/man/mke2fs)(8)
