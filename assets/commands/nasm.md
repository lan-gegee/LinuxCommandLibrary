# TAGLINE

采用 Intel 语法的可移植 x86 与 x86-64 汇编器

# TLDR

**汇编为目标文件**

```nasm -f [elf64] [source.asm] -o [output.o]```

**面向 Linux 32 位汇编**

```nasm -f elf32 [source.asm]```

**面向 Windows 64 位汇编**

```nasm -f win64 [source.asm]```

**生成列表文件**

```nasm -f [elf64] -l [listing.lst] [source.asm]```

**定义预处理宏**

```nasm -D [MACRO_NAME]=[value] [source.asm]```

**包含搜索路径**

```nasm -I [/path/to/includes/] [source.asm]```

**仅预处理**（输出到标准输出）

```nasm -E [source.asm]```

**显示可用的输出格式**

```nasm -hf```

# SYNOPSIS

**nasm** [_-f format_] [_-o outfile_] [_-l listfile_] [_-D name=value_] [_options_] _source.asm_

# PARAMETERS

**-f** _format_
> 输出格式（elf64、elf32、win64、win32、macho64、bin 等）。

**-o** _file_
> 输出文件名。

**-l** _file_
> 生成列表文件。

**-M**
> 生成 Makefile 依赖。

**-E**
> 仅预处理，输出到标准输出。

**-a**
> 仅预处理，不输出。

**-D** _macro_[=_value_]
> 定义预处理宏。

**-U** _macro_
> 取消定义预处理宏。

**-I** _path_
> 添加包含文件的搜索目录。

**-P** _file_
> 在源码之前预先包含文件。

**-w**[+|-]_warning_
> 启用/禁用某类警告。

**-g**
> 生成调试信息。

**-F** _format_
> 调试信息格式。

**-O** _level_
> 优化级别（0、1、多遍优化用 x）。

**-@** _file_
> 从文件读取额外的命令行选项。

**-Z** _file_
> 将错误信息重定向到文件。

**-s**
> 将错误输出到标准输出。

**-v**
> 显示版本。

**-y**
> 列出给定输出格式可用的调试信息格式。

**-h**
> 显示帮助。

**-hf**
> 列出可用的输出格式。

# DESCRIPTION

**NASM**（Netwide Assembler）是采用 Intel 语法的可移植 x86 和 x86-64 汇编器。它能生成面向多种操作系统和格式的目标文件，适合跨平台汇编开发。

NASM 使用的 Intel 语法通常被认为比 AT&T 语法更易读：目标操作数在前（mov eax, 1），内存引用使用方括号（[var]），大小说明符明确（dword、qword）。

输出格式覆盖主流平台：Linux/Unix 的 ELF、Windows 的 PE/COFF、macOS 的 Mach-O，以及用于引导加载程序和嵌入式系统的扁平二进制格式。-f 选项选择目标格式。

NASM 内置功能强大的宏预处理器，支持多行宏、条件汇编、字符串处理和文件包含。上下文局部标签支持可复用的代码结构。

在调试方面，NASM 以 DWARF 和 CodeView 等格式生成调试信息，与 GDB、LLDB 和 Visual Studio 调试器兼容。

# CAVEATS

Intel 语法与 GNU as（AT&T 语法）不同。目标文件必须经过链接（ld、gcc、link.exe）才能成为可执行文件。函数调用需要注意平台相关的调用约定。二进制输出需要手动规划内存布局。16 位和 32 位模式需要留意处理器模式。

# HISTORY

**NASM** 由 **Simon Tatham** 和 **Julian Hall** 于 **1996 年**开始编写，目标是创建一个语法简洁的 Intel 风格自由可移植汇编器。它成为许多需要底层代码的开源项目的首选汇编器。该项目得到了众多开发者的贡献，至今仍在积极维护，已支持包括 AVX-512 在内的现代处理器扩展。

# INSTALL

```apt: sudo apt install nasm```

```dnf: sudo dnf install nasm```

```pacman: sudo pacman -S nasm```

```apk: sudo apk add nasm```

```zypper: sudo zypper install nasm```

```brew: brew install nasm```

```nix: nix profile install nixpkgs#nasm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[as](/man/as)(1), [yasm](/man/yasm)(1), [ld](/man/ld)(1), [objdump](/man/objdump)(1), [gdb](/man/gdb)(1)
