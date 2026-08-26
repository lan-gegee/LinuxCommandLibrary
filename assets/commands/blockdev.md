# TAGLINE

查询和设置块设备参数

# TLDR

**报告**所有设备

```sudo blockdev --report```

报告**特定**设备

```sudo blockdev --report /dev/sda1```

获取以扇区计的**大小**

```sudo blockdev --getsz /dev/sda1```

设置**只读**

```sudo blockdev --setro /dev/sda1```

设置**读写**

```sudo blockdev --setrw /dev/sda1```

**刷新**缓冲区

```sudo blockdev --flushbufs /dev/sda1```

获取**物理扇区大小**

```sudo blockdev --getpbsz /dev/sda1```

以 512 字节扇区为单位设置**预读**

```sudo blockdev --setra 128 /dev/sda1```

**重新读取**分区表

```sudo blockdev --rereadpt /dev/sda```

# SYNOPSIS

**blockdev** [**-q**] [**-v**] _command_... _device_...

**blockdev** **--report** [_device_...]

# DESCRIPTION

**blockdev** 在命令行上查询和操作块设备的属性。它可以报告设备大小、设置只读/读写模式、刷新缓冲区，以及配置预读（read-ahead）等性能参数。

# PARAMETERS

**--report**
> 打印指定设备或所有设备的报告

**--getsz**
> 获取以 512 字节扇区计的大小

**--getsize64**
> 以字节为单位打印设备大小

**--getss**
> 打印逻辑扇区大小（字节），通常为 512

**--getpbsz**
> 获取物理块（扇区）大小

**--getbsz**
> 打印块大小（字节）（内核内部使用的值，与文件描述符相关）

**--getiomin**
> 获取最小 I/O 大小

**--getioopt**
> 获取最优 I/O 大小

**--getro**
> 获取只读状态。只读时打印 1，否则打印 0

**--setro**
> 将设备设为只读

**--setrw**
> 将设备设为读写

**--flushbufs**
> 刷新缓冲区

**--setra** _sectors_
> 以 512 字节扇区为单位设置预读值

**--getra**
> 获取当前预读值

**--rereadpt**
> 重新读取分区表

**-q**
> 安静模式

**-v**
> 详细输出

# CAVEATS

需要 root 权限。对已挂载的设备设置只读可能引发问题。更改预读会影响 I/O 性能，并非对所有负载都有益。

# HISTORY

**blockdev** 是 **util-linux** 软件包的一部分，在 Linux 系统上提供底层的块设备管理。

# INSTALL

```apt: sudo apt install util-linux```

```dnf: sudo dnf install util-linux```

```pacman: sudo pacman -S util-linux```

```apk: sudo apk add util-linux-misc```

```zypper: sudo zypper install util-linux```

```brew: brew install util-linux```

```nix: nix profile install nixpkgs#util-linux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lsblk](/man/lsblk)(8), [blkid](/man/blkid)(8), [fdisk](/man/fdisk)(8), [hdparm](/man/hdparm)(8), [partprobe](/man/partprobe)(8)

# RESOURCES

```[Source code](https://github.com/util-linux/util-linux)```

```[Documentation](https://www.man7.org/linux/man-pages/man8/blockdev.8.html)```

<!-- verified: 2026-06-19 -->
