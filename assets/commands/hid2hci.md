# TAGLINE

在 HID 和 HCI 模式之间切换蓝牙 USB 适配器

# TLDR

**将设备切换到 HCI 模式**

```sudo hid2hci --mode=hci --method=csr --devpath=[/sys/devices/...]```

**将 Dell 设备切换到 HCI 模式**

```sudo hid2hci --mode=hci --method=dell --devpath=[/sys/devices/...]```

**将设备恢复到 HID 模式**

```sudo hid2hci --mode=hid --method=csr --devpath=[/sys/devices/...]```

# SYNOPSIS

**hid2hci** [_options_]

# PARAMETERS

**--mode** _MODE_
> 要切换到的目标模式：hid 或 hci。

**--method** _METHOD_
> 特定厂商的切换方法（csr、csr2、logitech-hdi、dell）。

**--devpath** _PATH_
> /sys 中的设备路径。

**--help**
> 显示帮助信息。

# DESCRIPTION

**hid2hci** 在 HID 和 HCI 模式之间切换蓝牙 USB 适配器。某些设备启动时处于 HID 模式，需要切换后才能作为蓝牙控制器使用。

某些以键盘/鼠标模式启动的 USB 蓝牙适配器需要用到该工具。切换之后，bluez 才能使用该设备。

# CAVEATS

因设备而异。需要正确的 method 参数。属于 BlueZ 软件包的一部分。

# HISTORY

hid2hci 作为 **BlueZ** 的一部分开发，用于处理具有双模式固件的 USB 蓝牙适配器。

# SEE ALSO

[bluetoothctl](/man/bluetoothctl)(1), [hciconfig](/man/hciconfig)(1)
