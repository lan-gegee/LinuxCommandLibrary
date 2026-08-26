# TAGLINE

重放 ext 文件系统的撤销日志

# TLDR

显示**撤销文件信息**

```e2undo -h [path/to/undo_file] [/dev/sdXN]```

**试运行**并显示候选块

```e2undo -nv [path/to/undo_file] [/dev/sdXN]```

执行**撤销操作**

```e2undo [path/to/undo_file] [/dev/sdXN]```

以**详细输出**执行撤销

```e2undo -v [path/to/undo_file] [/dev/sdXN]```

覆盖前创建**备份撤销文件**

```e2undo -z [path/to/file.e2undo] [path/to/undo_file] [/dev/sdXN]```

# SYNOPSIS

**e2undo** [_options_] _undo-file_ _device_

# DESCRIPTION

**e2undo** 重放 ext2/ext3/ext4 文件系统的撤销日志。它可以撤销 e2fsck、resize2fs 或 tune2fs 等 e2fsprogs 工具失败或不合预期的操作，为文件系统修改提供一种安全机制。

当这些工具带 -z 选项运行时会生成撤销文件。撤销文件记录操作期间所有被修改的块，从而能够精确回滚到操作前的状态。这在测试文件系统修改或从被中断的操作中恢复时尤其有价值。

# PARAMETERS

**-f**
> 即使文件系统 UUID 或超级块与撤销文件不匹配也强制撤销

**-h**
> 显示撤销文件的信息而不应用它

**-n**
> 试运行：显示将要重放的内容而不修改文件系统

**-o** _offset_
> 文件系统在设备或镜像文件中的字节偏移

**-v**
> 详细输出

**-z** _file_
> 写一个新的撤销文件，记录本次撤销操作覆盖的块

# CAVEATS

需要撤销文件，而 e2fsprogs 工具只有在带各自的 **-z** 选项运行时才会创建它（例如 `e2fsck -z undo.e2undo /dev/sda1`）。文件系统必须处于卸载状态。如果文件系统自撤销文件写入后发生过变化，e2undo 会拒绝运行；除非给出 **-f**，但这有损坏文件系统的风险。属于 **e2fsprogs** 软件包。

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

[e2fsck](/man/e2fsck)(8), [tune2fs](/man/tune2fs)(8), [resize2fs](/man/resize2fs)(8), [mke2fs](/man/mke2fs)(8)

# RESOURCES

```[Source code](https://git.kernel.org/pub/scm/fs/ext2/e2fsprogs.git)```

```[Homepage](https://e2fsprogs.sourceforge.net/)```

<!-- verified: 2026-07-14 -->
