# TAGLINE

通过 IP 网络共享 USB 设备

# TLDR

列出**本地**设备

```usbip list -l```

在服务器上**绑定**设备

```sudo usbip bind -b [bus_id]```

在客户端加载**内核模块**

```sudo modprobe vhci-hcd```

**连接**到远程设备

```sudo usbip attach -r [ip_address] -b [bus_id]```

列出已**连接**的设备

```usbip port```

与设备**断开**

```sudo usbip detach -p [port]```

**解绑**设备

```usbip unbind -b [bus_id]```

# SYNOPSIS

**usbip** _COMMAND_ [_OPTIONS_]

# COMMANDS

**list**
> 列出 USB 设备

**bind**
> 绑定设备以供远程共享

**unbind**
> 解绑设备，取消共享

**attach**
> 连接到远程 USB 设备

**detach**
> 从远程设备断开

**port**
> 显示已连接的远程设备

# PARAMETERS

**-l, --local**
> 列出本地设备

**-r, --remote** _IP_
> 远程服务器地址

**-b, --busid** _ID_
> 设备的总线 ID

**-p, --port** _PORT_
> 断开连接时使用的端口号

# DESCRIPTION

**usbip** 让 USB 设备能够通过 IP 网络共享。设备可以从服务器导出，然后在客户端上挂接，使用起来就像本地连接一样。

服务器端运行 usbipd 守护进程并绑定待共享的设备。客户端加载 vhci-hcd 内核模块，然后连接到远程设备。

# CAVEATS

服务器和客户端都需要相应的内核模块。网络延迟会影响设备性能。不适合高带宽设备。安全性取决于网络配置。

# INSTALL

```apt: sudo apt install usbip```

```dnf: sudo dnf install usbip```

```pacman: sudo pacman -S usbip```

```apk: sudo apk add linux-tools-usbip```

```zypper: sudo zypper install usbip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lsusb](/man/lsusb)(8), [modprobe](/man/modprobe)(8)
