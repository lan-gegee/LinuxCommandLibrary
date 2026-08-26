# TAGLINE

缩减逻辑卷的大小

# TLDR

将卷缩减到**指定大小**

```sudo lvreduce -L 120G [logical_volume]```

缩减**一定数量**并同时调整文件系统大小

```sudo lvreduce -L -40G --resizefs [logical_volume]```

缩减若干**逻辑 extent**

```sudo lvreduce -l -3 [vg00/lvol1]```

**测试**缩减操作而不实际应用更改

```sudo lvreduce -t -L -10G [logical_volume]```

# SYNOPSIS

**lvreduce** [_options_] {**-L**|**-l**} [**-**]_size_ _lv_

# DESCRIPTION

**lvreduce** 缩减逻辑卷的大小。释放出的逻辑 extent 会归还给卷组，供其他逻辑卷使用。这是一项破坏性操作——被缩减区域中的数据会丢失。

在运行 **lvreduce** 之前，你应当确保卷上的文件系统已经缩小，使待移除的 extent 不再被使用；除非使用 **--resizefs** 选项。

# PARAMETERS

**-L**, **--size** _SIZE_[**k**|**m**|**g**|**t**]
> 新的绝对大小；若带前导负号，则表示从当前大小中减去的量。接受大小后缀：k（KiB）、m（MiB）、g（GiB）、t（TiB）。

**-l**, **--extents** [**-**]_Number_[**%**{**VG**|**FREE**|**PVS**|**ORIGIN**}]
> 以逻辑 extent 表示的新大小，或带负号前缀的相对缩减量。支持百分比后缀：%VG（占 VG 大小的百分比）、%FREE（占 VG 空闲空间的百分比）、%PVS（占指定 PV 的百分比）。

**-r**, **--resizefs**
> 使用 **fsadm**(8) 连同逻辑卷一起调整底层文件系统的大小。

**-f**, **--force**
> 强制缩减而不提示确认，即使可能造成数据丢失。

**-n**, **--nofsck**
> 调整大小前跳过文件系统检查。

**-y**, **--yes**
> 不提示确认；总是假定回答 yes。

**-t**, **--test**
> 以测试模式运行；命令不会更新元数据。

**-A**, **--autobackup** {**y**|**n**}
> 更改后自动备份元数据。

# CAVEATS

**数据丢失风险**：缩减前务必备份。除非使用 **--resizefs**，否则必须先缩小文件系统。XFS 和 GFS2 文件系统不支持缩小。只有 ext2/ext3/ext4 可以通过 **--resizefs** 缩小。

# INSTALL

```apt: sudo apt install lvm2```

```dnf: sudo dnf install lvm2```

```pacman: sudo pacman -S lvm2```

```apk: sudo apk add lvm2```

```zypper: sudo zypper install lvm2```

```nix: nix profile install nixpkgs#lvm2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lvextend](/man/lvextend)(8), [lvresize](/man/lvresize)(8), [lvcreate](/man/lvcreate)(8), [lvm](/man/lvm)(8), [resize2fs](/man/resize2fs)(8)
