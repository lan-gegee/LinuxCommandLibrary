# TAGLINE

GNU binutils 中的多线程 ELF 链接器

# TLDR

直接**链接目标文件**

```ld.gold -o [output] [file1.o] [file2.o]```

**链接系统库**

```ld.gold -o [output] [file.o] -l[library]```

通过 gcc **使用 gold**

```gcc -fuse-ld=gold -o [output] [file.c]```

**构建共享库**

```ld.gold -shared -o [lib.so] [file.o]```

**限制线程数**

```ld.gold --threads --thread-count=[4] -o [output] [*.o]```

**启用增量链接**

```ld.gold --incremental -o [output] [*.o]```

# SYNOPSIS

**ld.gold** [_options_] _files_...

# PARAMETERS

_FILES_
> 要链接的目标文件（.o）和归档文件（.a）。

**-o** _FILE_
> 将链接输出写入 _FILE_。

**-l** _NAME_
> 在链接路径中搜索 **libNAME.so** 或 **libNAME.a**。

**-L** _DIR_
> 将 _DIR_ 加入库搜索路径。

**-shared**
> 生成共享对象而非可执行文件。

**-static**
> 生成完全静态链接的可执行文件。

**--threads**, **--no-threads**
> 启用或禁用多线程链接阶段。

**--thread-count** _N_
> 当 **--threads** 开启时使用 _N_ 个工作线程。

**--incremental**
> 对未更改的输入复用上次链接的输出。

**--gc-sections**
> 从输出中丢弃未被引用的段。

**-r**, **--relocatable**
> 生成可重定位目标文件（部分链接）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ld.gold**（通常以 **gold** 调用）是为 **GNU binutils** 编写的高性能、仅支持 ELF 的链接器。与传统 **GNU ld** 相比，它在大型 C++ 代码库上明显更快，这得益于输入目标的并行处理、具备局部性感知的符号解析，以及针对现代多核 CPU 调优的内部设计。

大多数项目通过编译器驱动程序配合 **-fuse-ld=gold** 间接调用 gold。它接受 GNU ld 命令行的大多数常用选项，因此可以轻松地即插即用式替换。**--incremental** 增量链接、插件支持（LTO）和 DWARF 感知输出等专门功能则通过 gold 特有的选项提供。

# CAVEATS

仅支持 ELF：gold 无法生成 PE/COFF（Windows）或 Mach-O（macOS）输出。它只支持 GNU ld 链接器脚本的一个子集；非常复杂的脚本可能需要调整。现代项目往往改用 **LLVM lld**（更快且跨平台）；gold 的上游开发在 binutils 中已被降级。

# HISTORY

Gold 由 **Ian Lance Taylor** 在 **Google** 开发，旨在加速大型 C++ 链接，并于 **2008 年**贡献给 GNU binutils。整个 2010 年代它是许多发行版上的默认 ELF 链接器，直到 LLVM 的 **lld** 成熟。**2022 年**，binutils 维护者将 gold 置于维护模式，建议新工作采用 lld 或新的 ld 功能。

# INSTALL

```apt: sudo apt install binutils-gold```

```dnf: sudo dnf install binutils-gold```

```apk: sudo apk add binutils-gold```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ld](/man/ld)(1), [gcc](/man/gcc)(1)
