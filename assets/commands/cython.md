# TAGLINE

Python 到 C/C++ 的编译器

# TLDR

**将 Cython 文件编译**为 C

```cython [module.pyx]```

**以 Python 3 语言级别编译**

```cython -3 [module.pyx]```

**生成 C++ 代码**而非 C

```cython --cplus [module.pyx]```

**带注解编译**（生成 HTML 报告）

```cython -a [module.pyx]```

**指定输出文件名**

```cython -o [output.c] [module.pyx]```

**内嵌 Python 解释器**（创建独立可执行文件）

```cython --embed [module.pyx]```

# SYNOPSIS

**cython** [_options_] _source_file.pyx_

# PARAMETERS

**-o** _FILE_
> 指定输出的 C/C++ 文件名。

**-3**, **--3**
> 使用 Python 3 语法与语义。

**-2**, **--2**
> 使用 Python 2 语法与语义。

**--cplus**
> 生成 C++ 代码而非 C。

**-a**, **--annotate**
> 生成展示 Python/C 交互情况的注解 HTML。

**--embed** [_MAIN_]
> 生成用于内嵌 Python 的 main() 函数。

**-I** _DIR_, **--include-dir** _DIR_
> 添加包含目录。

**-w**, **--working** _DIR_
> 设置工作目录。

**--line-directives**
> 输出源代码行指令。

**-X** _NAME=VALUE_
> 设置编译器指令。

# DESCRIPTION

**Cython** 是一种编程语言和编译器，可将类似 Python 的代码翻译为 C 或 C++。它让你能用 Python 语法编写 Python 的 C 扩展，相比纯 Python 带来显著的性能提升。

该编译器接收 **.pyx** 文件（Cython 源码），并生成可编译为 Python 扩展模块的 C 或 C++ 文件。Cython 代码可以同时包含 Python 和 C 类型声明，从而实现细粒度的优化。

注解模式（**-a**) 对优化特别有用，它会生成一份 HTML 报告，标明哪些行产生 Python API 调用、哪些是纯 C 代码，并用颜色编码突出较慢的路径。

# CAVEATS

生成的 C 文件仍需用 C 编译器编译。setuptools 等构建系统通常会处理这一步。类型注解同时影响性能和行为。C 异常的处理方式与 Python 异常不同。

# HISTORY

Cython 演化自 Greg Ewing 于 **2002 年**创建的 **Pyrex**。Cython 分支始于 **2007 年**，陆续加入了类型化 memoryview 和并行支持等特性。它被广泛用于科学计算以及为 C 库创建 Python 绑定。

# INSTALL

```apt: sudo apt install cython3```

```pacman: sudo pacman -S cython```

```apk: sudo apk add cython```

```brew: brew install cython```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[python](/man/python)(1), [gcc](/man/gcc)(1), [cythonize](/man/cythonize)(1)

# RESOURCES

```[Source code](https://github.com/cython/cython)```

```[Homepage](https://cython.org)```

```[Documentation](https://docs.cython.org)```

<!-- verified: 2026-06-26 -->
