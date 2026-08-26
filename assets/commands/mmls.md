# TAGLINE

显示磁盘分区布局

# TLDR

**列出分区**

```mmls [disk.img]```

**从设备列出**

```mmls [/dev/sda]```

**添加一列**显示以字节计的分区大小

```mmls -B [disk.img]```

**指定镜像中的卷偏移量**（以扇区为单位）

```mmls -o [63] [disk.img]```

**强制指定分区表类型**

```mmls -t [gpt] [disk.img]```

**列出支持的表类型**

```mmls -t list```

**设置设备扇区大小**

```mmls -b [4096] [disk.img]```

# SYNOPSIS

**mmls** [_-t mmtype_] [_-o offset_] [_-i imgtype_] [_-b dev_sector_size_] [_-BrvV_] [_-aAmM_] _image_ [_images_]

# PARAMETERS

_IMAGE_
> 要分析的磁盘镜像（或设备）。分卷镜像可以给定多个文件名。

**-t** _TYPE_
> 要分析的分区表类型（例如 **dos**、**mac**、**bsd**、**sun**、**gpt**）。使用 **-t list** 列出受支持的类型。省略时自动检测。

**-i** _IMGTYPE_
> 镜像文件的格式（例如 **raw**、**ewf**）。使用 **-i list** 列出受支持的类型。省略时自动检测。

**-o** _OFFSET_
> 分区表所在卷在镜像中的起始扇区偏移量。

**-b** _SIZE_
> 底层设备扇区的大小，单位为字节。默认为 512。

**-B**
> 在输出中添加一列，给出每个分区以字节计的大小。

**-r**
> 递归进入 DOS 分区并查找其他分区表。

**-a**
> 只显示已分配的卷（分区表中列出的那些）。

**-A**
> 只显示未分配的卷（未划归任何分区的间隙）。

**-m**
> 显示元数据卷（保存分区表本身的那些扇区）。

**-M**
> 隐藏元数据卷。

**-v**
> 向 stderr 输出详细的调试信息。

**-V**
> 显示版本信息。

# DESCRIPTION

**mmls** 显示磁盘的布局，包括分区表和未分配空间。它是 The Sleuth Kit（TSK）的一部分——这是一套用于数字取证和磁盘镜像分析的命令行工具。

默认情况下它按起始扇区排序显示所有卷，包括未分配区域和元数据。每个条目都会报告其起止扇区和长度，这使得 mmls 很适合在检查单个分区时找出应传给其他 TSK 工具（如 **fls** 或 **fsstat**）的偏移量。它支持 DOS 分区、BSD 磁盘标签、Sun 切片、Mac 分区和 GPT。

# CAVEATS

mmls 是只读的取证工具：它从不修改镜像。此处报告的扇区值通常可直接作为其他 Sleuth Kit 工具的 **-o** 偏移量。对于扇区大小非标准的镜像，必须相应地设置 **-b**，否则偏移量将是错误的。

# HISTORY

mmls 是 **The Sleuth Kit** 的一部分，这套开源磁盘镜像分析取证工具由 **Brian Carrier** 创建，其前身是 Coroner's Toolkit（TCT）。

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

[fdisk](/man/fdisk)(8), [parted](/man/parted)(8), [fls](/man/fls)(1)
