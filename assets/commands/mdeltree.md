# TAGLINE

从 MS-DOS 文件系统中删除目录

# TLDR

**删除目录树**

```mdeltree [a:dirname]```

**删除多个目录**

```mdeltree [a:dir1] [a:dir2]```

**详细输出**

```mdeltree -v [a:dirname]```

# SYNOPSIS

**mdeltree** [_options_] _directories_

# PARAMETERS

_DIRECTORIES_
> 要在 MS-DOS 磁盘上删除的目录。

**-v**
> 详细输出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mdeltree** 从 MS-DOS 文件系统中删除目录。它删除目录及其所有内容。

该工具是 mtools 的一部分。它是 FAT 文件系统上 rm -rf 的 MS-DOS 等价物。

# CAVEATS

属于 mtools 的一部分。仅支持 FAT 文件系统。递归删除所有内容。

# HISTORY

mdeltree 是 **mtools** 的一部分，在 Unix 系统上提供 MS-DOS deltree 功能。

# INSTALL

```apt: sudo apt install mtools```

```dnf: sudo dnf install mtools```

```pacman: sudo pacman -S mtools```

```apk: sudo apk add mtools```

```zypper: sudo zypper install mtools```

```brew: brew install mtools```

```nix: nix profile install nixpkgs#mtools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mdel](/man/mdel)(1), [mmd](/man/mmd)(1), [mcopy](/man/mcopy)(1)
