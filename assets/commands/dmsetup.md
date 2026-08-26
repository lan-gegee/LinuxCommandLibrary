# TAGLINE

device-mapper 底层管理工具

# TLDR

**列出所有 device-mapper 设备**

```dmsetup ls```

**显示设备状态**

```dmsetup status [device_name]```

**显示详细信息**

```dmsetup info```

**显示设备表**

```dmsetup table [device_name]```

**创建一个 device-mapper 目标**

```dmsetup create [name] --table "[0 size linear /dev/sda 0]"```

**移除设备**

```dmsetup remove [device_name]```

**挂起设备**

```dmsetup suspend [device_name]```

# SYNOPSIS

**dmsetup** _command_ [_options_] [_device_name_]

# PARAMETERS

_COMMAND_
> 操作类型：ls、status、info、table、create、remove 等。

**ls**
> 列出 device-mapper 设备。

**status** [_DEVICE_]
> 显示设备状态。

**info** [_DEVICE_]
> 显示详细信息。

**table** [_DEVICE_]
> 显示设备表。

**create** _NAME_
> 创建新设备。

**remove** _DEVICE_
> 移除设备。

**suspend**/**resume** _DEVICE_
> 挂起/恢复设备。

**--table** _TABLE_
> 设备表定义。

# DESCRIPTION

**dmsetup** 是 Linux device-mapper 的底层管理工具。device-mapper 提供了一种通用机制，通过各种目标类型创建映射到物理设备的虚拟块设备。

该工具可以创建、配置和管理各类 device-mapper 设备，包括线性映射、条带卷、快照、镜像等。它是 LVM、dm-crypt 及其他 Linux 存储技术的底层基础。

虽然通常通过 LVM 或 cryptsetup 间接使用，但 dmsetup 提供了直接访问能力，适用于调试、自定义配置或理解 device-mapper 内部机制。

# CAVEATS

需要 root 权限。使用不当可能导致数据丢失。设备表必须指定有效的目标和参数。某些操作要求设备处于挂起状态。

# HISTORY

dmsetup 属于 **LVM2** 的 **device-mapper** 组件，主要由 **Red Hat** 和 **Sistina Software** 开发。device-mapper 于 **2003 年**合入 Linux 内核，为灵活的存储管理奠定了基础。

# INSTALL

```apt: sudo apt install dmsetup```

```dnf: sudo dnf install device-mapper```

```pacman: sudo pacman -S device-mapper```

```apk: sudo apk add device-mapper```

```zypper: sudo zypper install device-mapper```

```brew: brew install device-mapper```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lvm](/man/lvm)(8), [cryptsetup](/man/cryptsetup)(8), [dmraid](/man/dmraid)(8)

# RESOURCES

```[Source code](https://gitlab.com/lvmteam/lvm2)```

```[Homepage](https://sourceware.org/lvm2/)```

<!-- verified: 2026-07-11 -->
