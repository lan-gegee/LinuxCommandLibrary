# TAGLINE

C/C++ 静态分析工具

# TLDR

**检查单个文件**

```cppcheck [file.cpp]```

**检查目录**

```cppcheck [src/]```

**启用所有检查**

```cppcheck --enable=all [file.cpp]```

**启用特定检查**

```cppcheck --enable=warning,style [src/]```

**按 C++ 标准检查**

```cppcheck --std=c++17 [file.cpp]```

**输出为 XML**

```cppcheck --xml [src/] 2> [report.xml]```

**屏蔽特定警告**

```cppcheck --suppress=uninitvar [file.cpp]```

**使用多核**

```cppcheck -j [4] [src/]```

# SYNOPSIS

**cppcheck** [_options_] _path_...

# DESCRIPTION

**cppcheck** 对 C/C++ 源代码执行静态分析，在不运行程序的情况下检测缺陷、未定义行为和危险的编码模式。它专注于保持低误报率，使警告切实可信、值得处理。

该工具分析内存泄漏、空指针解引用、缓冲区溢出、未初始化变量等众多问题。它支持从 C++11 到 C++20 的各标准，可以检查单个文件或整个项目目录。

与编译器警告不同，cppcheck 会进行更深入的分析，包括流敏感检查和过程间分析。它能发现编译器通常会遗漏的问题，同时比 Clang Static Analyzer 这类全面型工具更快、更易配置。

# PARAMETERS

**--enable**=_checks_
> 启用检查：all、warning、style、performance、portability、information、unusedFunction

**--std**=_standard_
> C/C++ 标准：c89、c99、c11、c++03、c++11、c++14、c++17、c++20

**-j** _n_
> 使用 n 个线程

**--xml**
> 以 XML 输出

**--suppress**=_id_
> 屏蔽某类警告

**--suppressions-list**=_file_
> 从文件读取屏蔽规则

**-I** _dir_
> 头文件搜索目录

**-D** _name_
> 定义预处理符号

**--force**
> 检查所有配置组合

**--inconclusive**
> 报告不确定的结果

**--project**=_file_
> 使用编译数据库（compile_commands.json）或 Visual Studio 工程文件

**--check-level**=_level_
> 检查级别：normal（默认）、exhaustive（更深入的分析）、reduced（更快）

**--cppcheck-build-dir**=_dir_
> 构建目录，用于加快重复检查和进行全程序分析

**--platform**=_type_
> 目标平台：unix32、unix64、win32A、win32W、win64、native

**--template**=_format_
> 自定义错误消息格式（如 gcc、vs、{file}:{line}: {message}）

**--max-configs**=_n_
> 每个文件最多检查的配置数（默认：12）

**-q**, **--quiet**
> 抑制进度输出

# CHECK TYPES

**error**: 缺陷与未定义行为
**warning**: 防御性编码问题
**style**: 代码风格问题
**performance**: 性能优化建议
**portability**: 跨平台问题

# CAVEATS

没有正确的 include 路径就无法分析被包含的头文件。要进行全面分析请配合 clang-tidy 使用。

# INSTALL

```apt: sudo apt install cppcheck```

```dnf: sudo dnf install cppcheck```

```pacman: sudo pacman -S cppcheck```

```apk: sudo apk add cppcheck```

```zypper: sudo zypper install cppcheck```

```brew: brew install cppcheck```

```nix: nix profile install nixpkgs#cppcheck```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[clang-tidy](/man/clang-tidy)(1), [cpplint](/man/cpplint)(1), [gcc](/man/gcc)(1)
