# TAGLINE

重命名 MS-DOS 文件系统上的文件和目录

# TLDR

**重命名 MS-DOS 磁盘上的文件**

```mren [a:/oldname.txt] [a:/newname.txt]```

**重命名目录**

```mren [a:/olddir] [a:/newdir]```

**详细输出**

```mren -v [a:/old] [a:/new]```

# SYNOPSIS

**mren** [_options_] _source_ _target_

# PARAMETERS

_SOURCE_
> 原始的 MS-DOS 文件/目录名。

_TARGET_
> 新的 MS-DOS 文件/目录名。

**-v**
> 详细模式。

**-D** _conflictoption_
> 指定发生名称冲突时的处理方式（autorename、overwrite、skip）。

**-o**
> 直接覆盖已有文件，不提示。

# DESCRIPTION

**mren** 重命名 MS-DOS 文件系统上的文件和目录。它是 mtools 软件包的一部分。

该工具直接操作 FAT 磁盘，无需挂载文件系统。

# CAVEATS

属于 mtools。适用 MS-DOS 命名规则。在较老的系统上有 8.3 文件名长度限制。

# HISTORY

mren 是 **mtools** 的一部分，后者是面向 Unix 系统的 MS-DOS 文件系统工具集。

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

[mcopy](/man/mcopy)(1), [mmove](/man/mmove)(1), [mdel](/man/mdel)(1)
