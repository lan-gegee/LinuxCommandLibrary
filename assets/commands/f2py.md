# TAGLINE

Fortran 到 Python 的接口生成器

# TLDR

为 Fortran **生成 Python 包装模块**

```f2py -c [module.f90] -m [module_name]```

**创建签名文件**

```f2py [module.f90] -h [module.pyf]```

**使用指定**编译器构建

```f2py -c --fcompiler=[gfortran] [module.f90] -m [module_name]```

**链接外部库**

```f2py -c [module.f90] -m [module_name] -l[blas]```

**显示可用的编译器**

```f2py --help-fcompiler```

# SYNOPSIS

**f2py** [_options_] _fortran-files_ [_options_]

# PARAMETERS

_FORTRAN-FILES_
> Fortran 源文件（.f、.f90、.f95）。

**-c**
> 编译并构建扩展模块。

**-m** _NAME_
> 设置模块名。

**-h** _FILE_
> 生成签名文件。

**--fcompiler** _NAME_
> 指定 Fortran 编译器。

**-l** _LIBRARY_
> 链接指定的库。

**-L** _PATH_
> 库搜索路径。

**-I** _PATH_
> 头文件搜索路径。

**--help-fcompiler**
> 列出可用的 Fortran 编译器。

**--help**
> 显示帮助信息。

# DESCRIPTION

**f2py**（Fortran to Python）是 NumPy 的一个工具，可为 Fortran 代码创建 Python 绑定。它生成包装模块，让你可以直接从 Python 调用 Fortran 子例程和函数。

该工具自动处理 Python/NumPy 数组与 Fortran 数组之间的类型转换。它解析 Fortran 源代码或签名文件以确定接口，然后生成编译为 Python 扩展模块的 C 包装代码。

f2py 让你无需重写现有代码即可在 Python 科学计算工作流中使用高性能的 Fortran 库。

# CAVEATS

需要安装 Fortran 编译器和 NumPy。复杂的 Fortran 结构可能需要调整签名文件。Fortran（列优先）与 C（行优先）的数组排列顺序不同。

# HISTORY

f2py 由 **Pearu Peterson** 创建于 1990 年代末，后来成为 NumPy 的一部分。它将 Python 科学计算生态与数十年积累的 Fortran 数值库连接起来，使这些库得以在现代 Python 工作流中继续使用。

# INSTALL

```apt: sudo apt install python3-numpy```

```dnf: sudo dnf install python3-numpy```

```apk: sudo apk add py3-numpy-f2py```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[python](/man/python)(1), [gfortran](/man/gfortran)(1), [cython](/man/cython)(1)
