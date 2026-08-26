# TAGLINE

向 MS-DOS 文件系统复制或从中复制文件

# TLDR

**复制文件到 MS-DOS 磁盘**

```mcopy [file.txt] [a:]```

**从 MS-DOS 磁盘复制**

```mcopy [a:file.txt] [.]```

**复制多个文件**

```mcopy [*.txt] [a:]```

**保留修改时间**

```mcopy -m [file] [a:]```

**不提示直接覆盖**

```mcopy -o [file] [a:]```

**递归复制**

```mcopy -s [dir/] [a:]```

# SYNOPSIS

**mcopy** [_options_] _source_ _target_

# PARAMETERS

_SOURCE_
> 源文件或目录。

_TARGET_
> 目标位置。

**-m**
> 保留修改时间。

**-o**
> 不询问直接覆盖。

**-s**
> 递归复制。

**-n**
> 无需确认。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mcopy** 向 MS-DOS 文件系统复制或从中复制文件。它是 mtools 软件包的一部分。

该工具无需挂载即可访问 FAT 文件系统。适用于软盘和 U 盘。

# CAVEATS

属于 mtools 的一部分。需要 mtools 配置。仅支持 FAT 文件系统。

# HISTORY

mcopy 是 **mtools** 的一部分，后者是一组用于在 Unix 上访问 MS-DOS 磁盘的工具集合。

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

[mdel](/man/mdel)(1)
