# TAGLINE

可移动介质弹出工具

# TLDR

显示**默认**设备

```eject [-d|--default]```

**弹出**默认设备

```eject```

**弹出**指定设备

```eject [/dev/cdrom]```

**切换**托盘打开/关闭状态

```eject [-T|--traytoggle] [/dev/cdrom]```

弹出 **cd** 驱动器

```eject [-r|--cdrom] [/dev/cdrom]```

弹出**软盘**驱动器

```eject [-f|--floppy] [/mnt/floppy]```

弹出**磁带**驱动器

```eject [-q|--tape] [/mnt/tape]```

设置是否**忽略**物理按钮

```eject [-i|--manualeject] [on|off]```

# SYNOPSIS

**eject** [_options_] [_device_|_mountpoint_]

# DESCRIPTION

**eject** 弹出可移动介质，如 CD、DVD、软盘和磁带驱动器。它还可以控制托盘机构以及锁定/解锁设备。

设备类型的默认尝试顺序是 cd-rom、scsi、floppy，最后是 tape。

# PARAMETERS

**-d, --default**
> 显示默认设备

**-T, --traytoggle**
> 切换托盘打开/关闭状态

**-r, --cdrom**
> 使用 CD-ROM 方式弹出

**-f, --floppy**
> 使用软盘方式弹出

**-q, --tape**
> 使用磁带方式弹出

**-i, --manualeject** _on|off_
> 控制物理按钮是否有效

**-t, --trayclose**
> 关闭托盘

**-a, --auto** _on|off_
> 启用或禁用驱动器的自动弹出模式

**-m, --no-unmount**
> 即使设备已挂载也不卸载它

**-M, --no-partitions-unmount**
> 不卸载同一设备上的其他分区

**-n, --noop**
> 显示将要使用的设备但不实际弹出

**-p, --proc**
> 使用 /proc/mounts 而不是 /etc/mtab

**-s, --scsi**
> 使用 SCSI 命令弹出

**-x, --cdspeed** _speed_
> 设置 CD-ROM 驱动器速度（0 表示最大速度）

**-X, --listspeed**
> 列出驱动器支持的速度

**-v, --verbose**
> 打印更多关于当前操作的信息

# CAVEATS

eject 在弹出前会先卸载设备（默认还会卸载其上的所有其他分区）；使用 **-m** 可跳过这一步。如果仍有进程在已挂载的文件系统上打开文件，弹出会失败。许多笔记本和 USB 光驱会忽略托盘命令，**-x** 的速度控制取决于驱动器固件。属于 **util-linux** 软件包。

# INSTALL

```apt: sudo apt install eject```

```apk: sudo apk add util-linux-misc```

```nix: nix profile install nixpkgs#eject```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mount](/man/mount)(8), [umount](/man/umount)(8), [lsblk](/man/lsblk)(8), [udisksctl](/man/udisksctl)(1)

# RESOURCES

```[Source code](https://github.com/util-linux/util-linux)```

```[Documentation](https://man7.org/linux/man-pages/man1/eject.1.html)```

<!-- verified: 2026-07-14 -->
