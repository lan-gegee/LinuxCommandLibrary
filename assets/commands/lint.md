# TAGLINE

经典的 C 程序静态分析工具

# TLDR

**检查 C 程序**

```lint [program.c]```

**结合库进行检查**

```lint -l[library] [program.c]```

**抑制特定警告**

```lint -e[code] [program.c]```

**可移植模式**

```lint -p [program.c]```

# SYNOPSIS

**lint** [_options_] _files_...

# PARAMETERS

**-a**
> 报告条件表达式中的赋值。

**-b**
> 报告 break 语句相关的问题。

**-c**
> 生成 .ln 文件。

**-e** _code_
> 抑制指定错误代码。

**-l** _lib_
> 包含指定的 lint 库。

**-p**
> 可移植性 C 检查。

**-v**
> 详细输出。

# DESCRIPTION

**lint** 是一个经典的 C 程序静态分析工具。它检查源代码中的潜在缺陷、风格错误以及语法有效但很可能不正确的可疑结构。

lint 执行比编译器更深入的分析，能捕获类型不匹配、未使用的变量和有问题的代码模式。

# COMMON CHECKS

```
- Type consistency
- Unused variables
- Unreachable code
- Format string issues
- Missing return values
```

# CAVEATS

最初的 lint 已基本被编译器警告和 clang-tidy、cppcheck 等现代工具取代。传统 lint 可能并非在所有系统上都可用。

# HISTORY

lint 由 **Stephen C. Johnson** 于 **1978 年**在贝尔实验室编写。名字来源于它从程序中挑出的"绒毛"（lint）。它是静态分析工具的先驱。

# SEE ALSO

[cppcheck](/man/cppcheck)(1), [clang-tidy](/man/clang-tidy)(1), [gcc](/man/gcc)(1)
