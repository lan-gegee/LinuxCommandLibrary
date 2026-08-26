# TAGLINE

列出块设备的相关信息

# TLDR

以**树状格式**列出所有存储设备

```lsblk```

同时列出**空设备**

```lsblk -a```

以**字节**为单位打印 SIZE 列

```lsblk -b```

输出关于**文件系统**的信息

```lsblk -f```

输出关于**块设备拓扑**的信息

```lsblk -t```

使用 **ASCII 字符**绘制树形结构

```lsblk -i```

在输出中添加额外的列

```lsblk -o NAME,SIZE,FSTYPE,MOUNTPOINT,MODEL```

以 **JSON** 格式输出

```lsblk -J```

列出**指定设备**的信息

```lsblk /dev/sda```

# SYNOPSIS

**lsblk** [_-a_] [_-b_] [_-f_] [_-t_] [_-o columns_] [_device_...]

# DESCRIPTION

**lsblk** 列出所有可用或指定块设备的信息。它读取 sysfs 文件系统和 udev 数据库来收集信息，并以树状格式展示设备与分区之间的层级关系。

# PARAMETERS

**-a, --all**
> 同时列出空设备

**-b, --bytes**
> 以字节为单位打印 SIZE 列

**-f, --fs**
> 输出文件系统相关信息（FSTYPE、LABEL、UUID、MOUNTPOINT）

**-t, --topology**
> 输出块设备拓扑信息

**-i, --ascii**
> 使用 ASCII 字符绘制树形结构

**-l, --list**
> 以列表格式输出

**-o, --output columns**
> 指定要输出的列

**-e, --exclude list**
> 按主设备号排除设备

**-n, --noheadings**
> 不打印列标题

**-p, --paths**
> 打印完整的设备路径

**-d, --nodeps**
> 不打印持有者设备或从属设备（只显示顶层设备）

**-J, --json**
> 以 JSON 格式输出

**-S, --scsi**
> 输出 SCSI 设备信息

**-r, --raw**
> 使用原始输出格式

# AVAILABLE COLUMNS

NAME, KNAME, MAJ:MIN, FSTYPE, MOUNTPOINT, LABEL, UUID, SIZE, MODEL, SERIAL, TYPE, TRAN, RO, RM, HOTPLUG, ROTA

# CAVEATS

部分信息可能需要 root 权限。已挂载的文件系统会显示挂载点；未挂载则显示空白。

# HISTORY

属于 **util-linux** 软件包。相比 /proc/partitions 和 fdisk -l 提供了更易读的替代方案。

# INSTALL

```apt: sudo apt install util-linux```

```dnf: sudo dnf install util-linux```

```pacman: sudo pacman -S util-linux```

```apk: sudo apk add lsblk```

```zypper: sudo zypper install util-linux```

```brew: brew install util-linux```

```nix: nix profile install nixpkgs#util-linux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[blkid](/man/blkid)(8), [fdisk](/man/fdisk)(8), [findmnt](/man/findmnt)(8), [df](/man/df)(1), [mount](/man/mount)(8), [parted](/man/parted)(8)
