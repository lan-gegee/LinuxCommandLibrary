# TAGLINE

LLVM C++ 编译器前端

# TLDR

**编译一个 C++ 源文件**

```clang++ [source.cpp] -o [output]```

**以 C++17 标准编译**

```clang++ -std=c++17 [source.cpp] -o [output]```

**开启优化编译**

```clang++ -O2 [source.cpp] -o [output]```

**带调试符号编译**

```clang++ -g [source.cpp] -o [output]```

**开启所有警告并将其视为错误**

```clang++ -Wall -Wextra -Werror [source.cpp] -o [output]```

**定义预处理器宏并编译**

```clang++ -D[MACRO=value] [source.cpp] -o [output]```

**链接一个库**

```clang++ [source.cpp] -l[library] -o [output]```

**仅生成目标文件**

```clang++ -c [source.cpp] -o [source.o]```

# SYNOPSIS

**clang++** [_options_] _files..._

# PARAMETERS

**-o** _file_
> 输出文件名。

**-c**
> 仅编译，不链接。

**-std=**_standard_
> 设置 C++ 标准（c++11、c++14、c++17、c++20、c++23、c++26）。

**-O**_level_
> 优化等级（0、1、2、3、s、z）。

**-g**
> 生成调试信息。

**-Wall**
> 启用大多数警告。

**-Wextra**
> 启用额外警告。

**-I** _path_
> 添加头文件搜索目录。

**-L** _path_
> 添加库搜索路径。

**-l** _library_
> 链接指定库。

**-D** _macro=value_
> 定义预处理器宏。

**-Werror**
> 将警告视为错误。

**-Wpedantic**
> 就严格 ISO C++ 兼容性所要求的问题发出警告。

**-stdlib=**_library_
> 指定 C++ 标准库（libc++ 或 libstdc++）。

# DESCRIPTION

**clang++** 是 Clang 的 C++ 编译器前端，属于 LLVM 项目。它将 C++ 源代码编译为可执行文件或目标文件。Clang 提供快速编译、富有表现力的诊断信息以及与 GCC 的兼容性。

它支持现代 C++ 标准，并提供高级静态分析和工具集成。

# CAVEATS

某些 GCC 特有扩展可能不受支持。使用 **-stdlib=libc++** 选择 LLVM 的 libc++，或 **-stdlib=libstdc++** 选择 GNU 标准库。

# INSTALL

```apt: sudo apt install clang```

```dnf: sudo dnf install clang```

```pacman: sudo pacman -S clang```

```apk: sudo apk add clang22```

```zypper: sudo zypper install clang```

```nix: nix profile install nixpkgs#clang```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[clang](/man/clang)(1), [g++](/man/g++)(1), [clang-format](/man/clang-format)(1)
