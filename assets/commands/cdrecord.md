# TAGLINE

向 CD、DVD 和蓝光盘刻录数据

# TLDR

**将 ISO 镜像刻录**到 CD/DVD

```cdrecord -v dev=[/dev/sr0] [image.iso]```

**以指定速度刻录**

```cdrecord -v speed=[16] dev=[/dev/sr0] [image.iso]```

**从 WAV 文件刻录音频 CD**

```cdrecord -v -audio dev=[/dev/sr0] [track1.wav] [track2.wav]```

**扫描可用设备**

```cdrecord -scanbus```

**擦除 CD-RW**

```cdrecord -v blank=fast dev=[/dev/sr0]```

**刻录多区段光盘**

```cdrecord -v -multi dev=[/dev/sr0] [image.iso]```

**测试刻录**而不实际写入（模拟）

```cdrecord -v -dummy dev=[/dev/sr0] [image.iso]```

**启用缓冲区欠载保护刻录**

```cdrecord -v driveropts=burnfree dev=[/dev/sr0] [image.iso]```

# SYNOPSIS

**cdrecord** [_options_] _dev=device_ [_track-options_] _track_...

# DESCRIPTION

**cdrecord** 是一款向 CD、DVD 和蓝光盘刻录数据的命令行工具。它支持多种光盘格式，包括 CD-R、CD-RW、DVD-R、DVD+R、DVD-RW、DVD+RW 以及双层变体。

该工具可以写入 ISO 镜像、从 WAV 文件制作音频 CD，以及刻录多区段光盘。它提供 burn-free（缓冲区欠载保护）、FIFO 缓冲以及 SCSI/ATAPI 设备支持等功能。

注意，在许多 Linux 系统上，cdrecord 已被 cdrkit 项目中的 wodim 取代或补充，后者提供兼容的功能。

# PARAMETERS

**dev=** _device_
> 刻录设备（如 /dev/sr0 或 SCSI 地址）。

**speed=** _n_
> 刻录速度倍数。

**-v**
> 详细输出。

**-audio**
> 从 WAV 文件写入音频 CD。

**-data**
> 写入数据轨道（默认）。

**-multi**
> 启用多区段刻录。

**-dummy**
> 模拟模式，不实际写入。

**-eject**
> 刻录完成后弹出光盘。

**blank=** _type_
> 擦除 CD-RW（fast、all、session）。

**-scanbus**
> 扫描可用的 SCSI 设备。

**-toc**
> 显示目录表。

**-dao**
> 以 Disc At Once 模式写入，音轨之间没有间隙。

**-checkdrive**
> 检查光驱能力。

**-immed**
> 设置 SCSI IMMED 标志，使装载/弹出/擦除期间可在后台操作。

**driveropts=** _opts_
> 驱动特定选项（如 burnfree 用于缓冲区欠载保护）。

**fs=** _size_
> FIFO 缓冲区大小（默认 4 MB）。

**gracetime=** _secs_
> 开始刻录前的等待时间，单位为秒（默认 2）。

# CAVEATS

需要对光学设备的写权限（通常是 root 或属于 cdrom 组）。在不支持 burnfree 的情况下，缓冲区欠载可能毁掉光盘。CD-R 光盘无法擦除。音频 CD 需要特定的 WAV 格式（44.1kHz、16 位、立体声）。设备命名因系统而异。

# HISTORY

**cdrecord** 由 **J\u00f6rg Schilling** 自 **1995 年** 起开发，成为 Unix 上标准的 CD 刻录工具。**2006 年**，许可证纠纷催生了 **cdrkit** 分支项目，其中包含作为 cdrecord 替代品的 **wodim**。大多数 Linux 发行版改用 cdrkit/wodim，但有些仍包含原始的 cdrecord。这些工具在很大程度上保持命令兼容。

# INSTALL

```apt: sudo apt install wodim```

```dnf: sudo dnf install wodim```

```apk: sudo apk add cdrkit```

```zypper: sudo zypper install cdrecord```

```nix: nix profile install nixpkgs#cdrkit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wodim](/man/wodim)(1), [genisoimage](/man/genisoimage)(1), [mkisofs](/man/mkisofs)(1), [growisofs](/man/growisofs)(1)
