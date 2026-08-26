# TAGLINE

将 LLVM 中间表示编译为机器代码

# TLDR

**将 LLVM IR 编译为汇编代码**

```llc [input.ll]```

**输出到文件**

```llc -o [output.s] [input.ll]```

**编译为目标文件**

```llc -filetype=obj [input.ll]```

**指定目标架构**

```llc -march=[x86-64] [input.ll]```

**优化级别**

```llc -O[2] [input.ll]```

**列出支持的目标**

```llc --version```

# SYNOPSIS

**llc** [_options_] _file_

# PARAMETERS

_FILE_
> LLVM 位码或 IR 文件。

**-o** _FILE_
> 输出文件名。

**-filetype** _TYPE_
> 输出类型（asm、obj、null）。

**-march** _ARCH_
> 目标架构。

**-O** _LEVEL_
> 优化级别（0-3）。

**-mtriple** _TRIPLE_
> 目标三元组。

**--help**
> 显示帮助信息。

# DESCRIPTION

**llc** 是 LLVM 静态编译器，将 LLVM 中间表示（IR）转换为本机机器代码。它接受 LLVM 位码（.bc）或人类可读的 LLVM 汇编（.ll）格式的输入，并生成面向特定目标的汇编语言或目标文件。作为 LLVM 编译流水线的后端阶段，llc 执行指令选择、寄存器分配以及特定于机器的优化，为目标架构生成高效的代码。

该工具支持广泛的目标架构，包括 x86、ARM、AArch64、MIPS、RISC-V 等，可通过 `-march` 和 `-mtriple` 标志选择。从 `-O0`（无优化）到 `-O3`（激进优化）的优化级别控制 llc 在编译期间投入多少精力改进代码。输出可以是文本汇编（默认），也可以在使用 `-filetype=obj` 时生成可重定位目标文件，使 llc 既可用于检查生成的代码，也可用于直接生成可链接的产物。

# CAVEATS

需要 LLVM IR 输入。目标架构支持情况各异。属于 LLVM 工具链的一部分。

# HISTORY

llc 是 **LLVM** 编译器基础设施项目的组成部分，负责后端编译步骤。

# INSTALL

```apt: sudo apt install llvm```

```dnf: sudo dnf install llvm```

```pacman: sudo pacman -S llvm```

```apk: sudo apk add llvm```

```zypper: sudo zypper install llvm```

```brew: brew install llvm```

```nix: nix profile install nixpkgs#llvm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[clang](/man/clang)(1), [opt](/man/opt)(1), [lli](/man/lli)(1), [llvm-as](/man/llvm-as)(1)
