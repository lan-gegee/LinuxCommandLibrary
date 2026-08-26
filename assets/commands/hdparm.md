# TAGLINE

获取和设置 SATA/IDE 硬盘参数

# TLDR

**获取设备识别信息**

```sudo hdparm -I [/dev/sda]```

**测试缓冲读取和缓存读取速度**

```sudo hdparm -tT [/dev/sda]```

**获取或设置写缓存**

```sudo hdparm -W [1] [/dev/sda]```

**查看当前电源模式状态**

```sudo hdparm -C [/dev/sda]```

**设置高级电源管理级别**（1-127 允许停转，128-254 保持旋转）

```sudo hdparm -B [127] [/dev/sda]```

**设置待机超时时间**（数值以 5 秒为增量，0 表示禁用）

```sudo hdparm -S [60] [/dev/sda]```

**强制硬盘进入待机模式**

```sudo hdparm -y [/dev/sda]```

# SYNOPSIS

**hdparm** [_OPTIONS_] _device_

# DESCRIPTION

**hdparm** 用于获取和设置 SATA/IDE 硬盘参数。它可以显示设备信息、配置电源管理设置、测试性能，以及启用或禁用各种硬盘特性。

# PARAMETERS

**-I**
> 显示详细的设备识别信息

**-i**
> 显示内核缓存的识别信息

**-B** [_value_]
> 获取或设置高级电源管理（1-254）

**-C**
> 显示当前的电源模式状态

**-S** _value_
> 设置待机超时时间（0=关闭，1-240=以 5 秒递增，241-251=以 30 分钟递增）

**-y**
> 强制硬盘进入待机模式

**-Y**
> 强制硬盘进入休眠模式（可能需要断电重启才能恢复）

**-t**
> 测试缓冲读取速度

**-T**
> 测试缓存读取速度

**-g**
> 显示硬盘几何信息（柱面、磁头、扇区、容量）

**-M** [_value_]
> 获取或设置自动声学管理（0=关闭，128=安静，254=快速）

**-W** [_value_]
> 获取或设置写缓存（0=关闭，1=开启）

**-F**
> 刷新硬盘写缓存

**--security-erase** _password_
> 安全擦除硬盘（警告：会销毁所有数据）

# CAVEATS

部分功能需要内核和硬件支持。APM 值为 1-127 时允许停转，128-254 则保持盘片旋转。休眠模式（-Y）可能需要重新上电才能恢复。不给任何选项时，默认按 -acdgkmur 处理。

# HISTORY

自 IDE 硬盘时代早期以来，**hdparm** 就一直是 Linux 上控制硬盘参数的标准工具。

# INSTALL

```apt: sudo apt install hdparm```

```dnf: sudo dnf install hdparm```

```pacman: sudo pacman -S hdparm```

```apk: sudo apk add hdparm```

```zypper: sudo zypper install hdparm```

```nix: nix profile install nixpkgs#hdparm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[smartctl](/man/smartctl)(8), [blkid](/man/blkid)(8), [lsblk](/man/lsblk)(8)
