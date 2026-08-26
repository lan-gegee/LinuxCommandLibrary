# TAGLINE

向 CD 和 DVD 写入数据

# TLDR

**显示**可用的光驱

```wodim --devices```

**刻录**纯音频光盘

```wodim dev=[/dev/optical_drive] -audio [track*.cdaudio]```

**将文件刻录**到光盘并在完成后弹出

```wodim -eject dev=[/dev/optical_drive] -data [file.iso]```

以 track-at-once 模式**刻录**文件

```wodim -tao dev=[/dev/optical_drive] -data [file.iso]```

# SYNOPSIS

**wodim** [_options_] _track_...

# PARAMETERS

**dev=_device_**
> 指定刻录设备

**--devices**
> 扫描可用的驱动器

**-data**
> 写入数据轨道

**-audio**
> 写入音频轨道

**-eject**
> 刻录完成后弹出光盘

**-tao**
> 使用 track-at-once 写入模式

**-dao**
> 使用 disc-at-once 写入模式

**speed=_n_**
> 设置刻录速度

**-v**
> 详细输出

**-dummy**
> 模拟刻录（试运行）

**blank=_type_**
> 擦除可重写光盘（fast、all）

# DESCRIPTION

**wodim**（Write Optical DIsk Media）向 CD 和 DVD 记录数据。它是 cdrecord 的一个分支，在许多系统上作为 **cdrecord** 的别名存在。

该工具支持刻录 ISO 镜像、音频 CD 和多区段光盘。它还可以擦除可重写介质，并为不同类型的光盘提供多种写入模式。

# CAVEATS

高速刻录在某些介质上可能产生错误。擦除等某些操作可能导致数据丢失。需要相应的设备访问权限。最初因 cdrecord 的许可问题而分叉出来。

# INSTALL

```apt: sudo apt install wodim```

```dnf: sudo dnf install wodim```

```apk: sudo apk add cdrkit```

```nix: nix profile install nixpkgs#cdrkit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[genisoimage](/man/genisoimage)(1), [cdrdao](/man/cdrdao)(1), [growisofs](/man/growisofs)(1)
