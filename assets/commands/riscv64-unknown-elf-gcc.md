# TAGLINE

为 RISC-V 目标交叉编译 C 代码

# TLDR

**为 RISC-V 编译**

```riscv64-unknown-elf-gcc -o [output] [source.c]```

**以指定架构编译**

```riscv64-unknown-elf-gcc -march=rv64imac -o [output] [source.c]```

**为裸机编译**

```riscv64-unknown-elf-gcc -nostdlib -o [output] [source.c]```

**生成汇编代码**

```riscv64-unknown-elf-gcc -S [source.c]```

# SYNOPSIS

**riscv64-unknown-elf-gcc** [_options_] _files_...

# PARAMETERS

**-march=**_arch_
> 目标架构（例如 rv64imac、rv64gc、rv32imac）。

**-mabi=**_abi_
> 整数和浮点调用约定（例如 lp64、lp64d、lp64f、ilp32）。

**-nostdlib**
> 不链接标准库和启动文件。

**-T** _script_
> 使用指定的链接脚本。

**-mcmodel=**_model_
> 代码模型：medlow（默认）或 medany。

**-msave-restore**
> 使用更小但更慢的序言/尾声例程来减小代码体积。

**-msmall-data-limit=**_n_
> 将小于 _n_ 字节的全局和静态数据放入特殊段。

**--specs=**_file_
> 使用指定的 specs 文件（例如 newlib-nano 的 nano.specs）。

**-O**_level_
> 优化级别（0、1、2、3、s、g）。

# DESCRIPTION

**riscv64-unknown-elf-gcc** 是面向 RISC-V 64 位裸机目标的 GCC 交叉编译器。它可以为没有操作系统的 RISC-V 处理器编译 C/C++ 代码。

# EXAMPLES

```bash
# Basic compilation
riscv64-unknown-elf-gcc -o hello hello.c

# With specific ISA extensions
riscv64-unknown-elf-gcc -march=rv64gc -mabi=lp64d -o prog prog.c

# Bare metal with linker script
riscv64-unknown-elf-gcc -nostdlib -T link.ld -o firmware firmware.c

# Generate object file
riscv64-unknown-elf-gcc -c -o main.o main.c

# With newlib
riscv64-unknown-elf-gcc --specs=nano.specs -o app app.c
```

# ARCHITECTURES

```
rv64imac   - Integer, Multiply, Atomic, Compressed
rv64gc     - General purpose (IMAFDC) - equivalent to rv64imafdC
rv64imafdc - Same as rv64gc (explicit form)
rv32imac   - 32-bit: Integer, Multiply, Atomic, Compressed
rv32gc     - 32-bit general purpose
```

# CAVEATS

这是面向嵌入式领域的交叉编译器。需要安装 RISC-V 工具链。与 riscv64-linux-gnu-gcc 不同。

# HISTORY

RISC-V GCC 工具链作为 UC Berkeley 发起的 **RISC-V** 开放 ISA 项目的一部分而开发。

# INSTALL

```apt: sudo apt install gcc-riscv64-unknown-elf```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gcc](/man/gcc)(1), [objdump](/man/objdump)(1), [qemu-system-riscv64](/man/qemu-system-riscv64)(1)
