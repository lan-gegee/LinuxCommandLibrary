# TAGLINE

Python 连接 C 库的外部函数接口

# TLDR

**加载共享库**

```python -c "from ctypes import CDLL; lib = CDLL('[libname.so]')"```

**调用 C 函数**

```python -c "from ctypes import CDLL; lib = CDLL('libc.so.6'); print(lib.getpid())"```

**向 C 函数传递字符串参数**

```python -c "from ctypes import CDLL, c_char_p; lib = CDLL('libc.so.6'); lib.puts(c_char_p(b'Hello'))"```

**定义函数参数与返回类型**

```python -c "from ctypes import CDLL, c_int; lib = CDLL('libm.so.6'); lib.abs.argtypes = [c_int]; lib.abs.restype = c_int; print(lib.abs(-42))"```

**访问 Windows DLL**

```python -c "from ctypes import windll; windll.user32.MessageBoxW(0, 'Hello', 'Title', 0)"```

# SYNOPSIS

```python
from ctypes import CDLL, c_int, c_char_p, POINTER
```

# TYPES

**c_int**, **c_long**, **c_longlong**
> 整数类型。

**c_uint**, **c_ulong**
> 无符号整数。

**c_float**, **c_double**
> 浮点类型。

**c_char**, **c_wchar**
> 字符类型。

**c_char_p**, **c_wchar_p**
> 字符串指针（char*、wchar_t*）。

**c_void_p**
> void 指针。

**POINTER(type)**
> 指向 type 的指针。

**Structure**, **Union**
> C 结构体/联合体的基类。

# DESCRIPTION

**ctypes** 是 Python 标准库模块，用于调用 C 共享库和 DLL 中的函数。它提供与 C 兼容的数据类型，允许在指定恰当的参数与返回类型后调用函数。

该模块使 Python 代码无需编写 C 扩展模块即可对接原生库。它负责 Python 与 C 之间的类型转换、指针管理以及结构体/联合体的定义。

常见用途包括访问系统库、操作硬件接口、集成遗留 C 代码，以及调用平台专有 API（Windows DLL、macOS 框架）。

# CAVEATS

类型声明不正确可能导致崩溃或内存损坏。指针和内存管理需要小心处理。库路径因操作系统而异；为保证可移植性请使用 **find_library**。相比 C 扩展存在性能开销。不适用于带名称修饰（name mangling）的 C++ 库。

# HISTORY

ctypes 由 **Thomas Heller** 创建，并在 **2.5** 版（2006 年）合并进 Python 标准库。它源自 **2003 年**起就发布在 PyPI 上的早期 ctypes 项目。该模块让 Python 无需编译即可对接原生代码，是一项关键能力，使得纯 Python 访问系统库成为可能。

# SEE ALSO

[cython](/man/cython)(1)
