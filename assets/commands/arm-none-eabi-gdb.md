# TAGLINE

以交互方式调试裸机 ARM 固件。

# TLDR

**开始调试一个 ARM 固件二进制文件**

```arm-none-eabi-gdb [firmware.elf]```

**连接到远程目标**（通过 OpenOCD）

```arm-none-eabi-gdb -ex "target remote localhost:3333" [firmware.elf]```

**使用命令脚本启动**

```arm-none-eabi-gdb -x [commands.gdb] [firmware.elf]```

**加载固件并在目标上运行**

```arm-none-eabi-gdb -ex "target remote :3333" -ex "load" -ex "continue" [firmware.elf]```

**以 TUI 模式启动**并显示源代码

```arm-none-eabi-gdb -tui [firmware.elf]```

# SYNOPSIS

**arm-none-eabi-gdb** [_options_] [_executable_]

# PARAMETERS

**-ex** _command_
> 在加载程序后执行一条 GDB 命令。

**-x** _file_
> 从脚本文件中执行命令。

**-tui**
> 以文本用户界面（TUI）模式启动并显示源代码窗口。

**-q**, **--quiet**
> 不显示简介和版权信息。

**-batch**
> 以批处理模式运行，用于非交互式场景。

**-cd** _directory_
> 运行前切换到指定目录。

**-s** _file_
> 从指定文件读取符号。

**--args**
> 将其余参数传递给程序。

# COMMON GDB COMMANDS

**target remote** _host:port_
> 连接到远程调试服务器（OpenOCD、J-Link 等）。

**load**
> 将程序下载到目标的闪存/RAM。

**monitor reset halt**
> 复位目标并在起始处暂停。

**break** _location_
> 在函数或地址处设置断点。

**continue** / **c**
> 继续执行。

**step** / **next**
> 单步进入 / 单步跳过源码行。

**stepi** / **nexti**
> 按单条指令单步执行。

**info registers**
> 显示 CPU 寄存器内容。

**x** _address_
> 检查指定地址处的内存。

# DESCRIPTION

**arm-none-eabi-gdb** 是为裸机 ARM 目标（无操作系统的 Cortex-M、Cortex-A）配置的 GNU 调试器。它通过 JTAG/SWD 调试探针对运行在微控制器和嵌入式系统上的固件进行源代码级调试。

该调试器通过 OpenOCD、J-Link GDB Server 或 ST-Link 工具等调试服务器连接到硬件目标。这些服务器在 GDB 的远程协议与微控制器上的物理调试接口之间提供桥梁。

配合包含调试符号的 ELF 文件，arm-none-eabi-gdb 提供完整的源代码级调试：设置断点、检查变量、逐行执行代码以及查看内存和寄存器。它还支持 ARM 特有的功能，例如查看特殊寄存器和外设内存区域。

# CONFIGURATION

**~/.gdbinit**
> GDB 启动时执行的初始化命令，例如目标连接设置和自定义宏。

# CAVEATS

需要连接到目标的调试探针（J-Link、ST-Link、CMSIS-DAP）和调试服务器（OpenOCD、pyOCD）。ELF 文件必须与目标上的固件完全一致，符号才能正确对应。大多数 Cortex-M 设备的硬件断点数量有限（通常为 4-6 个）。经过优化的代码由于重排和内联，调试行为可能令人困惑。

# HISTORY

GNU 调试器（GDB）起源于 **1986** 年，是 GNU 计划的一部分。自 **2000** 年代初以来，ARM 交叉编译工具链就包含了面向裸机 ARM 的 GDB 构建，以支持不断增长的嵌入式系统市场。**arm-none-eabi** 前缀表示使用嵌入式 ABI、不带操作系统（裸机）的 ARM 架构。

# INSTALL

```pacman: sudo pacman -S arm-none-eabi-gdb```

```brew: brew install arm-none-eabi-gdb```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[openocd](/man/openocd)(1), [gdb](/man/gdb)(1)
