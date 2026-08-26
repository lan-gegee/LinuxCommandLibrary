# TAGLINE

编译 MPI C 程序

# TLDR

**编译 MPI C 程序**

```mpicc -o [program] [source.c]```

**带优化编译**

```mpicc -O2 -o [program] [source.c]```

**显示编译器命令**

```mpicc --showme [source.c]```

# SYNOPSIS

**mpicc** [_options_] _source_files_...

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

# DESCRIPTION

**mpicc** 用于编译 MPI C 程序。它是系统 C 编译器的包装器，会自动加上 MPI 头文件和库，并自动链接 MPI 库。

# INSTALL

```apk: sudo apk add openmpi-dev```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mpirun](/man/mpirun)(1), [mpic++](/man/mpic++)(1)
