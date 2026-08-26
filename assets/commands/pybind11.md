# TAGLINE

为 C++ 代码创建 Python 绑定

# TLDR

**获取 include 路径**

```python -m pybind11 --includes```

**获取 CMake 目录**

```python -m pybind11 --cmakedir```

**手动编译绑定**

```c++ -O3 -shared $(python3 -m pybind11 --includes) [example.cpp] -o [example.so]```

# SYNOPSIS

**python -m pybind11** [_options_]

# PARAMETERS

**--includes**
> 编译器所需的 include 标志。

**--cmakedir**
> CMake 模块路径。

# DESCRIPTION

**pybind11** 是一个仅含头文件的库，用于为 C++ 代码创建 Python 绑定。它以最少的样板代码实现 Python 与 C++ 之间的无缝互操作。

# EXAMPLE BINDING

```cpp
#include <pybind11/pybind11.h>

int add(int a, int b) {
    return a + b;
}

PYBIND11_MODULE(example, m) {
    m.def("add", &add, "Add two numbers");
}
```

# CMAKE SETUP

```cmake
find_package(pybind11 REQUIRED)
pybind11_add_module(example example.cpp)
```

# COMPILE MANUALLY

```bash
# Get flags
CFLAGS=$(python3 -m pybind11 --includes)
SUFFIX=$(python3-config --extension-suffix)

# Compile
c++ -O3 -Wall -shared -std=c++11 -fPIC \
    $CFLAGS example.cpp -o example$SUFFIX
```

# CAVEATS

仅含头文件（无需链接）。需要 C++11 及以上。相比纯 C API 性能开销极小。

# HISTORY

pybind11 由 **Wenzel Jakob** 创建，作为 Boost.Python 的轻量替代方案，重点利用 C++11 特性。

# INSTALL

```pacman: sudo pacman -S pybind11```

```brew: brew install pybind11```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cython](/man/cython)(1), [swig](/man/swig)(1), [python](/man/python)(1)
