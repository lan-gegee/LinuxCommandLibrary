# TAGLINE

启动 MPI 并行程序

# TLDR

以 N 个进程**运行**并行 MPI 程序

```mpiexec -n [4] [program]```

**跨多个主机运行**，主机列表来自 hostfile

```mpiexec -n [8] -f [hostfile] [program]```

**在指定主机上运行**

```mpiexec -host [host1,host2] -n [4] [program]```

在同一个 MPI 作业中**运行不同程序**（MPMD）

```mpiexec -n [2] [prog_a] : -n [4] [prog_b]```

向启动的各个 rank **传递环境变量**

```mpiexec -genv [OMP_NUM_THREADS] [2] -n [4] [program]```

不实际运行，只**显示将要启动的内容**

```mpiexec -info```

# SYNOPSIS

**mpiexec** [_global-options_] [_local-options_ _executable_ [_args_]] [**:** _local-options_ _executable_ [_args_]]...

# PARAMETERS

**-n** _num_, **-np** _num_
> 要启动的进程数（rank 数）。

**-f** _hostfile_, **-machinefile** _hostfile_
> 列出可用节点（及可选 slot 数）的文件。

**-host** _hostlist_
> 以逗号分隔的主机列表。

**-hosts** _hostlist_
> 与 **-host** 相同（Open MPI）。

**-ppn** _num_, **-perhost** _num_
> 每个节点的进程数。

**-wdir** _dir_
> 被启动进程的工作目录。

**-env** _var_ _value_
> 为当前命令段设置环境变量。

**-genv** _var_ _value_
> 全局为所有命令段设置环境变量。

**-envlist** _list_
> 从启动环境中转发指定名称的变量。

**-bind-to** _target_
> 绑定进程（core、socket、numa、none）。

**-map-by** _policy_
> 进程放置策略（slot、node、socket、numa 等）。

**-x** _VAR_
> Open MPI：将环境变量导出给远程进程。

**-info**
> 打印 MPI 运行时的构建/配置信息。

# DESCRIPTION

**mpiexec** 是 MPI-2 规范定义的标准 MPI 进程启动器。它通过派生所需数量的进程（rank）并安排它们之间的通信基础设施来启动并行 MPI 作业。具体实现取决于安装的是哪种 MPI：**MPICH**/Hydra、**Open MPI**、Intel MPI 等都提供 **mpiexec** 二进制文件，选项集相近但不完全相同。

**mpiexec** 还支持 MPMD（多程序多数据）作业：用冒号（**:**）分隔参数，即可让多个可执行文件作为同一个 MPI world 一起运行。

在大多数实现中，**mpirun** 是 **mpiexec** 的同义词（有时甚至是规范名称）；对常见场景而言两者可以互换。

# CAVEATS

各 MPI 实现之间的选项存在细微差异（尤其是 Hydra 与 Open MPI）；针对某个启动器编写的脚本换用另一个时可能需要调整。启动器必须能访问每个主机（通常通过 SSH），且各节点上的 MPI 运行时库必须一致。在同一个 shell 会话中混用来自不同 MPI 安装的 **mpiexec** 二进制文件会导致难以排查的失败。

# HISTORY

**mpiexec** 由 **MPI-2** 标准（1997 年）引入，作为一种可移植、被推荐的 MPI 程序启动方式，取代了各实现专属的启动器。现代 MPI 发行版仍同时提供 **mpiexec** 和 **mpirun**。

# INSTALL

```dnf: sudo dnf install openmpi```

```pacman: sudo pacman -S openmpi```

```apk: sudo apk add openmpi```

```brew: brew install openmpi```

```nix: nix profile install nixpkgs#openmpi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mpirun](/man/mpirun)(1), [mpicc](/man/mpicc)(1)
