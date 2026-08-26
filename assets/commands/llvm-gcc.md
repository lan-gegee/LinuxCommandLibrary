# TAGLINE

LLVM 编译器基础设施的 GCC 前端

# TLDR

**编译 C 程序**

```llvm-gcc -o [program] [source.c]```

**带优化编译**

```llvm-gcc -O2 -o [program] [source.c]```

**生成 LLVM 位码**

```llvm-gcc -emit-llvm -c [source.c]```

# SYNOPSIS

**llvm-gcc** [_options_] _source_files_...

# PARAMETERS

**-o** _file_
> 输出文件名。

**-O** _level_
> 优化级别（0-3）。

**-emit-llvm**
> 生成 LLVM 位码。

**-c**
> 仅编译，不链接。

**-S**
> 生成汇编输出。

**-g**
> 包含调试信息。

# DESCRIPTION

**llvm-gcc** 是 LLVM 编译器基础设施的 GCC 前端，提供与 GCC 兼容的接口并生成 LLVM 中间表示。现已被弃用，由 clang 取代。

# CAVEATS

该工具已被弃用。基于 LLVM 的编译请改用 **clang**。

# SEE ALSO

[clang](/man/clang)(1), [gcc](/man/gcc)(1), [llvm-g++](/man/llvm-g++)(1)
