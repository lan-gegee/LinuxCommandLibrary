# TAGLINE

为 GRUB 探测设备和文件系统信息

# TLDR

获取路径对应的 GRUB **文件系统模块**

```sudo grub-probe -t fs /boot/grub```

获取包含某路径的**系统设备**

```sudo grub-probe -t device /boot/grub```

获取系统设备对应的**底层磁盘**

```sudo grub-probe -t disk /dev/sdX -d```

获取**文件系统 UUID**

```sudo grub-probe -t fs_uuid /boot/grub```

获取**文件系统标签**

```sudo grub-probe -t fs_label /boot/grub```

获取 **MBR 分区类型**代码

```sudo grub-probe -t msdos_parttype /dev/sdX```

获取**分区表类型**

```sudo grub-probe -t partmap /boot/grub```

使用**自定义设备映射**进行探测

```sudo grub-probe -t fs /boot/grub -m [path/to/custom_device.map]```

# SYNOPSIS

**grub-probe** [_options_] **-t** _target_ _path_|_device_

# PARAMETERS

**-t**, **--target** _TARGET_
> 要探测的信息：fs、fs_uuid、fs_label、device、disk、drive、partmap、partuuid、abstraction、cryptodisk_uuid、msdos_parttype、gpt_parttype、hints_string、zero_check（默认：fs）

**-d**, **--device**
> 将参数视为系统设备而非路径

**-m**, **--device-map** _FILE_
> 使用自定义设备映射文件（默认：/boot/grub/device.map）

**-0**
> 使用 ASCII NUL 字符分隔输出中的条目

**-v**, **--verbose**
> 启用详细输出（传两次进入调试打印）

# DESCRIPTION

**grub-probe** 以 GRUB 的命名格式提取设备和文件系统信息。它主要由 GRUB 工具内部使用，但对调试启动配置也很有用。

目标类型包括 **fs**（文件系统模块）、**device**（系统设备路径）、**disk**（系统磁盘路径）、**drive**（GRUB 驱动器名如 hd0）、**fs_uuid**（文件系统 UUID）、**fs_label**（文件系统标签）、**partmap**（分区表类型）、**partuuid**（分区 UUID）、**abstraction**（抽象模块如 lvm）、**cryptodisk_uuid**、**msdos_parttype**、**gpt_parttype**，以及各种启动提示目标。

该工具将 Linux 设备名桥接到 GRUB 的命名约定，这对生成正确的启动配置至关重要。

# CAVEATS

大多数操作需要 root 权限。设备映射可能在两次启动之间变化，尤其是涉及可移动介质时。GRUB 的驱动器命名可能与 Linux 设备名不同。

# HISTORY

grub-probe 是 GRUB 2 工具集的一部分，提供 grub-install 和 grub-mkconfig 所使用的设备检测逻辑。它取代了 GRUB Legacy 中较简单的检测方法。

# INSTALL

```apt: sudo apt install grub-common```

```pacman: sudo pacman -S grub```

```apk: sudo apk add grub```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[grub-install](/man/grub-install)(8), [grub-mkconfig](/man/grub-mkconfig)(8), [grub-mkdevicemap](/man/grub-mkdevicemap)(8), [blkid](/man/blkid)(8)
