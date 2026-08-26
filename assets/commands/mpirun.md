# TAGLINE

启动 MPI 并行程序

# TLDR

**运行 MPI 程序**

```mpirun -np [4] [program]```

**在多个主机上运行**

```mpirun -np [8] --hostfile [hosts.txt] [program]```

**以每主机指定 slot 数运行**

```mpirun -np [4] --map-by node [program]```

# SYNOPSIS

**mpirun** [_options_] _program_ [_args_...]

# PARAMETERS

**-np** _n_
> 进程数量。

**--hostfile** _file_
> 包含主机列表的文件。

**--host** _hosts_
> 以逗号分隔的主机列表。

**--map-by** _policy_
> 进程映射方式（node、slot、core）。

**--bind-to** _policy_
> 进程绑定策略。

**-x** _var_
> 导出环境变量。

# DESCRIPTION

**mpirun** 用于启动 MPI 并行程序。它跨节点启动多个进程以进行分布式计算，属于 OpenMPI 或 MPICH 实现的一部分。

# INSTALL

```dnf: sudo dnf install openmpi```

```pacman: sudo pacman -S openmpi```

```apk: sudo apk add openmpi```

```brew: brew install openmpi```

```nix: nix profile install nixpkgs#openmpi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mpiexec](/man/mpiexec)(1), [mpicc](/man/mpicc)(1)
