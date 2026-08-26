# TAGLINE

LLVM C/C++/Objective-C 编译器

# TLDR

**编译** C 程序

```clang [program.c] -o [program]```

**开启优化编译**

```clang -O3 [program.c] -o [program]```

**带调试信息编译**

```clang -g [program.c] -o [program]```

**启用**所有警告

```clang -Wall -Wextra [program.c] -o [program]```

**编译** C++ 程序

```clang++ [program.cpp] -o [program]```

# SYNOPSIS

**clang** [_options_] _file_...

# DESCRIPTION

**clang** 是基于 LLVM 编译器基础设施的 C、C++ 和 Objective-C 编译器。它提供快速编译和清晰报错信息的出色诊断能力，并被设计为大多数平台上 GCC 的直接替代品。

Clang 以其富有表现力的错误信息著称，包括源码高亮、fix-it 提示以及优于 GCC 的模板回溯。其模块化的库架构使其可被 clang-format、clang-tidy 和 clangd 等工具复用。

该编译器支持现代语言标准（C17、C++20、C++23）、用于在运行时检测内存错误和未定义行为的 sanitizer，以及强大的静态分析功能。它是 macOS 和 FreeBSD 上的默认编译器，并在 Linux 上广泛使用。

# PARAMETERS

**-o** _file_
> 输出文件名

**-c**
> 只编译，不链接

**-g**
> 生成调试信息

**-O**[_level_]
> 优化等级（0、1、2、3、fast、s、z）

**-std=**_standard_
> 语言标准（c11、c17、c++17、c++20）

**-Wall**
> 启用常见警告

**-Wextra**
> 启用额外警告

**-Werror**
> 将警告视为错误

**-I** _dir_
> 添加头文件搜索目录

**-L** _dir_
> 添加库搜索目录

**-l** _lib_
> 链接指定库

**-fsanitize=**_type_
> 启用 sanitizer（address、thread、memory、undefined）

# OPTIMIZATION LEVELS

- **-O0** - 不优化（默认）
- **-O1** - 基本优化
- **-O2** - 中等优化（推荐）
- **-O3** - 激进优化
- **-Os** - 针对体积优化
- **-Ofast** - 最大速度（可能违反标准）

# WORKFLOW

```bash
# Simple compile
clang hello.c -o hello

# With warnings and optimization
clang -Wall -Wextra -O2 program.c -o program

# Debug build
clang -g -O0 program.c -o program

# C++ compilation
clang++ -std=c++20 program.cpp -o program

# With sanitizers
clang -fsanitize=address -g program.c -o program

# Multiple source files
clang main.c utils.c -o program

# Link with library
clang program.c -o program -lm -lpthread
```

# SANITIZERS

**Address Sanitizer:**
> 检测内存错误

**Thread Sanitizer:**
> 检测数据竞争

**Undefined Behavior Sanitizer:**
> 检测未定义行为

**Memory Sanitizer:**
> 检测未初始化内存读取

# CAVEATS

部分 GCC 特有特性不受支持。优化行为与 GCC 不同。sanitizer 会带来额外开销。错误信息比一些人偏好的更冗长。某些情况下编译速度可能慢于 GCC。

# HISTORY

**clang** 由 Apple 和 LLVM 社区自 **2007** 年开始创建，作为取代 GCC 的现代模块化编译器，于 **2009** 年首次发布。

# INSTALL

```apt: sudo apt install clang```

```dnf: sudo dnf install clang```

```pacman: sudo pacman -S clang```

```apk: sudo apk add clang22```

```zypper: sudo zypper install clang```

```nix: nix profile install nixpkgs#clang```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gcc](/man/gcc)(1), [clang++](/man/clang++)(1)
