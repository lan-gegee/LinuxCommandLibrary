# TAGLINE

Clang C/C++ 预处理器

# TLDR

对源文件**运行 C 预处理器**

```clang-cpp [source.c]```

**带宏定义进行预处理**

```clang-cpp -D[MACRO]=[value] [source.c]```

**带头文件搜索路径预处理**

```clang-cpp -I[/path/to/includes] [source.c]```

**输出到文件**

```clang-cpp [source.c] -o [output.i]```

# SYNOPSIS

**clang-cpp** [_options_] _file_

# PARAMETERS

**-D** _macro[=value]_
> 定义一个预处理器宏。

**-U** _macro_
> 取消定义一个预处理器宏。

**-I** _path_
> 添加头文件搜索路径。

**-o** _file_
> 将输出写入文件。

**-E**
> 仅预处理（隐含）。

# DESCRIPTION

**clang-cpp** 是 Clang 的 C 预处理器。它处理 #include 指令、宏展开和条件编译，输出预处理后的源代码。

它是 GCC 中 **cpp** 的 LLVM/Clang 等价物。

# INSTALL

```apk: sudo apk add clang22```

```zypper: sudo zypper install clang22```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[clang](/man/clang)(1), [clang++](/man/clang++)(1)
