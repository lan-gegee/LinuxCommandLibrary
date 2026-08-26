# TAGLINE

检查并修复 ext 文件系统

# TLDR

**检查**文件系统错误

```sudo e2fsck /dev/sdXN```

检查并**自动修复**（preen 模式）

```sudo e2fsck -p /dev/sdXN```

使用只读测试检查**坏块**

```sudo e2fsck -c /dev/sdXN```

即使文件系统干净也**强制**检查

```sudo e2fsck -f /dev/sdXN```

进行彻底的**坏块**测试

```sudo e2fsck -fccky /dev/sdXN```

**只读**检查，不做任何更改

```sudo e2fsck -n /dev/sdXN```

**详细**输出

```sudo e2fsck -v /dev/sdXN```

交互式修复，对所有问题回答**yes**

```sudo e2fsck -y /dev/sdXN```

# SYNOPSIS

**e2fsck** [_-panyrcdfvtDFV_] [_-b superblock_] [_-B blocksize_] _device_

# DESCRIPTION

**e2fsck** 检查并可选择性地修复 Linux 的 ext2、ext3 或 ext4 文件系统。运行此命令前应先卸载文件系统，或至少以只读方式挂载。

# PARAMETERS

**-a**
> 自动修复而不提示（与 -p 相同）

**-b SUPERBLOCK**
> 使用备用超级块

**-B BLOCKSIZE**
> 搜索超级块时指定块大小

**-c**
> 使用只读测试检查坏块

**-C FD**
> 将完成进度信息写入文件描述符

**-d**
> 打印调试输出

**-D**
> 优化目录

**-f**
> 即使文件系统看起来干净也强制检查

**-F**
> 检查前刷新缓冲区缓存

**-k**
> 保留已有的坏块列表

**-n**
> 以只读方式打开，对所有问题回答"no"

**-p**
> Preen 模式：自动修复安全的问题

**-t**
> 打印计时统计

**-v**
> 详细模式

**-y**
> 对所有问题回答"yes"

# CONFIGURATION

**/etc/e2fsck.conf**
> 配置文件，控制默认行为、问题处理和优化设置。

# CAVEATS

切勿在已挂载的文件系统上运行 e2fsck，除非它是以只读方式挂载的。**-y** 选项若使用不当可能导致数据丢失。修复前务必备份。

# HISTORY

**e2fsck** 是 **e2fsprogs** 的一部分，自 20 世纪 90 年代初起为 ext2/3/4 文件系统提供检查功能。

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

[fsck](/man/fsck)(8), [tune2fs](/man/tune2fs)(8), [dumpe2fs](/man/dumpe2fs)(8), [mke2fs](/man/mke2fs)(8), [badblocks](/man/badblocks)(8), [debugfs](/man/debugfs)(8)
