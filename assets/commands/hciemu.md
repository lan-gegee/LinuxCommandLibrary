# TAGLINE

通过 hci_vhci 内核模块模拟蓝牙 HCI 设备的旧版 BlueZ 工具

# TLDR

**以给定的本地地址模拟 HCI 设备**

```sudo hciemu [00:11:22:33:44:55]```

**模拟指定类型的设备**

```sudo hciemu -d [vhci] [00:11:22:33:44:55]```

**把模拟流量捕获到 snoop 文件**

```sudo hciemu -s [capture.snoop] [00:11:22:33:44:55]```

**在前台运行而不脱离终端**

```sudo hciemu -n [00:11:22:33:44:55]```

# SYNOPSIS

**hciemu** [_options_] _local-address_

# PARAMETERS

**-d** _device_
> 要模拟的设备类型（例如 vhci）。

**-b** _bdaddr_
> 要模拟的蓝牙设备地址。

**-s** _file_
> 把捕获的 HCI 数据包写入 snoop 文件。

**-n**
> 不从控制终端脱离。

# DESCRIPTION

**hciemu** 是一个旧版 BlueZ 测试工具，通过 **hci_vhci** 内核模块模拟蓝牙主机控制器接口（HCI）设备。它会创建一个具有指定本地地址的虚拟蓝牙控制器，让蓝牙协议栈和应用程序无需真实硬件即可得到测试。

# CAVEATS

需要 **hci_vhci** 内核模块和 root 权限。这个独立命令来自 BlueZ5 之前的 bluez-utils 测试套件，目前已从主流 Linux 发行版附带的工具中移除；现代 BlueZ 仅保留同名的内部模拟器库（供其自身测试套件使用），不再提供面向用户的二进制文件。如今需要进行交互式蓝牙测试时，请使用 **bluetoothctl**。

# HISTORY

hciemu 是最初 **BlueZ**（bluez-utils）测试工具的一部分，早于 BlueZ5 出现。此后它已从主流发行版的软件包中移除。

# SEE ALSO

[hciconfig](/man/hciconfig)(1), [hcitool](/man/hcitool)(1), [bluetoothctl](/man/bluetoothctl)(1)
