# TAGLINE

GNU C/C++ 编译器套件

# TLDR

将**源代码编译**为可执行文件

```gcc [source.c] -o [output]```

**启用警告编译**

```gcc -Wall -Wextra [source.c] -o [output]```

**带调试符号编译**

```gcc -g [source.c] -o [output]```

**带优化编译**

```gcc -O2 [source.c] -o [output]```

**编译多个文件**

```gcc [file1.c] [file2.c] -o [output]```

**链接库**

```gcc [source.c] -l[pthread] -o [output]```

仅**编译为目标文件**

```gcc -c [source.c]```

**指定 C 标准**

```gcc -std=c11 [source.c] -o [output]```

**添加头文件目录**

```gcc -I[/path/to/headers] [source.c] -o [output]```

# SYNOPSIS

**gcc** [_options_] _file_...

# DESCRIPTION

**GCC**（GNU Compiler Collection）是支持 C、C++、Objective-C、Fortran、Ada、Go 及其他语言的编译器系统。对 C 代码来说，gcc 是调用预处理器、编译器、汇编器和链接器的主前端。

编译过程依次经过预处理（宏展开、头文件包含）、编译（生成汇编）、汇编（生成目标代码）和链接（把目标文件与库组合成可执行文件）。

GCC 是大多数类 Unix 系统上的标准编译器，支持丰富的优化级别、调试功能和面向各种架构的代码生成选项。

# PARAMETERS

**-c**
> 编译为目标文件，不链接。

**-o** _file_
> 输出文件名。

**-g**
> 包含调试信息。

**-Wall**
> 启用常见警告。

**-Wextra**
> 启用额外警告。

**-Werror**
> 将警告视为错误。

**-O** _level_
> 优化级别（0、1、2、3、s、fast）。

**-I** _dir_
> 添加头文件搜索目录。

**-L** _dir_
> 添加库搜索目录。

**-l** _lib_
> 链接指定的库。

**-D** _name_[=_value_]
> 定义预处理器宏。

**-std=** _standard_
> C 语言标准（c89、c99、c11、c17、c23）。

**-E**
> 仅预处理，不编译。

**-S**
> 编译为汇编代码，不汇编。

**-v**
> 详细输出。

**-static**
> 阻止链接共享库。

# CAVEATS

默认行为因系统和 gcc 版本而异。链接时库的顺序很重要。-Wall 并未启用所有警告。调试与优化可能互相冲突。不同语言标准可能改变行为。

# HISTORY

**GCC** 由 **Richard Stallman** 于 **1987 年**作为 GNU 计划的一部分启动。最初名为 GNU C Compiler，随着其他语言支持的加入更名为 GNU Compiler Collection。GCC 已成为开源软件中使用最广泛的编译器套件，是多数 Linux 发行版和 BSD 系统的默认编译器。

# INSTALL

```apt: sudo apt install gcc```

```dnf: sudo dnf install gcc```

```pacman: sudo pacman -S gcc```

```apk: sudo apk add gcc```

```zypper: sudo zypper install gcc```

```brew: brew install gcc```

```nix: nix profile install nixpkgs#gcc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[g++](/man/g++)(1), [clang](/man/clang)(1), [make](/man/make)(1), [gdb](/man/gdb)(1)

# RESOURCES

```[Homepage](https://gcc.gnu.org/)```

```[Documentation](https://gcc.gnu.org/onlinedocs/)```

<!-- verified: 2026-07-15 -->
