# TAGLINE

基于 ST-Link 的 STM32 GDB 服务器

# TLDR

**启动 GDB 服务器**

```st-util```

**在指定端口启动**

```st-util -p [4242]```

**以详细输出模式启动**

```st-util -v```

**以多目标模式启动**

```st-util -m```

**通过序列号连接指定的 ST-Link**

```st-util --serial [serial-number]```

**启用半主机（semihosting）模式启动**

```st-util --semihosting```

# SYNOPSIS

**st-util** [_-p port_] [_-v_] [_-m_] [_options_]

# PARAMETERS

**-p** _PORT_
> GDB 服务器端口。

**-v**
> 详细输出。

**-m**
> 多目标模式。

**--serial** _SN_
> 设备序列号。

**--semihosting**
> 启用半主机（semihosting）。

**-n**
> 连接时不复位。

# DESCRIPTION

**st-util** 启动一个 GDB 服务器，将 GNU 调试器（GDB）通过 ST-Link 编程器/调试器桥接到 STM32 微控制器。它实现了 GDB 远程串行协议，允许使用标准的 GDB 命令来设置断点、单步执行代码以及检查内存和寄存器。

默认情况下，服务器在端口 4242 上监听 GDB 连接。多目标模式（**-m**）支持同时调试多个 ST-Link 设备。半主机（semihosting）功能使目标固件能够通过调试连接执行 I/O 操作（例如 printf）。它是开源 stlink 工具集的一部分。

# CAVEATS

需要通过 USB 连接的 ST-Link 编程器/调试器。默认只支持一个 ST-Link 设备；多设备请使用 **-m** 或 **--serial**。默认端口（4242）不能被其他进程占用。USB 访问可能需要 root 权限或 udev 规则。

# HISTORY

**st-util** 是 **stlink** 开源工具集的一部分，最初由 **texane** 创建，现由 stlink-org 社区维护。

# INSTALL

```apt: sudo apt install stlink-tools```

```dnf: sudo dnf install stlink```

```pacman: sudo pacman -S stlink```

```apk: sudo apk add stlink```

```zypper: sudo zypper install stlink```

```brew: brew install stlink```

```nix: nix profile install nixpkgs#stlink```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[st-flash](/man/st-flash)(1), [st-info](/man/st-info)(1), [gdb](/man/gdb)(1), [openocd](/man/openocd)(1)
