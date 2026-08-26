# TAGLINE

编译 MPI Java 程序

# TLDR

**编译 MPI Java 程序**

```mpijavac [MPIProgram.java]```

**编译到指定目录**

```mpijavac -d [classes/] [MPIProgram.java]```

**带 classpath 编译**

```mpijavac -cp [lib/*] [MPIProgram.java]```

# SYNOPSIS

**mpijavac** [_options_] _source_files_...

# PARAMETERS

**-d** _dir_
> class 文件的输出目录。

**-cp** _path_
> 编译用的 classpath。

**-sourcepath** _path_
> 源文件路径。

**--showme**
> 显示底层 javac 命令。

# DESCRIPTION

**mpijavac** 用于编译 MPI Java 程序。它是 javac 的包装器，会自动加上 MPI Java 绑定。配合 OpenMPI 的 Java 接口，可用于 Java 并行计算。

# INSTALL

```apt: sudo apt install openmpi-bin```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mpirun](/man/mpirun)(1), [javac](/man/javac)(1), [mpicc](/man/mpicc)(1)
