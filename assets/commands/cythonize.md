# TAGLINE

用于构建扩展模块的 Cython 编译封装工具

# TLDR

**编译 Cython 文件**

```cythonize -i [module.pyx]```

**使用构建目录编译**

```cythonize -b [module.pyx]```

**编译多个文件**

```cythonize -i [*.pyx]```

**并行编译**

```cythonize -j [4] -i [module.pyx]```

**强制重新编译**

```cythonize -f -i [module.pyx]```

**生成 HTML 注解**

```cythonize -a [module.pyx]```

# SYNOPSIS

**cythonize** [_options_] _files_...

# DESCRIPTION

**cythonize** 将 Cython 源文件（.pyx）编译为 C 扩展模块。Cython 是 Python 的超集，通过静态类型和直接访问 C API 获得 C 级别的性能。

该工具负责完整的编译流程：生成 C 代码、用 C 编译器编译，并构建可导入的 Python 模块。

# PARAMETERS

**-i**, **--inplace**
> 在原位置构建扩展模块。

**-b**, **--build**
> 使用临时构建目录进行构建。

**-j** _n_
> 并行编译任务数。

**-f**, **--force**
> 强制重新编译。

**-a**, **--annotate**
> 生成 HTML 注解。

**-3**
> 使用 Python 3 语法。

**-X** _directive_
> 设置 Cython 指令。

**-s** _option_
> 设置编译器选项。

**--cplus**
> 生成 C++ 代码。

# CAVEATS

需要已安装 C 编译器。平台相关的扩展不可移植。注解有助于识别以 Python 为主的代码。某些 Python 特性在 Cython 中会更慢。

# HISTORY

**Cython** 演化自 **Greg Ewing** 于 **2002 年**创建的 **Pyrex**。由 **Robert Bradshaw** 和 **Stefan Behnel** 主导的 Cython 分支增加了 Python 兼容性和诸多特性。cythonize 命令为整个编译过程提供了便捷的封装。

# INSTALL

```apt: sudo apt install cython3```

```pacman: sudo pacman -S cython```

```apk: sudo apk add cython```

```brew: brew install cython```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[python](/man/python)(1), [gcc](/man/gcc)(1), [pip](/man/pip)(1)
