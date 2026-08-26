# TAGLINE

将磁盘上分区的存在及编号告知 Linux 内核

# TLDR

**列出**块设备或磁盘镜像上的分区

```sudo partx -l [path/to/device_or_disk_image]```

把块设备中发现的所有分区**添加**到内核

```sudo partx -a -v [path/to/device_or_disk_image]```

从内核中**删除**全部分区（不改动磁盘上的分区）

```sudo partx -d [path/to/device_or_disk_image]```

# SYNOPSIS

**partx** [**-a** | **-d** | **-s** | **-u**] [**-t** _type_] [**-n** _M_:_N_] [**-**] _disk_

**partx** [**-a** | **-d** | **-s** | **-u**] [**-t** _type_] _partition_ [_disk_]

# PARAMETERS

**-a**, **--add**
> 将指定的分区添加到内核

**-d**, **--delete**
> 从内核中删除指定的分区

**-s**, **--show**
> 列出分区（未指定操作时的默认行为）

**-l**, **--list**
> 与 **--show** 相同（列出分区）

**-u**, **--update**
> 更新指定的分区

**-n**, **--nr** _M_:_N_
> 指定分区范围（M 到 N）

**-t**, **--type** _type_
> 指定分区表类型（dos、gpt 等）

**-o**, **--output** _list_
> 定义要显示哪些列

**-g**, **--noheadings**
> 不打印标题行

**-b**, **--bytes**
> 以字节为单位打印大小

**-r**, **--raw**
> 使用原始输出格式

**-v**, **--verbose**
> 详细模式

# DESCRIPTION

**partx** 将磁盘上分区的存在及其编号告知 Linux 内核。它会解析分区表并更新内核在内存中的表示，而不修改磁盘本身。当磁盘处于使用状态期间新增或删除了分区时，这一功能非常有用。

该工具可以从块设备和磁盘镜像文件中读取分区表。它支持多种分区表格式，包括 DOS/MBR、GPT、BSD 等。

# CAVEATS

需要 root 权限。为已挂载的文件系统修改内核分区状态可能很危险。**-d** 选项只是从内核中移除分区条目，并不会修改磁盘上实际的分区表。对于较简单的使用场景，可以改用 **partprobe**。

# HISTORY

属于标准 Linux 工具集 **util-linux**。与 **partprobe** 相比，它提供对内核分区感知的更底层控制；而对大多数使用场景来说，partprobe 通常已经足够。

# INSTALL

```apt: sudo apt install util-linux```

```dnf: sudo dnf install util-linux```

```pacman: sudo pacman -S util-linux```

```apk: sudo apk add partx```

```zypper: sudo zypper install util-linux```

```brew: brew install util-linux```

```nix: nix profile install nixpkgs#util-linux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[partprobe](/man/partprobe)(8), [fdisk](/man/fdisk)(8), [parted](/man/parted)(8), [blkid](/man/blkid)(8), [lsblk](/man/lsblk)(8)
