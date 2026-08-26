# TAGLINE

面向 ZFS、btrfs 和 nilfs2 的交互式文件级 Time Machine

# TLDR

**显示文件的所有可用版本**

```httm [path/to/file]```

**交互式浏览快照**

```httm -i [path/to/file]```

**从快照恢复文件**

```httm -r [path/to/file]```

**列出目录中被删除的文件**

```httm -d [path/to/directory]```

**递归列出被删除的文件**

```httm -R [path/to/directory]```

**交互式清理快照**

```httm --prune```

# SYNOPSIS

**httm** [**-i**|**-r**|**-d**|**-R**] [_options_] [_path_]

# DESCRIPTION

**httm** 会列出驻留在文件系统快照中的文件的所有唯一可用版本，包括其大小、日期及对应位置。它支持 **ZFS**、**btrfs**、**nilfs2** 快照，以及 **Restic** 和 **Time Machine** 备份。

该工具有四种原生交互模式：**browse** 用于浏览快照版本，**select** 用于选择特定版本，**prune** 用于删除旧快照，**restore** 用于恢复文件。它还能搜索并递归列出被删除的文件，包括隐藏在被删除目录之后的文件。

# CAVEATS

需要支持快照的文件系统（ZFS、btrfs 或 nilfs2）或兼容的备份系统。性能取决于快照的数量。恢复操作会覆盖当前版本的文件。

# HISTORY

**httm** 由 **kimono-koans** 创建，使用 **Rust** 编写。其设计目标是将 macOS Time Machine 直观的文件级浏览体验带到 Linux 上支持快照的文件系统中。

# INSTALL

```apk: sudo apk add httm```

```brew: brew install httm```

```nix: nix profile install nixpkgs#httm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[zfs](/man/zfs)(8), [btrfs](/man/btrfs)(8), [restic](/man/restic)(1)
