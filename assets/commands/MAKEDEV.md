# TAGLINE

在 /dev 中创建设备文件

# TLDR

**创建标准设备**

```MAKEDEV std```

**创建特定设备**

```MAKEDEV [sda]```

**创建所有设备**

```MAKEDEV generic```

**创建控制台设备**

```MAKEDEV console```

**创建 tty 设备**

```MAKEDEV tty```

# SYNOPSIS

**MAKEDEV** [_options_] _device_

# PARAMETERS

_DEVICE_
> 设备名或设备组。

**std**
> 标准设备。

**generic**
> 通用设备集。

**console**
> 控制台设备。

**-d** _DIR_
> 设备目录。

**--help**
> 显示帮助信息。

# DESCRIPTION

**MAKEDEV** 在 /dev 中创建设备文件。它会以正确的权限和类型建立设备节点。

在 udev 出现后，该工具已基本过时。现用于静态 /dev 环境或初始内存盘。

# CAVEATS

在 udev/devtmpfs 时代已过时。需要 root 权限。只能静态地创建设备。

# HISTORY

MAKEDEV 是 **udev** 自动化设备管理出现之前创建设备文件的传统方式。

# SEE ALSO

[mknod](/man/mknod)(1), [udevadm](/man/udevadm)(8)
