# TAGLINE

Tiny C Compiler（极小 C 编译器）

# TLDR

**编译并运行**

```tcc -run [program.c]```

**编译为可执行文件**

```tcc -o [program] [program.c]```

**编译为目标文件**

```tcc -c [program.c]```

**运行来自标准输入的 C 代码**

```echo 'int main(){return 0;}' | tcc -run -```

**链接库进行编译**

```tcc -o [program] [program.c] -l[m]```

**带参数运行**

```tcc -run [program.c] -- [arg1] [arg2]```

**编译为共享库**

```tcc -shared -o [lib.so] [lib.c]```

# SYNOPSIS

**tcc** [_-run_] [_-o output_] [_-c_] [_-l lib_] [_options_] _files_

# PARAMETERS

**-run**
> 编译并立即运行。

**-o** _FILE_
> 输出文件。

**-c**
> 仅编译为目标文件。

**-shared**
> 创建共享库。

**-l** _LIB_
> 链接库。

**-L** _DIR_
> 库搜索路径。

**-I** _DIR_
> 头文件搜索路径。

**-D** _NAME_
> 定义预处理器宏。

**-g**
> 生成调试信息。

**-b**
> 启用边界检查。

**-Wall**
> 启用警告。

**-v**
> 详细输出模式。

# DESCRIPTION

**tcc**（Tiny C Compiler）是一个速度极快的 C 编译器，还可以充当 C 脚本解释器。它的主要特点是编译速度——TCC 的编译速度比 GCC 快数倍，因此适合快速开发迭代，也适合把 C 当作脚本语言使用。

**-run** 标志将源代码直接编译进内存并立即执行，不生成中间目标文件或可执行文件。**--** 之后的参数会传给被编译的程序。这使得 C 文件可以像脚本一样使用，包括在 shebang 中使用。

TCC 支持大部分 C99 标准以及常见的 GCC 扩展以保持兼容。它能生成可执行文件、目标文件和共享库。内置的边界检查器（**-b**）可以在运行时捕获缓冲区溢出和越界访问，无需 Valgrind 之类的外部工具。尽管体积很小，TCC 已足够强大，甚至能编译它自己。

# CAVEATS

优化非常有限，生成的代码运行较慢。某些 C 特性的行为可能与 GCC 不同。不适合对性能有要求的生产构建。

# HISTORY

**TCC** 由 **Fabrice Bellard** 于 **2001 年**前后创建。Bellard 也是 QEMU、FFmpeg 等知名项目的作者。TCC 证明了完整的 C 编译器也可以做得非常小且快。

# INSTALL

```apt: sudo apt install tcc```

```pacman: sudo pacman -S tcc```

```apk: sudo apk add tcc```

```brew: brew install tcc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gcc](/man/gcc)(1), [clang](/man/clang)(1), [make](/man/make)(1)
