# TAGLINE

扫描设备上的磁盘坏块

# TLDR

**检查**设备坏块（只读）

```badblocks -v [/dev/sdb]```

**破坏性**写入测试

```badblocks -wsv [/dev/sdb]```

**非破坏性**读写测试

```badblocks -nsv [/dev/sdb]```

保存**坏块列表**

```badblocks -o [badblocks.txt] [/dev/sdb]```

# SYNOPSIS

**badblocks** [_options_] _device_ [_last-block_] [_first-block_]

# DESCRIPTION

**badblocks** 通过只读、写入或非破坏性读写测试来搜索设备上的坏块。它用于验证磁盘完整性，并为文件系统工具生成坏块列表。

该工具特别适合测试新硬盘或诊断出现故障的存储设备。

# PARAMETERS

**-v**
> 详细输出模式

**-w**
> 破坏性写入测试（会抹除数据）

**-n**
> 非破坏性读写测试

**-s**
> 显示进度

**-o** _file_
> 将坏块输出到文件

**-b** _size_
> 以字节为单位的块大小（默认：1024）

**-c** _blocks_
> 单次测试的块数（默认：64）

**-p** _passes_
> 测试遍数（默认：0，即单次）

**-t** _pattern_
> 测试模式（使用 `random` 表示随机数据，或取 0-255 的数值）

**-i** _file_
> 从文件读取已有的坏块列表（跳过已知块的重新测试）

**-f**
> 强制对已挂载的设备进行测试（危险，通常会被阻止）

# TEST MODES

**Read-only**（默认）
> 安全，检测已存在的坏块

**Write** (-w)
> 破坏性、彻底的测试，会抹除所有数据

**Non-destructive** (-n)
> 安全，先读取再将原始数据写回

# WORKFLOW

```bash
# Check for bad blocks (safe)
sudo badblocks -sv /dev/sdb

# Create bad block list for e2fsck
sudo badblocks -o badblocks.txt /dev/sdb
sudo e2fsck -l badblocks.txt /dev/sdb

# Thorough destructive test (WARNING: erases data)
sudo badblocks -wsv /dev/sdb
```

# CAVEATS

写入模式会销毁设备上的所有数据。需要 root 权限。在大容量硬盘上非常缓慢（可能需要数小时或数天）。现代硬盘会自动重映射坏扇区。非破坏性模式仍有较小的数据丢失风险。SMR 硬盘在测试期间可能表现不佳。

# HISTORY

**badblocks** 自 **20 世纪 90 年代初**起就是 e2fsprogs 的一部分，最初作为 ext2 文件系统管理的配套工具而创建。

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

[e2fsck](/man/e2fsck)(8), [fsck](/man/fsck)(8), [smartctl](/man/smartctl)(8), [dd](/man/dd)(1), [hdparm](/man/hdparm)(8)
