# TAGLINE

列出 Linux ext2/ext3/ext4 文件系统上的文件属性

# TLDR

**列出**属性

```lsattr```

列出**路径**下的属性

```lsattr path/to/file```

**递归**列出

```lsattr -R```

显示**隐藏**文件

```lsattr -a```

列出**目录**本身的属性（不含其内容）

```lsattr -d [path/to/dir]```

以**完整名称**显示属性

```lsattr -l [path/to/file]```

列出带**版本号**的属性

```lsattr -v [path/to/file]```

# SYNOPSIS

**lsattr** [_OPTIONS_] [_files_...]

# DESCRIPTION

**lsattr** 列出 Linux ext2/ext3/ext4 文件系统上的文件属性。它显示不可变（immutable）、仅追加（append-only）等由 chattr 设置的特殊扩展属性。

# PARAMETERS

**-R**
> 递归列出属性

**-a**
> 列出所有文件，包括隐藏文件

**-d**
> 列出目录本身而非其内容

**-v**
> 列出文件的版本/世代号

**-p**
> 列出文件的项目编号

**-l**
> 使用完整名称代替单字母缩写

**-V**
> 显示程序版本

# CAVEATS

仅显示支持扩展属性的文件系统（ext2/ext3/ext4、btrfs）上的属性。输出格式将属性标志显示为单个字符（如 i 表示 immutable，a 表示 append-only），未设置的标志用短横线（-）表示，后跟文件名。

# HISTORY

**lsattr** 属于 **e2fsprogs**，提供 Linux 文件系统的属性查看功能。

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

[chattr](/man/chattr)(1), [ls](/man/ls)(1)
