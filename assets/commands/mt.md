# TAGLINE

控制磁带驱动器操作

# TLDR

检查磁带驱动器的**状态**

```mt -f [/dev/nst0] status```

**倒带**至磁带开头

```mt -f [/dev/nst0] rewind```

向前跳过若干**文件**

```mt -f [/dev/nst0] fsf [count]```

**倒带并定位**到指定文件的开头

```mt -f [/dev/nst0] asf [count]```

定位到**数据末尾**

```mt -f [/dev/nst0] eod```

**倒带并弹出**磁带

```mt -f [/dev/nst0] eject```

在当前位置写入 **EOF 标记**

```mt -f [/dev/nst0] eof```

# SYNOPSIS

**mt** [**-f** _device_] _operation_ [_count_]

# PARAMETERS

**-f _device_, -t _device_**
> 指定磁带设备（如 /dev/nst0、/dev/st0）

**-h**
> 列出可用命令

**-V, --version**
> 显示版本信息

# OPERATIONS

**status**
> 打印磁带驱动器的状态和位置

**rewind**
> 将磁带倒回开头

**fsf _count_**
> 向前跳过指定数量的文件

**bsf _count_**
> 向后跳过指定数量的文件

**fsr _count_**
> 向前跳过指定数量的记录

**bsr _count_**
> 向后跳过指定数量的记录

**asf _count_**
> 倒带并定位到指定文件的开头

**eod, seod**
> 移动到有效数据的末尾

**weof _count_, eof**
> 写入 EOF（文件结束）标记

**eject, offline, rewoffl**
> 倒带并卸载/弹出磁带

**erase**
> 擦除整盘磁带（耗时操作）

**retension**
> 倒带、卷到末端、再倒带（整理磁带）

**setblk _size_**
> 设置硬件块大小（字节），0 表示可变大小

**seek _block_**
> 定位到指定块号（SCSI）

**tell**
> 打印当前块号（SCSI）

# DESCRIPTION

**mt** 控制磁带驱动器操作，常用于 LTO（Linear Tape-Open）和其他 SCSI 磁带驱动器。它提供定位、倒带、弹出以及在磁带上写入控制标记等命令。

设备通过 -f 选项或 TAPE 环境变量指定。非倒带设备使用 /dev/nstX（操作后保留位置），自动倒带设备使用 /dev/stX。

# CAVEATS

磁带操作可能很慢，尤其是 erase 和 retension。选错设备（st 与 nst）会导致磁带意外倒带。部分操作仅限 SCSI 设备。要允许非 root 用户访问，需确保设备权限正确。

# HISTORY

**mt**（magnetic tape）自早期 Unix 系统起就是控制磁带驱动的标准工具。Linux 版本在传统操作之外还支持更多 SCSI 磁带特性。

# INSTALL

```dnf: sudo dnf install mt-st```

```apk: sudo apk add mt-st```

```zypper: sudo zypper install mt-st```

```nix: nix profile install nixpkgs#mt-st```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tar](/man/tar)(1), [dd](/man/dd)(1), [st](/man/st)(4)
