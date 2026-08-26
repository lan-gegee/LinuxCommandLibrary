# TAGLINE

受损 btrfs 文件系统的恢复工具

# TLDR

**重建**文件系统元数据树（非常慢）

```sudo btrfs rescue chunk-recover [path/to/partition]```

修复**设备大小对齐**问题

```sudo btrfs rescue fix-device-size [path/to/partition]```

从副本中**恢复损坏的超级块**

```sudo btrfs rescue super-recover [path/to/partition]```

从中断的**事务中恢复**

```sudo btrfs rescue zero-log [path/to/partition]```

创建 **btrfs 控制设备**

```sudo btrfs rescue create-control-device```

# SYNOPSIS

**btrfs rescue** _subcommand_ [_options_] _device_

# DESCRIPTION

**btrfs rescue** 为受损的 btrfs 文件系统提供恢复工具。这些是正常挂载或 btrfs check 失败时的最后手段。

每个子命令针对特定的故障模式，例如元数据损坏、超级块损坏或事务中断。所有操作都要求文件系统处于卸载状态。

# SUBCOMMANDS

**chunk-recover**
> 扫描并重建块组树（非常慢，可能需要数小时到数天）

**fix-device-size**
> 修复导致无法挂载的设备大小不匹配问题

**super-recover**
> 从备份副本恢复超级块

**zero-log**
> 清空事务日志以修复日志回放失败问题

**create-control-device**
> 在 mknod 不可用时创建 /dev/btrfs-control

# CAVEATS

这些是紧急恢复工具。务必先备份所有可恢复的数据。在大文件系统上 chunk-recover 可能耗时极长。某些操作可能导致数据丢失。文件系统必须处于卸载状态。

# INSTALL

```apt: sudo apt install btrfs-progs```

```dnf: sudo dnf install btrfs-progs```

```pacman: sudo pacman -S btrfs-progs```

```apk: sudo apk add btrfs-progs```

```brew: brew install btrfs-progs```

```nix: nix profile install nixpkgs#btrfs-progs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[btrfs](/man/btrfs)(8), [btrfs-check](/man/btrfs-check)(8), [btrfs-restore](/man/btrfs-restore)(8)

# RESOURCES

```[Source code](https://github.com/kdave/btrfs-progs)```

```[Documentation](https://btrfs.readthedocs.io/)```

<!-- verified: 2026-06-22 -->
