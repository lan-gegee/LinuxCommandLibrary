# TAGLINE

向蓝牙设备发送 L2CAP 回显请求，类似于 IP 网络中的 ping

# TLDR

**Ping 一台蓝牙设备**

```l2ping [AA:BB:CC:DD:EE:FF]```

**发送指定数量的数据包**

```l2ping -c [5] [AA:BB:CC:DD:EE:FF]```

**设置数据包大小**

```l2ping -s [1024] [AA:BB:CC:DD:EE:FF]```

**使用指定的蓝牙适配器**

```l2ping -i [hci0] [AA:BB:CC:DD:EE:FF]```

**设置超时时间**

```l2ping -t [10] [AA:BB:CC:DD:EE:FF]```

# SYNOPSIS

**l2ping** [_options_] _bd_addr_

# PARAMETERS

**-i** _hciX_
> 使用指定的蓝牙适配器。

**-c** _count_
> 要发送的数据包数量。

**-s** _size_
> 数据包的大小（字节）。

**-t** _timeout_
> 响应超时时间（秒）。

**-d** _delay_
> 两次 ping 之间的延迟（秒）。

**-f**
> 泛洪 ping 模式（数据包之间不设延迟）。

**-r**
> 反向 ping 模式（发送回显应答而非回显请求）。

**-v**
> 校验响应负载与请求负载完全一致。

# DESCRIPTION

**l2ping** 向蓝牙设备发送 L2CAP 回显请求，作用类似于 IP 网络中的 ping。它可以测量往返时间、检测丢包并测试蓝牙连通性。它是 BlueZ 蓝牙协议栈的组成部分。

# CAVEATS

需要 root 权限。并非所有蓝牙设备都会响应 L2CAP ping。蓝牙适配器必须处于启用状态。

# INSTALL

```apt: sudo apt install bluez```

```dnf: sudo dnf install bluez```

```pacman: sudo pacman -S bluez```

```apk: sudo apk add bluez```

```zypper: sudo zypper install bluez```

```brew: brew install bluez```

```nix: nix profile install nixpkgs#bluez```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hcitool](/man/hcitool)(1), [bluetoothctl](/man/bluetoothctl)(1)
