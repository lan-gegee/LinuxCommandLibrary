# TAGLINE

sysfs 设备信息查看器

# TLDR

列出所有总线、类和**根设备**

```systool```

列出**总线**设备的全部属性值

```systool -b [pci] -v```

列出**类**设备的全部属性值

```systool -c [net] -v```

只显示某条总线上的**驱动**

```systool -b [bus] -D```

显示特定**模块**的属性

```systool -m [module_name] -v```

显示设备某个具名**属性**的值

```systool -A [attribute] -b [bus] [device]```

# SYNOPSIS

**systool** [_options_ [_device_]]

# PARAMETERS

**-b** _bus_
> 显示特定总线的信息（pci、usb 等）。

**-c** _class_
> 显示特定类的信息（block、net、drm 等）。

**-m** _module_
> 显示特定模块的信息。

**-a**
> 显示所请求资源的属性。

**-v**
> 显示全部属性及其值。

**-A** _attribute_
> 显示所请求资源某个具名属性的值。

**-d**
> 只显示设备。

**-D**
> 只显示驱动。

**-P**
> 显示设备的父设备。

**-p**
> 显示资源的绝对 sysfs 路径。

**-h**
> 显示用法。

# DESCRIPTION

**systool** 按总线、类和拓扑结构显示来自 sysfs 的系统设备信息。它为浏览 `/sys/bus/`、`/sys/class/` 和 `/sys/module/` 层级提供了便捷的接口。

不带参数运行时，**systool** 会列出所有可用的总线类型、设备类和根设备。在选项后传入 _device_ 名称可将输出限制为该单个设备。可用的总线可在 `/sys/bus/` 中找到，类可在 `/sys/class/` 中找到；常见总线有 pci、usb 和 scsi，常见类有 block、net 和 drm。

# CAVEATS

需要 sysfsutils 软件包。信息来自内核的 sysfs 接口。某些属性可能需要 root 权限才能读取。

# HISTORY

**systool** 是 **sysfsutils** 软件包的一部分，为导出内核设备信息的 Linux sysfs 虚拟文件系统提供友好的访问方式。

# INSTALL

```apt: sudo apt install sysfsutils```

```dnf: sudo dnf install sysfsutils```

```pacman: sudo pacman -S sysfsutils```

```apk: sudo apk add sysfsutils```

```zypper: sudo zypper install sysfsutils```

```nix: nix profile install nixpkgs#sysfsutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lspci](/man/lspci)(8), [lsusb](/man/lsusb)(8), [lsmod](/man/lsmod)(8), [udevadm](/man/udevadm)(8)
