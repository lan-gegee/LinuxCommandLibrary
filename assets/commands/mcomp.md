# TAGLINE

使用 mtools 比较两个文件

# TLDR

**比较 DOS 磁盘上的文件与本地文件**

```mcomp [a:file.txt] [path/to/local_file.txt]```

**比较磁盘镜像中的文件与本地文件**

```mcomp -i [path/to/disk.img] [::/file.txt] [path/to/local_file.txt]```

# SYNOPSIS

**mcomp** _msdos-file_ _local-file_

# PARAMETERS

_msdos-file_
> 通过 mtools 访问的 DOS/软盘上的文件。

_local-file_
> 用于比较的本地文件。

# DESCRIPTION

**mcomp** 逐字节比较两个文件，其中第一个文件位于可通过 mtools 访问的 DOS 格式磁盘（如软盘）上。它在功能上等同于先用 mcopy 将文件复制到本地，再用 cmp 比较。

此命令是 **mtools** 软件包的一部分，后者是一组用于在 Unix 上访问 MS-DOS 磁盘而无需挂载的工具集合。

# CAVEATS

第一个参数必须是可以通过 mtools 访问的文件（例如位于 DOS 格式磁盘或磁盘镜像上）。在现代系统中，先用 mcopy 再用 cmp 可实现相同功能且更为常用。

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

[cmp](/man/cmp)(1), [mcopy](/man/mcopy)(1), [diff](/man/diff)(1)
