# TAGLINE

控制 LXI 兼容的测试设备，例如示波器、频谱分析仪等

# TLDR

在可用网络上**发现** LXI 设备

```lxi discover```

捕获一张**屏幕截图**，自动检测插件

```lxi screenshot -a [ip_address]```

使用**指定插件**捕获屏幕截图

```lxi screenshot -a [ip_address] -p [rigol-1000z]```

向仪器发送一条 **SCPI 命令**

```lxi scpi -a [ip_address] "[*IDN?]"```

运行**基准测试**以测量请求与响应性能

```lxi benchmark -a [ip_address]```

# SYNOPSIS

**lxi** _command_ [_options_]

# PARAMETERS

**discover**
> 扫描网络以查找支持 LXI 的仪器

**screenshot**
> 从仪器显示屏捕获屏幕截图

**scpi**
> 发送 SCPI（Standard Commands for Programmable Instruments，可编程仪器标准命令）命令

**benchmark**
> 测试与仪器的通信性能

**-a, --address _ip_**
> 指定目标仪器的 IP 地址

**-p, --plugin _name_**
> 为该仪器型号使用特定的截图插件

# DESCRIPTION

**lxi** 通过以太网控制 LXI（LAN eXtensions for Instrumentation）兼容的测试设备，例如示波器、频谱分析仪、万用表以及其他测量仪器。

LXI 是一种仪器行业标准，它在 TCP/IP 网络上扩展了 GPIB/IEEE-488 接口。该工具使用 SCPI 命令与仪器通信，可实现远程控制、数据采集以及测量的自动化。

截图功能通过各种插件支持多种仪器品牌，并在可能的情况下自动检测合适的截图方式。

# CAVEATS

需要与 LXI 仪器的网络连通性。发现功能可能无法找到位于不同子网的仪器。截图插件必须与仪器型号匹配才能正确截取显示内容。SCPI 命令语法因制造商而异。

# HISTORY

lxi-tools 项目旨在为与 LXI 兼容测试设备的通信提供开源工具，支持基于网络的仪器标准 LXI 1.4+ 规范。

# INSTALL

```apt: sudo apt install lxi-tools```

```dnf: sudo dnf install lxi-tools```

```brew: brew install lxi-tools```

```nix: nix profile install nixpkgs#lxi-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO
