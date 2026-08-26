# TAGLINE

C++ 未使用代码与头文件查找器

# TLDR

在目录中**查找问题**

```cppclean [path/to/source]```

**检查特定文件**

```cppclean [file1.cpp] [file2.cpp]```

**添加额外的头文件搜索路径**

```cppclean --include-path [/path/to/includes] [source/]```

**以详细输出运行**

```cppclean --verbose [path/to/source]```

**抑制输出消息**

```cppclean --quiet [path/to/source]```

# SYNOPSIS

**cppclean** [_options_] _paths..._

# DESCRIPTION

**cppclean** 用于查找拖慢大型 C++ 代码库开发的各种问题，包括多种形式的未使用代码。它能检测出头文件中不必要的 #include 指令、未使用的前向声明、已声明但未定义的函数，以及带有虚方法却没有虚析构函数的类。

该工具能识别哪些头文件可以安全移除，从而减少编译依赖并加快增量构建。它还能检测 #include 路径中大小写不一致的情况（例如 `foo.h` 与 `Foo.h`），以及可能在多线程环境下引发问题的全局/静态数据。

# PARAMETERS

**--include-path** _path_
> 额外的 include 搜索路径（类似 gcc -I）。可多次指定。不递归。

**--verbose**
> 启用详细输出以便调试。

**--quiet**
> 抑制输出消息。

# CAVEATS

对条件编译的代码（如 `#ifdef` 块）可能产生误报。移除 include 前应先核实结果。对源文件（非头文件）中不必要 include 的检测能力有限。

# INSTALL

```nix: nix profile install nixpkgs#cppclean```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[clang-tidy](/man/clang-tidy)(1), [cppcheck](/man/cppcheck)(1), [cpplint](/man/cpplint)(1), [gcc](/man/gcc)(1), [cmake](/man/cmake)(1)
