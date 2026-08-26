# TAGLINE

GNU C++ 编译器

# TLDR

**编译 C++ 文件**

```g++ [source.cpp] -o [output]```

**带警告编译**

```g++ -Wall -Wextra [source.cpp] -o [output]```

**带优化编译**

```g++ -O2 [source.cpp] -o [output]```

**调试构建**

```g++ -g [source.cpp] -o [output]```

**按指定 C++ 标准编译**

```g++ -std=c++17 [source.cpp] -o [output]```

# SYNOPSIS

**g++** [_options_] _files_...

# PARAMETERS

_FILES_
> 要编译的源文件。

**-o** _FILE_
> 输出文件名。

**-c**
> 仅编译，不链接。

**-Wall**
> 启用常见警告。

**-Wextra**
> 在 -Wall 之外启用更多警告。

**-g**
> 生成调试信息。

**-O** _LEVEL_
> 优化级别（0-3、s、fast）。

**-std=**_STANDARD_
> C++ 标准（c++11、c++14、c++17、c++20、c++23）。

**-I** _PATH_
> 头文件搜索路径。

**-L** _PATH_
> 库搜索路径。

**-l** _LIBRARY_
> 链接库。

**--help**
> 显示帮助信息。

# DESCRIPTION

**g++** 是 GNU C++ 编译器，属于 GNU 编译器套件（GCC）。它将 C++ 源代码编译为可执行文件或目标文件，支持现代 C++ 标准。

编译器负责预处理、编译、汇编和链接全过程。它提供丰富的优化选项和警告控制，帮助产出高质量代码。

g++ 是 Linux 系统上的标准 C++ 编译器，支持完整的 C++ 语言特性。

# CAVEATS

大型代码库编译较慢。模板错误信息可能难以理解。不同标准的特性集各不相同。

# HISTORY

g++ 属于 **GCC**（GNU Compiler Collection），最初由 Richard Stallman 编写。它从最初的 GNU C 编译器演进而来，逐步支持包括 C++ 在内的多种语言。

# INSTALL

```apt: sudo apt install g++```

```apk: sudo apk add g++```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gcc](/man/gcc)(1), [clang++](/man/clang++)(1), [ld](/man/ld)(1), [make](/man/make)(1), [gdb](/man/gdb)(1)
