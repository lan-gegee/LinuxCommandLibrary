# TAGLINE

RISC-V 参考指令集模拟器

# TLDR

**运行模拟器**

```spike [program.elf]```

带 ISA 扩展规范

```spike --isa=rv64gc [program.elf]```

**交互式调试**

```spike -d [program.elf]```

以 4 核模拟

```spike -p4 [program.elf]```

带内存配置（base:size）

```spike -m0x80000000:0x10000000 [program.elf]```

**记录执行的指令**

```spike -l --isa=rv64gc [program.elf]```

# SYNOPSIS

**spike** [_--isa spec_] [_-d_] [_-p n_] [_options_] _program_

# PARAMETERS

**--isa** _SPEC_
> ISA 规范。

**-d**
> 调试模式。

**-p** _N_
> 处理器数量。

**-m** _RANGE_
> 内存配置。

**--pc** _ADDR_
> 起始地址。

**-l**
> 记录执行的指令

**-g**
> 统计 PC 的直方图

**-h**
> 打印帮助信息

**--ic=** _S:W:B_
> 实例化指令缓存（sets:ways:blocksize）

**--dc=** _S:W:B_
> 实例化数据缓存（sets:ways:blocksize）

**--l2=** _S:W:B_
> 实例化 L2 缓存（sets:ways:blocksize）

# DESCRIPTION

**spike** 是官方的 RISC-V ISA（指令集架构）参考模拟器。它提供 RISC-V 处理器的指令级精确仿真，支持 RV32 和 RV64 基础整数指令集，以及 M（乘除）、A（原子操作）、F/D（浮点）、C（压缩指令）等标准扩展。

模拟器包含交互式调试模式，可用于单步执行指令、设置断点以及检查寄存器和内存。它支持多核 SMP 模拟，处理器数量和内存布局均可配置，因此既适合测试裸机固件，也适合测试操作系统内核。

作为 RISC-V 项目维护的参考实现，spike 是验证硬件实现和编译器输出是否符合规范的黄金模型。

# CAVEATS

仅提供指令级模拟；不具备周期级精度。定位于开发和验证工具，不适用于性能估算。

# HISTORY

**spike** 是官方的 RISC-V ISA 模拟器，作为 RISC-V 架构的参考实现开发。

# INSTALL

```pacman: sudo pacman -S spike```

```nix: nix profile install nixpkgs#spike```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qemu](/man/qemu)(1), [riscv64-unknown-elf-gcc](/man/riscv64-unknown-elf-gcc)(1)
