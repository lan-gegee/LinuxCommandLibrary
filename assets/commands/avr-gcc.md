# TAGLINE

面向 AVR 微控制器的 GNU C 编译器

# TLDR

为 AVR 微控制器**编译 C 代码**

```avr-gcc -mmcu=[atmega328p] -o [output.elf] [source.c]```

以优化体积的方式**编译**

```avr-gcc -mmcu=[atmega328p] -Os -o [output.elf] [source.c]```

带调试符号**编译**

```avr-gcc -mmcu=[atmega328p] -g -O0 -o [output.elf] [source.c]```

**生成用于烧录的 hex 文件**

```avr-gcc -mmcu=[atmega328p] -Os -o [output.elf] [source.c] && avr-objcopy -O ihex [output.elf] [output.hex]```

带警告和链接器松弛**编译**

```avr-gcc -mmcu=[atmega328p] -Wall -Os -Wl,--relax -o [output.elf] [source.c]```

针对自由独立（freestanding）环境**编译**（不依赖宿主库）

```avr-gcc -mmcu=[atmega328p] -ffreestanding -Os -o [output.elf] [source.c]```

# SYNOPSIS

**avr-gcc** [_options_] _file_...

# PARAMETERS

**-mmcu=**_mcu_
> 目标 MCU（atmega328p、attiny85、atmega2560 等）；生成正确代码所必需

**-Os**
> 优化代码体积（嵌入式开发推荐）

**-O0**, **-O1**, **-O2**, **-O3**
> 优化级别（0=无，3=最高）

**-g**
> 包含调试信息

**-Wall**
> 启用所有常见警告

**-ffreestanding**
> 假定为自由独立环境（不对标准库做任何假设）

**-fno-jump-tables**
> 禁用跳转表（在大于 64KB 的设备上编写 bootloader 时必需）

**-mrelax**
> 启用链接器松弛，尽可能使用更短的指令

**-Wl,--relax**
> 将松弛选项传递给链接器

**-Wl,-gc-sections**
> 移除未使用的代码段以减小二进制体积

**-mcall-prologues**
> 用子程序实现函数的序言/尾声（节省空间）

**-DF_CPU=**_freq_
> 以赫兹定义 CPU 频率（如 -DF_CPU=16000000）

**-I**_path_
> 添加头文件搜索目录

**-L**_path_
> 添加库文件搜索目录

**-l**_library_
> 链接指定的库

# DESCRIPTION

**avr-gcc** 是面向 AVR 8 位微控制器配置的 GNU 编译器套件。它将 C 和 C++ 代码编译成 Atmel/Microchip AVR 芯片的机器码，这类芯片广泛用于 Arduino 和嵌入式系统。

**-mmcu** 选项至关重要，它为目标 MCU 配置代码生成、内存布局和可用指令。常见目标包括 atmega328p（Arduino Uno）、atmega2560（Arduino Mega）和 attiny85。

输出通常是 ELF 文件，需用 **avr-objcopy** 转换为 Intel HEX 格式，再通过 **avrdude** 等工具烧录到硬件。

嵌入式开发首选 **-Os** 优化，因为它在保持合理性能的同时最小化代码体积。由于 AVR 程序在没有操作系统的情况下运行，使用 **-ffreestanding** 标志是合适的做法。

AVR-GCC 通常作为 **avr-libc** 工具链的一部分安装，该工具链包含 C 库、头文件和其他工具。

# CAVEATS

**-mmcu** 选项必须与目标硬件完全匹配。优化级别 **-O3** 在 AVR 上常常会显著增大代码体积。由于 RAM 有限，程序应避免大量使用栈。整数运算默认是 16 位的；更大的数值请显式指定类型。

# HISTORY

**AVR-GCC** 源自 GCC 项目对 AVR 架构的支持，最初由 **Denis Chertykov** 在 **20 世纪 90 年代**末开发。与 **AVR-LibC** 结合后，它成为 AVR 开发的标准开源工具链。自 **2005** 年起，该工具链借助 Arduino 项目得到广泛应用，让爱好者和教育工作者也能轻松进行 AVR 编程。

# INSTALL

```apt: sudo apt install gcc-avr```

```dnf: sudo dnf install avr-gcc```

```pacman: sudo pacman -S avr-gcc```

```apk: sudo apk add gcc-avr```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[gcc](/man/gcc)(1), [avrdude](/man/avrdude)(1), [arduino-cli](/man/arduino-cli)(1)
