# TAGLINE

面向 HPC 并行应用的动态负载均衡库及工具

# TLDR

**列出所有 DLB 进程的 CPU 亲和性**

```dlb_taskset --list```

**为 DLB 进程设置 CPU 亲和性**

```dlb_taskset --set [0-3] --pid [pid]```

**为新应用借用 CPU**

```dlb_taskset --borrow --set [0-7] -- [application]```

**显示帮助信息**

```dlb_taskset --help```

# SYNOPSIS

**dlb_taskset** [_options_] [**--**] [_command_]

# PARAMETERS

**--list**
> 列出所有 DLB 进程的 CPU 亲和性。

**--set** _MASK_
> 为进程设置 CPU 亲和性掩码。

**--pid** _PID_
> 指定要操作的进程 ID。

**--borrow**
> 以借用的方式而非抢占方式获取 CPU；应用结束时归还所借 CPU。

**--color** _WHEN_
> 输出着色（yes、auto、no）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**DLB**（Dynamic Load Balancing，动态负载均衡）是一个库，可在同一共享内存节点内的多个进程之间动态重新分配计算资源。它通过调整内层并行（如 OpenMP）的资源来改善外层并行（如 MPI）的负载均衡。

DLB 提供三个主要组件：**LeWI**（Lend When Idle）在进程间重新分配空闲的 CPU，**DROM**（Dynamic Resource Ownership Manager）管理 CPU 亲和性，**TALP**（Tracking Application Live Performance）收集性能数据。

**dlb_taskset** 命令行工具管理启用了 DLB 的进程的 CPU 亲和性，并能以指定的 CPU 分配启动新应用。

# CAVEATS

要求应用链接 DLB 库并启用 DLB 支持。最适合负载变化频繁的迭代式 HPC 应用。各进程必须运行在同一共享内存节点上。

# HISTORY

DLB 由 **巴塞罗那超级计算中心（BSC）** 为高性能计算应用开发，采用 **LGPL-3.0** 许可证分发。

# SEE ALSO

[mpirun](/man/mpirun)(1), [srun](/man/srun)(1)
