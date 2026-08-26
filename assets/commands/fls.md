# TAGLINE

从磁盘镜像中列出文件和目录

# TLDR

**列出镜像中的文件**

```fls [disk.img]```

**列出已删除文件**

```fls -d [disk.img]```

**递归列出**

```fls -r [disk.img]```

**列出的特定目录**

```fls [disk.img] [inode]```

**连同文件类型一起列出**

```fls -p [disk.img]```

# SYNOPSIS

**fls** [_options_] _image_ [_inode_]

# PARAMETERS

_IMAGE_
> 磁盘镜像文件。

_INODE_
> 起始 inode（默认：根目录）。

**-r**
> 递归列出。

**-d**
> 显示已删除的条目。

**-l**
> 以长格式输出。

**-p**
> 显示完整路径。

**-m** _PREFIX_
> 以 mactime 格式输出。

**-o** _OFFSET_
> 分区偏移量。

**--help**
> 显示帮助信息。

# DESCRIPTION

**fls** 从磁盘镜像中列出文件和目录名。它是 The Sleuth Kit 取证工具集的一部分，无需挂载即可直接检查文件系统结构。

该工具会显示正常和已删除的文件条目，可用于数据恢复和取证分析。它支持多种文件系统，包括 NTFS、FAT、ext 和 HFS+。

fls 可以在不修改镜像内容的情况下检查磁盘镜像，保持取证完整性。

# CAVEATS

需要原始镜像或取证磁盘镜像。已删除文件的恢复取决于文件系统的状态。大型镜像的处理速度可能较慢。

# HISTORY

fls 是 Brian Carrier 所创建 **The Sleuth Kit** 的一部分。它由早期的取证工具演化而来，为数字调查提供跨平台的文件系统分析能力。

# INSTALL

```apt: sudo apt install sleuthkit```

```dnf: sudo dnf install sleuthkit```

```pacman: sudo pacman -S sleuthkit```

```apk: sudo apk add sleuthkit```

```zypper: sudo zypper install sleuthkit```

```brew: brew install sleuthkit```

```nix: nix profile install nixpkgs#sleuthkit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ils](/man/ils)(1), [mmls](/man/mmls)(1)
