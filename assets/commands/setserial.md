# TAGLINE

配置和查询串口设置

# TLDR

打印串口设备的**全部信息**

```setserial -a [/dev/ttyS0]```

打印适合启动脚本的**配置摘要**

```setserial -b [/dev/ttyS0]```

**设置**配置参数

```sudo setserial [/dev/ttyS0] [parameter] [value]```

打印**多个设备**的配置

```setserial -g [/dev/ttyS0] [/dev/ttyS1]```

**自动配置** UART 类型和 IRQ

```sudo setserial [/dev/ttyS0] autoconfig```

设置**自定义波特率**分频器

```sudo setserial [/dev/ttyS0] baud_base [115200] divisor [1]```

# SYNOPSIS

**setserial** [**-abqvVWz**] _device_ [_parameter_ [_arg_]]...

**setserial** **-g** [**-abGv**] _device_...

# PARAMETERS

**-a**
> 显示所有可用的配置信息

**-b**
> 打印适合启动脚本的配置摘要

**-g**
> 报告多个设备的特性

**-G**
> 以 setserial 命令行参数的形式打印配置

**-q**
> 安静模式；抑制状态输出

**-v**
> 详细模式；显示额外的状态信息

**-V**
> 打印版本并退出

**-z**
> 在设置新值前将标志清零

**port** _port_number_
> 设置 I/O 端口地址

**irq** _irq_number_
> 设置中断请求线

**uart** _uart_type_
> 设置 UART 类型（none、8250、16450、16550、16550A、16650、16650V2、16654、16750、16850、16950、16954）

**autoconfig**
> 自动检测 UART 类型和 IRQ

**baud_base** _baud_
> 设置基础波特率（时钟频率 / 16）

**divisor** _divisor_
> 为非标准波特率设置自定义时钟分频器

**spd_hi**
> 当应用程序请求 38400 波特时使用 57600 波特

**spd_vhi**
> 当应用程序请求 38400 波特时使用 115200 波特

**spd_cust**
> 当应用程序请求 38400 波特时使用自定义分频器（通过 divisor 参数设置）

**spd_normal**
> 使用标准 38400 波特率（重置 spd_hi、spd_vhi 等）

**close_delay** _delay_
> 端口关闭后 DTR 保持低电平的时间，以百分之一秒为单位

**closing_wait** _delay_
> 关闭时等待数据排空的时间，以百分之一秒为单位

**auto_irq**
> 在自动配置期间尝试确定 IRQ

**^auto_irq**
> 在自动配置期间禁用自动 IRQ 检测

**skip_test**
> 在自动配置期间跳过 UART 测试

**low_latency**
> 以额外的 CPU 开销为代价最小化接收延迟

**^low_latency**
> 禁用低延迟模式（默认）

# DESCRIPTION

**setserial** 配置和查询串口设置，包括 I/O 端口地址、IRQ 线、UART 类型和运行标志。它主要用于系统启动期间，以初始化标准 COM1-COM4 之外的串口或配置非标准硬件。

该命令可以自动检测 UART 类型并为专用硬件设置自定义波特率。配备 **udev** 的现代系统通常自动处理串口配置，但 setserial 对于老旧硬件和自定义配置仍然有用。

# CAVEATS

不正确的设置可能导致串口故障或与其他设备冲突。**-W** 通配中断初始化在 2.1 之后的内核上已过时。许多设置需要 root 权限。在使用 **systemd** 的系统上，串口配置可能通过 udev 规则以不同方式处理。

# HISTORY

**setserial** 由 **Theodore Ts'o** 编写，自 **20 世纪 90 年代初**起就是 Linux 的一部分，最初用于帮助配置那个年代五花八门的串口硬件。该工具曾是设置调制解调器、终端和串口鼠标的必备工具。虽然在现代硬件上自动检测已使它不再那么关键，但它仍保留在 **setserial** 软件包中以支持老旧设备。

# INSTALL

```apt: sudo apt install setserial```

```dnf: sudo dnf install setserial```

```apk: sudo apk add setserial```

```zypper: sudo zypper install setserial```

```nix: nix profile install nixpkgs#setserial```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[stty](/man/stty)(1), [getty](/man/getty)(8), [minicom](/man/minicom)(1), [cu](/man/cu)(1)
