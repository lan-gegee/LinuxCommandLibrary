# TAGLINE

编译 MPI C++ 程序

# TLDR

**编译 MPI C++ 程序**

```mpic++ -o [program] [source.cpp]```

**带优化编译**

```mpic++ -O2 -o [program] [source.cpp]```

**显示编译器命令**

```mpic++ --showme [source.cpp]```

# SYNOPSIS

**mpic++** [_options_] _source_files_...

# PARAMETERS

**-o** _file_
> 输出文件名。

**-O** _level_
> 优化级别。

**--showme**
> 显示底层编译器命令。

**-I** _dir_
> 头文件目录。

**-L** _dir_
> 库目录。

**-std=** _standard_
> C++ 标准版本（c++11、c++14、c++17、c++20）。

**-show**
> 打印将被调用的底层编译器命令行然后退出（MPICH 风格）。

**--showme:compile** / **--showme:link** / **--showme:command**
> 仅打印编译选项、仅打印链接选项，或仅打印被包装的编译器名称（Open MPI）。

# DESCRIPTION

**mpic++** 是随各 MPI 实现（Open MPI、MPICH、MVAPICH、Intel MPI）一起提供的编译器驱动，它会调用底层系统 C++ 编译器，并自动加上构建 MPI 程序所需的头文件路径、库路径和链接库。它是 **mpicc** 的 C++ 对应版本，通常是指向 **mpicxx** 的符号链接或别名。

可以通过 `OMPI_CXX`（Open MPI）或 `MPICH_CXX`（MPICH）环境变量覆盖被包装的编译器，使同一个包装器驱动 `g++`、`clang++`、`icpx` 等。

# CAVEATS

包装器注入的选项取决于具体的 MPI 实现；不要依赖 `--showme` 在 Open MPI 和 MPICH 之间语义完全一致。混用由不同 MPI 包装器编译的目标文件是不安全的。

# INSTALL

```apk: sudo apk add openmpi-dev```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mpirun](/man/mpirun)(1), [mpicxx](/man/mpicxx)(1), [mpicc](/man/mpicc)(1)
