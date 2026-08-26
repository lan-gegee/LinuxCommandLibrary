# TAGLINE

LLVM 编译器基础设施的 g++ 前端

# TLDR

**编译 C++ 程序**

```llvm-g++ -o [program] [source.cpp]```

**带优化编译**

```llvm-g++ -O2 -o [program] [source.cpp]```

**生成 LLVM 位码**

```llvm-g++ -emit-llvm -c [source.cpp]```

# SYNOPSIS

**llvm-g++** [_options_] _source_files_...

# PARAMETERS

**-o** _file_
> 输出文件名。

**-O** _level_
> 优化级别（0-3）。

**-emit-llvm**
> 生成 LLVM 位码。

**-c**
> 仅编译，不链接。

**-std=** _standard_
> C++ 标准版本。

**-g**
> 包含调试信息。

# DESCRIPTION

**llvm-g++** 是 LLVM 编译器基础设施的 G++ 前端，提供与 GCC 兼容的 C++ 接口并生成 LLVM 中间表示。现已被弃用，由 clang++ 取代。

# CAVEATS

该工具已被弃用。基于 LLVM 的 C++ 编译请改用 **clang++**。

# SEE ALSO

[clang++](/man/clang++)(1), [g++](/man/g++)(1), [llvm-gcc](/man/llvm-gcc)(1)
