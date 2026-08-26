# TAGLINE

ext2/ext3/ext4 文件系统的交互式调试器

# TLDR

以**只读**模式打开文件系统

```debugfs [/dev/sdXN]```

以**读写**模式打开文件系统

```debugfs -w [/dev/sdXN]```

从**文件**读取命令

```debugfs -f [path/to/cmd_file] [/dev/sdXN]```

执行**单条命令**后退出

```debugfs -R "stats" [/dev/sdXN]```

**列出已删除的** inode（交互模式）

```lsdel```

**恢复**已删除的 inode 到文件（交互模式）

```dump <[inode_number]> [/path/to/output]```

# SYNOPSIS

**debugfs** [_options_] [_device_]

# DESCRIPTION

**debugfs** 是 ext2/ext3/ext4 文件系统的交互式调试器。它允许直接操作文件系统结构，对数据恢复、分析和故障排查很有用。

可用于恢复已删除的文件、检查 inode 以及手动修复文件系统问题。

# PARAMETERS

**-w**
> 以读写模式打开（默认只读）

**-c**
> 以灾难模式打开（初始不读取 inode 和组位图，强制只读）

**-n**
> 禁用元数据校验和验证

**-f** _cmd_file_
> 从文件读取并执行命令，然后退出

**-R** _request_
> 执行单条命令后退出

**-b** _blocksize_
> 强制使用指定的块大小（字节）而非自动检测

**-s** _superblock_
> 从给定的块号读取超级块（需要 -b）

**-i**
> 将设备视为由 e2image 创建的 ext2 镜像文件

**-D**
> 使用直接 I/O 打开设备，绕过缓冲区缓存

**-z** _undo_file_
> 覆盖前将旧块内容写入撤销文件（配合 e2undo 使用）

# INTERACTIVE COMMANDS

**stats**
> 显示文件系统统计信息

**ls** _dir_
> 列出目录内容

**cat** _file_
> 显示文件内容

**lsdel**
> 列出已删除的 inode

**undel** _<inode>_ _[pathname]_
> 取消删除 inode，并可选地链接到指定路径名

**dump** _inode_ _file_
> 将 inode 内容转储到文件

**ncheck** _inode_
> 将 inode 号转换为路径名

**icheck** _block_
> 将块号转换为 inode

**logdump**
> 转储 ext3/ext4 日志内容

# CAVEATS

需要 root 权限。写入模式下务必极其谨慎。修改前先卸载文件系统。使用不当可能导致数据丢失。

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

[e2fsck](/man/e2fsck)(8), [dumpe2fs](/man/dumpe2fs)(8), [tune2fs](/man/tune2fs)(8)
