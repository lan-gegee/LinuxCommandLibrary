# TAGLINE

Open MPI 的 C++ 包装编译器

# TLDR

**编译 MPI C++ 程序**

```mpicxx -o [program] [source.cpp]```

**带优化编译**

```mpicxx -O3 -o [program] [source.cpp]```

**显示完整的底层编译器命令**

```mpicxx --showme```

**仅显示编译选项**

```mpicxx --showme:compile```

**仅显示链接选项**

```mpicxx --showme:link```

**编译并链接额外的库**

```mpicxx -o [program] [source.cpp] -l[library]```

# SYNOPSIS

**mpicxx** [_options_] _source_files_...

# PARAMETERS

**-o** _file_
> 输出文件名。

**-O** _level_
> 优化级别（0、1、2、3）。

**--showme**
> 显示将被调用的完整编译器命令，但不实际编译。

**--showme:compile**
> 仅显示 MPI 包装器添加的编译选项。

**--showme:link**
> 仅显示 MPI 包装器添加的链接选项。

**--showme:command**
> 显示底层 C++ 编译器命令。

**--showme:incdirs**
> 显示 MPI 包装器使用的头文件目录。

**--showme:libdirs**
> 显示 MPI 包装器使用的库目录。

**--showme:libs**
> 显示用于链接的库名称。

**--showme:version**
> 显示 Open MPI 的版本。

**-I** _dir_
> 将目录添加到头文件搜索路径。

**-L** _dir_
> 将目录添加到库搜索路径。

**-l** _library_
> 链接指定的库。

# DESCRIPTION

**mpicxx** 是 Open MPI 的 C++ 包装编译器。它本身不是编译器，而是一个便捷包装：为 MPI 程序添加必要的编译和链接选项，然后调用底层系统 C++ 编译器。它与 **mpic++** 等价。

该包装器会透明地添加针对 MPI 库进行编译和链接所需的 **-I**、**-L** 和 **-l** 选项。所有其他选项都会直接传给底层 C++ 编译器。你可以使用 **--showme** 系列选项确切查看添加了哪些选项。

可以使用 **OMPI_CXX**（Open MPI）或 **MPICH_CXX**（MPICH）等环境变量覆盖包装器使用的底层 C++ 编译器。

# INSTALL

```apk: sudo apk add openmpi-dev```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mpirun](/man/mpirun)(1), [mpiexec](/man/mpiexec)(1), [mpic++](/man/mpic++)(1), [mpicc](/man/mpicc)(1), [g++](/man/g++)(1)
