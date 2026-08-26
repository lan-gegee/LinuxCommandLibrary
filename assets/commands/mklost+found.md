# TAGLINE

在当前工作目录中创建 lost+found 目录

# TLDR

创建预分配的 **lost+found** 目录（供 fsck 使用）

```mklost+found```

# SYNOPSIS

**mklost+found**

# DESCRIPTION

**mklost+found** 在 ext2、ext3 和 ext4 文件系统的当前工作目录中创建一个 lost+found 目录。该工具为目录预先分配磁盘块，以支持文件系统恢复操作。

当 e2fsck 执行文件系统恢复时，会把恢复出的文件碎片存放到 lost+found 目录中。预分配块可避免恢复工具在恢复过程中再分配空间——如果文件系统严重受损，这一步可能失败。

# PARAMETERS

此命令不接受任何选项或参数。它会在当前工作目录中创建该目录。

# CAVEATS

由 mke2fs 创建的每个 ext 文件系统的根目录下通常已存在 lost+found 目录。本工具用于在需要时于其他位置创建额外的实例。必须在 ext2/ext3/ext4 文件系统上运行。创建目录需要相应权限。

# HISTORY

**mklost+found** 由 **Remy Card** 创建，目前由 **Theodore Ts'o** 维护。它属于 **e2fsprogs** 软件包，即 Linux 上管理 ext 文件系统的标准工具集。

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

[e2fsck](/man/e2fsck)(8), [mke2fs](/man/mke2fs)(8), [fsck](/man/fsck)(8)
