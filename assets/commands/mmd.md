# TAGLINE

在 MS-DOS 文件系统上创建目录

# TLDR

**在 MS-DOS 上创建目录**

```mmd [a:dirname]```

**创建多个目录**

```mmd [a:dir1] [a:dir2]```

**创建嵌套路径**

```mmd [a:path/to/dir]```

**详细输出**

```mmd -v [a:dirname]```

# SYNOPSIS

**mmd** [_options_] _directories_

# PARAMETERS

_DIRECTORIES_
> 要在 MS-DOS 磁盘上创建的目录。

**-v**
> 详细输出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mmd** 在 MS-DOS 文件系统上创建目录。它是 mtools 的一部分。

该工具无需挂载即可在 FAT 文件系统上创建目录。

# CAVEATS

属于 mtools。仅支持 FAT 文件系统。相当于 DOS 版的 mkdir。

# HISTORY

mmd 属于 **mtools**，为 Unix 上的 MS-DOS 文件系统提供 mkdir 功能。

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

[mcopy](/man/mcopy)(1), [mdel](/man/mdel)(1)
