# TAGLINE

列出文件系统镜像中的 inode 信息

# TLDR

**列出 inode**

```ils [image.dd]```

**只显示已分配的**

```ils -a [image.dd]```

**只显示未分配的**

```ils -e [image.dd]```

**指定偏移量**

```ils -o [2048] [image.dd]```

**机器可读输出**

```ils -m [image.dd]```

# SYNOPSIS

**ils** [_options_] _image_

# PARAMETERS

_IMAGE_
> 磁盘或分区镜像。

**-a**
> 只显示已分配的。

**-e**
> 只显示未分配的。

**-o** _OFFSET_
> 分区偏移量。

**-m**
> 机器可读输出。

**-f** _FSTYPE_
> 文件系统类型。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ils** 列出文件系统镜像中的 inode 信息。它是数字取证工具集 The Sleuth Kit 的一部分。

该工具显示已分配和已删除文件的 inode 元数据。它对文件恢复和取证分析很有用。

# CAVEATS

属于 sleuthkit。取证工具。只读分析。

# HISTORY

ils 是 **Brian Carrier** 开发的 **The Sleuth Kit** 的一部分，用于文件系统取证。

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

[fls](/man/fls)(1), [mmls](/man/mmls)(1)
