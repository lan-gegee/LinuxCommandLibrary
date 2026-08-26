# TAGLINE

文件系统检查与修复工具

# TLDR

**检查**文件系统

```sudo fsck /dev/sdXN```

检查并在完成后**报告**统计信息

```sudo fsck -r /dev/sdXN```

**自动**修复而不提示

```sudo fsck -a /dev/sdXN```

检查 /etc/fstab 中的**所有**文件系统

```sudo fsck -A```

即使状态干净也**强制**检查

```sudo fsck -f /dev/sdXN```

显示**进度**

```sudo fsck -C /dev/sdXN```

# SYNOPSIS

**fsck** [_-sAVRTMNP_] [_-t fstype_] [_filesystem_...] [_--_] [_fs-specific-options_]

# DESCRIPTION

**fsck** 用于检查和修复 Linux 文件系统。它是一个前端，会调用针对特定文件系统的检查工具（fsck.ext4、fsck.xfs 等）。运行 fsck 时应先卸载文件系统。

# PARAMETERS

**-a**
> 自动修复而不提示。

**-A**
> 检查 /etc/fstab 中列出的所有文件系统。

**-C [FD]**
> 显示进度条。

**-f**
> 即使文件系统看似干净也强制检查。

**-M**
> 不检查已挂载的文件系统。

**-N**
> 试运行 —— 只显示将执行的操作。

**-P**
> 并行检查文件系统（配合 -A）。

**-R**
> 跳过根文件系统（配合 -A）。

**-r** _[fd]_
> 每个文件系统检查完成后输出统计信息（退出状态、耗时、内存）。

**-l**
> 用独占 flock 锁定整盘设备。只能用于单个设备（与 -A 互斥）。

**-s**
> 串行化 fsck 操作。

**-T**
> 启动时不显示标题。

**-t TYPE**
> 指定文件系统类型。

**-V**
> 详细输出。

**-y**
> 对所有问题回答 "yes"。

**-n**
> 对所有问题回答 "no"（只读检查）。

# CONFIGURATION

**/etc/fstab**
> 定义使用 -A 选项时检查哪些文件系统以及检查顺序（pass 字段）。

# CAVEATS

绝不要对已挂载的文件系统运行 fsck（只读模式除外）。自动修复（**-a** 或 **-y**）可能造成数据丢失。修复前务必备份重要数据。

# HISTORY

**fsck** 是 **util-linux** 的一部分，为不同文件系统类型的检查提供统一接口。

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

[e2fsck](/man/e2fsck)(8), [xfs_repair](/man/xfs_repair)(8), [mount](/man/mount)(8), [fstab](/man/fstab)(5)
