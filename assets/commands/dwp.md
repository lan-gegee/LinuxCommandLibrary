# TAGLINE

打包 DWARF 调试信息

# TLDR

**将多个 .dwo 文件打包**为单个 .dwp

```dwp -o [out.dwp] [a.dwo] [b.dwo]```

**打包可执行文件引用的所有 .dwo 文件**

```dwp -e [program] -o [program.dwp]```

**从响应文件读取要打包的 .dwo 文件列表**

```dwp @[dwo_list.txt] -o [out.dwp]```

**显示帮助**并退出

```dwp -h```

# SYNOPSIS

**dwp** [**-e** _executable_] [**-o** _output.dwp_] [_dwo-file_...]

# PARAMETERS

**-e** _executable_, **--exec** _executable_
> 从给定的可执行文件或共享库内部的 **DW_AT_GNU_dwo_name** 属性读取 .dwo 文件列表。

**-o** _file_, **--output** _file_
> 将打包后的 DWARF 写入 _file_。省略时默认为 **a.dwp**。

**-v**, **--verbose**
> 在添加每个 .dwo 文件时打印其名称。

**@**_file_
> 从 _file_ 读取额外的命令行参数（通常是 .dwo 文件名），每行一个。

**-h**, **--help**
> 显示用法信息。

**-V**, **--version**
> 打印版本信息。

# DESCRIPTION

**dwp**（DWARF packaging utility）将来自多个 split-DWARF 目标文件（.dwo）的 DWARF 调试信息合并为单个包文件（.dwp）。这是由 **gcc -gsplit-dwarf** 或 **clang -gsplit-dwarf** 启用的 split-DWARF 工作流的一部分：编译器将大部分调试数据写入每个翻译单元各自的 .dwo 文件，而不是嵌入到链接后的二进制文件中。

用 **dwp** 打包 .dwo 文件后，调试信息可以作为单个文件分发，调试器也能通过可执行文件中存储的 **DW_AT_GNU_dwo_name** / **DW_AT_GNU_dwo_id** 引用来定位符号。

Split DWARF 能显著缩短链接时间并减小可执行文件体积，同时保留完整的源码级调试能力，这对大型 C++ 代码库尤其有价值。

# CAVEATS

需要 split-DWARF 编译（**-gsplit-dwarf**）。调试器必须支持 .dwp 格式（较新的 GDB 和 LLDB 均支持）。使用 **-e** 时，**dwp** 按编译器记录的磁盘路径查找 .dwo 文件；如果构建树被移动过，除非这些 .dwo 文件位于可执行文件旁边，否则可能找不到。

# HISTORY

**dwp** 是 GNU **binutils** 的一部分，与 LLVM 项目中的 **llvm-dwp** 对应。split-DWARF 格式及其打包工具的引入是为了解决大型 C++ 项目中的编译/链接时间和二进制体积问题。

# INSTALL

```apt: sudo apt install binutils-gold```

```dnf: sudo dnf install binutils-gold```

```pacman: sudo pacman -S binutils```

```apk: sudo apk add binutils```

```zypper: sudo zypper install binutils```

```brew: brew install binutils```

```nix: nix profile install nixpkgs#binutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gdb](/man/gdb)(1), [objcopy](/man/objcopy)(1), [readelf](/man/readelf)(1)
