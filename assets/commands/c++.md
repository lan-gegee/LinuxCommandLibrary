# TAGLINE

将 C++ 源代码编译为可执行文件

# TLDR

**编译** C++ 程序

```c++ [program.cpp] -o [program]```

**开启优化**编译

```c++ -O2 [program.cpp] -o [program]```

**附带调试信息**编译

```c++ -g [program.cpp] -o [program]```

**指定** C++ 标准

```c++ -std=c++17 [program.cpp] -o [program]```

**链接**库

```c++ [program.cpp] -o [program] -l[library]```

# SYNOPSIS

**c++** [_options_] _file_...

# DESCRIPTION

**c++** 通常是系统 C++ 编译器（g++ 或 clang++）的符号链接。它将 C++ 源代码编译为可执行程序或目标文件，处理预处理、编译和链接。

该命令以标准命名约定提供对 C++ 编译器的访问。

# PARAMETERS

**-o** _file_
> 输出文件名

**-c**
> 只编译不链接

**-g**
> 包含调试信息

**-O**[_level_]
> 优化级别（0、1、2、3、s）

**-std=**_standard_
> C++ 标准（c++11、c++14、c++17、c++20、c++23）

**-Wall**
> 启用所有警告

**-Werror**
> 将警告视为错误

**-I** _dir_
> 添加头文件目录

**-L** _dir_
> 添加库目录

**-l** _lib_
> 链接库

# C++ STANDARDS

- **c++98** / **c++03** - 经典 C++
- **c++11** - 现代 C++（auto、lambda 等）
- **c++14** - 小幅改进
- **c++17** - 重大更新（filesystem 等）
- **c++20** - Concepts、ranges、模块
- **c++23** - 最新标准

# WORKFLOW

```bash
# Simple compile
c++ hello.cpp -o hello

# Modern C++ with warnings
c++ -std=c++20 -Wall -Wextra program.cpp -o program

# Optimized release build
c++ -std=c++17 -O3 -DNDEBUG program.cpp -o program

# Debug build
c++ -std=c++17 -g -O0 program.cpp -o program

# Link with libraries
c++ program.cpp -o program -lpthread -lm

# Multiple source files
c++ main.cpp utils.cpp -o program
```

# CAVEATS

实际使用的编译器取决于系统（g++、clang++ 等）。不同编译器之间的行为可能有差异。C++ 编译比 C 慢。模板错误可能难以理解。需注意编译器版本间的 ABI 兼容性。

# HISTORY

自 **1980 年代** C++ 编译器普及以来，**c++** 命令名一直是标准惯例，通常是指向系统 C++ 编译器的符号链接。

# INSTALL

```apk: sudo apk add g++```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[g++](/man/g++)(1), [clang++](/man/clang++)(1), [gcc](/man/gcc)(1)

# RESOURCES

```[Homepage](https://gcc.gnu.org/)```

<!-- verified: 2026-06-22 -->
