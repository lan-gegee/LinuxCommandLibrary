# TAGLINE

从 MS-DOS 文件系统中删除目录

# TLDR

**从 mtools 磁盘中删除目录**

```mrd [a:/dirname]```

**从特定驱动器删除**

```mrd [b:/path/to/dir]```

**详细输出**

```mrd -v [a:/dirname]```

# SYNOPSIS

**mrd** [**-v**] _msdosdirectory_ [_msdosdirectories..._]

# PARAMETERS

_MSDOSDIRECTORY_
> 要删除的 MS-DOS 目录。

**-v**
> 详细模式。

**-V**
> 显示 mtools 的版本。

# DESCRIPTION

**mrd** 从 MS-DOS 文件系统中删除目录。它是 mtools 软件包的一部分。如果目录不存在或非空则会报错。可以在命令行上指定多个目录。

该工具删除 FAT 驱动器上的目录，无需挂载文件系统即可工作。

# CAVEATS

属于 mtools。目录必须为空。仅支持 MS-DOS/FAT 文件系统。

# HISTORY

mrd 是 **mtools** 的一部分，自 1992 年起就在 Unix 系统上提供 MS-DOS 文件系统访问能力。

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

[mmd](/man/mmd)(1), [mcopy](/man/mcopy)(1), [mdel](/man/mdel)(1)
