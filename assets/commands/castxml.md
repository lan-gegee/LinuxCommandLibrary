# TAGLINE

生成 C/C++ 声明的 XML 描述

# TLDR

**从 C++ 头文件生成 XML**

```castxml --castxml-output=1 [header.hpp] -o [output.xml]```

**生成 gccxml 兼容的输出**

```castxml --castxml-gccxml [header.hpp] -o [output.xml]```

**针对 GNU 编译器进行配置**

```castxml --castxml-cc-gnu [g++] [header.hpp] -o [output.xml]```

**从指定声明开始遍历 AST**

```castxml --castxml-start [ClassName] [header.hpp] -o [output.xml]```

**包含路径与宏定义**

```castxml -I[/include/path] -D[MACRO] [header.hpp] -o [output.xml]```

# SYNOPSIS

**castxml** [_options_] _input_file_

# DESCRIPTION

**castxml** 从源文件创建 C 和 C++ 声明的 XML 表示。它使用 Clang 编译器前端解析 C 系源代码，并输出结构化的 XML，描述类型、函数、类和其他声明。

该工具常被用作生成语言绑定的基础，让 pygccxml 之类的项目能够自动为 C++ 库创建 Python 封装。它也可作为代码分析后端，用于需要头文件的机器可读表示的场景。

CastXML 的诞生是为了取代已废弃的 GCC-XML 工具，提供一个基于 Clang 的现代替代品，同时提供兼容的输出格式以保持向后兼容。

# PARAMETERS

**--castxml-output**=_version_
> 生成 castxml 格式的输出（版本必须为 '1'）

**--castxml-gccxml**
> 生成 gccxml 兼容的输出格式

**--castxml-cc-gnu** _compiler_
> 为 GNU 编译器配置预处理器/目标

**--castxml-cc-msvc** _compiler_
> 为 MSVC 编译器配置预处理器/目标

**--castxml-cc-gnu-c** _compiler_
> 针对 GNU C 编译器进行配置

**--castxml-cc-msvc-c** _compiler_
> 针对 MSVC C 编译器进行配置

**--castxml-start** _name_
> 从指定名称的声明开始遍历 AST

**-o** _file_
> 输出文件路径

**-I** _path_
> 添加包含搜索路径

**-D** _macro_
> 定义预处理器宏

**-std**=_standard_
> C++ 标准（c++11、c++14、c++17 等）

# USE CASES

**语言绑定**
> 为 Python、Rust 等语言生成绑定。

**代码分析**
> 解析并分析 C++ 代码库。

**文档**
> 提取 API 信息。

# CAVEATS

输出格式取决于所选选项。GCCXML 格式仅为旧版兼容而提供。配合 pygccxml 可进行基于 Python 的分析。

# INSTALL

```apt: sudo apt install castxml```

```dnf: sudo dnf install castxml```

```pacman: sudo pacman -S castxml```

```brew: brew install castxml```

```nix: nix profile install nixpkgs#castxml```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[clang](/man/clang)(1), [g++](/man/g++)(1)

# RESOURCES

```[Source code](https://github.com/CastXML/CastXML)```

```[Documentation](https://github.com/CastXML/CastXML/blob/master/doc/manual/castxml.1.rst)```

<!-- verified: 2026-06-22 -->
