# TAGLINE

用覆写模式安全删除文件

# TLDR

**安全擦除文件**

```wipe [file]```

**强制擦除文件**（不确认）

```wipe -f [file]```

**递归擦除目录**

```wipe -r [directory]```

**快速擦除**（4 次覆写而非 34 次）

```wipe -q [file]```

**自定义次数的快速擦除**

```wipe -Q [8] [file]```

**擦除但不移除文件**

```wipe -k [file]```

**详细输出**

```wipe -v [file]```

# SYNOPSIS

**wipe** [_-rcfsvq_] [_-Q passes_] [_-a_] [_file ..._]

# PARAMETERS

**-f**
> 强制；禁用确认提示

**-r**
> 递归擦除目录及其内容

**-c**
> 对每个文件请求确认（普通文件默认如此）

**-s**
> 静默模式；抑制大部分输出

**-v**
> 详细模式；显示进度

**-q**
> 快速擦除；使用 4 次覆写而非 34 次

**-Q** _passes_
> 以指定次数进行快速擦除

**-a**
> 出错即中止而不是继续

**-k**
> 擦除后保留文件（不做 unlink）

**-Z**
> 单次全零覆写（快但安全性较低）

**-l** _LENGTH_
> 设置擦除的文件大小上限

**-e**
> 使用精确文件大小（不向上取整以擦除松弛空间）

# DESCRIPTION

**wipe** 通过用特殊模式覆写文件内容来安全删除文件，防止数据被恢复。默认情况下它执行 34 次写入，其中包括 8 种随机模式，这基于 Peter Gutmann 关于安全数据擦除的研究。

该命令会覆写文件、多次重命名、截断，最后解除链接。这个多步骤过程可以挫败针对磁存储的各种数据恢复技术。

若要更快地操作，可用 **-q** 进行 4 次覆写，或用 **-Q** 指定 4 到 34 之间的自定义次数。

# CAVEATS

由于磨损均衡和写放大，安全擦除对 SSD 无效；SSD 应改用 ATA Secure Erase 或加密。日志式文件系统（ext3、ext4、XFS）可能仍会在日志中保留数据。RAID 系统和写时复制文件系统（ZFS、Btrfs）可能在冗余位置保留旧数据。

# HISTORY

wipe 实现了 Gutmann 安全删除方法，源自 Peter Gutmann **1996 年**关于磁介质数据安全清除的论文。该工具为 GNU coreutils 中的 **shred** 提供了更彻底的替代方案。

# INSTALL

```apt: sudo apt install wipe```

```dnf: sudo dnf install wipe```

```pacman: sudo pacman -S wipe```

```apk: sudo apk add wipe```

```zypper: sudo zypper install wipe```

```nix: nix profile install nixpkgs#wipe```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[shred](/man/shred)(1), [srm](/man/srm)(1), [rm](/man/rm)(1), [dd](/man/dd)(1)
