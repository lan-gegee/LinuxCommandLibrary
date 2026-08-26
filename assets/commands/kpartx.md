# TAGLINE

为磁盘镜像或块设备中的分区创建 device mapper 条目

# TLDR

**添加**分区映射并打印

```kpartx -av [whole_disk.img]```

**删除**分区映射

```kpartx -d [whole_disk.img]```

**列出**分区映射

```kpartx -l [whole_disk.img]```

# SYNOPSIS

**kpartx** [_options_] _device_

# PARAMETERS

**-a**
> 添加分区映射

**-d**
> 删除分区映射

**-l**
> 只列出分区映射而不添加

**-v**
> 详细输出

**-s**
> 同步模式（等待 udev 更新）

**-f**
> 强制创建映射

# DESCRIPTION

**kpartx** 为磁盘镜像或块设备中的分区创建 device mapper 条目。这样每个分区都可以作为独立的块设备访问，从而进行挂载和操作。

添加映射时，kpartx 会创建 /dev/mapper/loop0p1、/dev/mapper/loop0p2 等条目，与镜像中找到的每个分区一一对应。

# CAVEATS

需要 root 权限。内核必须启用 device mapper 和 loop 设备支持。分离 loop 设备前应先移除映射。

# HISTORY

kpartx 是 multipath-tools 软件包的一部分。它的开发目的是简化分区磁盘镜像的处理，对虚拟机镜像和系统管理任务尤其有用。

# INSTALL

```apt: sudo apt install kpartx```

```dnf: sudo dnf install kpartx```

```apk: sudo apk add kpartx```

```zypper: sudo zypper install kpartx```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[losetup](/man/losetup)(8), [dmsetup](/man/dmsetup)(8), [mount](/man/mount)(8)
