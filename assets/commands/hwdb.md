# TAGLINE

将硬件属性映射到 udev 设备属性的 systemd 组件

# TLDR

**更新硬件数据库**

```sudo systemd-hwdb update```

**查询设备属性**

```systemd-hwdb query [modalias]```

显示硬件数据库路径

```systemd-hwdb --help```

# SYNOPSIS

**systemd-hwdb** [_options_] _command_

# PARAMETERS

**update**
> 将 hwdb 文件编译为二进制格式。

**query** _modalias_
> 查询指定 modalias 的属性。

**--path** _path_
> 自定义 hwdb 路径。

**--root** _root_
> 根目录。

**--strict**
> 严格解析模式。

**--usr**
> 使用 /usr 目录。

# DESCRIPTION

**hwdb**（Hardware Database，硬件数据库）是一个 systemd 组件，用于将硬件属性映射到 udev 设备属性。它通过 modalias 字符串匹配硬件，并设置设备名称、权限和驱动提示等属性。

该数据库由 /usr/lib/udev/hwdb.d/ 和 /etc/udev/hwdb.d/ 中的文本文件编译成二进制格式，以实现快速匹配。

# HWDB FILE FORMAT

```
# /etc/udev/hwdb.d/70-custom.hwdb
# Match USB keyboard
usb:v04D9p1702*
 KEYBOARD_KEY_70039=leftctrl
 KEYBOARD_KEY_3a=capslock

# Match by PCI ID
pci:v00001234d00005678*
 ID_VENDOR=Custom Vendor
```

# USAGE

```bash
# Update after editing hwdb files
sudo systemd-hwdb update
sudo udevadm trigger

# Find modalias for device
udevadm info /dev/input/event0 | grep MODALIAS
```

# CAVEATS

修改后需要执行 hwdb update 和 udevadm trigger。modalias 格式因总线类型而异。错误的条目可能导致设备问题。

# SEE ALSO

[udevadm](/man/udevadm)(8)
