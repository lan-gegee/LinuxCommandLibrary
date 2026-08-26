# TAGLINE

GNU Fortran 编译器

# TLDR

**编译 Fortran 文件**

```gfortran [source.f90] -o [output]```

**开启优化编译**

```gfortran -O3 [source.f90] -o [output]```

**启用警告**

```gfortran -Wall [source.f90] -o [output]```

**调试版构建**

```gfortran -g [source.f90] -o [output]```

**链接数学库**

```gfortran [source.f90] -o [output] -lm```

# SYNOPSIS

**gfortran** [_options_] _files_...

# PARAMETERS

_FILES_
> Fortran 源文件（.f、.f90、.f95）。

**-o** _FILE_
> 输出文件名。

**-c**
> 只编译，不链接。

**-g**
> 生成调试信息。

**-O** _LEVEL_
> 优化级别（0-3）。

**-Wall**
> 启用警告。

**-l** _LIBRARY_
> 链接库。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gfortran** 是 GNU Fortran 编译器，属于 GCC 的一部分。它将 Fortran 77、90、95、2003 和 2008 标准编译为本地可执行文件。

该编译器提供丰富的优化选项、调试支持以及与 C 代码的互操作性。它受益于 GCC 成熟的基础设施。

gfortran 是科学计算领域的标准开源 Fortran 编译器。

# CAVEATS

标准符合程度因特性而异。数组边界检查为可选功能。遗留代码可能需要适配修改。

# HISTORY

从 GCC 4.0 起，gfortran 取代 g77 成为 GCC 的 Fortran 编译器。它在保持与旧代码兼容的同时支持现代 Fortran 标准。

# INSTALL

```apt: sudo apt install gfortran```

```apk: sudo apk add gfortran```

```brew: brew install gfortran```

```nix: nix profile install nixpkgs#gfortran```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gcc](/man/gcc)(1), [f2py](/man/f2py)(1)
