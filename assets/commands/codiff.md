# TAGLINE

比较两个目标文件之间的 DWARF 调试信息差异

# TLDR

**比较两个目标文件**（默认显示结构体和函数的变化）

```codiff [old.o] [new.o]```

**只显示结构体的变化**

```codiff -s [old.o] [new.o]```

**只显示函数的变化**

```codiff -f [old.o] [new.o]```

**输出简洁的类型变化**

```codiff -t [old.o] [new.o]```

**详细输出**每个符号的完整细节

```codiff -V [old.o] [new.o]```

**安静模式**（只有退出状态，无任何输出）

```codiff -q [old.o] [new.o]```

# SYNOPSIS

**codiff** [_options_] _OLD_FILE_ _NEW_FILE_

# PARAMETERS

**-s**, **--structs**
> 显示结构体/联合体/类定义的差异：成员的新增、删除、大小变化或位置调整。

**-f**, **--functions**
> 显示函数签名和原型的差异：参数或返回类型的变化、新增与删除。

**-t**, **--terse_type_changes**
> 为每个发生变化的类型输出一行紧凑摘要，而非完整明细。

**-V**, **--verbose**
> 详细输出：显示每个受影响类型的偏移量、大小、对齐方式以及逐成员的变化。

**-q**, **--quiet**
> 仅设置退出状态，抑制所有输出。适合脚本使用。

**-F** _list_, **--format_path** _list_
> 按顺序尝试的调试格式列表，以逗号分隔（如 **dwarf**、**ctf**、**btf**）。

**--help**
> 打印帮助文本并退出。

# DESCRIPTION

**codiff** 比较两个 ELF 目标文件中内嵌的 **DWARF**（或 **CTF/BTF**）调试信息，并报告 C 层面类型、结构和函数原型的差异。它是 **dwarves** 工具集的一员，与 **pahole**、**pfunct**、**pglobal** 和 **pdwtags** 并列。

典型用法是验证某个补丁对内核模块、库或大型二进制文件的影响：开发者分别在修改前后编译同一个翻译单元，然后运行 **codiff** 查看哪些结构体变大了、哪些字段移动了、哪些导出函数的签名发生了改变。由于比较是基于结构而非文本进行的，无关符号的重命名和无关声明的重新排序会被自动过滤掉。

不指定 **-s** 或 **-f** 时，会同时生成结构体和函数两方面的差异。输入文件必须带调试信息编译（GCC/Clang 使用 **-g**）。

# CAVEATS

输入文件必须包含兼容的调试信息；已剥离的二进制文件不会产生任何输出。跨不同工具链或 DWARF 版本进行比较可能产生噪音。**codiff** 主要用于目标文件（.o）和小型库——对完整的 vmlinux 进行比较可能耗费大量时间和内存。

# HISTORY

**codiff** 由 **Arnaldo Carvalho de Melo** 编写，属于 **dwarves** 项目，最初于 **2007 年**发布，旨在帮助内核开发者分析结构体布局变化的二进制影响。该工具集与 **pahole** 一同演进，如今广泛应用于 **Linux 内核**开发流程，包括为 **eBPF** 生成 **BTF**。

# INSTALL

```apt: sudo apt install pahole```

```pacman: sudo pacman -S pahole```

```apk: sudo apk add pahole```

```nix: nix profile install nixpkgs#pahole```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[readelf](/man/readelf)(1), [objdump](/man/objdump)(1)
