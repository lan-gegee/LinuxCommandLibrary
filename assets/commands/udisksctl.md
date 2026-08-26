# TAGLINE

命令行版 udisks2 存储设备管理器

# TLDR

显示磁盘**状态**概览

```udisksctl status```

显示设备的**详细信息**

```udisksctl info -b /dev/sdX```

**挂载**设备分区

```udisksctl mount -b /dev/sdX1```

**卸载**设备分区

```udisksctl unmount -b /dev/sdX1```

安全地给设备**断电**

```udisksctl power-off -b /dev/sdX```

**监视**守护进程事件

```udisksctl monitor```

**解锁**加密设备

```udisksctl unlock -b /dev/sdX1```

**锁定**加密设备

```udisksctl lock -b /dev/sdX1```

# SYNOPSIS

**udisksctl** _COMMAND_ [_OPTIONS_]

# DESCRIPTION

**udisksctl** 是与 udisksd 守护进程交互的命令行界面。它允许非特权用户查询和操作存储设备，授权通过 polkit 管理。操作包括挂载、卸载和关闭设备电源。

# PARAMETERS

**status**
> 显示磁盘驱动器和块设备的高层级信息

**info**
> 显示某个对象、设备或驱动器的详细信息

**mount**
> 挂载设备；文件系统会出现在 /run/media 层级中

**unmount**
> 卸载已挂载的设备

**unlock**
> 解锁加密设备

**lock**
> 锁定已解锁的加密设备

**loop-setup**
> 设置回环设备

**loop-delete**
> 删除回环设备

**power-off**
> 安全地关闭驱动器电源以便移除

**smart-simulate**
> 使用 SMART 数据模拟磁盘故障场景

**monitor**
> 监视守护进程的事件

**dump**
> 显示守护进程的当前状态

**-b, --block-device DEVICE**
> 指定块设备（例如 /dev/sda）

**--object-path PATH**
> 指定 UDisks 对象路径

**--filesystem-type TYPE**
> 指定挂载使用的文件系统类型

**--options OPTIONS**
> 指定挂载选项

**--force**
> 强制卸载（延迟卸载）

# CAVEATS

该命令行界面并非为脚本设计；语法可能在不保证向后兼容的情况下变动。由于授权由 polkit 处理，无需超级用户权限。

# HISTORY

**udisksctl** 是 **udisks2** 的一部分，后者是 DeviceKit-disks 的继任者，为 Linux 桌面环境提供现代磁盘管理设施。

# INSTALL

```apt: sudo apt install udisks2```

```dnf: sudo dnf install udisks2```

```pacman: sudo pacman -S udisks2```

```apk: sudo apk add udisks2```

```zypper: sudo zypper install udisks2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[udisksd](/man/udisksd)(8), [mount](/man/mount)(8), [umount](/man/umount)(8), [polkit](/man/polkit)(8)
