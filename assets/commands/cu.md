# TAGLINE

串口终端通信工具

# TLDR

**打开**串口

```sudo cu -l [/dev/ttyXYZ]```

以**指定波特率**打开串口

```sudo cu -l [/dev/ttyXYZ] -s [115200]```

以**半双工**模式打开（本地回显）

```sudo cu -l [/dev/ttyXYZ] -s [115200] -h```

带**校验位**且无流控制地打开

```sudo cu -l [/dev/ttyXYZ] -s [115200] --parity=[even] -f --nostop```

**退出** cu 会话

```<Enter><~><.>```

# SYNOPSIS

**cu** [_options_] [_system_|_phone_|_host_]

# DESCRIPTION

**cu**（Call Up）连接到另一系统，充当拨入终端。它常用于对嵌入式设备、路由器、交换机等硬件进行串口控制台访问。

断开连接的转义序列为：按 Enter，然后按 ~（波浪号），再按 .（句点）。

# PARAMETERS

**-l, --line** _device_
> 要使用的串行设备

**-s, --speed** _baud_
> 波特率（如 9600、115200）

**-h, --halfduplex**
> 在本地回显字符

**--parity** _type_
> 校验位：even、odd 或 none

**-f, --nortscts**
> 禁用硬件流控制

**--nostop**
> 禁用软件流控制

# CAVEATS

通常需要 root 权限或属于 dialout/uucp 组。转义字符（~）必须位于行首。cu 是 UUCP 软件包（通常是 GNU/Taylor UUCP）的一部分，不属于 coreutils。

# INSTALL

```apt: sudo apt install cu```

```dnf: sudo dnf install cu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[screen](/man/screen)(1), [minicom](/man/minicom)(1), [picocom](/man/picocom)(1)

# RESOURCES

```[Homepage](https://www.gnu.org/software/uucp/)```

<!-- verified: 2026-06-26 -->
