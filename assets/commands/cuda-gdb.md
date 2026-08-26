# TAGLINE

NVIDIA CUDA 内核调试器

# TLDR

**调试 CUDA 应用程序**

```cuda-gdb [./program]```

**带参数调试**

```cuda-gdb --args [./program] [arg1] [arg2]```

**附加到运行中的进程**

```cuda-gdb -p [pid]```

**调试核心转储**

```cuda-gdb [./program] [core]```

在指定 GPU 上运行

```CUDA_VISIBLE_DEVICES=[0] cuda-gdb [./program]```

# SYNOPSIS

**cuda-gdb** [_options_] [_executable_] [_core_|_pid_]

# PARAMETERS

**--args**
> 向被调试的程序传递参数。

**-p** _pid_
> 附加到运行中的进程。

**-x** _file_
> 从文件执行 GDB 命令。

**-tui**
> 启用文本用户界面模式。

**-q**, **--quiet**
> 不显示启动消息。

**--cuda-use-lockfile=0**
> 禁用 GPU 锁文件（用于多实例调试）。

# CUDA-SPECIFIC COMMANDS

**cuda kernel**
> 切换到指定的内核。

**cuda block**
> 切换到指定的块。

**cuda thread**
> 在块内切换到指定线程。

**info cuda kernels**
> 列出活动的 CUDA 内核。

**info cuda threads**
> 列出 CUDA 线程。

**info cuda devices**
> 列出 CUDA 设备。

**cuda device**
> 切换到指定设备。

**cuda grid**
> 切换到指定网格。

**info cuda sms**
> 列出 CUDA 流式多处理器。

**info cuda warps**
> 列出 CUDA warp。

**info cuda lanes**
> 列出 CUDA lane。

**info cuda launch trace**
> 显示内核启动轨迹。

**set cuda break_on_launch**
> 在内核启动时中断（应用程序或系统内核）。

**set cuda memcheck on**
> 启用内存检查以捕获越界访问。

# DESCRIPTION

**cuda-gdb** 是 NVIDIA 对 GNU GDB 的扩展，用于调试 CUDA 应用程序。它支持同时调试 CPU 和 GPU 代码，可在 CUDA 内核中设置断点、单步执行和检查变量。

该调试器可以在内核内的特定线程或块处停止执行、检查设备内存并捕获内存错误。它将 CUDA 的并行执行模型融入 GDB 的界面，允许在上千个并发线程之间导航。

聚焦（focus）模式让开发者可以检查特定的块和线程。内存检查可捕获越界访问等错误。与 NVIDIA Nsight 系统集成后还可进行基于 IDE 的调试。

# CAVEATS

需要计算能力 2.0 以上的 NVIDIA GPU。调试模式会禁用部分 GPU 优化并强制以 **-O0** 编译。除非使用 **--cuda-use-lockfile=0**，否则每块 GPU 只能有一个调试会话。某些 GDB 功能可能无法用于 GPU 代码。CUDA 内核必须使用 **nvcc -g -G** 选项编译（若要在开启优化的情况下进行行级调试则用 **-lineinfo**）。

# HISTORY

cuda-gdb 由 **NVIDIA** 于 **2009 年**随 CUDA 2.2 一同推出，提供内核调试能力。它将熟悉的 GDB 界面扩展到了 GPU 并行性上，解决了当时 CUDA 开发者调试手段匮乏的迫切需求。该工具随每个 CUDA 工具包版本不断演进，陆续增加了内存检查和更好的多 GPU 支持等特性。

# SEE ALSO

[gdb](/man/gdb)(1), [nvcc](/man/nvcc)(1), [nvidia-smi](/man/nvidia-smi)(1)
