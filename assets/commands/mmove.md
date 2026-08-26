# TAGLINE

移动或重命名 MS-DOS 文件或子目录

# TLDR

**在 MS-DOS 磁盘上移动/重命名文件**

```mmove a:oldname a:newname```

**将文件移动到磁盘上的目录**

```mmove a:[file.txt] a:[dir]/```

**移动匹配通配符的多个文件**

```mmove a:*.[txt] a:[backup]/```

**移动子目录**

```mmove a:[olddir] a:[newdir]```

**移动时显示详细输出**

```mmove -v a:[file] a:[newfile]```

# SYNOPSIS

**mmove** [**-v**] [**-D** _clash_option_] _source_ [_sources_...] _target_

# PARAMETERS

_SOURCE_
> MS-DOS 文件系统上的源文件或子目录。驱动器字母前缀（如 a:）用于指定设备。

_TARGET_
> 目标文件名或目录。

**-v**
> 详细模式。在每个文件被移动时打印其名称。

**-D** _clash_option_
> 指定文件名冲突时的处理方式。小写字母作用于主（长）文件名，大写字母作用于次（短）文件名：o/O（覆盖）、r/R（重命名）、s/S（跳过）、a/A（自动重命名）。

# DESCRIPTION

**mmove** 无需先挂载即可移动或重命名 MS-DOS（FAT）文件系统上的文件和子目录。与 MS-DOS 的 MOVE 命令不同，mmove 还能移动子目录。它是 **mtools** 软件包的一部分，该软件包提供了一组从 Unix 访问 FAT 文件系统的实用工具。

源和目标必须位于同一个 MS-DOS 文件系统上。不支持跨设备移动——请改用 **mcopy** 和 **mdel**。

# CAVEATS

只能用于 FAT 文件系统。无法在不同驱动器之间移动文件。驱动器映射在 **/etc/mtools.conf** 或 **~/.mtoolsrc** 中配置。

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

[mcopy](/man/mcopy)(1), [mdel](/man/mdel)(1), [mren](/man/mren)(1), [mmd](/man/mmd)(1)
