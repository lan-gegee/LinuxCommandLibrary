# TAGLINE

模块化的 x86 与 AMD64 汇编器

# TLDR

**汇编为 ELF64 目标文件**

```yasm -f elf64 -o [output.o] [input.asm]```

**面向 Windows 64 位汇编**

```yasm -f win64 -o [output.obj] [input.asm]```

**汇编 32 位 ELF**

```yasm -f elf32 -o [output.o] [input.asm]```

**使用 GAS 语法**

```yasm -p gas -f elf64 -o [output.o] [input.s]```

生成 DWARF 格式的**调试信息**

```yasm -g dwarf2 -f elf64 -o [output.o] [input.asm]```

仅进行**预处理**

```yasm -e [input.asm]```

**定义宏**

```yasm -D [DEBUG=1] -f elf64 -o [output.o] [input.asm]```

# SYNOPSIS

**yasm** [_options_] _infile_

# PARAMETERS

**-f** _format_, **--oformat=**_format_
> 输出格式（默认：bin）：bin、elf32、elf64、win32、win64、macho32、macho64、coff。

**-o** _outfile_, **--objfile=**_outfile_
> 输出文件名。

**-a** _arch_, **--arch=**_arch_
> 目标架构（默认：x86）。

**-m** _machine_, **--machine=**_machine_
> 机器子类型：x86、amd64。

**-p** _parser_, **--parser=**_parser_
> 语法解析器：nasm（默认）、gas。

**-r** _preproc_, **--preproc=**_preproc_
> 预处理器：nasm（默认）、raw、cpp、gas。

**-g** _debug_, **--dformat=**_debug_
> 调试格式：dwarf2、stabs、cv8、null。

**-L** _list_, **--lformat=**_list_
> 列表文件格式（默认：nasm）。

**-l** _file_, **--list=**_file_
> 输出列表文件名。

**-D** _macro[=value]_
> 定义预处理宏。

**-U** _macro_
> 取消定义宏。

**-I** _path_
> 添加 include 搜索目录。

**-P** _file_
> 在输入之前预先包含文件。

**-e**, **--preproc-only**
> 仅预处理（不汇编），输出到标准输出。

**-w**
> 抑制所有警告消息。

**-Werror**
> 将警告视为错误。

**-Worphan-labels**
> 对缺少尾随冒号的标签发出警告（NASM 模式）。

**-X** _style_
> 错误/警告报告风格：gnu 或 vc。

**--force-strict**
> 将所有带尺寸的操作数视为严格模式。

**--version**
> 显示版本。

**-h**, **--help**
> 显示帮助。

# DESCRIPTION

**yasm** 是一款支持 x86 与 AMD64 指令集的模块化汇编器。它是在 BSD 许可证下对 NASM 的完全重写，支持多种输入语法和输出格式。

支持的语法包括 NASM（默认）和 GAS（GNU Assembler）。输出格式涵盖 ELF、Win32/Win64 PE、Mach-O、COFF 以及原始二进制（bin，即默认值）。调试信息可生成为 DWARF 2、STABS 或 CodeView 8 格式。使用 `yasm -f help` 可列出所有可用的目标格式。

该汇编器用于底层系统编程、操作系统开发以及对性能要求苛刻的代码。它可以通过标准目标文件格式与 C/C++ 工具链集成。

# CAVEATS

某些 NASM 语法扩展可能不完全兼容。GAS 语法的支持尚不完整。AMD64 模式需要通过 -m amd64 或 64 位目标格式显式选择。

# HISTORY

**yasm** 由 Peter Johnson 和 Michael Urman 创建，是以模块化架构对 NASM 的重写。它旨在支持多种架构和语法的同时保持与 NASM 兼容。项目始于 2001 年，至今仍在各种构建系统中被积极使用。

# INSTALL

```apt: sudo apt install yasm```

```dnf: sudo dnf install yasm```

```pacman: sudo pacman -S yasm```

```apk: sudo apk add yasm```

```zypper: sudo zypper install yasm```

```brew: brew install yasm```

```nix: nix profile install nixpkgs#yasm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nasm](/man/nasm)(1), [as](/man/as)(1), [ld](/man/ld)(1), [objdump](/man/objdump)(1)
