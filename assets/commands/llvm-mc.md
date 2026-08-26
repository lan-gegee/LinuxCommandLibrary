# TAGLINE

LLVM 机器代码试验场

# TLDR

**汇编为目标文件**

```llvm-mc -filetype=obj [input.s] -o [output.o]```

对 x86_64 **反汇编十六进制字节**

```echo "0x90" | llvm-mc --disassemble -triple=x86_64```

**针对特定目标三元组进行汇编**

```llvm-mc -triple=x86_64-linux-gnu [input.s]```

在汇编输出旁**显示指令编码**

```llvm-mc -show-encoding [input.s]```

使用 Intel 语法而非 AT&T 进行**汇编**

```llvm-mc -x86-asm-syntax=intel [input.s]```

**针对 ARM 目标进行汇编**

```llvm-mc -triple=aarch64-linux-gnu -filetype=obj [input.s] -o [output.o]```

# SYNOPSIS

**llvm-mc** [_options_] [_file_]

# PARAMETERS

**-filetype**=_type_
> 输出文件类型：**asm**（汇编清单，默认）、**obj**（目标文件）或 **null**（无输出）。

**-triple**=_triple_
> 用于汇编/反汇编的目标三元组（如 x86_64-linux-gnu、aarch64-linux-gnu）。

**--disassemble**, **-disassemble**
> 将十六进制编码的输入字节反汇编为汇编代码。

**-show-encoding**
> 在汇编输出的旁边以注释形式打印指令编码。

**-show-inst**
> 在输出中显示 LLVM 内部的指令表示。

**-o** _file_
> 输出文件名（默认：stdout）。

**-x86-asm-syntax**=_syntax_
> x86 的汇编语法：**att**（默认）或 **intel**。

**-mcpu**=_cpu_
> 指定用于指令选择的目标 CPU。

**-mattr**=_attributes_
> 目标特有的属性（如 +sse4.2,+avx）。

**-output-asm-variant**=_N_
> 选择汇编输出变体（x86 上 0 = AT&T，1 = Intel）。

**-g**
> 在目标文件输出中生成 DWARF 调试信息。

# DESCRIPTION

**llvm-mc** 是 LLVM 的机器代码试验场。它可以将汇编源码汇编成机器代码，也可以将机器代码字节反汇编回各种目标架构的汇编代码。适用于测试汇编语法、检查指令编码、验证汇编器行为以及底层调试。

汇编模式的输入是汇编源文件。反汇编模式（**--disassemble**）的输入是十六进制编码的字节，可以从 stdin 管道传入。未给出输入文件时读取 stdin。

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

[llvm-as](/man/llvm-as)(1), [llvm-objdump](/man/llvm-objdump)(1), [as](/man/as)(1), [nasm](/man/nasm)(1), [objdump](/man/objdump)(1)
