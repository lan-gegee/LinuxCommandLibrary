# TAGLINE

显示目标文件的信息

# TLDR

**反汇编可执行文件**

```objdump -d [binary]```

**显示所有头信息**

```objdump -x [binary]```

**显示区段内容**

```objdump -s [binary]```

**反汇编并显示源代码**

```objdump -S [binary]```

**显示符号表**

```objdump -t [binary]```

**显示动态符号**

```objdump -T [binary]```

**反汇编特定区段**

```objdump -d -j [.text] [binary]```

**使用 Intel 语法反汇编**（x86）

```objdump -d -M intel [binary]```

**反汇编并还原 C++ 符号名**

```objdump -d -C [binary]```

**显示文件头**信息

```objdump -f [binary]```

**显示重定位条目**

```objdump -r [binary]```

# SYNOPSIS

**objdump** [_options_] _files_...

# DESCRIPTION

**objdump** 显示目标文件的信息。它可以反汇编可执行文件，显示头信息、符号表和重定位。它是二进制分析、调试和逆向工程的必备工具。

该工具支持 ELF、PE/COFF、Mach-O 以及 BFD 库支持的其他目标文件格式。在 x86 上，反汇编默认采用 AT&T 语法；使用 **-M intel** 可切换为 Intel 语法。当存在调试信息时，**-S** 选项会将源代码与反汇编交错显示，对理解编译器输出很有价值。

# PARAMETERS

**-d**, **--disassemble**
> 反汇编代码区段。

**-D**
> 反汇编所有区段。

**-S**, **--source**
> 将源代码混入反汇编输出。

**-t**, **--syms**
> 符号表。

**-T**, **--dynamic-syms**
> 动态符号表。

**-x**, **--all-headers**
> 所有头信息。

**-h**, **--section-headers**
> 区段头。

**-r**, **--reloc**
> 重定位条目。

**-j** _section_
> 仅针对特定区段。

**-M** _options_
> 反汇编器选项。

**-C**, **--demangle**
> 还原 C++ 符号名。

**-s**, **--full-contents**
> 显示所有区段的完整内容。

**-f**, **--file-headers**
> 显示文件头信息。

**-l**, **--line-numbers**
> 在反汇编中包含源文件和行号（需要调试信息）。

**-w**, **--wide**
> 为超过 80 列的宽度格式化输出。

**--no-show-raw-insn**
> 不在反汇编旁显示原始指令字节。

**-D**, **--disassemble-all**
> 反汇编所有区段，而不仅是代码段。

**--disassembler-color** _mode_
> 启用彩色反汇编输出（off、terminal、on、extended）。

**--visualize-jumps**
> 在反汇编中绘制 ASCII 箭头以标示跳转目标。

**-e**, **--debugging-tags**
> 以兼容 ctags 的格式显示调试信息。

# CAVEATS

已剥离的二进制缺少调试信息。大型二进制会产生冗长的输出。反汇编可能遗漏代码区段中的数据。

# HISTORY

**objdump** 属于 **GNU Binutils**，始于 **1980 年代末期**。它提供了一个统一的工具，用于检查不同架构上的各种目标文件格式。

# INSTALL

```apt: sudo apt install binutils```

```dnf: sudo dnf install binutils```

```pacman: sudo pacman -S binutils```

```apk: sudo apk add binutils```

```zypper: sudo zypper install binutils```

```brew: brew install binutils```

```nix: nix profile install nixpkgs#binutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[readelf](/man/readelf)(1), [nm](/man/nm)(1), [gdb](/man/gdb)(1), [strings](/man/strings)(1)
