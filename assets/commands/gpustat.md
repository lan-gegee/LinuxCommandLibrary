# TAGLINE

简洁的 NVIDIA GPU 状态监视器

# TLDR

**显示 GPU 状态**

```gpustat```

**显示进程信息**

```gpustat -p```

**持续监控**

```gpustat -i [1]```

**显示完整的命令名称**

```gpustat -cp```

**JSON 输出**

```gpustat --json```

**显示进程用户名**

```gpustat -u```

# SYNOPSIS

**gpustat** [_options_]

# PARAMETERS

**-p**, **--show-pid**
> 显示进程 PID。

**-u**, **--show-user**
> 显示进程用户名。

**-c**, **--show-cmd**
> 显示进程命令。

**-f**, **--show-full-cmd**
> 显示运行中进程的完整命令行和 CPU 统计信息。

**-F**, **--show-fan-speed**
> 显示 GPU 风扇转速。

**-P**, **--show-power**
> 显示 GPU 功耗/用电量及上限。

**-e**, **--show-codec**
> 显示编码器/解码器利用率。

**-i**, **--interval**, **--watch** _seconds_
> 以 watch 模式运行，每 _seconds_ 秒刷新一次。

**--json**
> 以 JSON 格式输出。

**--no-color**
> 禁用彩色输出。

**--no-header**
> 隐藏表头。

**--no-processes**
> 省略运行中进程的信息（内存、用户等）。

**-a**, **--show-all**
> 显示所有信息。

**--id** _id_
> 仅显示指定的 GPU。

**-v**, **--version**
> 显示版本信息。

# DESCRIPTION

**gpustat** 以简洁的格式显示 GPU 状态，类似于 nvidia-smi 但更易读。它可以一目了然地显示 GPU 利用率、内存占用、温度和运行中的进程。

该工具专为机器学习训练或其他 GPU 密集型任务期间的 NVIDIA GPU 快速监控而设计。

# CAVEATS

需要 NVIDIA GPU 及其驱动。内部使用 nvidia-smi。不适用于非 NVIDIA GPU。查看进程信息需要相应的权限。

# HISTORY

**gpustat** 由 **Jongwook Choi** 创建，是为机器学习从业者打造的简易 GPU 监控工具。它提供了比 nvidia-smi 冗长输出更清爽的替代方案，专注于关键指标。

# INSTALL

```nix: nix profile install nixpkgs#gpustat```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nvidia-smi](/man/nvidia-smi)(1), [nvtop](/man/nvtop)(1), [htop](/man/htop)(1), [watch](/man/watch)(1)

# RESOURCES

```[Source code](https://github.com/wookayin/gpustat)```

<!-- verified: 2026-07-17 -->
