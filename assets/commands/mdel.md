# TAGLINE

从 MS-DOS 文件系统中删除文件

# TLDR

**从 MS-DOS 磁盘删除文件**

```mdel [a:file.txt]```

**删除多个文件**

```mdel [a:*.bak]```

**详细输出**

```mdel -v [a:file.txt]```

**删除目录内容**

```mdel [a:dirname/*]```

# SYNOPSIS

**mdel** [_options_] _files_

# PARAMETERS

_FILES_
> 要在 MS-DOS 磁盘上删除的文件。

**-v**
> 详细输出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mdel** 从 MS-DOS 文件系统中删除文件。它是 mtools 软件包的一部分。

该工具无需挂载即可从 FAT 文件系统中删除文件。适用于软盘和 U 盘。

# CAVEATS

属于 mtools 的一部分。仅支持 FAT 文件系统。无法删除目录。

# HISTORY

mdel 是 **mtools** 的一部分，后者是一组用于在 Unix 上访问 MS-DOS 磁盘的工具集合。

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

[mcopy](/man/mcopy)(1), [mdeltree](/man/mdeltree)(1)
